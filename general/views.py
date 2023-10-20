from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django.http import HttpResponse, HttpRequest
from django.db import IntegrityError
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm

from  django.views import generic
def home(request):
	return render (request, 'general/home.html')

def index(request):
    if request.method == 'GET':
        return render(request, 'general/index.html', {"form": CustomUserCreationForm()})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user) #para crear una cookie xd
                return redirect('login')
            except IntegrityError:  #para manejar los intregacion de errores especificios de la base de datos 
                return render(request, 'general/index.html', {"form": CustomUserCreationForm, "error": "El usuario ya existe."})

        return render(request, 'general/index.html', {"form": CustomUserCreationForm, "error": "Contrasena no es la misma."})

def store(request):
     return render(request, 'general/productos.html')

def cerrar(request):
     logout(request)
     return render(request,'general/home.html')

def entrar(request):
    if request.method == 'GET':
        return render(request, 'general/login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'general/login.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('vista')
    
from .forms import CrearProductoForm
from .models import Producto, comentarios, Categoria
from .forms import ProductoF
from .forms import comentariosZ

def crear_producto(request):
    if request.method == 'POST':
        form = CrearProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vista')  
    else:
        form = CrearProductoForm()
    return render(request, 'general/producto.html', {'form': form})


class listaView(generic.TemplateView):
	template_name = "general/vista.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
        
		productos = Producto.objects.all()
		categorias = Categoria.objects.all()
		
		context["productos"] = productos
		context["categorias"] = categorias
		return context


def actualizar(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        form = ProductoF(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('rate', producto_id=producto_id)
    else:
        form = ProductoF(instance=producto)
    return render(request, 'general/actualizar.html', {'form': form})


#review de comentarios
def detalle(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        form = comentariosZ(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.producto = producto
            nuevo_comentario.autor = request.user
            nuevo_comentario.save()
            return redirect('rate', producto_id=producto_id)
    else:
        form = comentariosZ()
    return render(request, 'general/comentario.html', {'producto': producto, 'form': form})

def rate(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    comentario = comentarios.objects.filter(producto=producto)
    return render(request, 'general/rate.html', {'producto': producto, 'comentarios': comentario})

#seccion de categoria 

from .forms import CrearCategoriaForm

def ver_categoria(request):
    categoria = Categoria.objects.all()
    return render(request, 'general/vistacate.html', {'categoria': categoria})

def crear_categoria(request):
    if request.method == 'POST':
        form = CrearCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vista') 
    else:
        form = CrearCategoriaForm()
    return render(request, 'general/categoria.html', {'form': form})

def editar_categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    if request.method == 'POST':
        form = CrearCategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('vista') 
    else:
        form = CrearCategoriaForm(instance=categoria)
    return render(request, 'general/editar.html', {'form': form})
