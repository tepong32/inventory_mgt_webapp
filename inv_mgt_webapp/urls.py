from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views     # authentication views for logins and logouts
from user.views import (
    register,
    user_search_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    # path('about/', about, name="about"),
    path('u/', include('user.urls')),

    ## django-allauth
    path('accounts/', include('allauth.urls')),

    ## ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),

    ## these 'views/html' templates are inside the "user" app because they're related to user accounts
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout' ),
    path('register/', register, name='register' ),
    path('search/', user_search_view, name="user-search"), 
    
    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password-change'),

    path('password-reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'), name='password-reset-confirm'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset.html'), name='password-reset'),
    
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password-reset-complete'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


