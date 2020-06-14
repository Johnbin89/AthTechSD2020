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
    total_esyd = ApplicationForm.objects.filter(foreas= request.user)
    total_ypan = ApplicationYpanForm.objects.filter(foreas = request.user)
    context['total_esyd'],context['total_ypan'] = total_esyd,total_ypan
    return render(request, 'foreasReport.html', context)

@esyd_required
def report_esyd(request):
    context = {'reporting': True}
    subFields = ApplicationSubField.objects.filter(application__status = 'Εγκρίθηκε',expDate__gte=date.today())
    total = ApplicationForm.objects.all()
    context['subFields'],context['total'] = subFields,total
    return render(request, 'esydReport.html', context)

@ypan_required
def report_ypan(request):
    context = {'reporting': True}
    subFields = ApplicationYpanSubField.objects.filter(application__status = 'Εγκρίθηκε',expDate__gte=date.today())
    total = ApplicationYpanForm.objects.all()
    context['subFields'],context['total'] = subFields,total
    return render(request, 'ypanReport.html', context)