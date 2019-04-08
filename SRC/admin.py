from django.contrib import admin
from SRC.models import Course
# Register your models here.

class CourseModelAdmin(admin.ModelAdmin):
    list_display=["title"]

admin.site.register(Course, CourseModelAdmin)
