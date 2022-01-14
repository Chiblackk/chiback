from django.db import models
from .Person import Person

class Certificate(models.Model):
    class Meta:
        app_label = 'chiback'
        db_table = 'CERTIFICATE'

    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    initDate = models.DateField()
    endDate = models.DateField()
    idCredential = models.CharField(max_length=200)
    linkCredential = models.URLField()
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='certificates')

    def __str__(self):
        return f'Certificación de {self.user} en {self.name}'

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)