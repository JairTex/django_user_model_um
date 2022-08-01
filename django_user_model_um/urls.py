from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'Sistema de Post'
admin.site.site_title = 'Publique o que você quiser!'
admin.site.index_title = 'Sistema de Gerenciamento de Posts'
