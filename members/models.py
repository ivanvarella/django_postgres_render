from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    # phone = models.IntegerField(null=True)
    phone = models.BigIntegerField(null=True)  # Alterado para BigIntegerField
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
