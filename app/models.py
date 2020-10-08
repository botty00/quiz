from django.db import models

class Question_model(models.Model):
    question = models.TextField(
    
    )

    answer = models.BooleanField(

    )

    comment = models.TextField(

    )



# Create your models here.
