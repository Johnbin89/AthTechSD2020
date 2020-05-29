from django.shortcuts import render, reverse
from applications.forms import UploadDocumentForm, EsydStatusForm
from .models import ApplicationForm, ApplicationSubField
from django.contrib.auth.decorators import login_required
from accounts.decorators import foreas_required, ypan_required, esyd_required
from accounts.models import ApplicantProfile
from django.contrib import messages
from django.utils.html import format_html
from django.http import HttpResponseRedirect

@login_required
def user_home(request):
    context = {'home': True}
    if request.user.is_foreas == True:
        esyd_pending_apps = ApplicationForm.objects.filter(foreas = request.user.id).filter(status='Σε εκκρεμότητα').count()
        esyd_approved_apps = ApplicationForm.objects.filter(foreas = request.user.id).filter(status='Εγκρίθηκε').count()
        esyd_rejected_apps = ApplicationForm.objects.filter(foreas = request.user.id).filter(status='Απορρίφθηκε').count()
    if request.user.is_esyd == True:
        esyd_pending_apps = ApplicationForm.objects.all().filter(status='Σε εκκρεμότητα').count()
        esyd_approved_apps = ApplicationForm.objects.all().filter(status='Εγκρίθηκε').count()
        esyd_rejected_apps = ApplicationForm.objects.all().filter(status='Απορρίφθηκε').count()
    context.update({'esyd_pending_apps':esyd_pending_apps, 'esyd_approved_apps':esyd_approved_apps, 'esyd_rejected_apps':esyd_rejected_apps})
    return render(request, 'user_index.html', context)

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
                return HttpResponseRedirect(reverse('esyd_for_foreas'))
    context['form'],context['pendingApps'] = form, pendingApps
    return render(request, 'esydApp.html', context)

@esyd_required
def esyd_xeiristis(request):
    context = {'esyd_page': True}
    pendingApps = ApplicationForm.objects.all()
    status_forms = {}
    for application in pendingApps:
        num_subfields = ApplicationSubField.objects.filter(application=application.id).count()
        if num_subfields > 1:
            list_obj = list(ApplicationSubField.objects.filter(application=application.id))
            for obj in list_obj:
                no_space_sub_name = str(obj).replace(" ","")
                form_name = "form%s%s" % (application.id, no_space_sub_name)
                status_forms.update({form_name:EsydStatusForm(instance=obj)})
        else:
            obj = ApplicationSubField.objects.get(application=application.id)
            no_space_sub_name = str(obj).replace(" ","")
            form_name = "form%s%s" % (application.id, no_space_sub_name)
            status_forms.update({form_name:EsydStatusForm(instance=obj)})   
    print(status_forms)
    context.update({'pendingApps':pendingApps, 'status_forms':status_forms})
    return render(request, 'esydApp.html', context)






def ypan_application(request):
    context = {'ypan_page': True}
    return render(request, 'ypan_application.html', context)