from django.views import generic

from .models import Contact


class ContactListView(generic.ListView):
    model = Contact
    template_name = 'contact_list.html'
    context_object_name = 'contacts'


class ContactDetailView(generic.DetailView):
    model = Contact
    template_name = 'contact_detail.html'
    context_object_name = 'contact'


class ContactCreateView(generic.CreateView):
    model = Contact
    template_name = 'contact_form.html'
    fields = ['name', 'birthday', 'phone', 'email']
    success_url = '/'
    context_object_name = 'contact'


class ContactUpdateView(generic.UpdateView):
    model = Contact
    template_name = 'contact_form.html'
    fields = ['name', 'birthday', 'phone', 'email']
    success_url = '/'
    context_object_name = 'contact'


class ContactDeleteView(generic.DeleteView):
    model = Contact
    template_name = 'contact_delete.html'
    success_url = '/'
    context_object_name = 'contact'
