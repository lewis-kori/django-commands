import re
from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer.generics import \
    ObserverModelInstanceMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Post
from .serializers import PostDetailSerializer


class ListPostsConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    queryset = Post.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = PostDetailSerializer

    @model_observer(Post)
    async def post_change_handler(self, message, observer=None, **kwargs):
        # called when a subscribed item changes
        await self.send_json(message)

    @post_change_handler.groups_for_signal
    def post_change_handler(self, instance: Post, **kwargs):
        # DO NOT DO DATABASE QURIES HERE
        # This is called very often through the lifecycle of every instance of a Post model
        for hashtag in re.findall(r"#[a-z0-9]+", instance.content.lower()):
            yield f'-hashtag-{hashtag}'

    @post_change_handler.groups_for_consumer
    def post_change_handler(self, hashtag=None, list=False, **kwargs):
        # This is called when you subscribe/unsubscribe
        if hashtag is not None:
            yield f'-hashtag-#{hashtag}'

    @action()
    async def subscribe_to_hashtag(self, hashtag, **kwargs):
        await self.post_change_handler.subscribe(hashtag=hashtag)
        return {}, 201

    @action()
    async def unsubscribe_from_hashtag(self, hashtag, **kwargs):
        await self.post_change_handler.unsubscribe(hashtag=hashtag)
        return {}, 204

    @post_change_handler.serializer
    def post_change_handler(self, instance: Post, action, **kwargs):
        if action == 'delete':
            return {"id": instance.id}
        return {
            "data": {
                "id": instance.id,
                "title": instance.title,
                "content": instance.content
            }
        }


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = PostDetailSerializer


class ObservePostChange(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    queryset = Post.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = PostDetailSerializer
