from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, FriendRequest, Profile


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional info', {'fields': ('email',)}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'daily_calorie_goal', 'birth_date', 'height_cm', 'weight_kg')
    search_fields = ('user__username', 'user__email')


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('from_user__username', 'to_user__username')

# Register your models here.
