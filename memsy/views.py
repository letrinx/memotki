
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from memsy import forms
from memsy.models import Mems


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

class AddMemView(View):
    def get(self, request):
        form = forms.MemForm()
        return render(request, 'add-mem.html', {'form': form})
    def post(self, request):
        form = forms.MemForm(request.POST, request.FILES)
        if form.is_valid():
            form.mem = form.cleaned_data['mem']
            form.save()
            return HttpResponseRedirect(redirect_to="/")
        return HttpResponseRedirect(redirect_to="/mem/{}".format(form.id))



class ShowMemView(View):
    def get(self, request, id):
        mem = Mems.objects.get(id=id)
        return render(request, "showmem.html", {'title': mem.title, 'mem': mem.mem})