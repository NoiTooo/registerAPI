from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    # api/auth/ ^users/$ [name='user-list']
    # api/auth/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
    # api/auth/ ^users/activation/$ [name='user-activation']
    # api/auth/ ^users/activation\.(?P<format>[a-z0-9]+)/?$ [name='user-activation']
    # api/auth/ ^users/me/$ [name='user-me']
    # api/auth/ ^users/me\.(?P<format>[a-z0-9]+)/?$ [name='user-me']
    # api/auth/ ^users/resend_activation/$ [name='user-resend-activation']
    # api/auth/ ^users/resend_activation\.(?P<format>[a-z0-9]+)/?$ [name='user-resend-activation']
    # api/auth/ ^users/reset_password/$ [name='user-reset-password']
    # api/auth/ ^users/reset_password\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password']
    # api/auth/ ^users/reset_password_confirm/$ [name='user-reset-password-confirm']
    # api/auth/ ^users/reset_password_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password-confirm']
    # api/auth/ ^users/reset_email/$ [name='user-reset-username']
    # api/auth/ ^users/reset_email\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username']
    # api/auth/ ^users/reset_email_confirm/$ [name='user-reset-username-confirm']
    # api/auth/ ^users/reset_email_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username-confirm']
    # api/auth/ ^users/set_password/$ [name='user-set-password']
    # api/auth/ ^users/set_password\.(?P<format>[a-z0-9]+)/?$ [name='user-set-password']
    # api/auth/ ^users/set_email/$ [name='user-set-username']
    # api/auth/ ^users/set_email\.(?P<format>[a-z0-9]+)/?$ [name='user-set-username']
    # api/auth/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
    # api/auth/ ^jwt/create/? [name='jwt-create']
    # api/auth/ ^jwt/refresh/? [name='jwt-refresh']
    # api/auth/ ^jwt/verify/? [name='jwt-verify']
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
