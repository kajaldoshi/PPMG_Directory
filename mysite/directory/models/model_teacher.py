from django.db import models
from django.utils.safestring import mark_safe

from mysite.directory import db_const
from mysite.directory.models import Room, Subject


def upload_path_handler(self, filename):
    import os
    try:
        os.unlink(u'' + db_const.PHOTO_STORAGE.location + "/photo/{file}.jpg".format(file=self.t_id))
    except Exception as e:
        pass
    return "photo/{file}.jpg".format(file=self.teacher_id)


class Teacher(models.Model):
    first_name = models.CharField('First Name', max_length=100, null=True, blank=True)
    last_name = models.CharField('Last Name', max_length=100, null=True, blank=True)
    photo = models.ImageField('Profile Picture', upload_to=upload_path_handler, storage=db_const.PHOTO_STORAGE,
                              blank=True, null=True,
                              max_length=200)
    email = models.CharField('Email Address', unique=True, max_length=db_const.MAX_EMAIL, editable=False, blank=False)
    phone_number = models.CharField('Mobile Number', max_length=db_const.MAX_EMP_MOBILE, null=True, blank=True,
                                    editable=True)
    room_number = models.ForeignKey(Room, default=0, verbose_name="Room Number", on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, verbose_name="Subjects Taught")

    def profile_tag(self):
        src = self.photo.path
        return mark_safe('<img src="%s" width="150" height="150" />' % src)

    profile_tag.short_description = 'Preview'

    def generate_unique_email(self):
        from django.conf import settings
        domain = settings.EMAIL_ADDRESS_DOMAIN
        val = "{0}{1}".format(self.first_name, self.last_name).lower()
        email = "{0}{1}".format(val, domain)
        x = 1
        unique = False
        while not unique:
            obj = Teacher.objects.filter(email=email).first()
            if obj:
                email = "{0}{1}{2}".format(val, x, domain)
                x += 1
            else:
                unique = True
                break
        return email

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        obj = Teacher.objects.filter(first_name=self.first_name, last_name=self.last_name, email=self.email)
        if obj and len(obj)>1:
            self.email = self.generate_unique_email()
        elif obj:
            force_update = True
        super(Teacher, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        app_label = 'directory'
