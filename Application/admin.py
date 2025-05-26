from django.contrib import admin

from Application.models import RealEstate, Agent, Characteristic, CharacteristicRealEstate, AgentRealEstate

# Register your models here.



admin.site.register(RealEstate)
admin.site.register(Agent)
admin.site.register(Characteristic)
admin.site.register(CharacteristicRealEstate)
admin.site.register(AgentRealEstate)

