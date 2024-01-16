# contacts/views.py
from django.shortcuts import render
from api.models import Contact
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ContactForm


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


# contacts/views.py
def contact_add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/add.html', {'form': form})



# contacts/views.py
def contact_delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/delete.html', {'contact': contact})




# contacts/views.py

def contact_update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/update.html', {'form': form, 'contact': contact})



def home(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/home.html', {'contacts': contacts})


from django.shortcuts import render, get_object_or_404


def contact_detail(request, contact_id):
    # Retrieve the contact from the database using its ID
    contact = get_object_or_404(Contact, pk=contact_id)

    # Render the template with the contact details
    return render(request, 'contacts/contact_detail.html', {'contact': contact})
