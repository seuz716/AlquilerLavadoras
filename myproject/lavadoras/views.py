# lavadoras/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Lavadora

class LavadoraListView(ListView):
    model = Lavadora
    template_name = 'lavadoras/lavadora_list.html'
    context_object_name = 'lavadoras'

class LavadoraCreateView(CreateView):
    model = Lavadora
    template_name = 'lavadoras/lavadora_form.html'
    fields = '__all__'

class LavadoraUpdateView(UpdateView):
    model = Lavadora
    template_name = 'lavadoras/lavadora_form.html'
    fields = '__all__'

class LavadoraDeleteView(DeleteView):
    model = Lavadora
    template_name = 'lavadoras/lavadora_confirm_delete.html'
    success_url = reverse_lazy('lavadoras-list')
