from django.shortcuts import render

# Create your views here.
from django.views import generic
from blogapp import models
from blogapp.models import Post
from blogapp import forms
from django.core.urlresolvers import reverse_lazy
from random import randint

class KreirajPostView(generic.CreateView):
    model = models.Post
    fields = ('naslov', 'poruka',)
    form = forms.PostForm()
    template_name = 'blogapp/post_form.html'
    # success_url = reverse_lazy('blogapp:post_pojedinacan')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.autor = self.request.user
        self.object.save()
        return super().form_valid(form)



class ListaPostovaView(generic.ListView):
    model = models.Post
    def get_queryset(self):
        queryset = Post.objects.order_by('-datum_kreiranja').all()
        return queryset


class DetaljPostaView(generic.DetailView):
    model = Post


class AboutMeView(generic.TemplateView):
    """docstring for AboutMeView"TemplateView def __init__(self, arg):
        super(AboutMeView,TemplateView.__init__()
        self.arg = arg"""
    template_name = 'aboutme.html'

    def get_context_data(self, **kwargs):
        context = super(AboutMeView, self).get_context_data(**kwargs)
        
        neki_broj = randint(1,100)

        context['nasumicni_broj'] = neki_broj
        return context