from django.db import models


class Pincode(models.Model):
    pincode = models.IntegerField(primary_key = True , max_length= 6)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)



    def __str__(self):
        return f"{self.city} , {self.district}"

