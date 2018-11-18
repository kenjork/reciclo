from django.http import HttpResponse
from django.shortcuts import render
from .models import TrashCan, Level

from django.shortcuts import redirect
from django.views.generic import View
from .forms import TrashCanForm
from .serializers import TrashCanSerializer, LevelSerializer
from rest_framework import routers, serializers, viewsets


def my_view(request):
    template_name = 'trashcan/lista.html'
    context = {
        'cans': TrashCan.objects.get_lat_lng(),
    }
    return render (request,template_name,context)

class CreateView(View):
    template_name = "trashcan/crear.html"

    form = TrashCanForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home_app:home')
        context = {
            'errors': kwargs.get('errors'),
            'form': self.form,
        }
        return render(request, self.template_name, context)

    def post(self, request):

        form = self.form(request.POST)
        
        if form.is_valid():
            data = dict(request.POST)
            data.pop('csrfmiddlewaretoken')

            data = {k: v[0] for k, v in data.items()}
            TrashCan.objects.create(
                **data
            )
            return redirect('trashcan_app:can-list')
        return self.get(request, errors=form.errors)


class ListView(View):

    template_name = "trashcan/detalle.html"

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('home_app:home')

        context = {
            'errors': kwargs.get('errors'),
            'can': TrashCan.objects.filter(pk=kwargs.get('pk')).first(),
            'levels': Level.objects.get_levels(kwargs.get('pk')),
        }        
        return render(request, self.template_name, context)


class TrashCanViewSet(viewsets.ModelViewSet):
    queryset = TrashCan.objects.all()
    serializer_class = TrashCanSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer



# Create your views here.
def my_view_crear(request):
    return HttpResponse('<h1>Yo creo</h1>')

def my_view_detail(request, id):
    return HttpResponse('<h1>Yo soy el detalle {}</h1>'.format(id))