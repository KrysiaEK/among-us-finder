from django.utils import timezone

from .forms import CreateRoomForm, MessageForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView, DetailView
from .models import Room
from django.urls import reverse_lazy


class CreateRoomFormView(FormView):
    template_name = 'rooms/create_room.html'
    form_class = CreateRoomForm
    success_url = 'room_created'

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
        ctx = super(RoomDetail, self).get_context_data(**kwargs)
        ctx['msgs'] = self.object.messeges.all()
        return ctx


class RoomConversation(DetailView, FormView):
    model = Room
    template_name = 'rooms/room_conversation.html'
    form_class = MessageForm

    def get_context_data(self, **kwargs):
        ctx = super(RoomConversation, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            ctx['user'] = self.request.user
            ctx['msgs'] = self.object.messages.all()
        return ctx

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('rooms:room_conversation', kwargs={'pk': self.kwargs.get('pk')})
