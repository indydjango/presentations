from django.db import models

class NewsItem(models.Model):
    date = models.DateField(auto_now_add=True, null=True)
    title = models.CharField(max_length=64, null=True)
    text = models.TextField(null=True)

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return '{0}: {1}'.format(self.date, self.title)

