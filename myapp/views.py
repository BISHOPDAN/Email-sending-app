from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from .models import Gmail
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.




    


class EmailList(ListView):
    template_name = 'Emaillist.html'
    context_object_name = 'emails'
    model = Gmail

class EmailCreate(CreateView):
    template_name = 'Emailcreate.html'
    model = Gmail
    fields = ('email',)

class EmailUpdate(UpdateView):
    template_name = 'Emailupdate.html'
    model = Gmail
    fields = ('email',)

class EmailDelete(DeleteView):
    template_name = 'Emaildelete.html'
    model = Gmail
    success_url = reverse_lazy('myapp:emails')

def send_email(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
                subject,
                message,
                'emekajamb@gmail.com',
                list(Gmail.objects.all().values_list('email',flat=True)),fail_silently=False
        )
    emails = Gmail.objects.all()
    return render(request,'send.html',{'emails':emails})

    


def base(request):
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html',{})