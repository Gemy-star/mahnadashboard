from django.contrib import admin

from .models import CompareBuilding , ResidentBuilding , ResidentDocument

# Register your models here.
admin.site.register(CompareBuilding)

admin.site.register(ResidentDocument)
admin.site.register(ResidentBuilding)
