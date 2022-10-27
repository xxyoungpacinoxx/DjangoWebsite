from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'family', 'university']
    list_filter = ['university', ]
    search_fields = ['name']
    fieldsets = [
        ['Personal info', {'fields': ('name', 'family', 'age')}],
        ['Education Status', {'fields': ('university', 'status')}],
    ]


admin.site.register(Student, StudentAdmin)
