from django.db.models.signals import post_save
from django.dispatch import receiver
from django_drf_filepond.models import TemporaryUpload
from django_drf_filepond.api import store_upload
import os
 
 
@receiver(post_save, sender=TemporaryUpload, dispatch_uid="store_upload") 
def create_profile(sender, instance, created, **kwargs):
    if created:
        #print("TemporaryUpload created, storing to FTP server")
        su = store_upload(instance.upload_id, os.path.join(instance.upload_id, instance.upload_name))