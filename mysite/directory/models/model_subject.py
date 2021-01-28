from django.db import models
from mysite.directory import db_const


class Subject(models.Model):
    subject_id = models.CharField('Subject ID', max_length=db_const.MAX_SUBJECT_ID, blank=True)
    subject_name = models.CharField('Subject Name', max_length=db_const.MAX_SUBJECT_NAME, unique=True, blank=False)

    def __str__(self):
        return self.subject_name

    class Meta:
        app_label = 'directory'
