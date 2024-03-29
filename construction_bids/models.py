from django.db import models

# Create your models here.

class ConstructionBid(models.Model):
    job_title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    estimate = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.job_title}"

class Client(models.Model):
    construction_bid = models.ForeignKey(ConstructionBid, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Task(models.Model):
    client = models.ForeignKey(ConstructionBid, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"