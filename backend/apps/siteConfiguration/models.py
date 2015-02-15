from django.db import models
from solo.models import SingletonModel

class SiteConfiguration(SingletonModel):
    filespath = models.CharField(
        'Files path',
        help_text='Path for downloaded/uploaded files',
        max_length=255,
        default='files',
        )


    def __unicode__(self):
        return u"Site configuration"

    class Meta:
        verbose_name = "Site configuration"
