from django.db import models


class Blog(models.Model):
    head=models.CharField(max_length=100)
    para=models.CharField(max_length=300)
    image=models.ImageField(upload_to='article_images/') 
    date=models.DateField()

