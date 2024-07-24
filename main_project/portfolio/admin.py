from django.contrib import admin
from .models import *


@admin.register(Skill)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(FAQ)
class FQA(admin.ModelAdmin):
    list_display = ['question' , 'answer']

class ProjectImages(admin.StackedInline):
    model = ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description', 'demo', 'category']
    readonly_fields = ['slug']
    inlines = [ProjectImages]



@admin.register(MyEmail)
class EmailsAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email', 'message']



