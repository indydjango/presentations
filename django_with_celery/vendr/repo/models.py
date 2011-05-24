from django.db import models
from django.conf import settings

class RepoFile(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    uuid = models.CharField(max_length=64, null=True, blank=True)
    filename = models.CharField(max_length=128, null=True, blank=True)
    download_count = models.PositiveIntegerField(null=True, blank=True, default=0)

    class Meta:
        ordering = ['-date_created']

    def __unicode__(self):
        return '{0} {1}'.format(self.date_created, self.filename)
