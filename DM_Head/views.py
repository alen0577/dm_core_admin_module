from django.shortcuts import render,redirect
from Registration_Login.models import *
from .models import *
from django.core import serializers
from django.db.models import Q
from django.utils import timezone
from datetime import date, datetime,timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Count


def head_dashboard(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

           # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_dashboard.html',content)

    else:
            return redirect('/')



# Profile Page -------------------------
def head_profile(request):  
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_profile.html',content)

    else:
            return redirect('/')
    

    
def profile_detailsUpdate(request):
     
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')


        # Details Save -----------------

        if request.POST:
             
             emp_obj = EmployeeRegister_Details.objects.get(id=dash_details.id)

             emp_obj.emp_name = request.POST['empname']
             emp_obj.emp_contact_no = request.POST['contactno']
             emp_obj.emp_email = request.POST['empEmail']
             emp_obj.emp_address1 = request.POST['add1']
             emp_obj.emp_address2 = request.POST['add2']
             emp_obj.emp_address3 = request.POST['add3']
             emp_obj.emp_pin = request.POST['pincode']
             emp_obj.emp_location = request.POST['loc']
             emp_obj.emp_district = request.POST['empdist']
             emp_obj.emp_state = request.POST['empState']

             if request.FILES.get('empProfile'):
                emp_obj.emp_profile = request.FILES.get('empProfile')

             else:
                emp_obj.emp_profile =  emp_obj.emp_profile 

             if request.FILES.get('empResume'):
                emp_obj.emp_file = request.FILES.get('empResume')

             else:
                emp_obj.emp_file =  emp_obj.emp_file 

             emp_obj.save()
             success_text = 'Profile Details Updated.'
             success = True

             dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        
             content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'success_text':success_text,
                    'success':success}

        else:
            error_text = 'Profile Details Updated.'
            error = True
            content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'error_text':error_text,
                    'error':error}

        return render(request,'HD_profile.html',content)

    else:
            return redirect('/')
    

# Remove Profile Image ---------------

def profileImage_remove(request):
    emp_id = request.POST.get('emp_id')
    dash_details = EmployeeRegister_Details.objects.get(id=emp_id)
    dash_details.emp_profile = ''
    dash_details.save()
    return JsonResponse({'message': 'Received emp_id: ' + emp_id})
     
# End ------------------------------------------------


# Password Section -----------------------------------

def head_password(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_password.html',content)

    else:
            return redirect('/')


def user_passwordUpdate(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        if request.POST:
           
           emp_dash.log_username = request.POST['emp_uname']
           emp_dash.log_password = request.POST['emp_password']

           emp_dash.save()  
           success = True
           success_text = 'User name or password change.'
        
           content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'success':success,
                   'success_text':success_text}
        else:

            error=True
            error_text = 'Oops! something went wrong.'
            content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'error':error,
                    'error_text':error_text}

        return render(request,'HD_password.html',content)

    else:
            return redirect('/')


# Work section  ----------------------------------

