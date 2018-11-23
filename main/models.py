from django.db import models
from django.core.validators import FileExtensionValidator
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):#포스팅에 저장될 공간
	postname = models.CharField(max_length=50)
	Lat = models.FloatField(null=True)
	Lng = models.FloatField(null=True)
	mainphoto = models.ImageField(blank=True, null=True, validators=[FileExtensionValidator(['jpg'])])
	publishedDate = models.DateTimeField(blank=True, null=True)
	modifiedDate = models.DateTimeField(blank=True, null=True)
	contents = models.TextField()
	tag = TaggableManager(blank=True)

	def __str__(self):
		return self.postname


class Language_log(models.Model):#포스팅에 저장될 공간
	kind = models.CharField(max_length=50)
	# Lat = models.FloatField(null=True)
	# Lng = models.FloatField(null=True)
	# mainphoto = models.ImageField(blank=True, null=True, validators=[FileExtensionValidator(['jpg'])])
	who = models.CharField(max_length=50)
	where = models.CharField(max_length=50)
	startDate = models.DateTimeField(blank=True, null=True)
	endDate = models.DateTimeField(blank=True, null=True)
	topic = models.CharField(max_length=50)
	summary = models.TextField()
	# tag = TaggableManager(blank=True)
	what = models.CharField(max_length=50)

	def __str__(self):
		return self.topic		