from django.urls import path
from django.contrib import admin
<<<<<<< HEAD
from core import views as core_views
from rest_framework import routers


=======
from rest_framework import routers

>>>>>>> 1dfba54f1272c1f92fa2949c1038b6845b34ac7e
router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('contact/', core_views.ContactAPIView.as_view()),
]
=======
]
>>>>>>> 1dfba54f1272c1f92fa2949c1038b6845b34ac7e
