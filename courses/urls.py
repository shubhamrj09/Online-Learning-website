from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from courses.views import MyCoursesList,HomePageView ,coursePage, SignupView , LoginView ,signout, checkout,verifyPayment
from django.conf.urls.static import static 
from codeshubham.settings import MEDIA_ROOT ,MEDIA_URL
from django.conf import settings
urlpatterns = [ 
    path('', HomePageView.as_view(), name='home'),
    path('logout', signout, name='logout'),
    path('my-courses', MyCoursesList.as_view(), name='my-courses'),
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'), 
    path('course/<str:slug>', coursePage, name='coursePage'),
    path('check-out/<str:slug>', checkout, name='check-out'),
    path('verify_payment',verifyPayment, name='verify_payment'),
    path('about/',TemplateView.as_view(template_name='courses/about.html'),name='about'),
    path('contact/',TemplateView.as_view(template_name='courses/contact.html'),name='contact'),
    path('testimonials/',TemplateView.as_view(template_name='courses/testimonials.html'),name='testimonials'),
    path('index/',TemplateView.as_view(template_name='courses/index.html'),name='index'),
    path('check_out/',TemplateView.as_view(template_name='courses/check_out.html'),name='check_out'),
    path('teams/',TemplateView.as_view(template_name='courses/teams.html'),name='teams'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)