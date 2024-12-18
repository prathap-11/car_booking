from django.contrib import admin
from .models import carsList

class carsListAdmin(admin.ModelAdmin):
    list_display=('carname','carrent','carpdf')
admin.site.register(carsList,carsListAdmin)

# Register your models here.
