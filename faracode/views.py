from django.shortcuts import render
from projects_app.models import project
from contactus_app.models import Message

def home(request):
    projects = project.objects.all()
    
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Sub = request.POST.get('sub')
        Body = request.POST.get('body')
        Message.objects.create(name=Name, email=Email, sub=Sub, body=Body)



    return render(request, 'index.html', context={'projects': projects})