from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'rooms'

urlpatterns = [
	path('create_room', views.CreateRoomFormView.as_view(), name='create_room_form'),
	path('room_created', views.RoomCreatedView.as_view(), name='room_created'),
	path('room_list', views.RoomList.as_view(), name='room_list'),
	path('<int:pk>', views.RoomDetail.as_view(), name='room_detail'),
	path('room_conversation/<int:pk>', login_required(views.RoomConversation.as_view()), name='room_conversation'),
	path('leave_room/<int:pk>', views.LeaveRoomView.as_view(), name='leave_room'),
	path('user_rooms', login_required(views.UserRooms.as_view()), name='user_room'),
	path('participants_list/<int:pk>', views.ParticipantList.as_view(), name='participants_list'),
	path('delete_participant/<int:room_pk>/<int:user_pk>/', views.DeleteParticipant.as_view(), name='participant_delete'),
	path('join_error/<str:error_code>/', views.JoinRoomError.as_view(), name='join_room_error'),
	#  path('search', views.RoomSearchView.as_view(), name='search')
]