def Head_work_section(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_workSection.html',content)

    else:
            return redirect('/')


def head_createClient(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        if request.POST:
             
            client_obj = ClientRegister()

            client_obj.compId = dash_details.emp_comp_id
            client_obj.client_name = request.POST['cName']
            client_obj.client_email_primary = request.POST['cName']
            client_obj.client_email_alter = request.POST['cName']
            client_obj.client_name = request.POST['cName']
            client_obj.client_name = request.POST['cName']
            client_obj.client_name = request.POST['cName']

            client_obj.save()
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_createClient.html',content)

    else:
            return redirect('/')


def head_createWork(request): 

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        Tasks = Work_Task.objects.filter(comp_taskid=dash_details.emp_comp_id.id)

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'Tasks':Tasks}

        return render(request,'HD_workCreate.html',content)

    else:
            return redirect('/')


def head_WorkviewEdit(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_Viem_Edit.html',content)

    else:
            return redirect('/')
    

def head_allocateWok(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_workAllocate.html',content)

    else:
            return redirect('/')


def head_WorkProgress(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_workProgress.html',content)

    else:
            return redirect('/')    


def head_tasksForWork(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        data_box = {}
        if request.POST:
             
            taskName = request.POST['task_name']
            taskDiscription = request.POST['task_discription']

            task_obj = Work_Task()
            task_obj.task_name = taskName
            task_obj.task_discription = taskDiscription
            task_obj.comp_taskid = dash_details.emp_comp_id
            task_obj.save()
            success = True
            success_text= 'Task add successful.' 
                
            data_box = {'success':success,'success_text':success_text}
            
            
        Tasks = Work_Task.objects.filter(comp_taskid=dash_details.emp_comp_id.id)

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'Tasks':Tasks}
        
        content = {**data_box, **content}

        return render(request,'HD_workTasks.html',content)

    else:
            return redirect('/')
     


# Employee Section ---------------------------------


def Head_employees_section(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_employeeSection.html',content)

    else:
            return redirect('/')    


def head_viewEmployees(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=dash_details.emp_comp_id)
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,'employees':employees}

        return render(request,'HD_employeeView.html',content)

    else:
            return redirect('/')    


def head_employeeAllocate(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

          # Team Leads featch----
        Team_leads_desig_obj = DesignationRegister_details.objects.get(dashboard_id=2) 
        Team_leads = EmployeeRegister_Details.objects.filter(emp_designation_id=Team_leads_desig_obj)
        TeamLead_emp_ids = [leads.id for leads in Team_leads]

        data_box ={}

        if request.POST:
            allocateTo =  request.POST['alocated_to']
            employee_list = request.POST.getlist('selected_emp')
            dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

            count_allocate = 0

            for emp_id in employee_list:
                allocate_obj = Allocation_Details()
                allocate_obj.allocatEmp_id = EmployeeRegister_Details.objects.get(id=int(emp_id))
                allocate_obj.allocat_to = EmployeeRegister_Details.objects.get(id=int(allocateTo))
                allocate_obj.allocate_status = 1
                allocate_obj.alloaction_date = date.today()
                allocate_obj.save()
                count_allocate =count_allocate +  1
                success = True
                success_text= str(count_allocate) + " " +'Allocation successful.' 
                
                data_box = {'success':success,'success_text':success_text}


             
        # Allocated Employees -------------------
        allocated_emp = Allocation_Details.objects.filter(allocate_status=1)
        allocated_emp_ids = [allocation.allocatEmp_id.id for allocation in allocated_emp]

        # Pending to allocate ------------
        allocate_employees = EmployeeRegister_Details.objects.filter(
            emp_comp_id=dash_details.emp_comp_id).exclude(
            id__in=allocated_emp_ids).exclude(
            id=dash_details.id).exclude(
            id__in=TeamLead_emp_ids)
        
        allocation_counts = Allocation_Details.objects.values('allocat_to__id', 'allocat_to__emp_name').annotate(count=Count('allocatEmp_id'))
        

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'Team_leads':Team_leads,
                   'employees':allocate_employees,
                   'allocation_counts':allocation_counts}
        
        content = {**data_box, **content}

        return render(request,'HD_employeeAllocate.html',content)

    else:
            return redirect('/')    


def head_employeeAllocated_list(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=dash_details.emp_comp_id)

        Team_leads_desig_obj = DesignationRegister_details.objects.get(dashboard_id=2) 
        Team_leads = EmployeeRegister_Details.objects.filter(emp_designation_id=Team_leads_desig_obj)
        TeamLead_emp_ids = [leads.id for leads in Team_leads]
        
        allocated_employees = Allocation_Details.objects.filter(allocat_to__in=TeamLead_emp_ids).order_by('allocat_to')

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'allocated_employees':allocated_employees,
                   'Team_leads':Team_leads,
                   'employees':employees}

        return render(request,'HD_employeeAllocatedList.html',content)

    else:
            return redirect('/')    

     

#Schedule -------------------------------------------

def head_schedule(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
         # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
          
        today = date.today()
        schedules = EmployeeSchedule.objects.filter(emp_id=dash_details,schedule_date=today)
        schedule_days = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today).values('schedule_date').distinct()

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'schedules':schedules,
                   'schedule_days':schedule_days}

        return render(request,'HD_dayTaskschedule.html',content)

    else:
            return redirect('/')
    
    
def head_scheduleRemove(request,pk):
     
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
         # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        schedule_remove = EmployeeSchedule.objects.get(id=pk)
        schedule_remove.delete()  

        error = True
        error_text = 'Schedule task removed'
        
        today = date.today()
        schedules = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today)
        schedule_days = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today).values('schedule_date').distinct()

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'schedules':schedules,
                   'schedule_days':schedule_days,'error':error,'error_text':error_text}

        return render(request,'HD_dayTaskschedule.html',content)

    else:
            return redirect('/')
    

