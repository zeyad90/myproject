from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', admin.site.urls),
    path('app2/',include('app2.urls')),
]
