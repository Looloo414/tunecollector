from django.contrib import admin
from .models import Tune, Group, Instrument

# Register your models here.
admin.site.register(Tune)
admin.site.register(Group)
admin.site.register(Instrument)