from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin class definition """
    readonly_fields = ['password']
