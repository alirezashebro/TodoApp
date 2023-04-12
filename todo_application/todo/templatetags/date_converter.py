from django import template
from jalali_date import datetime2jalali, date2jalali

register = template.Library()

@register.filter(name='jalali_date_time_convertor')
def jalali_date_time_convertor(value):
    return datetime2jalali(value).strftime("%y/%m/%d - %H:%M:%S")

@register.filter(name='jalali_date_convertor')
def jalali_date_convertor(value):
    return date2jalali(value)
