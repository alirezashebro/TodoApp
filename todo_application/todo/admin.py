from django.contrib import admin
from .models import *
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin

admin.site.site_header = "اپلیکیشن مدیریت تسک ها"

@admin.register(Task)
class TaskModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['creator', 'title', 'description', 'state', 'creation_date', 'do_date', 'last_modified', 'get_created_jalali']
    
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')
