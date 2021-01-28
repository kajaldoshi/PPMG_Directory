from django.contrib import admin
from django import forms
from django.shortcuts import render, redirect
from django.conf.urls import url
import csv, io
from mysite.directory.models import Room, Subject, Teacher
from mysite.directory import db_const
from os import path


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


def extract_zip(zip_file):
    from zipfile import ZipFile
    upload_path = db_const.PHOTO_STORAGE.location + '/photo/'
    with ZipFile(zip_file) as file:
        print(file.namelist())
        file.extractall(upload_path)


def import_data(row):
    upload_path = db_const.PHOTO_STORAGE.location + '/photo/'
    first_name = row[0]
    last_name = row[1]
    photo_path = upload_path + row[2]
    photo = 'photo/' + row[2]
    if not path.exists(photo_path):
        photo = 'photo/userImage.gif'
    email = row[3]
    mobile = row[4]
    rooms = Room.objects.filter(room_number=row[5])
    if rooms:
        room = rooms[0]
    else:
        room = Room(room_number=row[5])
        room.save()
    subjects = row[6:]
    subs = []
    for s in subjects:
        sname = s.replace('"', '').strip().lower()
        sub_objs = Subject.objects.filter(subject_name=sname)
        if sub_objs:
            sub_obj = sub_objs[0]
        else:
            sub_obj = Subject(subject_name=sname)
            sub_obj.save()
        subs.append(sub_obj.id)

    if len(subs) > 5:
        raise RuntimeWarning('Only 5 Subjects can be selected!')
    teacher = Teacher.objects.filter(first_name=first_name, last_name=last_name, email=email)
    if not teacher:
        teacher = Teacher(first_name=first_name, last_name=last_name, email=email, photo=photo, phone_number=mobile,
                          room_number=room)
        teacher.save()
        teacher.subjects.set(subs)
    else:
        t = teacher[0]
        t.photo = photo
        t.room_number = room
        t.phone_number = mobile
        t.save(force_update=True)
        t.subjects.set(subs)


def import_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')
        zip_file = request.FILES.get('zip_file')
        if zip_file:
            extract_zip(zip_file)
        if csv_file:
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                import_data(column)
        return redirect("..")
    form = CsvImportForm()
    payload = {"form": form}
    return render(request, "csv_form.html", payload)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'photo', 'email', 'phone_number', 'get_room', 'get_subjects')
    list_filter = ('last_name', 'subjects',)
    fields = ['first_name', 'last_name', ('photo', 'profile_tag'),'email', 'phone_number', 'room_number', 'subjects']
    readonly_fields = ['profile_tag', 'email']
    change_list_template = "admin_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url(r'import_csv/', import_csv),

        ]
        return my_urls + urls

    def get_room(self, obj):
        return obj.room_number.room_number

    get_room.short_description = 'Room'

    def get_subjects(self, obj):
        return "\n".join([p.subject_name for p in obj.subjects.all()])

    get_subjects.short_description = 'Subjects'

    def get_queryset(self, request):
        search_lastname = request.GET.get("last_name")
        search_subject = request.GET.get("subject")

        if search_lastname:
            qs = Teacher.objects.filter(last_name__startswith=search_lastname)
        elif search_subject:
            qs = Teacher.objects.filter(subjects_subject_name__startswith=search_subject)
        else:
            qs = Teacher.objects.all()
        return qs
