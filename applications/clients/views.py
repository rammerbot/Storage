
from django.shortcuts import render, redirect
from .models import Clients
from .forms import AddClientForm, EditClientForm
from django.contrib import messages
# Create your views here.

# clients Windows
def clients_view(request):
    clients = Clients.objects.all()
    client_form = AddClientForm
    edit_client_form = EditClientForm

    context = {
        "clients" : clients,
        'add_client_form':client_form,
        'edit_client_form': edit_client_form
        }

    return render(request,'clients/clients.html', context)

# Add Clients modal
def add_client_view(request):
    if request.POST:
        form = AddClientForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al agregar el Cliente nuevo")
                return redirect('clients_app:clients')
    return redirect('clients_app:clients')

# Edit clients modal
def edit_client_view(request):
        
    if request.POST:
        client = Clients.objects.get(pk=request.POST.get('edit_client_id'))
        form = EditClientForm(request.POST, request.FILES, instance=client)
    if form.is_valid:
        try:
            form.save()
        except:
            messages(request, "Error al agregar el Cliente nuevo")
            return redirect('clients_app:clients')

    return redirect('clients_app:clients')

# Delete Clients button
def delete_client_view(request):
    
    if request.POST:
        client = Clients.objects.get(pk=request.POST.get('delete_client_id'))
        client.delete()


    return redirect('clients_app:clients')