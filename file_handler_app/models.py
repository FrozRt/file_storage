from django.db import models
from django.utils import timezone

from .utils import generate_sha1, upload_to_unique_folder, MediaFileSystemStorage


class Data(models.Model):
    file_id = models.AutoField(primary_key=True)
    file = models.FileField(null=True, upload_to=upload_to_unique_folder, storage=MediaFileSystemStorage())
    file_hash = models.CharField(max_length=256, default='Null')
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.file_hash = generate_sha1(str(self.file.name))
        super(Data, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.file.name)

