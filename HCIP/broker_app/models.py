from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    user_number = models.CharField(max_length=11, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    currency = models.CharField(max_length=3, default='USD')
    last_name = models.CharField(max_length=50, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    transaction = models.CharField(max_length=500, default='Current transaction name')
    senders_name = models.CharField(max_length=500, default='Current senders name')
    senders_country = models.CharField(max_length=500, default='Current senders country name')
    recipent_name = models.CharField(max_length=500, default='Current Recipients name')
    recipent_country = models.CharField(max_length=500, default='Current country name')
    recipent_bank = models.CharField(max_length=500, default='Current recipient bank name')
    senders_bank = models.CharField(max_length=500, default='Current senders bank name')
    Total_Transfer_Amount = models.CharField(max_length=500, default='Current Total transfer amount')
    current_date = models.DateField(auto_now=True)
    status_update = models.CharField(max_length=500, default='In progress')
    status_text = models.CharField(max_length=5000, default='current overhead or current payments due')
    estimated_delivery_time = models.CharField(max_length=500, default='time duration of funds unlocking proccess')
    Recipients_IBAN = models.CharField(max_length=500, default='DE31269513110168360295')
    image = models.ImageField(upload_to='images/', default="image_field")


    def __str__(self):
        return self.user.username