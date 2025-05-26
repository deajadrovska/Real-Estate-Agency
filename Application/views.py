from django.shortcuts import render

from Application.forms import RealEstateForm
from Application.models import RealEstate


# Create your views here.


def index(request):
    properties = RealEstate.objects.filter(sold= False, area__gte=100)

    return render(request,'index.html',{'properties':properties})

def edit(request, property_id):
    house = RealEstate.objects.filter(id=property_id).first()
    if request.method == 'POST':
        pass


    form = RealEstateForm(instance=house)
    return render(request,'edit.html',{'form':form, 'house':house})