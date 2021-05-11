from django.forms import ModelForm
from .models import Room, Message
from django.core.exceptions import PermissionDenied


class CreateRoomForm(ModelForm):

    class Meta:
        model = Room
        fields = ["name", "game_start", "map", "level", "players_number", "searched_players_number", "comment"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('host', None)
        super().__init__(*args, **kwargs)
        self.fields['level'].label = 'Level of advancement'
        self.fields['searched_players_number'].label = 'How many players are you looking for'
        self.fields['name'].label = 'Name of the room (optional)'
        self.fields['map'].label = 'Map (optional)'
        self.fields['comment'].label = 'Comment (optional)'
        self.fields['game_start'].label = 'Date and time'
        self.fields['map'].required = False

    def save(self, commit=True):
        if not self.user:
            raise PermissionDenied()
        else:
            self.instance.host = self.user
            instance = super().save(commit)
            instance.participants.add(self.user)
            return instance

    def full_clean(self):
        super(CreateRoomForm, self).full_clean()
        if self.is_valid():
            if self.cleaned_data.get('searched_players_number') >= self.cleaned_data.get('players_number'):
                self.add_error('searched_players_number', "It can't be bigger than players number")


class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ["comment", 'author', 'room']

    def __init__(self, *args, **kwargs):
        self.room = kwargs.pop('room')
        self.author = kwargs.pop('author')
        super().__init__(*args, **kwargs)
        self.fields['author'].required = False
        self.fields['room'].required = False

    def save(self, commit=True):
        self.instance.author = self.author
        self.instance.room = self.room
        instance = super().save(commit)
        instance.save()
        return instance

class ReportUser(ModelForm):
    pass


"""
class RoomSearchForm(Form):
    time = forms.TimeField()
    date = forms.DateField()
    map = forms.ChoiceField(choices=Room.MAP_CHOICES)
"""
