from django.urls import path
from .views import ExpoPushTokenView, ExpoPushTokensListView, ExpoPushTokenDetailView, ExpoPushTokenDeleteView, ExpoPushTokenUpdateView, ExpoPushTokenCreateView

urlpatterns = [
    path('notifications/', ExpoPushTokenView.as_view(), name='create-expo-push-token'),
    path('notifications/user/list/', ExpoPushTokensListView.as_view(), name='list-expo-push-tokens'),
    path('notifications/<int:id>/', ExpoPushTokenDetailView.as_view(), name='retrieve-expo-push-token'),
    path('notifications/<int:id>/delete/', ExpoPushTokenDeleteView.as_view(), name='delete-expo-push-token'),
    path('notifications/<int:id>/update/', ExpoPushTokenUpdateView.as_view(), name='update-expo-push-token'),
    path('notifications/create/', ExpoPushTokenCreateView.as_view(), name='create-expo-push-token'),
]
