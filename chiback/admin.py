from django.contrib import admin
from chiback.models.Person import Person
from chiback.models.Experience import Experience
from chiback.models.Education import Education
from chiback.models.Achievement import Achievement
from chiback.models.Certificate import Certificate

# Register your models here.
admin.site.register(Person)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Achievement)
admin.site.register(Certificate)