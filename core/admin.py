from django.contrib import admin
from .models import Category, Expense

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'amount', 'date', 'description']
    list_filter = ['category', 'date', 'user']
    search_fields = ['description', 'user__username']
