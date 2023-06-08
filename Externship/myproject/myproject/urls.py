from django.urls import include, path

urlpatterns = [
    # Other URL patterns for your project
    path("auth/", include("authentication.urls")),
]
