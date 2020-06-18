from django.shortcuts import render, reverse
from applications.forms import UploadDocumentForm, EsydStatusForm,UploadYpanDocumentForm,YpanStatusForm
from .models import ApplicationForm, ApplicationSubField,ApplicationYpanForm,ApplicationYpanSubField
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from accounts.decorators import foreas_required, ypan_required, esyd_required
from accounts.models import ApplicantProfile
from django.contrib import messages
from django.utils.html import format_html
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import json
from background_task import background

@login_required
def user_home(request):
    context = {'home': True}
    if request.user.is_foreas == True:
        esyd_pending_apps = ApplicationForm.objects.filter(foreas = request.user.id).filter(status='Σε εκκρεμότητα').count()
        esyd_approved_apps = ApplicationForm.objects.filter(foreas = request.user.id).filter(status='Εγκρίθηκε').count()
        esyd_rejected_apps = ApplicationForm.objects.filter(foreas = request.user.id).filter(status='Απορρίφθηκε').count()
        ypan_pending_apps = ApplicationYpanForm.objects.filter(foreas = request.user.id).filter(status='Σε εκκρεμότητα').count()
        ypan_approved_apps = ApplicationYpanForm.objects.filter(foreas = request.user.id).filter(status='Εγκρίθηκε').count()
        ypan_rejected_apps = ApplicationYpanForm.objects.filter(foreas = request.user.id).filter(status='Απορρίφθηκε').count()
    if request.user.is_esyd == True:
        esyd_pending_apps = ApplicationForm.objects.all().filter(status='Σε εκκρεμότητα').count()
        esyd_approved_apps = ApplicationForm.objects.all().filter(status='Εγκρίθηκε').count()
        esyd_rejected_apps = ApplicationForm.objects.all().filter(status='Απορρίφθηκε').count()
        ypan_pending_apps = 0
        ypan_approved_apps = 0
        ypan_rejected_apps = 0
    if request.user.is_ypan == True:
        esyd_pending_apps = 0
        esyd_approved_apps = 0
        esyd_rejected_apps = 0
        ypan_pending_apps = ApplicationYpanForm.objects.all().filter(status='Σε εκκρεμότητα').count()
        ypan_approved_apps = ApplicationYpanForm.objects.all().filter(status='Εγκρίθηκε').count()
        ypan_rejected_apps = ApplicationYpanForm.objects.all().filter(status='Απορρίφθηκε').count()

    # if esyd_pending_apps != 0 and esyd_approved_apps != 0 and esyd_rejected_apps != 0:
    context.update({'esyd_pending_apps':esyd_pending_apps, 
                    'esyd_approved_apps':esyd_approved_apps, 
                    'esyd_rejected_apps':esyd_rejected_apps,
                    'ypan_pending_apps':ypan_pending_apps, 
                    'ypan_approved_apps':ypan_approved_apps, 
                    'ypan_rejected_apps':ypan_rejected_apps})
    return render(request, 'user_index.html', context)

@foreas_required
def esyd_for_foreas(request):
    context = {'esyd_page': True}
    pendingApps = ApplicationForm.objects.filter(foreas = request.user.id) ##.filter(status='Σε εκκρεμότητα')
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
    pendingApps = ApplicationForm.objects.all() ##.filter(status='Σε εκκρεμότητα')
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

@csrf_exempt
def updateSub_onEsyd(request):
    status = request.POST.get('status')
    date = request.POST.get('date')
    application_id = request.POST.get('application_id')
    field_id = request.POST.get('field_id')
    field_name = request.POST.get('field_name')
    subfields_of_app = ApplicationSubField.objects.filter(application_id=application_id)
    field = subfields_of_app.get(pk=field_id)
    field.status = status
    field.expDate = date
    field.save()
    if status == 'Εγκρίθηκε':
        messages.success(request, "Το πεδίο ' "+ field_name +" ' της αίτησης Νο. ' "+ application_id + " ' αποθηκεύτηκε. ("+ status + ")" )
    elif status == 'Σε εκκρεμότητα':
        messages.warning(request, "Το πεδίο ' "+ field_name +" ' της αίτησης Νο. ' "+ application_id + " ' αποθηκεύτηκε. ("+ status + ")" )
    else:
        messages.error(request, "Το πεδίο ' "+ field_name +" ' της αίτησης Νο. ' "+ application_id + " ' αποθηκεύτηκε. ("+ status + ")" )
    completed = True
    for subfield in subfields_of_app:
        if subfield.status == 'Σε εκκρεμότητα' or subfield.status == 'Απορρίφθηκε' :
            completed = False
        if subfield.status == 'Απορρίφθηκε':
            esyd_app = ApplicationForm.objects.get(pk=application_id)
            esyd_app.status = 'Απορρίφθηκε'
            esyd_app.save()
            messages.success(request, "H αίτηση Νο. ' " + application_id + " ' απορρίφθηκε")
        if subfield.status == 'Σε εκκρεμότητα':
            esyd_app = ApplicationForm.objects.get(pk=application_id)
            esyd_app.status = 'Σε εκκρεμότητα'
            esyd_app.save()
            messages.success(request, "H αίτηση Νο. ' " + application_id + " ' είναι σε εκκρεμότητα")

    if completed == True:
        esyd_app = ApplicationForm.objects.get(pk=application_id)
        esyd_app.status = 'Εγκρίθηκε'
        esyd_app.save()
        messages.success(request, "H αίτηση Νο. ' "+ application_id +" ' εγκρίθηκε" )

    return JsonResponse('Test Updated!', safe=False)




