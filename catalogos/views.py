from django.shortcuts import render

from catalogos.models import Catalogo
# Create your views here.
def catalogos(request):

    catalogos = Catalogo.objects.all()
    return render(request, "catalogos.html", {"catalogos": catalogos})