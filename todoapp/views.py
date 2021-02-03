from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import Tasks,Profile
from django.views.generic import CreateView, ListView
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt



# Create your views here
@login_required(login_url='login')
def index(request):
    tasks = Tasks.objects.all()

    form = TasksForm()

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form': form}
    return render(request, 'index.html', context)
	



class TaskCreateView(CreateView):
    model = Tasks
    template_name = 'update_task.html'   
    fields= ['title','complete']    


@csrf_exempt
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form =CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Account was created successfully')
                return redirect('login')
        context = {'form': form}
    return render(request,'registration/register.html',  context)

@csrf_exempt
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username ,password=password)
            if user is not None:   
                login(request, user)
        context={}
        return render(request,'registration/login.html',  context) 

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)



