from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.Home.as_view(), name = "databob-home"),
    path("product/<int:pk>/", views.ProductDetail.as_view(), name = "databob-sbd"),
    path("user/<int:pk>/", views.UserDetail.as_view(), name = "databob-usr"),
    path("register/", views.register, name = "databob-register"),
    path("login/", views.login_user, name = "databob-login"),
    path("logout/", views.logout_user, name = "databob-logout"),
] 

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)