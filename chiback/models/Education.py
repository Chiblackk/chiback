from django.db import models
from .Person import Person


class Education(models.Model):
    class Meta:
        app_label = 'chiback'
        db_table = 'EDUCATION'

    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=150)
    initDate = models.DateField()
    endDate = models.DateField()
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='educationList')

    def __str__(self):
        return f'Educación de {self.user} en {self.name}'

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)