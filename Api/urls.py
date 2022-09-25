from django.urls import path, include

from . import views 

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    
    path('login/', views.LoginView.as_view()),
    # path('profile/', views.ProfileView.as_view()),
    
    path('accountFunding/', views.accountFunding, name='accountFunding',),
    path('withdraw/', views.withdraw, name='withdraw',),
    path('transfert/', views.transfert, name='transfert',),
    
    
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# router = DefaultRouter()
# router.register(r"user", views.UserViewSet, basename="user")
# urlpatterns += router.urls