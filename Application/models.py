from django.contrib.auth.models import User
from django.db import models

# Create your models here.


#PROPERTY
class RealEstate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    area = models.FloatField()
    date = models.DateField()
    image = models.ImageField(upload_to='images/')
    reserved = models.BooleanField()
    sold = models.BooleanField()

    def __str__(self):
        return f'{self.name} - {self.area} - {self.sold}'

class Agent(models.Model):
    name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    profile_url = models.CharField(max_length=100)
    total_sales = models.IntegerField()
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.email}'

#AGENT - PROPERTY
class AgentRealEstate(models.Model):
    realestate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.realestate.name} - {self.agent.name}'

class Characteristic(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()

    def __str__(self):
        return f'{self.name} - {self.value}'

class CharacteristicRealEstate(models.Model):
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    realestate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.characteristic.name} - {self.realestate.name}'