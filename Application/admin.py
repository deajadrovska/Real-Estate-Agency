from django.contrib import admin

from Application.models import RealEstate, Agent, Characteristic, CharacteristicRealEstate, AgentRealEstate

# Register your models here.



class AgentRealEstateInline(admin.TabularInline):
    model = AgentRealEstate
    extra = 1

class CharacteristicRealEstateInline(admin.TabularInline):
    model = CharacteristicRealEstate
    extra = 1

class RealEstateAdmin(admin.ModelAdmin):
    inlines = [AgentRealEstateInline, CharacteristicRealEstateInline]

admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(Agent)
admin.site.register(Characteristic)
# admin.site.register(CharacteristicRealEstate)
# admin.site.register(AgentRealEstate)

