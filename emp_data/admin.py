from django.contrib import admin
from .models import student

# Define your ModelAdmin class
class emp_admin(admin.ModelAdmin):
    list_display = ('name', 'classes', 'phone_number')
    search_fields = ('name',)
    list_filter = ['classes']  # Corrected list_filter as a list

# Register your model with the ModelAdmin class
admin.site.register(student, emp_admin)
