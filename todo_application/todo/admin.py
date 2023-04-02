from django.contrib import admin
from django.forms import TextInput, Textarea
from .models import *
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from taggit.apps import TaggitAppConfig

admin.site.site_header = "اپلیکیشن مدیریت تسک ها"

TaggitAppConfig.verbose_name = 'مدیریت برچسب ها'

@admin.register(Task)
class TaskModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['creator', 'title', 'description', 'state', 'creation_date_jalali', 'due_date_jalali', 'tag_list', 'last_modified_jalali']

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':35})},
    }

    
    def creation_date_jalali(self, obj):
        return datetime2jalali(obj.creation_date).strftime("%y/%m/%d - %H:%M:%S")
    
    def due_date_jalali(self, obj):
        return date2jalali(obj.due_date)
    
    def last_modified_jalali(self, obj):
        if obj.last_modified:
            return datetime2jalali(obj.last_modified).strftime("%y/%m/%d - %H:%M:%S")
        else:
            return "-"
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    creation_date_jalali.short_description = "تاریخ ایجاد"
    due_date_jalali.short_description = "تاریخ انجام"
    tag_list.short_description = "لیست برچسب ها"
    last_modified_jalali.short_description = "آخرین بروزرسانی"
