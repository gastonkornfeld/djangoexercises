


from django.urls import path
from . import views


urlpatterns = [
    path('sign_up', views.sign_up_user, name='sign_up_user'),
    path('login_user', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),
    path('profile', views.profile_user, name = 'profile_user'),

]

