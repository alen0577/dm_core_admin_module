# Generated by Django 4.2.5 on 2023-10-06 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration_Login', '0010_employeeregister_details_emp_verify_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeregister_details',
            old_name='emp_profife',
            new_name='emp_profile',
        ),
    ]
