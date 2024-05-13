from django.contrib import admin

# Register your models here.
from .models import Human, Child, IceCream, Kiosk



admin.site.register(Human)
admin.site.register(Child)
admin.site.register(IceCream)
admin.site.register(Kiosk)