from django.urls import path

from someapp.views import SomeModelView

urlpatterns = [
    path("get-items", SomeModelView.as_view())
]
