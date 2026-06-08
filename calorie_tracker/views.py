from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import date
from .models import FoodItem

def home(request):
    """Display all food items and total calories for today"""
    today = date.today()
    food_items = FoodItem.objects.filter(date_added=today)
    total_calories = sum(item.calories for item in food_items)
    
    # Calculate progress percentage
    daily_goal = 2000
    if total_calories >= daily_goal:
        progress_percent = 100
    else:
        progress_percent = int((total_calories / daily_goal) * 100)
    
    context = {
        'food_items': food_items,
        'total_calories': total_calories,
        'today': today,
        'daily_goal': daily_goal,
        'progress_percent': progress_percent,
    }
    return render(request, 'calorie_tracker/home.html', context)

def add_food(request):
    """Add a new food item"""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        calories = request.POST.get('calories', '')
        
        if not name:
            messages.error(request, 'Please enter a food name')
        elif not calories:
            messages.error(request, 'Please enter calorie count')
        else:
            try:
                calories = int(calories)
                if calories <= 0:
                    messages.error(request, 'Calories must be greater than 0')
                elif calories > 5000:
                    messages.error(request, 'That seems too high! Please check the calories')
                else:
                    FoodItem.objects.create(name=name.title(), calories=calories)
                    messages.success(request, f'{name.title()} added! ({calories} calories)')
            except ValueError:
                messages.error(request, 'Please enter a valid number for calories')
        
        return redirect('home')
    return redirect('home')

def delete_food(request, food_id):
    """Delete a food item"""
    food_item = get_object_or_404(FoodItem, id=food_id)
    
    if request.method == 'POST':
        food_name = food_item.name
        food_item.delete()
        messages.success(request, f'{food_name} removed from your list')
        return redirect('home')
    
    return render(request, 'calorie_tracker/delete.html', {'food_item': food_item})

def reset_day(request):
    """Reset all food items for today"""
    if request.method == 'POST':
        today = date.today()
        count = FoodItem.objects.filter(date_added=today).count()
        if count > 0:
            FoodItem.objects.filter(date_added=today).delete()
            messages.success(request, f'Reset complete! Removed {count} items for today')
        else:
            messages.info(request, 'No items to reset for today')
        return redirect('home')
    return redirect('home')