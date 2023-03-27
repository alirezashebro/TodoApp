from django.conf import settings
from django.db import models
from django.utils import timezone


class Task(models.Model):
    STATES = [
        ("1", "انجام نشده"),
        ("2", "در حال انجام"),
        ("3", "انجام شده"),
    ]
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="ایجاد کننده", on_delete=models.PROTECT)
    title = models.CharField("عنوان", max_length=200)
    description = models.TextField("شرح")
    state = models.CharField("وضعیت", max_length=30, choices=STATES, default="")
    creation_date = models.DateTimeField("تاریخ ایجاد", default=timezone.now)
    do_date = models.DateField("تاریخ انجام", blank=True, null=True)
    last_modified = models.DateTimeField("آخرین بروز رسانی", blank=True, null=True)

    class Meta:
        verbose_name = "تسک"
        verbose_name_plural = "تسک ها"

    def modify(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    