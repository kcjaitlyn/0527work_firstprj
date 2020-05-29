from django.contrib import admin
from django.urls import path
from theapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'), #main
    path('intro/', views.intro, name='intro'),
    path('gallery/', views.photos, name='photos'),
    path('design/',views.design, name='design' )
]
