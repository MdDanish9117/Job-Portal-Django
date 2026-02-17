from django.shortcuts import render,redirect
from .models import user , job
# Create your views here.


def register(request):
    if request.method == 'POST':
        user.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            passsword=request.POST['password']
        )
        return redirect('login')
    return render(request,'register.html')



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = user.objects.get(email=email, password=password)
            request.session['user'] = user.name
            return redirect('dashboard')
        except:
            return render(request,'login.html',{'error':'Invalid Login'})

    return render(request,'login.html')
def dashboard(request):
    return render(request,'dashboard.html')


def post_job(request):
    if request.method == 'POST':
        job.objects.create(
            title=request.POST['title'],
            company=request.POST['company'],
            description=request.POST['description']
        )
        return redirect('jobs')
    return render(request,'post_job.html')

def jobs(request):
    data = job.objects.all()
    return render(request,'jobs.html',{'jobs':data})
