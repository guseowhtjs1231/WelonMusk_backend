from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name  = models.CharField(max_length = 50)
    email      = models.EmailField(max_length = 100, null=False, unique = True)
    password   = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'users'