def head_schedule_save(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        schedules = None
        schedule_days = None

        if request.POST:

            if request.POST['scheduleId']:

                schedule_obj = EmployeeSchedule.objects.get(id=int(request.POST['scheduleId']))

                schedule_obj.emp_id=dash_details
                schedule_obj.start_time=request.POST['stime']
                schedule_obj.end_time=request.POST['etime']
                schedule_obj.schedule_head=request.POST['task_head']
                schedule_obj.todo_content=request.POST['task_content']
                schedule_obj.log_time = timezone.now()
                schedule_obj.schedule_date = date.today()
                schedule_obj.save()

                today = date.today()
                schedules = EmployeeSchedule.objects.filter(emp_id=dash_details,schedule_date=today)
                schedule_days = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today).values('schedule_date').distinct()
                success_text = 'Schedule edit successful.'
                success = True

            else:

    
                schedule_obj = EmployeeSchedule()

                schedule_obj.emp_id=dash_details
                schedule_obj.start_time=request.POST['stime']
                schedule_obj.end_time=request.POST['etime']
                schedule_obj.schedule_head=request.POST['task_head']
                schedule_obj.todo_content=request.POST['task_content']
                schedule_obj.log_time = timezone.now()
                schedule_obj.schedule_date = request.POST['schedule_date']

                schedule_obj.save()

                today = date.today()
                schedules = EmployeeSchedule.objects.filter(emp_id=dash_details,schedule_date=today)
                schedule_days = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today).values('schedule_date').distinct()

                success_text = 'Schedule save successful.'
                success = True

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'success_text':success_text,
                   'success':success,
                   'schedules':schedules,
                   'schedule_days':schedule_days}

        return render(request,'HD_dayTaskschedule.html',content)

    else:
            return redirect('/')


def ScheduleEdit(request):

    schedule_id = request.GET.get('scheduleid')
    try:
            schedule = EmployeeSchedule.objects.get(id=schedule_id)
           
            data = {
                'scheduleid':schedule.id,
                'start_time': schedule.start_time,
                'end_time': schedule.end_time,
                'task_head': schedule.schedule_head,
                'task_content': schedule.todo_content,
            }
            return JsonResponse(data)
    except EmployeeSchedule.DoesNotExist:
            return JsonResponse({'error': 'Schedule not found'}, status=404)  


def update_schedule_status(request):
        schedule_id = request.POST.get('schedule_id')
        checked = request.POST.get('checked')

        # Retrieve the schedule by ID
        schedule = EmployeeSchedule.objects.get(id=schedule_id)
        if schedule.schedule_status == 0:
            schedule.schedule_status =  1
        else: 
            schedule.schedule_status =  0
        schedule.save()
        return JsonResponse({'success': True})


def head_employees_schedule(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        
        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company).exclude(Q(id=dash_details.id))

        success_text, schedules, employee_name = None, None, None
        success = False

        today = date.today()

        if request.POST:   

                employee_id= int(request.POST['employeeId'])
                schedules = EmployeeSchedule.objects.filter(emp_id__id=employee_id,schedule_date__gte=today,
                schedule_date__lte=today).order_by('start_time')

                employee_name = EmployeeRegister_Details.objects.get(id=employee_id)
            
        

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,'success':success,
                   'today':today,'success_text':success_text,
                   'employees':employees,'schedules':schedules,'employee_name':employee_name}

        return render(request,'HD_employees_dayTaskschedule.html',content)

    else:
            return redirect('/')
    
     
