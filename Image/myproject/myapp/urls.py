from django.urls import path
from django.conf import settings
# from django.conf.urls.static import static

from myapp import views
# from myproject.myapp import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('upload/', views.image_upload_view,name='out'),
    # path('secret/', views.secret_page, name='secret'),
    # path('secret2/', views.SecretPage.as_view(), name='secret2'),
    # path('register/', views.out, name='out'),
    # path('admin/', views.site.urls),

]
