from django.forms import ModelForm
from .models import Room, Message


class CreateRoomForm(ModelForm):

    class Meta:
        model = Room
        fields = ["name", "game_start", "map", "players_number", "level", "searched_players_number", "comment"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['level'].label = 'Level of advancement'
        self.fields['searched_players_number'].label = 'How many players are you looking for'
        self.fields['name'].label = 'Name of the room (optional)'
        self.fields['map'].label = 'Map (optional)'
        self.fields['comment'].label = 'Comment (optional)'
        self.fields['game_start'].label = 'Date and time'

class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ["comment"]


"""
class RoomSearchForm(Form):
    time = forms.TimeField()
    date = forms.DateField()
    map = forms.ChoiceField(choices=Room.MAP_CHOICES)
"""
