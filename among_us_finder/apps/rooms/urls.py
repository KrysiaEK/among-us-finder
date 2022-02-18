from django.urls import path
from django.contrib.auth.decorators import login_required

from among_us_finder.apps.rooms import views

app_name = 'rooms'

urlpatterns = [
    path('create_room', login_required(views.CreateRoomFormView.as_view()), name='create_room_form'),
    path('room_created', views.RoomCreatedView.as_view(), name='room_created'),
    path('room_list', views.RoomList.as_view(), name='room_list'),
    path('<int:pk>', views.JoinRoom.as_view(), name='room_detail'),
    path('room_conversation/<int:pk>', login_required(views.RoomConversation.as_view()), name='room_conversation'),
    path('leave_room/<int:pk>', login_required(views.LeaveRoomView.as_view()), name='leave_room'),
    path('user_rooms', login_required(views.UserRooms.as_view()), name='user_room'),
    path('participants_list/<int:pk>', login_required(views.ParticipantList.as_view()), name='participants_list'),
    path('delete_participant/<int:room_pk>/<int:user_pk>/', login_required(views.DeleteParticipant.as_view()),
         name='participant_delete'),
    path('join_error/<str:error_code>/', views.JoinRoomError.as_view(), name='join_room_error'),
    path('report_user/<int:user_pk>/<int:room_pk>/', login_required(views.ReportUserFormView.as_view()),
         name='report_user'),
    path('report_user/<int:user_pk>/<int:room_pk>/user_reported/', views.ReportSuccess.as_view(), name='user_reported'),
