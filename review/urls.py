from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostCommentsViewSet, RestourantCommentsViewSet, CreateRatingAPIView #, favourite_post, favourite_rest


router = DefaultRouter()

router.register('post-comments', PostCommentsViewSet)
router.register('rest-comments', RestourantCommentsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('rating/', CreateRatingAPIView.as_view()),
    # path('post-favorites', favourite_post),
    # path('rest-favorites', favourite_rest),
]