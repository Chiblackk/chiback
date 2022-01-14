from django.db import models
from .Person import Person


class Achievement(models.Model):
    class Meta:
        app_label = 'chiback'
        db_table = 'ACHIEVEMENT'

    typeAch = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='achievements')

    def __str__(self):
        return f'Logros de {self.user} en {self.typeAch}'

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)