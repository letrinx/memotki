from django.contrib.auth.models import User
from django.forms import ModelForm, HiddenInput
from memsy.models import Mems, Comment


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class MemForm(ModelForm):
    class Meta:
        model = Mems
        fields = ['title',
                   'mem']
        labels = {'title':'Tytuł', 'mem': 'Mem'}

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'mem', 'user']
        labels = {'text': 'Komentarz'}
        widgets = {'mem': HiddenInput(), 'user': HiddenInput()}