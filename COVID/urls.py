from django.conf.urls import url
from COVID import views


urlpatterns = [
    url(r'^covidin$',views.COVID_India_request),
    url(r'^covidin/(.*)$',views.COVID_India_request)
]
