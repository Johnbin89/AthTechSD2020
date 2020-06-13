from django.shortcuts import render, reverse
from django.shortcuts import render
from applications.forms import UploadDocumentForm, EsydStatusForm,UploadYpanDocumentForm,YpanStatusForm
from applications.models import ApplicationForm, ApplicationSubField,ApplicationYpanForm,ApplicationYpanSubField
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from accounts.decorators import foreas_required, ypan_required, esyd_required
from accounts.models import ApplicantProfile,Regulation
from django.contrib import messages
from django.utils.html import format_html
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from datetime import date
import json


# Create your views here.
@foreas_required
def report_foreas(request):
    context = {'reporting': True}
    pendingApps = ApplicationForm.objects.filter(foreas = request.user.id) ##.filter(status='Σε εκκρεμότητα')
    userProfile = ApplicantProfile.objects.filter(user =  request.user.id)
    form = UploadDocumentForm(current_user=request.user)
    context['form'],context['pendingApps'] = form, pendingApps
    return render(request, 'foreasReport.html', context)

@esyd_required
def report_esyd(request):
    context = {'reporting': True}
    pendingApps = ApplicationForm.objects.filter(foreas = request.user.id) ##.filter(status='Σε εκκρεμότητα')
    userProfile = ApplicantProfile.objects.filter(user =  request.user.id)
    form = UploadDocumentForm(current_user=request.user)
    context['form'],context['pendingApps'] = form, pendingApps
    return render(request, 'esydReport.html', context)

@ypan_required
def report_ypan(request):
    context = {'reporting': True}
    subFields = ApplicationYpanSubField.objects.filter(status = 'Εγκρίθηκε',expDate__gte=date.today())
    context['subFields'] = subFields
    return render(request, 'ypanReport.html', context)