from django.urls import path
from . import views

# home page
urlpatterns = [
    path('', views.htmxhome, name='htmxhome'),
    path('sandwich/', views.sandwich, name='sandwich'),
    path('hello/', views.hello, name='hello'),
    path('submit-form/', views.submit_form, name='submit_form')
]