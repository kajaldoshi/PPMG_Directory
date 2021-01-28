from django.db import models
from mysite.directory import db_const


class Room(models.Model):
    room_number = models.CharField('Room Number', max_length=db_const.MAX_ROOM_NUMBER, unique=True, blank=False)
    room_name = models.CharField('Room Name', blank=False, max_length=db_const.MAX_ROOM_NUMBER)

    def __str__(self):
        return self.room_number

    class Meta:
        app_label = 'directory'
