from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from cinema import views as cinema
from movie import views as movie

app_name = 'api'

urlpatterns = [
    # authentication api
    path('token/', obtain_jwt_token),
    path('token/verify/', verify_jwt_token),
    path('token/refresh/', refresh_jwt_token),

    # cinema api
    path('cinema/', cinema.cinema_api_list_view, name='cinema'),
    path('cinema/<int:pk>/', cinema.cinema_api_detail_view, name='cinema-detail'),
    # TODO: Fix schedules api to get default movies & cinemas
    # path('api/schedules/', views.ScheduleAPIView.as_view(), name='api-reservation-list-cinema'),
    path('schedule/cinema/<int:pk>/', cinema.schedule_cinema_api_view, name='schedule-detail-cinema'),
    path('schedule/movie/<int:pk>/', cinema.schedule_movie_api_view, name='schedule-detail-movie'),

    # review api
    path('review/', movie.review_api_view, name='review'),
    path('review/<int:pk>/', movie.review_detail_api_view, name='review-detail'),

    # movie api
    path('movie/box-office/', movie.box_office_movie_api_view, name='movie-box-office'),
    path('movie/not-open/', movie.not_open_movie_api_view, name='movie-not-open'),
    path('movie/<int:pk>/', movie.movie_detail_api_view, name='movie-detail'),
    path('movie/<int:pk>/staff/', movie.movie_staff_api_view, name='movie-staff'),
    path('movie/<int:pk>/images/', movie.movie_image_api_view, name='movie-images'),
    path('movie/<int:pk>/videos/', movie.movie_video_api_view, name='movie-videos'),
    path('movie/<int:pk>/reviews/', movie.movie_review_api_view, name='movie-reviews'),
]
