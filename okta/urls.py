
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

from okta import views

urlpatterns = [
    path('oidc/', include('mozilla_django_oidc.urls')),
    path('',TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('login',TemplateView.as_view(template_name='login.html')),
    path('okta_error',views.OktaErrorView.as_view(),name='okta_error')
]
