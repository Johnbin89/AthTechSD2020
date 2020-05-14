from django.contrib import admin
from .models import User, ApplicantProfile, XeiristisYpourgeiou, XeiristisEsyd
# Register your models here.
admin.site.register(User)
admin.site.register(ApplicantProfile)
admin.site.register(XeiristisEsyd)
admin.site.register(XeiristisYpourgeiou)