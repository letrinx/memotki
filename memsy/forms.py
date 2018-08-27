from django.contrib.auth.models import User
from django.forms import ModelForm
from memsy.models import Mems


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