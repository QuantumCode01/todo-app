from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=('id','name','title','complete','created')
    prepopulated_fields = {"slug": ("name","title",)}
    
    
   