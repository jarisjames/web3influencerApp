from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('merch/', views.merch, name='merch'),  # Merch page
]
