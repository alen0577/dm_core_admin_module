# Generated by Django 4.2.5 on 2023-10-16 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration_Login', '0015_employeeregister_details_emp_regid'),
        ('DM_Head', '0007_work_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_task',
            name='comp_taskid',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.businessregister_details'),
        ),
    ]