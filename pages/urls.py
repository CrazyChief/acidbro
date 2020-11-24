from django.urls import path
from .views import IndexView


urlpatterns = [
    path('<slug:slug>/', IndexView.as_view(), name='page_detail')
]
