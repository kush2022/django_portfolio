from django.urls import path
from . import views 


urlpatterns = [
    path('sign-up/', views.register_user, name='sign-up'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]