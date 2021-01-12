from .forms import CreateRoomForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView
from .models import Room


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
    ordering = ['date']
