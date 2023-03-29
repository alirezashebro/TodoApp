# Generated by Django 4.1.7 on 2023-03-28 15:11

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("todo", "0002_alter_task_do_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="do_date",
            new_name="due_date",
        ),
        migrations.AddField(
            model_name="task",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
