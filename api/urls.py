from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = [
    path("get-token/", obtain_auth_token),
    path("auth/", include('rest_framework.urls')),
    path("bucketlists/", CreateView.as_view(), name="create"),
    path("bucketlists/<int:pk>/", DetailsView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
