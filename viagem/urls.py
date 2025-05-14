
from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

from django.conf import settings
from rest_framework import routers
from blog.views import TopicoViewSet

router = routers.DefaultRouter()
router.register('blog',TopicoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('cadastro/', include('cadastro.urls')),
    path('destinos/', include('destinos.urls')),
    path('fotos/', include('fotos.urls')),
    path('blog/', include('blog.urls')),
]

urlpatterns +=[
    path('accounts/',include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

