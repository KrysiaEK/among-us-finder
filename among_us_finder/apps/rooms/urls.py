from django.urls import path
from . import views
app_name = 'rooms'

urlpatterns = [
	path('create_room', views.CreateRoomFormView.as_view(), name='create_room_form'),
	path('room_created', views.RoomCreatedView.as_view(), name='room_created'),
	path('room_list', views.RoomList.as_view(), name='room_list'),
	path('<int:pk>', views.RoomDetail.as_view(), name='room_detail'),
	path('room_conversation/<int:pk>', views.RoomConversation.as_view(), name='room_conversation'),
	#path('search', views.RoomSearchView.as_view(), name='search')
]
