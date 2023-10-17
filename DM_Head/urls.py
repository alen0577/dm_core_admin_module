from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   
    # Head Module --------------------------------

    path('Head-Dashboard',views.head_dashboard,name='head_dashboard'),
    path('Head-Logout',views.head_logout,name='head_logout'),

    # Profile ------------------------------

    path('Profile',views.head_profile,name='head_profile'),
    path('Profile-Update',views.profile_detailsUpdate,name='profile_detailsUpdate'),
    path('Profile-Image\Remove',views.profileImage_remove,name='profileImage_remove'),

    # Password ----------------------------

    path('Password',views.head_password,name='head_password'),
    path('Password-Update',views.user_passwordUpdate,name='user_passwordUpdate'),


    # Work Section ---------------------

    path('Work-Section',views.Head_work_section,name='Head_work_section'),
    path('Work-Create-Client',views.head_createClient,name='head_createClient'),
    path('Work-Create',views.head_createWork,name='head_createWork'),
    path('Work-View-Edit',views.head_WorkviewEdit,name='head_WorkviewEdit'),
    path('Work-Allocate',views.head_allocateWok,name='head_allocateWok'),
    path('Work-Progress',views.head_WorkProgress,name='head_WorkProgress'),
    path('Work-Tasks',views.head_tasksForWork,name='head_tasksForWork'),
    
    
    # Employees Section -----------------

    path('Employees-Section',views.Head_employees_section,name='Head_employees_section'),
    path('Employees-View',views.head_viewEmployees,name='head_viewEmployees'),
    path('Employees-Allocate',views.head_employeeAllocate,name='head_employeeAllocate'),
    path('Employees-Allocate-List',views.head_employeeAllocated_list,name='head_employeeAllocated_list'),
    
    
    

    #Schedule ----------------------------

    path('Schedule',views.head_schedule,name='head_schedule'),
     
    path('Head-schedule-save',views.head_schedule_save,name='head_schedule_save'),
    path('Head-schedule-Edit',views.ScheduleEdit,name='ScheduleEdit'),
    path('Head-update_schedule_status',views.update_schedule_status,name='update_schedule_status'),
    path('Head-schedule-remove/<int:pk>',views.head_scheduleRemove,name='head_scheduleRemove'),
    path('Head-Employees-schedule',views.head_employees_schedule,name='head_employees_schedule'),
    path('Head-Employees-scheduleAdd',views.head_employee_scheduleAdd,name='head_employee_schrduleAdd'),
    path('Head-Employees-scheduleEdit/<int:pk>',views.head_employeeScheduleEdit,name='head_employeeScheduleEdit'),
    path('Head-schedule-view',views.head_scheduleFilter,name='head_scheduleFilter'),
    

    # Feedback  --------------------------

    path('Head-Feedback',views.head_feedback,name='head_feedback'),
    path('Head-Feedback-Type-Change',views.feedback_Typechange,name='feedback_Typechange'),
    

    # Complaints --------------------------

    path('Head-Complaints',views.head_complaints,name='head_complaints'),

    # Action Taken  --------------------------

    path('Head-Action-Taken',views.head_actionTaken,name='head_actionTaken'),
    path('Head-EditAction-Taken/<int:pk>',views.head_action_takenEdit,name='head_action_takenEdit'),
    

    # Notification ----------------------

    path('Head-Notification',views.head_allnotification,name='head_allnotification'),
    path('Head-Notification-Update',views.head_notificationUpdate,name='head_notificationUpdate'),
    path('Head-Notification-Remove',views.head_delete_notifications,name='head_delete_notifications'),

    # Leave ---------------------------
    
    path('Head-Leave',views.head_leave,name='head_leave'),
    path('Head-Approve-Reject',views.head_leaveApprove_Reject,name='head_leaveApprove_Reject'),
    path('Head-Leave-Seach',views.head_leaveSearch,name='head_leaveSearch'),
    
    

    

    
    

    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)