from django.contrib import admin
from .models import Vol, Planification, Reservation, Suivi

admin.site.register(Vol)
admin.site.register(Planification)
admin.site.register(Reservation)
admin.site.register(Suivi)
