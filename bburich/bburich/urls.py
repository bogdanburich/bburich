from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include(('main_page.urls', 'main_page'), namespace='main_page')),
    path('admin/', admin.site.urls), 
]
