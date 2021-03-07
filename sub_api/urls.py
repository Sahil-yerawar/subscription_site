# sub_api/urls.py

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'subscriptions',views.SubscriptionsViewSet)
#router.register(r'homepage',views.index,basename='index')

urlpatterns = [
        path('',include(router.urls)),
        path('api-auth/', include('rest_framework.urls',
            namespace='rest_framework')),
        path('homepage',views.index,name='index'),
        path(r'subscribe',views.add_email_form,name='subscribe')
        ]
