from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/01', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/',user_views.loginPage,name = "login" ),
    path('logout/',user_views.logoutUser,name = "logout" ),
    path('', include('blog.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
