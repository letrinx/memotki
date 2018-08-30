from random import randint

from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View, generic
from django.views.generic import DetailView, ListView
from memsy import forms
from memsy.forms import CommentForm
from memsy.models import Mems, Comment


class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


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


class ShowMemView(View):
    def get(self, request, id):
        mem = get_object_or_404(Mems, id=id)
        if not mem.likes.filter(id=request.user.id):
            is_liked = False
        else:
            is_liked = True
        comments = Comment.objects.filter(mem=id)

        context = {'title': mem.title, 'mem': mem.mem,
                   'mem.id': mem.id, 'is_liked': is_liked,
                   'total_likes': Mems.total_likes(mem),
                   'comments': comments,
                   'id': mem.id}
        return render(request, "showmem.html", context)

    def post(self, request, id):
        mem = get_object_or_404(Mems, id=id)
        if mem.likes.filter(id=request.user.id).exists():
            mem.likes.remove(request.user)
        else:
            mem.likes.add(request.user)
        return HttpResponseRedirect('/mem/{}'.format(mem.id))


class RandomMemView(View):
    def get(self, request):
        count = Mems.objects.all().count()
        random = randint(0, count - 1)
        mem = Mems.objects.all()[random]
        return HttpResponseRedirect('/mem/{}'.format(mem.id))


class HomeView(ListView):
    model = Mems
    template_name = 'home.html'
    context_object_name = 'mem_list'
    paginate_by = 5
    queryset = Mems.objects.all()

class TopMemsView(View):
    def get(self, request):
        mem_list = Mems.objects.annotate(Count('likes')).order_by('-likes__count')[:3]
        return render(request, 'toplist.html', {'mem_list': mem_list})

class AddCommentView(View):
    def get(self, request, pk):
        form = CommentForm()
        return render(request, 'addcoment.html', {'form': form})

    def post(self, request, pk):
        form = CommentForm(request.POST)
        form.mem = pk
        form.user = request.user.id
        if form.is_valid():
            form.save()
        url = reverse('showmem', kwargs={'id': pk})
        return HttpResponseRedirect(url)