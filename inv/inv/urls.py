from rest_framework.routers import DefaultRouter,SimpleRouter
from inv_api import views
from django.urls.conf import  path,include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls


schema_view = get_swagger_view(title='Invoice API')





router = DefaultRouter()

# register viewset with router

router.register("invoice", views.invoiceModelViewSet, basename="invoice")
urlpatterns = [
    path('', include(router.urls)),
    path(r'swagger-docs/', schema_view),
    path(r'docs/', include_docs_urls(title='Invoice API'))
]