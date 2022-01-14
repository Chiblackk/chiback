from django.db import models


class Person(models.Model):
    class Meta:
        app_label = 'chiback'
        db_table = 'PERSON'

    names = models.CharField(max_length=120)
    surnames = models.CharField(max_length=120)
    image = models.URLField()
    description = models.TextField(null=True, blank=True)
    summary = models.CharField(max_length=150)
    email = models.CharField(max_length=120, unique=True)
    phone = models.CharField(max_length=15,null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    nacionality = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField()
    age = models.IntegerField()
    apitude = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Persona {self.names} {self.surnames}'

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