def ypan_application(request):
    context = {'ypan_page': True}
    pendingApps = ApplicationYpanForm.objects.filter(foreas = request.user.id) ##.filter(status='Σε εκκρεμότητα')
    userProfile = ApplicantProfile.objects.filter(user = request.user.id)
    form = UploadYpanDocumentForm(current_user=request.user)
    if userProfile[0].has_empty_fields() :
        account_message = format_html("{} <a href='{}'>{}</a>",
                      "Συμπληρώστε τα στοιχεία σας στην ενότητα ", 
                      reverse('foreas_profile', args=(request.user.id,)),
                      'Λογαριασμός')
        messages.error(request, account_message)
    else:
        @background(schedule=1)
        def handle_post_ypan():
            if form.is_valid():
                form.save()
        if request.method == 'POST':
            form = UploadYpanDocumentForm(request.POST, request.FILES, current_user = request.user)
            form.instance.foreas = request.user
            handle_post_ypan()
            return HttpResponseRedirect(reverse('ypan_application'))
    context['form'],context['pendingApps'] = form, pendingApps
    return render(request, 'ypan_application.html', context)


        


@ypan_required
def ypan_xeiristis(request):
    context = {'ypan_page': True}
    pendingApps = ApplicationYpanForm.objects.all() ##.filter(status='Σε εκκρεμότητα')
    status_forms = {}
    for application in pendingApps:
        num_subfields = ApplicationYpanSubField.objects.filter(application=application.id).count()
        if num_subfields > 1:
            list_obj = list(ApplicationYpanSubField.objects.filter(application=application.id))
            for obj in list_obj:
                no_space_sub_name = str(obj).replace(" ","")
                form_name = "form%s%s" % (application.id, no_space_sub_name)
                status_forms.update({form_name:YpanStatusForm(instance=obj)})
        else:
            obj = ApplicationYpanSubField.objects.get(application=application.id)
            no_space_sub_name = str(obj).replace(" ","")
            form_name = "form%s%s" % (application.id, no_space_sub_name)
            status_forms.update({form_name:YpanStatusForm(instance=obj)})  
    print(status_forms)
    context.update({'pendingApps':pendingApps, 'status_forms':status_forms})
    return render(request, 'ypan_application.html', context)


@csrf_exempt
def updateSub_onYpan(request):
    status = request.POST.get('status')
    date = request.POST.get('date')
    application_id = request.POST.get('application_id')
    field_id = request.POST.get('field_id')
    field_name = request.POST.get('field_name')
    subfields_of_app = ApplicationYpanSubField.objects.filter(application_id=application_id)
    field = subfields_of_app.get(pk=field_id)
    field.status = status
    field.expDate = date
    field.save()
    if status == 'Εγκρίθηκε':
        messages.success(request, "Το πεδίο ' "+ field_name +" ' της αίτησης Νο. ' "+ application_id + " ' αποθηκεύτηκε. ("+ status + ")" )
    elif status == 'Σε εκκρεμότητα':
        messages.warning(request, "Το πεδίο ' "+ field_name +" ' της αίτησης Νο. ' "+ application_id + " ' αποθηκεύτηκε. ("+ status + ")" )
    else:
        messages.error(request, "Το πεδίο ' "+ field_name +" ' της αίτησης Νο. ' "+ application_id + " ' αποθηκεύτηκε. ("+ status + ")" )
    completed = True
    for subfield in subfields_of_app:
        if subfield.status == 'Σε εκκρεμότητα' or subfield.status == 'Απορρίφθηκε':
            completed = False
        if subfield.status == 'Απορρίφθηκε':
            ypan_app = ApplicationYpanForm.objects.get(pk=application_id)
            ypan_app.status = 'Απορρίφθηκε'
            ypan_app.save()
            messages.success(request, "H αίτηση Νο. ' " + application_id + " ' απορρίφθηκε")
        if subfield.status == 'Σε εκκρεμότητα':
            ypan_app = ApplicationYpanForm.objects.get(pk=application_id)
            ypan_app.status = 'Σε εκκρεμότητα'
            ypan_app.save()

    if completed == True:
        ypan_app = ApplicationYpanForm.objects.get(pk=application_id)
        ypan_app.status = 'Εγκρίθηκε'
        ypan_app.save()
        messages.success(request, "H αίτηση Νο. ' "+ application_id +" ' εγκρίθηκε" )
    return JsonResponse('Test Updated!', safe=False)