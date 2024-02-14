from django.db import models

# Create your models here.


def file_path(instance, filename):
    return "ftp_interface-files/{0}".format(filename)


class File(models.Model):
    file = models.FileField(upload_to=file_path)
    username = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
