from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AuthView, CategoryViewSet, CommentsViewSet, GenreViewSet,
                    ReviewsViewSet, TitlesViewSet, TokenView, UserViewSet)

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)
router.register('titles', TitlesViewSet)
router.register(r'titles/(?P<title_id>[0-9]+)/reviews', ReviewsViewSet,
                basename='reviews')
router.register(r'titles/(?P<title_id>[0-9]+)/reviews/('
                r'?P<review_id>[0-9]+)/comments',
                CommentsViewSet,
                basename='comments')
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token/', TokenView.as_view(), name='get_token'),
    path('v1/auth/email/', AuthView.as_view(),
         name='get_confirmation_code'),
]
