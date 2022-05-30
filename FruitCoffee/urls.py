from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
#from APIFruitCoffee.views.viewUsuario import User
#from django.conf import settings
#from django.contrib.staticfiles.urls import static

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('login.urls')),
    path('',include('APIFruitCoffee.urls')),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


