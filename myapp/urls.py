from django.urls import path
from  myapp import views


app_name = 'myapp'

urlpatterns = [
  path('emails/',views.EmailList.as_view(), name = 'emails'),
  path('add/',views.EmailCreate.as_view(), name = 'create'),
  path('edit/<pk>',views.EmailUpdate.as_view(), name = 'update'),
  path('remove/<pk>',views.EmailDelete.as_view(), name = 'delete'),
  path('send/',views.send_email, name = 'send'),
  path('',views.base, name = 'home'),
  path('about/',views.about, name = 'about'),
  

]