from django.contrib import admin
from .models import User, ApplicantProfile, XeiristisYpourgeiou, XeiristisEsyd, Regulation
# Register your models here.
admin.site.register(User)
admin.site.register(ApplicantProfile)
admin.site.register(XeiristisEsyd)
admin.site.register(XeiristisYpourgeiou)
admin.site.register(Regulation)