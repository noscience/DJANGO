from django.contrib import admin

from .models import Question
from .models import student

admin.site.register(Question)
admin.site.register(student)