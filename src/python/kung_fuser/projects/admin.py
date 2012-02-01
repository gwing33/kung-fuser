from kung_fuser.projects.models import Project, UserTest, Task
from django.contrib import admin

class UserTestAdmin(admin.TabularInline):
  model = UserTest
  extra = 1

class ProjectAdmin(admin.ModelAdmin):
  inlines = [UserTestAdmin]

admin.site.register(Project, ProjectAdmin)