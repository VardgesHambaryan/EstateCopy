from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import ContactForm

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, context = {})

    def post(self, request):
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
        
        return redirect('/')

class GalleryListView(ListView):
    template_name = 'gallery.html'

    def get(self, request):

        return render(request, self.template_name, context = {})

class VorakListView(ListView):
    template_name = 'vorak.html'

    def get(self, request):

        return render(request, self.template_name, context = {})
