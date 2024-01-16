from django.urls import path
from . import views
from .views import contact_list, contact_add, contact_delete, contact_update,home,contact_detail

urlpatterns = [
    path('contacts/', contact_list, name='contact_list'),
    path('contacts/add/', contact_add, name='contact_add'),
    path('contacts/<int:contact_id>/delete/', contact_delete, name='contact_delete'),
    path('contacts/<int:contact_id>/update/', contact_update, name='contact_update'),
    path('', home, name='home'),
    path('contacts/<int:contact_id>/', contact_detail, name='contact_detail'),
]
