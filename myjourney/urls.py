
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
# from . .settings import MEDIA_ROOT

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('blog/', views.blog),
    path('portfoliyo/', views.portfoliyo),
    path('contact/', views.contact),
    path('blog_details/', views.blog_details),

    
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

