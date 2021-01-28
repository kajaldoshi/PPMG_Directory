from django.contrib import admin

from mysite.directory.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number','room_name',)