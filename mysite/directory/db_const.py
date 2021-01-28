from django.core.files.storage import FileSystemStorage
import os 
from django.conf import settings

PHOTO_STORAGE = FileSystemStorage(
    location=os.path.relpath(settings.ADDITION_FILE_ROOT),
)

MAX_EMP_FIRST_NAME = 50
MAX_EMP_LAST_NAME = 50
MAX_EMP_MOBILE = 20
MAX_ROOM_NUMBER = 20
MAX_ROOM_NAME = 50
MAX_SUBJECT_ID = 20
MAX_SUBJECT_NAME = 50
MAX_EMAIL=150
MAX_TEACHER_ID=10