from django.urls import path
from django.conf import settings
from  django.conf.urls.static import  static
from .views import RegisterApiView, checkRegistrationstatus,Approvereg


urlpatterns=[
    path('regapi/',RegisterApiView.as_view()),
    path('checkstatus/<int:pk>/',checkRegistrationstatus.as_view()),
    path('aprove/<int:pk>/',Approvereg.as_view())

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)