from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views import View
from .models import Noticia, Like, Bodega, BodegaTipo
from django.urls import reverse_lazy
from .forms import CustomAuthenticationForm, CustomUserCreationForm

class HomeView(ListView):
    model = Noticia
    template_name = 'home.html'
    context_object_name = 'noticias'

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'
    
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

@method_decorator(login_required, name='dispatch')
class CotizarView(View):
    def get(self, request):
        #Filtrar los tipos de bodega que tienen al menos una bodega disponible, así no mostramos bodegas no disponibles
        tipos_bodegas = BodegaTipo.objects.filter(bodega__disponible=True).distinct()
        return render(request, 'cotizar.html', {'tipos_bodegas': tipos_bodegas})

    def post(self, request):
        tipo_id = request.POST.get('tipo_bodega')
        tipo = BodegaTipo.objects.get(id=tipo_id)
        #Selecciona la última bodega disponible de ese tipo
        bodega = Bodega.objects.filter(tipo_bodega=tipo, disponible=True).last()

        if bodega:
            #Marcar la bodega como no disponible para que no se pueda agregar más de una, y la agregamos a la sesión
            bodega.disponible = False
            bodega.save()
            if 'bodegas_seleccionadas' not in request.session:
                request.session['bodegas_seleccionadas'] = []
            request.session['bodegas_seleccionadas'].append({
                'codigo': bodega.codigo,
                'tipo': bodega.tipo_bodega.tipo,
                'precio': bodega.tipo_bodega.precio
            })
            request.session.modified = True

        return redirect('cotizar')

@method_decorator(login_required, name='dispatch')
class ResultadoCotizacionView(View):
    #Recuperamos la lista de bodegas seleccionadas en la sesión de usuario
    def get(self, request):
        bodegas_seleccionadas = request.session.get('bodegas_seleccionadas', [])
        total = 0
        detalles = []

        #Obtenemos la información de cada bodega seleccionada en la sesión y acumulamos resultados
        for bodega_info in bodegas_seleccionadas:
            bodega = get_object_or_404(Bodega, codigo=bodega_info['codigo'])
            detalles.append(bodega)
            total += bodega.tipo_bodega.precio

        return render(request, 'resultado_cotizacion.html', {'detalles': detalles, 'total': total})


#Vista para relación Like-Noticia. Si se da like sobre un like ya dado, se borra (Unlike).
@login_required
def like_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    like, created = Like.objects.get_or_create(user=request.user, noticia=noticia)

    if not created:
        like.delete()

    return redirect('home')