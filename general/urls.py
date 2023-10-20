from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

	path('', views.home, name="home"),
    path('index/', views.index, name="home"),
    path('producto/', views.crear_producto, name="producto"),
    path('producto/rate/<int:producto_id>/', views.rate, name='rate'),
    path('comentario/<int:producto_id>/', views.detalle, name="comentario"),
    path('vista/', views.listaView.as_view(), name="vista"),
    path('logout/', views.cerrar, name="logout"),
    path('categoria/editar/<int:categoria_id>/', views.editar_categoria, name='editar'),
    path('categoria/crear/', views.crear_categoria, name='crear'),
    path('vistacate/', views.ver_categoria, name='ver'),
    path('actualizar/<int:producto_id>/', views.actualizar, name='actualizar'),
    path('login/', views.entrar, name="login")
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)