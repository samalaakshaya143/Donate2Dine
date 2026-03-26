from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

@login_required
def chat_inbox(request):
    # Find all users this user has messaged with
    sent_to = ChatMessage.objects.filter(sender=request.user).values_list('receiver', flat=True)
    received_from = ChatMessage.objects.filter(receiver=request.user).values_list('sender', flat=True)
    
    user_ids = set(sent_to).union(set(received_from))
    contacts = User.objects.filter(id__in=user_ids).exclude(id=request.user.id)
    
    return render(request, 'chat/inbox.html', {'contacts': contacts})

@login_required
def chat_thread(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        message_text = request.POST.get('message')
        if message_text:
            ChatMessage.objects.create(
                sender=request.user,
                receiver=other_user,
                message=message_text
            )
            return redirect('chat_thread', user_id=other_user.id)
            
    # Mark messages as read
    ChatMessage.objects.filter(sender=other_user, receiver=request.user, is_read=False).update(is_read=True)
            
    messages = ChatMessage.objects.filter(
        Q(sender=request.user, receiver=other_user) | 
        Q(sender=other_user, receiver=request.user)
    ).order_by('timestamp')
    
    return render(request, 'chat/thread.html', {
        'other_user': other_user,
        'chat_messages': messages
    })
