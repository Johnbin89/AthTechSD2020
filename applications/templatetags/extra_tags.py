from django import template
from datetime import date
from storages.backends.ftp import FTPStorage
from django_drf_filepond.models import StoredUpload
import re
register = template.Library()


@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

@register.filter
def to_str(value):
    """converts int to string"""
    return str(value)


@register.filter
def get_item(dictionary, key):
    form = dictionary.get(key)
    return form

@register.filter
def get_type(value):
    return type(value)

@register.filter
def index(indexable, i):
    return indexable[i]

@register.filter
def cut_re(value, search): 
    return re.sub(search, "", value)