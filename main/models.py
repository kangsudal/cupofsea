from django.db import models

# Create your models here.
class Post(models.Model):#포스팅에 저장될 공간
	postname = models.CharField(max_length=50)
	mainphoto = models.ImageField(blank=True, null=True)
	contents = models.TextField()

	def __str__(self):
		return self.postname