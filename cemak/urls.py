from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import (
    LoginView, SignupView, LogoutView, PasswordResetView, EmailView
)



urlpatterns = [
    # cemak
    path('', homeView, name='home'),
    path('aulas/', alunoView, name='aulas'),
    
    
    #path('eventos/', eventosView, name='eventos'),
    #path('campanhas/', campanhasView, name='campanhas'),
    
    # allauth
    path('account/', include(('allauth.urls', 'auth'), namespace='auth')),
    path('account/login/', LoginView.as_view(), name='account_login'),
    path('account/signup/', SignupView.as_view(), name='account_signup'),
    path('account/logout/', LogoutView.as_view(), name='account_logout'),
    path('account/password/reset/', PasswordResetView.as_view(), name='account_reset_password'),
    path('account/email/', EmailView.as_view(), name='account_email'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



