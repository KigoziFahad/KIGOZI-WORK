from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    # path('contact_view', views.contact_view, name='contact_view_name'),
]