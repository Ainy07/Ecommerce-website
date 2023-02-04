from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('contactus/',views.contact_us , name="contact_us"),
]
