# Generated by Django 4.2.5 on 2023-10-11 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DM_Head', '0002_alter_actiontaken_act_emp_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeleave',
            name='end_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='employeeleave',
            name='start_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]