def head_employee_scheduleAdd(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        
        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company).exclude(Q(id=dash_details.id))

        

        today = date.today()

        if request.POST:   

            employee_id= int(request.POST['add_employeeId'])
                 
            schedule_obj = EmployeeSchedule()

            schedule_obj.emp_id=EmployeeRegister_Details.objects.get(id=employee_id)
            schedule_obj.start_time=request.POST['stime']
            schedule_obj.end_time=request.POST['etime']
            schedule_obj.schedule_head=request.POST['task_head']
            schedule_obj.todo_content=request.POST['task_content']
            schedule_obj.log_time = timezone.now()
            schedule_obj.schedule_date = request.POST['schedule_date']

            schedule_obj.save()

            emp_obj=EmployeeRegister_Details.objects.get(id=int(request.POST['add_employeeId']))

            schedules = EmployeeSchedule.objects.filter(emp_id__id=int(request.POST['add_employeeId']),schedule_date__gte=today,
            schedule_date__lte=today).order_by('start_time')
            
            success_text = 'Schedule saved for ' + emp_obj.emp_name + ' successfully.'
            success = True      

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,'success':success,
                   'today':today,'success_text':success_text,
                   'employees':employees,'schedules':schedules,
                   'employee_name':emp_obj}

            return render(request,'HD_employees_dayTaskschedule.html',content)
      
        

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,'employees':employees}

        return render(request,'HD_employees_dayTaskscheduleAdd.html',content)

    else:
            return redirect('/')

    
def head_employeeScheduleEdit(request,pk):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        
        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company).exclude(Q(id=dash_details.id))

        schedules = EmployeeSchedule.objects.get(id=pk)

        today = date.today()

        if request.POST:   

            employee_id= int(request.POST['add_employeeId'])
                 
            schedule_obj = EmployeeSchedule()

            schedule_obj.emp_id=EmployeeRegister_Details.objects.get(id=employee_id)
            schedule_obj.start_time=request.POST['stime']
            schedule_obj.end_time=request.POST['etime']
            schedule_obj.schedule_head=request.POST['task_head']
            schedule_obj.todo_content=request.POST['task_content']
            schedule_obj.log_time = timezone.now()
            schedule_obj.schedule_date = request.POST['schedule_date']

            schedule_obj.save()

            emp_obj=EmployeeRegister_Details.objects.get(id=int(request.POST['add_employeeId']))

            schedules = EmployeeSchedule.objects.filter(emp_id__id=int(request.POST['add_employeeId']),schedule_date__gte=today,
            schedule_date__lte=today).order_by('start_time')
            
            success_text = 'Schedule saved for ' + emp_obj.emp_name + ' successfully.'
            success = True      

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,'success':success,
                   'today':today,'success_text':success_text,
                   'employees':employees,'schedules':schedules,
                   'employee_name':emp_obj}

            return render(request,'HD_employees_dayTaskschedule.html',content)
      
        

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,'schedules':schedules,
                   'employees':employees}

        return render(request,'HD_employees_dayTaskscheduleAdd.html',content)

    else:
            return redirect('/')


def head_scheduleFilter(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

          # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company).exclude(Q(id=dash_details.id))
      

        schedules = None 
        emp_obj=None
        today = date.today()

        if request.POST:
             
            empId = request.POST['emp_name']
            from_date = request.POST['fDate']
            to_date = request.POST['toDate']
       

            if empId != '0' and from_date and to_date :

                emp_obj = EmployeeRegister_Details.objects.get(id=empId)
                schedules = EmployeeSchedule.objects.filter(emp_id=emp_obj,schedule_date__gte=from_date,
                schedule_date__lte=to_date).order_by('emp_id')
            
            elif empId == '0' and from_date and to_date :

                schedules = EmployeeSchedule.objects.filter(emp_id__in=employees,schedule_date__gte=from_date,
                schedule_date__lte=to_date).order_by('emp_id')

            elif empId != '0' :

                emp_obj = EmployeeRegister_Details.objects.get(id=empId)
                schedules = EmployeeSchedule.objects.filter(emp_id=emp_obj,schedule_date__gte=today,
                schedule_date__lte=today).order_by('emp_id')

            else:
                schedules = EmployeeSchedule.objects.filter(emp_id__in=employees,schedule_date__gte=today,
                schedule_date__lte=today).order_by('emp_id')
        
        else:
            
            schedules = EmployeeSchedule.objects.filter(emp_id__in=employees,schedule_date__gte=today,
            schedule_date__lte=today).order_by('emp_id')
                 

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'schedules':schedules,'emp_obj':emp_obj}

        return render(request,'HD_scheduleFilter.html',content)

    else:
            return redirect('/')
     

# Feedback -------------------------

