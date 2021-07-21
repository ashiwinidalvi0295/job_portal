from django.shortcuts import render,redirect
from jobapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from jobapp.models import ITJobs, MechJobs, CivilJobs, JobsApplied, UserData

# Create your views here.
def index_view(request):
    return render(request,'jobapp/index.html')

def register_view(request):
    form=user_reg()
    if request.method == 'POST':
        form=user_reg(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. login to continue...")
            return redirect('/login/')

    return render(request,'jobapp/register.html',{'form':form})

@login_required(login_url='/login/')
def profile_view(request):
    if request.user.is_superuser:
        pdata = User.objects.all()
        data=[]
        for i in pdata:
            if i.is_superuser != True:
                temp={}
                sdata = UserData.objects.all().filter(user_id=i.id)
                temp['pdata'] = i
                if sdata:
                    temp['sdata'] = sdata[0]
                data.append(temp)
        return render(request, 'jobapp/user_profile_admin_view.html', {'data':data})
    else:
        pdata = User.objects.get(id=request.user.id)
        sdata = UserData.objects.all().filter(user_id=request.user.id)
        form1 = user_reg(instance=pdata)
        temp=None
        if sdata:
            form2 = user_profile_view(instance=sdata[0])
            temp=sdata[0]
        else:
            form2 = user_profile_view()
        return render(request, 'jobapp/user_profile_view.html', {'pdata': pdata, 'form2':form2, 'sdata': temp})

@login_required(login_url='/login/')
def save_profile_view(request,id):
    sdata = UserData.objects.all().filter(user_id=request.user.id)
    pdata = User.objects.get(id=request.user.id)
    if request.method   ==  'POST':
            if sdata:
                form    =   user_profile_view(request.POST, request.FILES, instance=sdata[0])
            else:
                form = user_profile_view(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return render(request,'jobapp/user_profile_view.html',{'pdata': pdata, 'form2':form})

@login_required(login_url='/login/')
def homepage_view(request):
    if request.user.is_superuser:
        jobm=[]
        t=MechJobs.objects.all()
        jobm.append(t)
        t=ITJobs.objects.all()
        jobm.append(t)
        t=CivilJobs.objects.all()
        jobm.append(t)
        print(jobm)
        return render(request, 'jobapp/home_admin.html', {'data':jobm})

    else:
        jobs=JobsApplied.objects.all().filter(user_id=request.user.id)
        pdata = User.objects.get(id=request.user.id)
        sdata = UserData.objects.all().filter(user_id=request.user.id)
        jobm=[]
        for i in jobs:
            if i.job_cat == "mech":
                t=MechJobs.objects.all().filter(id=i.job_id)
                jobm.append(t)
            if i.job_cat == "it":
                t=ITJobs.objects.all().filter(id=i.job_id)
                jobm.append(t)
            if i.job_cat == "civil":
                t=CivilJobs.objects.all().filter(id=i.job_id)
                jobm.append(t)
            temp=None
            if sdata:
                temp=sdata[0]
        print(jobm)
        return render(request, 'jobapp/home.html', {'data':jobm, 'pdata':pdata, 'sdata':temp})

def add_it_job_form_view(request):
    if request.user.is_superuser:
        form    =   add_it_job_form()
        if request.method   ==  'POST':
            form    =   add_it_job_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/it-job/')
            else:
                form    =   add_it_job_form()
        return render(request,'jobapp/add_it_job.html',{'form':form})
    else:
        return render(request,'jobapp/home.html')

def it_jobs_view(request):
    if request.user.is_superuser:
        data = ITJobs.objects.all()
        return render(request, 'jobapp/read_it.html', {'data':data})
    else:
        joba = JobsApplied.objects.all().filter(user_id = request.user.id)
        data = ITJobs.objects.all()
        return render(request, 'jobapp/it_jobs.html', {'data':data, 'jobsapplied':joba})

def update_it_job_form_view(request, id):
    data = ITJobs.objects.get(pk=id)
    form    =   update_it_job_form(instance=data)
    if request.method   ==  'POST':
        form    =   update_it_job_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/it-job/')
        else:
            form    =   update_it_job_form()
    return render(request,'jobapp/update_it_job.html',{'form':form})

def del_it_job_form_view(request, id):
    data = ITJobs.objects.get(pk=id)
    data.delete()
    return redirect('/it-job/')

def add_mech_job_form_view(request):
    form    =   add_mech_job_form()
    if request.method   ==  'POST':
        form    =   add_mech_job_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mech-job/')

        else:
            form    =   add_mech_job_form()
    return render(request,'jobapp/add_mech_job.html',{'form':form})

def mech_jobs_view(request):
    if request.user.is_superuser:
        data = MechJobs.objects.all()
        return render(request, 'jobapp/read_mech.html', {'data':data})
    else:
        joba = JobsApplied.objects.all().filter(user_id = request.user.id)
        data = MechJobs.objects.all()
        return render(request, 'jobapp/mech_jobs.html', {'data':data , 'jobsapplied': joba, 'temp':0})

def update_mech_job_form_view(request, id):
    data = MechJobs.objects.get(pk=id)
    form    =   update_mech_job_form(instance=data)
    if request.method   ==  'POST':
        form    =   update_mech_job_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/mech-job/')
        else:
            form    =   update_mech_job_form()
    return render(request,'jobapp/update_mech_job.html',{'form':form})

def del_mech_job_form_view(request, id):
    data = MechJobs.objects.get(pk=id)
    data.delete()
    return redirect('/mech-job/')

def add_civil_job_form_view(request):
    form    =   add_civil_job_form()
    if request.method   ==  'POST':
        form    =   add_civil_job_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            form    =   add_civil_job_form()
    return render(request,'jobapp/add_civil_job.html',{'form':form})

def civil_jobs_view(request):
    if request.user.is_superuser:
        data = CivilJobs.objects.all()
        return render(request, 'jobapp/read_civil.html', {'data':data})
    else:
        joba = JobsApplied.objects.all().filter(user_id = request.user.id)
        data = CivilJobs.objects.all()
        return render(request, 'jobapp/civil_jobs.html', {'data':data,'jobsapplied':joba})

def update_civil_job_form_view(request, id):
    data = CivilJobs.objects.get(pk=id)
    form    =   update_civil_job_form(instance=data)
    if request.method   ==  'POST':
        form    =   update_civil_job_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/civil-job/')
        else:
            form    =   update_civil_job_form()
    return render(request,'jobapp/update_civil_job.html',{'form':form})

def del_civil_job_form_view(request, id):
    data = CivilJobs.objects.get(pk=id)
    data.delete()
    return redirect('/civil-job/')

def apply_job_view(request,id,cat):
            ja=JobsApplied(user_id=request.user.id, job_id=id, job_cat=cat)
            ja.save()
            return redirect("/home/")
