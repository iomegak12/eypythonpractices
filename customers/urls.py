from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from django.conf.urls import url, include
from .apis import CustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    url(r'^home$', TemplateView.as_view(template_name='customers/home.html')),
    url(r'', include(router.urls))
]
