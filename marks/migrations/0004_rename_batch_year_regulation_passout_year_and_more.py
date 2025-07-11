# Generated by Django 5.2.3 on 2025-07-01 17:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("marks", "0003_rename_passout_year_regulation_batch_year_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="regulation",
            old_name="batch_year",
            new_name="passout_year",
        ),
        migrations.RenameField(
            model_name="student",
            old_name="current_semester",
            new_name="semester",
        ),
        migrations.RenameField(
            model_name="student",
            old_name="current_year",
            new_name="year",
        ),
        migrations.RemoveField(
            model_name="student",
            name="admission_year",
        ),
    ]
