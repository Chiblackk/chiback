from django.db import models
from .Person import Person


class Experience(models.Model):
    class Meta:
        app_label = 'chiback'
        db_table = 'EXPERIENCE'

    name = models.CharField(max_length=100)
    initDate = models.DateField()
    endDate = models.DateField()
    location = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='experiences')

    def __str__(self):
        return f'Experiencia de {self.user} en {self.name}'

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)