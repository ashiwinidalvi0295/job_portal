from django.urls import path
from jobapp import views

urlpatterns = [
    path('', views.index_view),
    path('register/', views.register_view),
    path('home/', views.homepage_view),
    path('profile/', views.profile_view),
    path('save-profile/<int:id>/', views.save_profile_view),
    path('add-it/', views.add_it_job_form_view),
    path('update-it/<int:id>/', views.update_it_job_form_view),
    path('del-it/<int:id>/', views.del_it_job_form_view),
    path('it-job/', views.it_jobs_view),
    path('add-mech/', views.add_mech_job_form_view),
    path('update-mech/<int:id>/', views.update_mech_job_form_view),
    path('del-mech/<int:id>/', views.del_mech_job_form_view),
    path('mech-job/', views.mech_jobs_view),
    path('add-civil/', views.add_civil_job_form_view),
    path('update-civil/<int:id>/', views.update_civil_job_form_view),
    path('del-civil/<int:id>/', views.del_civil_job_form_view),
    path('civil-job/', views.civil_jobs_view),
    path('apply-job/<int:id>/<str:cat>/', views.apply_job_view),

]
