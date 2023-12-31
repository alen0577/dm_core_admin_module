# Generated by Django 4.2.5 on 2023-10-09 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Registration_Login', '0012_alter_employeeregister_details_emp_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notific_head', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('notific_content', models.TextField(blank=True, default='', null=True)),
                ('notific_time', models.TimeField(auto_now_add=True, null=True)),
                ('notific_status', models.IntegerField(default=0)),
                ('notific_date', models.DateField(auto_now=True, null=True)),
                ('emp_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.businessregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_id', models.IntegerField(default=0)),
                ('from_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('feedback_content', models.TextField(blank=True, default='', null=True)),
                ('feedback_date', models.DateField(null=True)),
                ('feedback_emp_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.businessregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(blank=True, default='', null=True)),
                ('end_time', models.TimeField(blank=True, default='', null=True)),
                ('schedule_head', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('todo_content', models.TextField(blank=True, default='', null=True)),
                ('log_time', models.TimeField(auto_now_add=True, null=True)),
                ('schedule_status', models.IntegerField(default=0)),
                ('schedule_date', models.DateField(null=True)),
                ('emp_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.businessregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.TimeField(blank=True, default='', null=True)),
                ('end_date', models.TimeField(blank=True, default='', null=True)),
                ('leave_type', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('leave_reason', models.TextField(blank=True, default='', null=True)),
                ('leave_status', models.IntegerField(default=0)),
                ('leave_apply_date', models.DateField(null=True)),
                ('emp_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.businessregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compaint_head', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('compaint_content', models.TextField(blank=True, default='', null=True)),
                ('complaint_date', models.DateField(auto_now=True, null=True)),
                ('action', models.TextField(blank=True, default='', null=True)),
                ('action_date', models.DateField(null=True)),
                ('status', models.IntegerField(default=0)),
                ('complaint_emp_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.businessregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='ActionTaken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_from_id', models.IntegerField(default=0)),
                ('act_from_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('act_reason', models.TextField(blank=True, default='', null=True)),
                ('act_head', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('act_content', models.TextField(blank=True, default='', null=True)),
                ('action_date', models.DateField(null=True)),
                ('status', models.IntegerField(default=0)),
                ('act_emp_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.businessregister_details')),
            ],
        ),
    ]
