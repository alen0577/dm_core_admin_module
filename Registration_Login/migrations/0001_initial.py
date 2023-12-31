# Generated by Django 4.2.5 on 2023-10-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogRegister_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_username', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('log_password', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('log_date', models.DateField(auto_now_add=True, null=True)),
                ('log_time', models.TimeField(auto_now_add=True, null=True)),
                ('is_staff', models.IntegerField(default=0)),
                ('active_status', models.IntegerField(default=0)),
            ],
        ),
    ]