def head_feedback(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

          # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company)

        feedback_data = Feedback.objects.filter(feedback_emp_id__in=employees).exclude(
            Q(feedback_emp_id=dash_details) | Q(feedback_emp_id=None)).order_by('-id')


        # Saveing Feedback 
        if request.POST:

            feedback_obj = Feedback()
            feedback_obj.feedback_emp_id = EmployeeRegister_Details.objects.get(id=int(request.POST['to_id']))
            feedback_obj.from_id = dash_details.id
            feedback_obj.from_name = dash_details.emp_name
            feedback_obj.feedback_content = request.POST['feedback_content']
            feedback_obj.feedback_date = date.today()
            feedback_obj.save()

            success=True
            success_text = 'Feedback add successfully.'

            feedback_data =Feedback.objects.filter(feedback_emp_id__in=employees).exclude(
            Q(feedback_emp_id=dash_details) | Q(feedback_emp_id=None)).order_by('-id')

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,

                   'employees':employees,
                   'feedback_data':feedback_data,
                   'success':success,
                   'success_text':success_text}
        
        else:

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,

                   'employees':employees,
                   'feedback_data':feedback_data}

        return render(request,'HD_feedback.html',content)

    else:
            return redirect('/')


def feedback_Typechange(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company)

       

        selected_value = request.GET.get('value')
    
        if selected_value == '1':
            feedback_data =Feedback.objects.filter(feedback_emp_id__in=employees).exclude(
            Q(feedback_emp_id=dash_details) | Q(feedback_emp_id=None)).order_by('-id')
        else:
            feedback_data =Feedback.objects.filter(feedback_emp_id=dash_details).order_by('-id')
        
        data_list = []
        for feedback in feedback_data:
            data = {
                'feedback_date': feedback.feedback_date,
               
                'from_name': feedback.from_name,
                
                'to_name': feedback.feedback_emp_id.emp_name,
                'feedback_content': feedback.feedback_content
            }
            data_list.append(data)
        
        return JsonResponse(data_list, safe=False)
     

# Complaints ---------------------

def head_complaints(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company)
        complaints_data = Complaints.objects.filter(complaint_emp_id__in=employees).order_by('status')

        # Save action taken to the selected complaint
        if request.POST:
            complaints_obj = Complaints.objects.get(id=int(request.POST['complaintId']))
            complaints_obj.action = request.POST['action_content']
            complaints_obj.action_date = date.today()
            complaints_obj.status = 1
            complaints_obj.save()

            success=True
            success_text = 'Response add successfully.'
            complaints_data = Complaints.objects.filter(complaint_emp_id__in=employees).order_by('status')

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'complaints_data':complaints_data,
                   'success':success,
                   'success_text':success_text}

        else:

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'complaints_data':complaints_data}

        return render(request,'HD_complaints.html',content)

    else:
            return redirect('/')
     

# Action Taken -------------------

def head_actionTaken(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)
        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        
        action_taken_data = ActionTaken.objects.filter(act_emp_id__in=employees)

        # Save data
        if request.POST:
             
             action_taken_obj = ActionTaken()
             action_taken_obj.act_emp_id = EmployeeRegister_Details.objects.get(id=int(request.POST['action_employeeId']))
             action_taken_obj.act_from_id = dash_details.id
             action_taken_obj.act_from_name = dash_details.emp_name
             action_taken_obj.act_head = request.POST['reason_content_head']
             action_taken_obj.act_reason = request.POST['reason_content']
             action_taken_obj.act_content = request.POST['what_action_content']
             action_taken_obj.action_date = request.POST['action_taken_date']
             action_taken_obj.status = 1
             action_taken_obj.save()

             success=True
             success_text = 'Action taken add successfully.'
             action_taken_data = ActionTaken.objects.filter(act_emp_id__in=employees)

             content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'action_taken_data':action_taken_data,
                   'success':success,
                   'success_text':success_text}

        else:

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'action_taken_data':action_taken_data}

        return render(request,'HD_actionTaken.html',content)

    else:
            return redirect('/')


