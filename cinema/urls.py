from django.urls import path, include
from rest_framework import routers

from cinema.views import (GenreDetail,
                          GenreList,
                          ActorList,
                          ActorDetail,
                          CinemaHallList,
                          CinemaHallDetail,
                          MovieViewSet)
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinemahall/", CinemaHallList.as_view(), name="cinemahall-list"),
    path("cinemahall/<int:pk>/",
         CinemaHallDetail.as_view(),
         name="cinemahall-detail"
         ),
    path("", include(router.urls)),
]

app_name = "cinema"
