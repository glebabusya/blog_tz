from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListAPIView.as_view(), name='post_list'),
    path('<int:pk>', views.PostDetailAPIView.as_view(), name='post_detail'),
    path('upvote/<int:pk>', views.upvote, name='upvote')
]