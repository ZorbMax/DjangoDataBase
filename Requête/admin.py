from django.contrib import admin

from .models import Requête
class RequêteAdmin(admin.ModelAdmin):
    list_display =  ('titre','description')
admin.site.register(Requête, RequêteAdmin)

from .models import pays
admin.site.register(pays)
