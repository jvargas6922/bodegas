from django.urls import path
from .views import HomeView, CustomLoginView, RegisterView, like_noticia, CotizarView, ResultadoCotizacionView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('like/<int:noticia_id>/', like_noticia, name='like_noticia'),
    path('cotizar/', CotizarView.as_view(), name='cotizar'),
    path('resultado_cotizacion/', ResultadoCotizacionView.as_view(), name='resultado_cotizacion'),
]