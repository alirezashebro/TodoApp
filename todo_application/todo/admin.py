from django.contrib import admin
from .models import *
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from taggit.apps import TaggitAppConfig

admin.site.site_header = "اپلیکیشن مدیریت تسک ها"

TaggitAppConfig.verbose_name = 'مدیریت برچسب ها'

@admin.register(Task)
class TaskModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['creator', 'title', 'description', 'state', 'creation_date', 'due_date', 'tag_list', 'last_modified', 'get_created_jalali']
    
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
