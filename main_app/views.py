from django.shortcuts import render
from .models import Treasure as TreasureModel


# Create your views here.
def index(request):
    treasures = TreasureModel.objects.all()
    return render(request, 'index.html', {'treasures': treasures})
