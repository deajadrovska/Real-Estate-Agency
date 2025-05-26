from datetime import date

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
    list_display = ('name', 'area', 'description')
    inlines = [AgentRealEstateInline, CharacteristicRealEstateInline]

    def has_add_permission(self, request):
        return Agent.objects.filter(user = request.user).exists()

    def has_delete_permission(self, request, obj=None):
        return not CharacteristicRealEstate.objects.filter(realestate= obj).exists()

    def has_change_permission(self, request, obj=None):
        return obj and AgentRealEstate.objects.filter(realestate= obj, agent__user = request.user).exists()

    def get_queryset(self, request):
        return RealEstate.objects.filter(date=date.today())





class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    def has_add_permission(self, request):
        return request.user.is_superuser

class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    def has_add_permission(self, request):
        return request.user.is_superuser

admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(Agent)
admin.site.register(Characteristic)
# admin.site.register(CharacteristicRealEstate)
# admin.site.register(AgentRealEstate)

