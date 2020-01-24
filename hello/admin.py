from django.contrib import admin
from hello.models import login

@admin.register(login)
class PhotoAdmin(admin.ModelAdmin):
    def log(obj):
        return obj
    
    list_display=['username','password']


