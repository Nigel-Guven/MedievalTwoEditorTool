from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("medieval/", include("medieval.urls")),
    path("admin/", admin.site.urls),
]