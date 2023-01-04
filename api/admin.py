from django.contrib import admin
from api.models import Project, Type

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'project_url', 'image_url')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Type, TypeAdmin)

