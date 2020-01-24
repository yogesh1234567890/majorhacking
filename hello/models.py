from django.db import models

class login(models.Model):
    class Meta:
        db_table = "tbl_login"
        verbose_name_plural = "login"
    username = models.CharField(max_length=50)
    password =models.CharField(max_length=32)

    def __str__(self):
        return self.username


