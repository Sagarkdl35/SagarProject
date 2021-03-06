from unicodedata import name
from django.urls import path
from firstapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('vehicles',views.vehicles,name='vehicles'),
    path('add_vehicle',views.add_vehicle,name='add_vehicle'),
    path('book',views.book,name='book')
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)