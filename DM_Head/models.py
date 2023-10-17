from django.db import models
from  Registration_Login.models import EmployeeRegister_Details,BusinessRegister_Details


class EmployeeSchedule(models.Model):
    emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    start_time = models.TimeField(auto_now=False,default='',null=True,blank=True)
    end_time = models.TimeField(auto_now=False,default='',null=True,blank=True)
    schedule_head = models.CharField(max_length=255,default='',null=True,blank=True)
    todo_content = models.TextField(default='',null=True,blank=True)
    log_time = models.TimeField(auto_now_add=True,null=True,blank=True)
    schedule_status = models.IntegerField(default=0)
    schedule_date = models.DateField(auto_now=False,null=True)


class Feedback(models.Model):
    
    feedback_emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    from_id = models.IntegerField(default=0)
    from_name = models.CharField(max_length=255,default='',null=True,blank=True)
    feedback_content = models.TextField(default='',null=True,blank=True)
    feedback_date = models.DateField(auto_now=False,null=True)

class Complaints(models.Model):
    complaint_emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    compaint_head = models.CharField(max_length=255,default='',null=True,blank=True)
    compaint_content = models.TextField(default='',null=True,blank=True)
    complaint_date = models.DateField(auto_now=True,null=True)
    action = models.TextField(default='',null=True,blank=True)
    action_date = models.DateField(auto_now=False,null=True)
    status = models.IntegerField(default=0)
    
class ActionTaken(models.Model):
    act_emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    act_from_id = models.IntegerField(default=0)
    act_from_name = models.CharField(max_length=255,default='',null=True,blank=True)
    act_reason = models.TextField(default='',null=True,blank=True)
    act_head = models.CharField(max_length=255,default='',null=True,blank=True)
    act_content = models.TextField(default='',null=True,blank=True)
    action_date = models.DateField(auto_now=False,null=True)
    status = models.IntegerField(default=0)


class Notification(models.Model):
    emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    notific_head = models.CharField(max_length=255,default='',null=True,blank=True)
    notific_content = models.TextField(default='',null=True,blank=True)
    notific_time = models.TimeField(auto_now_add=True,null=True,blank=True)
    notific_status = models.IntegerField(default=0)
    notific_date = models.DateField(auto_now=True,null=True)


class EmployeeLeave(models.Model):
    emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    start_date = models.DateField(auto_now=False,default='',null=True,blank=True)
    end_date = models.DateField(auto_now=False,default='',null=True,blank=True)
    leave_type = models.CharField(max_length=255,default='',null=True,blank=True)
    leave_reason = models.TextField(default='',null=True,blank=True)
    no_of_days = models.IntegerField(default=0)
    leave_status = models.IntegerField(default=0)
    leave_apply_date = models.DateField(auto_now=False,null=True)
    leave_statuChange_date = models.DateField(auto_now=False,null=True)


class Allocation_Details(models.Model):
    allocatEmp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    allocat_to = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, related_name="EmployeeRegister", null=True,default='')
    allocate_status = models.IntegerField(default=0)
    alloaction_date = models.DateField(auto_now=False,null=True)


class Previos_Allocation_Details(models.Model):
    allocate_id = models.ForeignKey(Allocation_Details, on_delete=models.CASCADE, null=True,default='')
    newallocation_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    previous_from_date = models.DateField(auto_now=False,null=True)
    previous_to_date = models.DateField(auto_now=False,null=True)
    previousemp_id = models.IntegerField(default=0)
    previousemp_name = models.CharField(max_length=255,default='',null=True,blank=True)
    previousemp_allocatedTo = models.IntegerField(default=0)
    previousemp_allocatedName = models.CharField(max_length=255,default='',null=True,blank=True)


    

# Work section -------------------------

class Work_Task(models.Model):
    comp_taskid = models.ForeignKey(BusinessRegister_Details, on_delete=models.CASCADE, null=True,default='') 
    task_name = models.CharField(max_length=255,default='',null=True,blank=True)
    task_discription = models.TextField(default='',null=True,blank=True)
    task_add_time = models.TimeField(auto_now_add=True,null=True,blank=True)
    task_status = models.IntegerField(default=0)
    task_add_date = models.DateField(auto_now=True,null=True)


