from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Contact
import json
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


# List all contacts
# def contact_list(request):
#     if request.method == 'GET':
#         contacts = Contact.objects.all()
#         data = [{'id': contact.id, 'name': contact.name, 'email': contact.email} for contact in contacts]
#         return JsonResponse(data, safe=False)


from django.http import JsonResponse

def contact_list(request):
    contacts = Contact.objects.all()
    data = [{'id': contact.id, 'name': contact.name, 'email': contact.email} for contact in contacts]
    return JsonResponse(data, safe=False)



# Create a new contact
# @require_POST
@csrf_exempt
def contact_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        contact = Contact.objects.create(name=data['name'], email=data['email'], phone=data.get('phone', ''), address=data.get('address', ''))
        return JsonResponse({'id': contact.id, 'name': contact.name, 'email': contact.email}, status=201)

# Retrieve a specific contact
def contact_detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    if request.method == 'GET':
        data = {'id': contact.id, 'name': contact.name, 'email': contact.email, 'phone': contact.phone, 'address': contact.address}
        return JsonResponse(data)

    # Update an existing contact
    elif request.method == 'PUT':
        data = json.loads(request.body)
        contact.name = data['name']
        contact.email = data['email']
        contact.phone = data.get('phone', '')
        contact.address = data.get('address', '')
        contact.save()
        return JsonResponse({'id': contact.id, 'name': contact.name, 'email': contact.email})

    # Delete a contact
    elif request.method == 'DELETE':
        contact.delete()
        return JsonResponse({'message': 'Contact deleted successfully'}, status=204)
