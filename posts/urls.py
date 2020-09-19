from django.urls import path

from .views import PostListAPIView

urlpatterns = [path('normal/posts/', PostListAPIView.as_view())]
