from django.urls import path
from .views import *
from django.urls import path
from .views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView

app_name = 'users'

urlpatterns = [
    path('create/', UserCreate.as_view(), name="create_user"),
    path('users/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),


    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),

]
