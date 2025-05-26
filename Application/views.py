from django.shortcuts import render

from Application.forms import RealEstateForm
from Application.models import RealEstate, CharacteristicRealEstate


# Create your views here.


def index(request):
    properties = RealEstate.objects.filter(sold= False, area__gte=100)

    for property in properties:
        price = 0
        characteristics = CharacteristicRealEstate.objects.filter(realestate = property).all()
        for characteristic in characteristics:
            characteristic_price = characteristic.characteristic.value
            price += characteristic_price
        # real_estate_context.append({'property': property}, 'price': price)


    return render(request,'index.html',{'properties':properties})

def edit(request, property_id):
    house = RealEstate.objects.filter(id=property_id).first()
    if request.method == 'POST':
        pass


    form = RealEstateForm(instance=house)
    return render(request,'edit.html',{'form':form, 'house':house})