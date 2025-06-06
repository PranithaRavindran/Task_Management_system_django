from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from notes_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes_app.urls')),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
