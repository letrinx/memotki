"""memotki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
import memsy.views as views
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.HomeView.as_view(), name='home'),
    path('newmem/', views.AddMemView.as_view(), name='addnew'),
    re_path(r'^mem/(?P<id>(\d+))/', views.ShowMemView.as_view(), name='showmem'),
    path('random/', views.RandomMemView.as_view(), name='random'),
    path('top', views.TopMemsView.as_view(), name="top"),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    re_path(r'^addcomment/(?P<pk>(\d+))/', views.AddCommentView.as_view(), name='addcomment'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)