def head_action_takenEdit(request,pk):  
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)
        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        
        action_taken_data =  ActionTaken.objects.get(id=pk)

        # Edit and Save data
        if request.POST:
             
             action_taken_obj = ActionTaken.objects.get(id=pk)
             action_taken_obj.act_emp_id = EmployeeRegister_Details.objects.get(id=int(request.POST['action_employeeId']))
             action_taken_obj.act_from_id = dash_details.id
             action_taken_obj.act_from_name = dash_details.emp_name
             action_taken_obj.act_head = request.POST['reason_content_head']
             action_taken_obj.act_reason = request.POST['reason_content']
             action_taken_obj.act_content = request.POST['what_action_content']
             action_taken_obj.action_date = request.POST['action_taken_date']
             action_taken_obj.status = 1
             action_taken_obj.save()

             success=True
             success_text = 'Action taken edit successfully.'
             action_taken_data = ActionTaken.objects.filter(act_emp_id__in=employees)

             content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'action_taken_data':action_taken_data,
                   'success':success,
                   'success_text':success_text}
             
             return render(request,'HD_actionTaken.html',content)
        else:

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'action_taken_data':action_taken_data}
             

        return render(request,'HD_actionTakenedit.html',content)

    else:
            return redirect('/')  


# Leave ------------------------------

def count_weekdays(start_date, end_date):
    current_date = start_date
    weekdays_count = 0

    # Iterate through each date within the range
    while current_date <= end_date:
        # Check if the current date is a weekday (Monday to Saturday)
        if current_date.weekday() < 6:
            weekdays_count += 1
        
        # Move to the next day
        current_date += timedelta(days=1)

    return weekdays_count


def head_leave(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company).exclude(
            Q(id=dash_details.id) | Q(id=None)).order_by('-id')
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)

        leave_data = EmployeeLeave.objects.filter(emp_id=dash_details).order_by('-id')
        empleave_data = EmployeeLeave.objects.filter(emp_id__in=employees).exclude(
            Q(emp_id=dash_details) | Q(emp_id=None)).order_by('-id')
        leave_request = EmployeeLeave.objects.filter(leave_status=0)

        #save date 
        if request.POST:
             leave_obj = EmployeeLeave()
             leave_obj.start_date = request.POST['fromDate']
             leave_obj.end_date = request.POST['toDate']
             leave_obj.leave_type = request.POST['type_select']
             leave_obj.leave_reason = request.POST['reason_content']
             leave_obj.emp_id = dash_details
             leave_obj.leave_apply_date = date.today()

             # day calculation
             
             start_date_str = request.POST['fromDate']
             end_date_str = request.POST['toDate'] 

             # Convert the date strings to datetime objects
             start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
             end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

             # Calculate the difference in days
             weekdays_count = (count_weekdays(start_date, end_date))
             
             leave_obj.no_of_days = weekdays_count
             leave_obj.save()
             
             success=True
             success_text = 'Leave applied successfully, waiting for approvel.'

             leave_data = EmployeeLeave.objects.filter(emp_id=dash_details).order_by('-id')
        

             content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'empleave_data':empleave_data,
                   'leave_request':leave_request,
                   'success':success,
                   'success_text':success_text,'leave_data':leave_data}

        else:

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'employees':employees,
                   'empleave_data':empleave_data,
                   'leave_request':leave_request,
                   'notifications':notifications,
                   'leave_data':leave_data}

        return render(request,'HD_leave.html',content)

    else:
            return redirect('/')


def head_leaveApprove_Reject(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company).exclude(
            Q(id=dash_details.id) | Q(id=None)).order_by('-id')
        
        employees_leave = EmployeeRegister_Details.objects.filter(emp_comp_id=company)
        
        
        if request.method == 'POST':
            leave_id = request.POST.get('leaveId')
            action = request.POST.get('action')

            leave_obj = EmployeeLeave.objects.get(id=int(leave_id)) 

            if action == 'approve':
                leave_obj.leave_status = 1 
                leave_obj.leave_statuChange_date = date.today()
                leave_obj.save()

                # Adding Notification --------

                notification_obj = Notification()

                notification_obj.emp_id = dash_details
                notification_obj.notific_head = 'Leave Approved'
                notification_obj.notific_content = "I'm pleased to inform you that your request for " + str(leave_obj.leave_type) + "leave from " + str(leave_obj.start_date) + " to " + str(leave_obj.end_date) + " has been approved."


                notification_obj.save()
                
            elif action == 'reject':

                leave_obj.leave_status = 2
                leave_obj.leave_statuChange_date = date.today()
                leave_obj.save()

                   # Adding Notification --------

                notification_obj = Notification()

                notification_obj.emp_id = dash_details
                notification_obj.notific_head = 'Leave Rejectd'
                notification_obj.notific_content = "I regret to inform you that your request for " + leave_obj.leave_type + " from " + str(leave_obj.start_date) + " to " + str(leave_obj.end_date) + " has been reviewed and unfortunately, we are unable to approve it at this time."


                notification_obj.save()



            leave_data = EmployeeLeave.objects.filter(emp_id=dash_details).order_by('-id')
            empleave_data = EmployeeLeave.objects.filter(emp_id__in=employees_leave).order_by('-id')
            leave_request = EmployeeLeave.objects.filter(leave_status=0)
            
            # Serialize the leave_request queryset to JSON
            leave_request_json = serializers.serialize('json', leave_request)
            
            my_leave = render(request, 'HD_leaveAjaxresponse.html', {'leave_data': leave_data,'dash_details':dash_details}).content.decode('utf-8')
            employe_leave = render(request, 'HD_employeeLeave_ajaxresponse.html', {'emp_data': empleave_data,'employees':employees}).content.decode('utf-8')

        # Return the updated HTML content in the AJAX response
            response_data = {'html_content': employe_leave,'my_leave':my_leave,'leave_request':leave_request_json}
            return JsonResponse(response_data)

        # Return an error response if the request method is not POST
        return JsonResponse({'error': 'Invalid request method'}, status=400)
       

    else:
            return redirect('/')



