from django.urls import path

from . import consumers

urlpatterns = [
    # path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
    path(r'ws/chat/<slug:room_name>/', consumers.ChatConsumer),
]