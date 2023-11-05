from django.db import models

# Create your models here.
class Report(models.Model):
    '''
    '_id', 'incident_id', 'authors', 'date_downloaded', 'date_modified',
       'date_published', 'date_submitted', 'description',
       'epoch_date_downloaded', 'epoch_date_modified', 'epoch_date_published',
       'epoch_date_submitted', 'image_url', 'language', 'ref_number',
       'report_number', 'source_domain', 'submitters', 'text', 'title', 'url',
       'tags'
    '''
    # incident = models.ManyToManyField(Incident)
    authors = models.CharField(max_length=300, default="")
    date_downloaded = models.DateTimeField("Date downloaded", blank=True, null=True)
    date_modified = models.DateTimeField("Date report was modified", blank=True, null=True)
    date_published = models.DateTimeField("Date report was published", blank=True, null=True)
    date_submitted = models.DateTimeField("Date report was submitted", blank=True, null=True)
    description = models.CharField(max_length=5000)
    epoch_date_downloaded = models.DateTimeField(blank=True, null=True)
    epoch_date_modified = models.DateTimeField(blank=True, null=True)
    epoch_date_published = models.DateTimeField(blank=True, null=True)
    epoch_date_submitted = models.DateTimeField(blank=True, null=True)
    image_url = models.CharField(max_length=1000, default="")
    language = models.CharField(max_length=7, default="")
    report_number = models.IntegerField()
    source_domain = models.CharField(max_length=1000, default="")
    submitters = models.CharField(max_length=1000, default="")
    text = models.CharField(max_length=100000, default="")
    title = models.CharField(max_length=1000, default="")
    url = models.CharField(max_length=1000, default="")

class Incident(models.Model):
    '''
    'incident_id', 'date', 'reports',
       'alleged deployer of ai system', 'alleged developer of ai system',
       'alleged harmed or nearly harmed parties', 'description', 'title'
    '''
    incident_id = models.IntegerField(null=True)
    date = models.DateTimeField("Incident Date", blank=True, null=True)
    # reports = models.ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
    algd_deployer = models.CharField(max_length=1000, default="")
    algd_developer = models.CharField(max_length=1000, default="")
    algd_harm = models.CharField(max_length=1000, default="")
    description = models.CharField(max_length=10000, default="")
    title=models.CharField(max_length=1000, default="")
    reports = models.ManyToManyField(Report)