from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('donor/', views.donor_dashboard, name='donor_dashboard'),
    path('acceptor/', views.acceptor_dashboard, name='acceptor_dashboard'),
    path('donations/add/', views.add_food, name='add_food'),
    path('donations/edit/<int:pk>/', views.edit_food, name='edit_food'),
    path('donations/delete/<int:pk>/', views.delete_food, name='delete_food'),
    path('donations/<int:pk>/', views.food_detail, name='food_detail'),
    path('donations/<int:pk>/claim/', views.claim_food, name='claim_food'),
]
