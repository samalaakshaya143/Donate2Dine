from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FoodItem, FoodClaim
from .forms import FoodItemForm

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')

@login_required
def dashboard(request):
    if request.user.role == 'DONOR':
        return redirect('donor_dashboard')
    elif request.user.role == 'ACCEPTOR':
        return redirect('acceptor_dashboard')
    return redirect('home')

@login_required
def donor_dashboard(request):
    if request.user.role != 'DONOR':
        return redirect('dashboard')
    food_items = FoodItem.objects.filter(donor=request.user).order_by('-created_at')
    return render(request, 'donations/donor_dashboard.html', {'food_items': food_items})

@login_required
def acceptor_dashboard(request):
    if request.user.role != 'ACCEPTOR':
        return redirect('dashboard')
    available_food = FoodItem.objects.filter(status='AVAILABLE').order_by('-created_at')
    query = request.GET.get('q')
    if query:
        available_food = available_food.filter(food_name__icontains=query)
    my_claims = FoodClaim.objects.filter(acceptor=request.user).order_by('-claimed_at')
    
    return render(request, 'donations/acceptor_dashboard.html', {
        'available_food': available_food,
        'my_claims': my_claims
    })

@login_required
def add_food(request):
    if request.user.role != 'DONOR':
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.donor = request.user
            food.save()
            messages.success(request, 'Food item added successfully!')
            return redirect('donor_dashboard')
    else:
        form = FoodItemForm()
    
    return render(request, 'donations/food_form.html', {'form': form, 'title': 'Add Food Availability'})

@login_required
def edit_food(request, pk):
    food = get_object_or_404(FoodItem, pk=pk, donor=request.user)
    if request.method == 'POST':
        form = FoodItemForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food item updated successfully!')
            return redirect('donor_dashboard')
    else:
        form = FoodItemForm(instance=food)
    
    return render(request, 'donations/food_form.html', {'form': form, 'title': 'Edit Food Availability'})

@login_required
def delete_food(request, pk):
    food = get_object_or_404(FoodItem, pk=pk, donor=request.user)
    if request.method == 'POST':
        food.delete()
        messages.success(request, 'Food item deleted successfully!')
        return redirect('donor_dashboard')
    return render(request, 'donations/food_confirm_delete.html', {'food': food})

@login_required
def food_detail(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    return render(request, 'donations/food_detail.html', {'food': food})

@login_required
def claim_food(request, pk):
    if request.user.role != 'ACCEPTOR':
        return redirect('dashboard')
    
    food = get_object_or_404(FoodItem, pk=pk, status='AVAILABLE')
    if request.method == 'POST':
        FoodClaim.objects.create(food_item=food, acceptor=request.user)
        food.status = 'CLAIMED'
        food.save()
        messages.success(request, f'You have successfully claimed {food.food_name}. Please contact the donor.')
        return redirect('acceptor_dashboard')
    
    return render(request, 'donations/food_detail.html', {'food': food})
