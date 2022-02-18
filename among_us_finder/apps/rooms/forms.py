from django.forms import ModelForm
from django import forms
from django.core.exceptions import PermissionDenied

from among_us_finder.apps.rooms.models import Room, Message


class CreateRoomForm(ModelForm):

    class Meta:
        model = Room
        fields = ["name", "game_start", "game_map", "level", "players_number", "searched_players_number", "comment"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('host', None)
        super().__init__(*args, **kwargs)
        self.fields['level'].label = 'Level of advancement'
        self.fields['searched_players_number'].label = 'How many players are you looking for'
        self.fields['name'].label = 'Name of the room (optional)'
        self.fields['game_map'].label = 'Map (optional)'
        self.fields['comment'].label = 'Comment (optional)'
        self.fields['game_start'].label = 'Date and time'
        self.fields['game_map'].required = False

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

    """Form to create comment in room"""

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


class ReportUser(forms.Form):

    """Form to report abuse"""

    reason = forms.CharField(widget=forms.Textarea)
