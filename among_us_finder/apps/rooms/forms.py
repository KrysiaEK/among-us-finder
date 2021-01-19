from django.forms import ModelForm
from .models import Room
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class CreateRoomForm(ModelForm):

    class Meta:
        model = Room
        fields = ["name", "date", "time", "map", "players_number", "level", "searched_players_number", "comment"]
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['level'].label = 'Level of advancement'
        self.fields['searched_players_number'].label = 'How many players are you looking for'
        self.fields['name'].label = 'Name of the room (optional)'
        self.fields['map'].label = 'Map (optional)'
        self.fields['comment'].label = 'Comment (optional)'
