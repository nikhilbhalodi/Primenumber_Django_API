from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app1.views import PrimeView


# router = routers.DefaultRouter()
# router.register(r'create', PrimeView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('create/', PrimeView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
