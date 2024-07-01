from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Contact(models.Model):

    name = models.CharField("User name", max_length=255)
    email = models.EmailField("Email",  max_length=254, default="empty@gmail", null=True)
    phone = PhoneNumberField(null=True)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    