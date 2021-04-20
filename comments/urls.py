from django.urls import path
from . import views

urlpatterns = [
    path("", views.CommentListApiView.as_view(), name="comment_list"),
    path("<int:pk>", views.CommentDetailAPIView.as_view(), name="comment_detail"),
    path("create", views.CommentCreateAPIView.as_view(), name="comment_create"),
]
