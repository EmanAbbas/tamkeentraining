from django.contrib import admin
from .models import Workshop ,Subscriber,ContactMessage
from tamkeenapp.models import Course, Certificate



admin.site.register(Workshop)
admin.site.register(Subscriber)
admin.site.register(Course)
admin.site.register(Certificate)
admin.site.register(ContactMessage)










admin.site.site_title='Tamkeen Adminstration'
admin.site.index_title='Tamkeen Adminstration'
admin.site.site_header='Tamkeen Adminstration'


