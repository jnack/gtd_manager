from django.contrib import admin
from .models import Task, Stage, Project, Context

# Register your models here.
admin.site.register(Task)
admin.site.register(Stage)
admin.site.register(Context)
admin.site.register(Project)
