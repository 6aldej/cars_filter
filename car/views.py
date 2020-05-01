from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView
from car.models import Car
from django.http import HttpResponse
from django.template import loader

def car_list(request):
    cars = Car.objects.all()
    return HttpResponse(cars)

def index(request):
    template = loader.get_template('index.html')
    cars = Car.objects.all()
    car_data = {
        "title": "Наши автомобили",
        "cars": cars,
    }
    return HttpResponse(template.render(car_data))

class CarsView(TemplateView):
    template_name = "car/templates/index.html"

    def get_context_data(self, **kwargs):
        params = self.request.GET
        query = Q()
        for key, value in params.items():
            if value and key in vars(Car):
                query &= Q(**{key: value})
        return {"cars": Car.objects.filter(query)}
