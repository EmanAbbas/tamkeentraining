# Create your views here.
from django.shortcuts import render, get_object_or_404
from tamkeenapp.models import Course, ContactMessage, Subscriber
from tamkeenapp.models import Certificate
from tamkeenapp.models import Workshop
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from smtplib import SMTP
import datetime

from django.http import HttpResponseRedirect, HttpResponse
import smtplib
def home(request):
     
     errors = []
     context={}
       
     context["workshops"]= Workshop.objects.filter(start_date__gt=(datetime.datetime.now()))
     if request.method == 'POST':
        if not request.POST.get('name', ''):
            errors.append('Enter your name.')
       
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            try:
                subscribero=  Subscriber.objects.create (name=request.POST['name'],email=request.POST['email'])
                subscribero.save()
                context['result']='Thank you, for subscribtion'
           
                return  render(request, 'home.html',
        context)
            except Exception, err: 
             errors.append(err)
             context['errors']=errors
             return render(request, 'home.html',context
        )
           
                
     
     return render(request,'home.html' ,context)

  #def home(request):
       
  #  assert isinstance(request, HttpRequest)
  #  return render(
  #      request,
  #      'app/index.html',
  #      context_instance = RequestContext(request,
  #      {
  #          'title':'Home Page',
  #          'year':datetime.now().year,
  #      })
  #  )
def services(request):
    return render(request,'services.html')

def contact(request):
     result=''
     errors = []
     if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
          try:
             
              EMAIL_HOST_USER ='arabic.kanz.contact@gmail.com'
              EMAIL_HOST_PASSWORD='AKCOMPANY'
              contct=  ContactMessage.objects.create (name=request.POST['name'],subject=request.POST['subject'],email=request.POST['email'],enquiry=request.POST['message'])
              contct.save()
              msg = "\r\n".join([
              "From: arabic.kanz.contact@gmail.com",
              "To: info@tamkeen-4st.com",
             "Subject:"+request.POST['subject'],
               "", "From:"+request.POST['email']+"  \n Name:"+request.POST['name'] +"\n Message:"+
            request.POST['message']
             ])
              server = smtplib.SMTP('smtp.gmail.com:587')
              server.ehlo()
              server.starttls()
              server.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
              #info@tamkeen-4st.com
              server.sendmail(EMAIL_HOST_USER, 'info@tamkeen-4st.com', msg)
              server.quit()
              result='Thank you, form has been submitted successfully'
           
              return  render(request, 'contact_us.html',
        {'result': result})
          except Exception, err: 
             errors.append(err)
             return render(request, 'contact_us.html',
        {'errors': errors})
     return render(request, 'contact_us.html',
        {'errors': errors})
   


def certificates(request):
    context={}
    context["certificates"]=Certificate.objects.all()
    return render(request,'certificates.html',context)

class Training(ListView):
    model = Course
    template_name = 'training.html'

#def training(request):
#    context={}
#    context['courselist']= Course.objects.all()
#    return render(request,'training.html',context)


class CourseDetail(DetailView):
    model=Course
    template_name = 'coursedetails.html'

class WorkshopDetail(DetailView):
    model=Workshop
    template_name = 'workshopdetails.html'
#def course(request,pk):
#    context={}
#    context['course']= get_object_or_404(Course, pk=pk)
#    return render(request,'coursedetails.html',context)