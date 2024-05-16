


from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path('blogs/', views.BlogListCreate.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', views.BlogRetrieveUpdateDestroy.as_view(), name='blog-detail'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
