from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator

# @method_decorator(login_required, name='dispatch')
from applications.forms import UploadDocumentForm
from django.views.generic import DetailView
from .models import ApplicationForm


from django.contrib.auth.decorators import login_required
from accounts.decorators import foreas_required, ypan_required, esyd_required
# def esydApp(request):
#     return render(request, 'esydApp.html', {})
from accounts.models import ApplicantProfile
from django.contrib import messages

@foreas_required
def esydApp(request):
    form = UploadDocumentForm()
    pendingApps = ApplicationForm.objects.filter(foreas = request.user.id)

    userProfile = ApplicantProfile.objects.filter(user =  request.user.id)
    if userProfile[0].has_empty_fields() :
        messages.error(request, "Συμπληρώστε τα στοιχεία σας στην ενότητα Your Account")
    else:
        if request.method == 'POST':
            form = UploadDocumentForm(request.POST, request.FILES)
            form.instance.foreas = request.user
            if form.is_valid():
                # Do something with our files or simply save them
                # if saved, our files would be located in media/ folder under the project's base folder
                form.save()
    return render(request, 'esydApp.html', locals())
