from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import path
from mysite.directory.admin.teacher_admin import extract_zip, import_data

@login_required
def import_csv(request):
    from django.template.response import TemplateResponse
    import csv, io
    if request.method.lower() == 'get':
        return TemplateResponse(request, 'import_data.html', {})
    elif request.method.lower() == 'post':
        csv_file = request.FILES['csv_file']
        zip_file = request.FILES['zip_file']
        extract_zip(zip_file)
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            import_data(column)
        return HttpResponse()

urlpatterns = [
    path('admin/', admin.site.urls),
   url(r'import/', import_csv),
]
