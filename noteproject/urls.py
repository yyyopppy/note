from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views 
#from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    # path('', login_required(index_view), name="index"),
    path('admin/', admin.site.urls),
    path('', include('note.urls')),
    # path('', include('accounts.urls')),
    #path('', include('note.urls')),
    path('login/', include('accounts.urls')),
    # path('mypage', include('note.urls')),
    # path('update', include('note.urls')),
    path('', include("django.contrib.auth.urls")),
    path('note/', include('note.urls')),
    # path('reactions/', include('reactions.urls')),


    # path('password_reset/',
    #     auth_views.PasswordResetView.as_view(
    #     template_name = "password_reset.html"),
    #     name ='password_reset'),
    
    # path('password_reset/done/',
    #     auth_views.PasswordResetDoneView.as_view(
    #     template_name = "password_reset_sent.html"),
    #     name ='password_reset_done'),
    
    # path('reset/<uidb64>/<token>',
    #     auth_views.PasswordResetConfirmView.as_view(
    #     template_name = "password_reset_form.html"),
    #     name ='password_reset_confirm'),
    

    # path('reset/done/',
    #     auth_views.PasswordResetCompleteView.as_view(
    #     template_name = "password_reset_done.html"),
    #     name ='password_reset_complete'),

]

# urlpatterns += static(
#     settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT
# )


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)