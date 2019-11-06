from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Labs)
admin.site.register(Term)
admin.site.register(Appointment)
admin.site.register(Variable)

