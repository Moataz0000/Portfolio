from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Skill, FAQ, Project
from .forms import EmailForm
from django.core.mail import send_mail
import os
from django.http import FileResponse, Http404

def main(request):
    mySkill = Skill.objects.all()
    myFAQ = FAQ.objects.all()
    projects = Project.objects.all()

    sent = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # name = f"From :{cd['name']}"
            subject = f"{cd['subject']}"
            message = f"{cd['message']}"
            send_mail(subject , message , 'motazfawzy73@gmail.com' , [cd['email']])
            sent = True
    else:
        form = EmailForm() 
    context = {
        'myskills': mySkill,
        'myfaq': myFAQ,
        'projects': projects,
        'form': form,
        'sent': sent,
    }
    
    return render(request, 'portfolio/home.html', context)




def project_details(request, pk, slug):
    project_detail = get_object_or_404(Project, id=pk , slug=slug)
    context = {
        'details':project_detail,
    }
    return render(request, 'portfolio/project_details.html', context)





def download_cv(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'backend.pdf')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    else:
        raise Http404('File Not Found!')



def custom_404(request, exception):
    return render(request, '404.html', status=404)