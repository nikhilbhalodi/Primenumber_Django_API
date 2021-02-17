from django.contrib import admin
from django.urls import path,include
from app1.views import PrimeView



#create path for view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', PrimeView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
