from django.db import models

class Entry(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return '{0}'.format(self.date)

