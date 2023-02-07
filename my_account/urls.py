from django.urls import path
from . import views 


urlpatterns = [
    path('contact-me/', views.contact_view, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('msg/', views.message_view, name='message')

]