from django.shortcuts import render, reverse
from applications.forms import UploadDocumentForm
from .models import ApplicationForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import foreas_required, ypan_required, esyd_required
from accounts.models import ApplicantProfile
from django.contrib import messages
from django.utils.html import format_html
from django.http import HttpResponseRedirect



@foreas_required
def esyd_for_foreas(request):
    context = {'esyd_page': True}
    pendingApps = ApplicationForm.objects.filter(foreas = request.user.id)
    userProfile = ApplicantProfile.objects.filter(user =  request.user.id)
    form = UploadDocumentForm(current_user=request.user)
    if userProfile[0].has_empty_fields() :
        account_message = format_html("{} <a href='{}'>{}</a>",
                      "Συμπληρώστε τα στοιχεία σας στην ενότητα ", 
                      reverse('foreas_profile', args=(request.user.id,)),
                      'Λογαριασμός')
        messages.error(request, account_message)
    else:
        if request.method == 'POST':
            form = UploadDocumentForm(request.POST, request.FILES, current_user = request.user)
            form.instance.foreas = request.user
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('esyd'))
    context['form'],context['pendingApps'] = form, pendingApps
    return render(request, 'esydApp.html', context)

def ypan_application(request):
    context = {'ypan_page': True}
    return render(request, 'ypan_application.html', context)