from django.shortcuts import render
from .models import Treasure as TreasureModel


# Create your views here.
def index(request):
    treasures = TreasureModel.objects.all()
    return render(request, 'index.html', {'treasures': treasures})


class Treasure:
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location

treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM",
             "https://www.pexels.com/photo/depth-of-field-fir-cone-forest-gravel-285935/"),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO",
             "https://www.pexels.com/photo/pumpkin-on-brown-wooden-surface-633480/"),
    Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA',
             "https://www.pexels.com/photo/selective-focus-photo-of-red-flower-633709/")
]
