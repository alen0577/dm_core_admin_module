# Generated by Django 4.2.5 on 2023-10-06 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration_Login', '0011_rename_emp_profife_employeeregister_details_emp_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeregister_details',
            name='emp_profile',
            field=models.ImageField(default='', upload_to='profiles'),
        ),
    ]