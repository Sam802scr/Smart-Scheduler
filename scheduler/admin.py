from django.contrib import admin
from .models import Event, Task, Schedule

admin.site.register(Event)
admin.site.register(Task)
admin.site.register(Schedule)
