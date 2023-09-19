from django.contrib import admin
from About_Us.models import teacher

# Register your models here.
class teacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'tid', 'tname', 'temail')
admin.site.register(teacher,teacherAdmin)

