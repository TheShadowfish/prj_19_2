from django.contrib import admin

# Register your models here.
from main.models import Student

# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active','avatar')
    list_filter = ('is_active','first_name')
    search_fields = ('first_name', 'last_mame',)