class ClientRegister(models.Model):
    compId = models.ForeignKey(BusinessRegister_Details, on_delete=models.CASCADE, null=True,default='') 
    client_name = models.CharField(max_length=255,default='',null=True,blank=True)
    client_email_primary = models.EmailField(default='client@gmail.com',null=True,blank=True)
    client_email_alter = models.EmailField(default='client@gmail2.com',null=True,blank=True)
    client_phone = models.CharField(max_length=255,default='9000000009',null=True,blank=True)
    client_phone_alter = models.CharField(max_length=255,default='9800000089',null=True,blank=True)
    client_address1 = models.CharField(max_length=255,default='',null=True,blank=True)
    client_address2 = models.CharField(max_length=255,default='',null=True,blank=True)
    client_address3 = models.CharField(max_length=255,default='',null=True,blank=True)
    client_pincode = models.CharField(max_length=255,default='',null=True,blank=True)
    client_district = models.CharField(max_length=255,default='',null=True,blank=True)
    client_state = models.CharField(max_length=255,default='',null=True,blank=True)
    client_profile = models.ImageField(upload_to='client\profile',default='')
    

    # Bussiness Details ---

    client_bussiness_email_primary = models.EmailField(default='client@gmail.com',null=True,blank=True)
    client_bussiness_email_alter = models.EmailField(default='client@gmail2.com',null=True,blank=True)
    client_bussiness_phone = models.CharField(max_length=255,default='9000000009',null=True,blank=True)
    client_bussiness_website = models.CharField(max_length=255,default='',null=True,blank=True)
    client_bussiness_phone_alter = models.CharField(max_length=255,default='9800000089',null=True,blank=True)
    client_bussiness_address1 = models.CharField(max_length=255,default='',null=True,blank=True)
    client_bussiness_address2 = models.CharField(max_length=255,default='',null=True,blank=True)
    client_bussiness_address3 = models.CharField(max_length=255,default='',null=True,blank=True)
    client_bussiness_pincode = models.CharField(max_length=255,default='',null=True,blank=True)
    client_bussiness_district = models.CharField(max_length=255,default='',null=True,blank=True)
    client_bussiness_state = models.CharField(max_length=255,default='',null=True,blank=True)
    client_bussiness_file = models.FileField(upload_to='client\files',default='')
    bussiness_logo = models.ImageField(upload_to='client\logo',default='')

    more_discription = models.TextField(default='',null=True,blank=True)
    client_add_time = models.TimeField(auto_now_add=True,null=True,blank=True)
    client_status = models.IntegerField(default=0)
    client_reg_date = models.DateField(auto_now=True,null=True)


class WorkRegister(models.Model):
    clientId = models.ForeignKey(ClientRegister, on_delete=models.CASCADE, null=True,default='') 
    work_discription = models.TextField(default='',null=True,blank=True)
    work_create_time = models.TimeField(auto_now_add=True,null=True,blank=True)
    work_file = models.FileField(upload_to='work\files',default='')
    work_progress = models.IntegerField(default=0)
    work_allocate_status = models.IntegerField(default=0)
    work_status = models.IntegerField(default=0)
    work_create_date = models.DateField(auto_now=False,null=True)
    work_end_date = models.DateField(auto_now=False,null=True)


class ClientTask_Register(models.Model):
    client_Id = models.ForeignKey(ClientRegister, on_delete=models.CASCADE, null=True,default='') 
    work_Id = models.ForeignKey(WorkRegister, on_delete=models.CASCADE, null=True,default='') 
    task_discription = models.TextField(default='',null=True,blank=True)
    task_file = models.FileField(upload_to='work\task\files',default='')
    task_allocate_status = models.IntegerField(default=0)
    task_status = models.IntegerField(default=0)
    task_create_date = models.DateField(auto_now=False,null=True)
