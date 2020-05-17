from django.shortcuts import render, reverse
from django.utils.decorators import method_decorator
from applications.forms import UploadDocumentForm
from django.views.generic import DetailView
from .models import ApplicationForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import foreas_required, ypan_required, esyd_required
from accounts.models import ApplicantProfile
from django.contrib import messages
from django.utils.html import format_html



@foreas_required
def esyd_for_foreas(request):
    form = UploadDocumentForm()
    esyd_page = True
    pendingApps = ApplicationForm.objects.filter(foreas = request.user.id)

    userProfile = ApplicantProfile.objects.filter(user =  request.user.id)
    if userProfile[0].has_empty_fields() :
        account_message = format_html("{} <a href='{}'>{}</a>",
                      "Συμπληρώστε τα στοιχεία σας στην ενότητα ", 
                      reverse('foreas_profile', args=(request.user.id,)),
                      'Λογαριασμός')
        messages.error(request, account_message)
    else:
        if request.method == 'POST':
            form = UploadDocumentForm(request.POST, request.FILES)
            form.instance.foreas = request.user
            if form.is_valid():
                # Do something with our files or simply save them
                # if saved, our files would be located in media/ folder under the project's base folder
                form.save()
    return render(request, 'esydApp.html', locals())

def ypan_application(request):
    context = {'ypan_page': True}
    return render(request, 'ypan_application.html', context)