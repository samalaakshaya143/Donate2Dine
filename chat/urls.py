from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_inbox, name='chat_inbox'),
    path('<int:user_id>/', views.chat_thread, name='chat_thread'),
]
