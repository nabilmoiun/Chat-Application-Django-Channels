from django.contrib import admin
from django.urls import path, include
from django.conf.urls import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from chat.views import login_view, logout_view, signup_view
urlpatterns = [
    # path('accounts/login/', auth_views.LoginView.as_view()),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

