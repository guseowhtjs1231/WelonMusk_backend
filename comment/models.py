from django.db import models

# Create your models here.
from user.models import Users

class Comment(models.Model):
    user       = models.ForeignKey(Users,on_delete=models.CASCADE)
    comment    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'

