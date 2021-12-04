from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.
def accept(request):

    def __str__(self):
        return self.name

    if request.method =="POST":
        name= request.POST.get('name','')
        mobno= request.POST.get('mobno','')
        email= request.POST.get('email','')
        degree= request.POST.get('degree','')
        school=request.POST.get('school','')
        uni= request.POST.get('uni','')
        summary= request.POST.get('summary','')
        previous_work= request.POST.get('previous_work','')
        skills= request.POST.get('skills','')

        profile= Profile(name=name,mobno=mobno,email=email,degree=degree,school=school,uni=uni,summary=summary,previous_work=previous_work,skills=skills)
        profile.save()

    return render(request,'pdf/accept.html')



def resume(request,id):
    user_profile= Profile.objects.get(pk=id)
    template= loader.get_template('pdf/resume.html')
    html= template.render({'user_profile':user_profile})
    options={
       'page-size': 'Letter',
       'encoding': "UTF-8",
    }
  
    pdf= pdfkit.from_string(html,False,options)
    response= HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    filename= "resume.pdf"

    return response


def listt(request):
    profiles= Profile.objects.all()
    return render(request,'pdf/listt.html',{'profiles':profiles})
