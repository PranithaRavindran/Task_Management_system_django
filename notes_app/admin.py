from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Note

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'bio')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('bio',)}),
    )

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'due_date', 'is_completed')
    list_filter = ('priority', 'is_completed')
    search_fields = ('title', 'content')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Note, NoteAdmin)