from django.contrib import admin
from .models import FoodItem, FoodClaim

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'donor', 'quantity', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('food_name', 'location', 'donor__username')

@admin.register(FoodClaim)
class FoodClaimAdmin(admin.ModelAdmin):
    list_display = ('food_item', 'acceptor', 'claimed_at')
    search_fields = ('food_item__food_name', 'acceptor__username')
