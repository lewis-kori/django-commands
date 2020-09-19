from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from djangochannelsrestframework.consumers import view_as_consumer

from posts.views import ListPostsConsumer, ObservePostChange, PostListAPIView

application = ProtocolTypeRouter({
    'websocket':
    AuthMiddlewareStack(
        URLRouter([
            path('websockets/', ListPostsConsumer),
            path('blogposts/', view_as_consumer(PostListAPIView.as_view())),
            path('blogposts/observer/', ObservePostChange)
        ]))
})