def head_leaveSearch(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company).exclude(
            Q(id=dash_details.id) | Q(id=None)).order_by('-id')
        

        leave_data = EmployeeLeave.objects.filter(emp_id=dash_details).order_by('-id')
        empleave_data = EmployeeLeave.objects.filter(emp_id__in=employees).order_by('-id')
        leave_request = EmployeeLeave.objects.filter(leave_status=0)
        leave_request_json = serializers.serialize('json', leave_request)
        

        if request.method == 'POST':
            employeeid = request.POST.get('searchValue')
            fdate = request.POST.get('f_Date')
            edate = request.POST.get('e_Date')

            if fdate and edate :

                if  dash_details.id == int(employeeid):
                    try:
                        leave_data = EmployeeLeave.objects.filter(emp_id__id=int(employeeid),start_date__gte=fdate,end_date__lte=edate).order_by('-id')
                    except EmployeeLeave.DoesNotExist:
                        leave_data = EmployeeLeave.objects.filter(emp_id=dash_details).order_by('-id')
                    
                else:
                    try:
                        empleave_data = EmployeeLeave.objects.filter(emp_id__id=int(employeeid),start_date__gte=fdate,end_date__lte=edate).order_by('-id')
                    except EmployeeLeave.DoesNotExist:
                        empleave_data = EmployeeLeave.objects.filter(emp_id__in=employees).order_by('-id')
            else: 
                 
                 return redirect('head_leave')

            my_leave = render(request, 'HD_leaveAjaxresponse.html', {'leave_data': leave_data,'dash_details':dash_details}).content.decode('utf-8')
            employe_leave = render(request, 'HD_employeeLeave_ajaxresponse.html', {'emp_data': empleave_data,'employees':employees}).content.decode('utf-8')

            response_data = {'html_content': employe_leave,'my_leave':my_leave,'leave_request':leave_request_json}
            return JsonResponse(response_data)

        # Return an error response if the request method is not POST
        return JsonResponse({'error': 'Invalid request method'}, status=400)
       

    else:
            return redirect('/')
    

# Notification -----------------------


def head_allnotification(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        notifications_data = Notification.objects.filter(Q(notific_status=0) | Q(notific_status=1),emp_id=dash_details,).order_by('-notific_date')
        
        

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'notifications_data':notifications_data}

        return render(request,'HD_allnotification.html',content)

    else:
            return redirect('/')


def head_notificationUpdate(request):
    
    if request.method == 'POST':
        notification_id = request.POST.get('notification_id')
        
        try:
            notification = Notification.objects.get(pk=notification_id)
            notification.notific_status = 1
            notification.save()
            return JsonResponse({'status': 'success', 'message': 'Notification status updated'})
            

        except Notification.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Notification not found'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


@method_decorator(csrf_exempt, name='dispatch')
def head_delete_notifications(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids[]')

        try:
            # Delete notifications with the selected IDs
            Notification.objects.filter(id__in=selected_ids).update(notific_status=2)
            return JsonResponse({'status': 'success', 'message': 'Notifications deleted successfully'})
        except Notification.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Notification not found'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def head_logout(request):
    request.session.pop('emp_id', None)
    return redirect('login_page')
