from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone

from .constants import ROOM_ERROR_MAP
from .forms import CreateRoomForm, MessageForm, ReportUser
from django.views.generic.edit import FormView, FormMixin
from django.views.generic import TemplateView, ListView, DetailView
from .models import Room, Message
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import mail_admins
import smtplib

from ..users.models import User


class CreateRoomFormView(FormView):
    template_name = 'rooms/create_room.html'
    form_class = CreateRoomForm
    success_url = 'room_created'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs()
        if self.request.user.is_authenticated:
            kwargs['host'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RoomCreatedView(TemplateView):
    template_name = 'rooms/created.html'


class RoomList(ListView):
    model = Room
    template_name = 'rooms/room_list.html'
    ordering = ['game_start']

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['maps'] = Room.MAP_CHOICES
        return ctx

    def get_queryset(self):
        qs = super().get_queryset().filter(game_start__gte=timezone.now())
        if self.request.GET.get('game_start_before'):
            time_before = self.request.GET.get('game_start_before')
            qs = qs.filter(game_start__lte=time_before)
        if self.request.GET.get('game_start_after'):
            time_after = self.request.GET.get('game_start_after')
            qs = qs.filter(game_start__lte=time_after)
        if self.request.GET.get('map'):
            map = self.request.GET.get('map')
            qs = qs.filter(map=map)
        return qs


class RoomDetail(DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            ctx['user'] = self.request.user
        return ctx

    def post(self, *args, **kwargs):
        room = self.get_object()
        if self.request.user in room.participants.all():
            return redirect('rooms:join_room_error', error_code='already_in_room')
        if room.participants.count() >= room.searched_players_number:
            return redirect('rooms:join_room_error', error_code='no_place')
        else:
            room.participants.add(self.request.user)
            return redirect('rooms:room_conversation', pk=self.kwargs.get('pk'))


class JoinRoomError(TemplateView):
    template_name = 'rooms/no_place.html'

    def get_context_data(self, **kwargs):
        ctx = super(JoinRoomError, self).get_context_data(**kwargs)
        ctx['error_msg'] = ROOM_ERROR_MAP.get(self.kwargs.get('error_code'))
        return ctx


class RoomConversation(PermissionRequiredMixin, FormMixin, DetailView):
    model = Room
    template_name = 'rooms/room_conversation.html'
    form_class = MessageForm
    http_method_names = ['get', 'post']

    def has_permission(self):
        room = self.get_object()
        return room.participants.filter(pk=self.request.user.pk).exists()

    def handle_no_permission(self):
        return redirect(reverse_lazy("rooms:room_list"))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            ctx['user'] = self.request.user
            ctx['msgs'] = self.get_object().messages.all()
        return ctx

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['author'] = self.request.user
        kwargs['room'] = self.get_object()
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('rooms:room_conversation', kwargs={'pk': self.kwargs.get('pk')})


class ParticipantList(DetailView):
    model = Room
    template_name = 'rooms/participantslist.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            ctx['user'] = self.request.user
            ctx['participants'] = self.get_object().participants.all()
            ctx['host'] = self.get_object().host
            ctx['is_host'] = self.get_object().host == self.request.user
        return ctx


class DeleteParticipant(TemplateView):
    model = Room
    template_name = 'rooms/delete_user.html'

    def post(self, *args, **kwargs):
        room = Room.objects.get(pk=kwargs.get('room_pk'))
        if self.request.user != room.host:
            return HttpResponse('Unauthorized', status=401)
        room.participants.remove(User.objects.get(pk=kwargs.get('user_pk')))
        return redirect('rooms:participants_list', pk=kwargs.get('room_pk'))


class LeaveRoomView(DetailView):
    model = Room
    template_name = 'rooms/leave_room.html'

    def post(self, *args, **kwargs):
        room = self.get_object()
        room.participants.remove(self.request.user)
        return redirect('rooms:room_list')


class UserRooms(ListView):
    model = Room
    template_name = 'rooms/user_view.html'
    context_object_name = 'rooms_types'

    def get_queryset(self):
        rooms = Room.objects.filter(participants=self.request.user).order_by("-game_start")
        qs = {'Actual': rooms.filter(game_start__gte=timezone.now()),
              'Old': rooms.filter(game_start__lt=timezone.now())}
        return qs


class ReportUserFormView(FormView):
    template_name = 'rooms/report_user.html'
    form_class = ReportUser
    success_url = 'user_reported'

    def form_valid(self, form):
        reporting_user = self.request.user
        reported_user = get_object_or_404(User, pk=self.kwargs.get('user_pk'))
        room = get_object_or_404(Room, pk=self.kwargs.get('room_pk'))
        reason = form.cleaned_data['reason']
        subject = "Abuse report"
        body = {
            'username': reporting_user.username,
            'reported_username': reported_user.username,
            'room': str(room.id),
            'reason': reason,
        }
        try:
            message = "\n".join(body.values())
            mail_admins(subject, message)
            return super().form_valid(form)
        except smtplib.SMTPException:
            return HttpResponse('Invalid header found.')


class ReportSuccess(TemplateView):
    template_name = 'rooms/report_success.html'
