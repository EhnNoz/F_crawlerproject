from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Count


class Platform(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=200, blank=False, null=False, unique=True)
    active = models.BooleanField(verbose_name=_('Active'), default=True)

    class Meta:
        verbose_name = _('Platform')
        verbose_name_plural = _('Platforms')

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name


class Config(models.Model):
    plan = models.CharField(verbose_name=_('Plan'), max_length=200, blank=False, null=False, unique=True)
    platforms = models.ManyToManyField(Platform, verbose_name='Platforms', blank=True)
    reousrces = models.ManyToManyField('Resource', verbose_name='Resources', blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk is None and Config.objects.count() == 1:
            raise Exception(_('Maximum allowed Conf object is 1.'))

        return super(Config, self).save(force_insert=False, force_update=False, using=None,
                                 update_fields=None)
        
    def __str__(self):
        return self.plan
    
    def __unicode__(self):
        return self.plan


class Resource(models.Model):
    platform = models.ForeignKey(Platform, verbose_name=_('Platform'), on_delete=models.SET_NULL, null=True)
    name = models.CharField(verbose_name=_('Name'), max_length=200, blank=False, null=False, unique=True)
    active = models.BooleanField(verbose_name=_('Active'), default=True)

    class Meta:
        verbose_name = _('Resource')
        verbose_name_plural = _('Resources')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Manifest(models.Model):
    keywords = models.CharField(verbose_name=_('Keyword'), max_length=10000, blank=False, unique=False)
    resources = models.ManyToManyField(Resource, verbose_name='Resources')
    active = models.BooleanField(verbose_name='Active', default=True)
    

    class Meta:
        verbose_name = _('Manifest')
        verbose_name_plural = _('Manifests')

    def __str__(self):
        return self.keywords
    
    def __unicode__(self):
        return self.keywords

    def total_crawled_records(self):
        # @todo: must implement
        return 100

    def total_delivered_records(self):
        # @todo: must implement
        return 50
    
    def status(self):
        
        status= "Not Started"

        return status


    
class News(models.Model):
    Platform = models.CharField(verbose_name=_('Platform'), max_length=200, blank=False, null=False, unique=False)
    Sender_Name = models.CharField(verbose_name=_('Sender Name'), max_length=200, blank=False, null=False, unique=False)
    Message = models.CharField(verbose_name=_('Message'), max_length=1000, blank=False, null=False, unique=False)
    Message_Time = models.CharField(verbose_name=_('Message Time'), max_length=200, blank=False, null=False, unique=False)
#    status = models.CharField(verbose_name=_('Status'), max_length=200, blank=False, null=False, unique=False)
    Time = models.DateTimeField(verbose_name=_('Date'), auto_now_add=True)
    Message_Link = models.CharField(verbose_name=_('Message Link'), max_length=200, blank=False, null=False, unique=False)
#    message = models.CharField(verbose_name=_('Message'), max_length=1000, blank=False, null=False, unique=False)

    class Meta:
        verbose_name = _('News')
#        verbose_name_plural = _('News')

    def __str__(self):
        return self.message
    
    def __unicode__(self):
        return self.message
    
#    def total_crawled(self):
#        
#        crawled_records = News.objects.values('status').annotate(Count('status'))
#
#        # @todo: must implement
#        return crawled_records
    

    


    
    