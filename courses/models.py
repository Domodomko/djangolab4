from django.db import models

CONTACT_TYPES = (
    ('PHONE', 'PHONE'),
    ('FACEBOOK', 'FACEBOOK'),
    ('EMAIL', 'EMAIL'),
)


class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    imgpath = models.CharField(max_length=100, default='')


class Course(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    logo = models.CharField(max_length=100, default='')


class Branch(models.Model):
    latitude = models.CharField(max_length=100, default='latitude')
    longitude = models.CharField(max_length=100, default='longitude')
    address = models.CharField(max_length=100, default='address')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branches')


class Contact(models.Model):
    type = models.CharField(choices=CONTACT_TYPES, max_length=10)
    value = models.CharField(max_length=100, default='value')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contacts')