from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer.generics import \
    ObserverModelInstanceMixin
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Post
from .serializers import PostDetailSerializer


class ListPostsConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    queryset = Post.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = PostDetailSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = PostDetailSerializer


class ObservePostChange(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    queryset = Post.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = PostDetailSerializer
