from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from gpblog.views import *

urlpatterns = [
    path('', home),
    path('blog/<slug:url>', post),
    path('category/<slug:url>',category),
    path('about/',about),
    path('contact/',contact),
    

]
