# Generated by Django 4.1.7 on 2023-04-02 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0003_rename_do_date_task_due_date_task_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="is_disabled",
            field=models.BooleanField(default=False, verbose_name="غیرفعال شده"),
        ),
        migrations.AlterField(
            model_name="task",
            name="creation_date",
            field=models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
        ),
        migrations.AlterField(
            model_name="task",
            name="last_modified",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="آخرین بروز رسانی"
            ),
        ),
    ]
