from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from .forms import FormularioRegistro
from .models import Usuario



from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.


def registro(request):
    print("hola que hace xd")
    
    if request.method =="POST":
        form =FormularioRegistro(request.POST) 
        usuarios=Usuario.objects.all()
        correos=[]
        for c in usuarios:
            correos.append(c.correo)
        print("hola que hace xdd")
        if form.is_valid():
            correoR=form.cleaned_data.get('correo') 
            print("hola que hace xddd")
            if correoR not in correos:
                print("hola que hace xdddd")
                usuario = form.save()
                nombre_usuario=form.cleaned_data.get('username')
                messages.success(request, f"Nueva Cuenta Creada:{nombre_usuario}")
                u = Usuario()
                u.user_id = usuario.id
                u.username = form.cleaned_data.get('username')
                u.password = form.cleaned_data.get('password1')
                u.correo = form.cleaned_data.get('correo')
                u.save()
                login(request, usuario)
                messages.info(request, f"Has sido logeado como:{nombre_usuario}")
                return redirect('Inicio')
            else:
                messages.error(request,f"Este correo ya existe")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: form.error_messages[msg]")

    form = FormularioRegistro()
    return render(request,"registro/registro.html",{"form":form})


#class VRegistro(View):

#    def get(self, request):
#        form=UserCreationForm()
#        return render(request,"registro/registro.html",{"form":form})

#    def post(self, request):
#        form=UserCreationForm(request.POST)

#        if form.is_valid():
#           usuario=form.save()
#            login(request, usuario)
#            return redirect('Inicio')


#        else:
#            for msg in form.error_messages:
#                messages.error(request, form.error_messages[msg])
 #           return render(request,"registro/registro.html",{"form":form})


def cerrar_sesion(request):
    logout(request)

    return redirect('Inicio')

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Inicio')
            else:
                messages.error(request, "usuario no válido")
        else:
            messages.error(request, "información incorrecta")

    form=AuthenticationForm()
    return render(request,"login/login.html",{"form":form})




    

        
