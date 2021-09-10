from django.urls import include, path
from rest_framework import routers
from .views import StudentViewSet,TeacherViewSet,CoursesViewSet,EventViewSet

router = routers.DefaultRouter()
router.register(r"student", StudentViewSet)
router.register(r"teacher", TeacherViewSet)
router.register(r"courses", CoursesViewSet)
router.register(r"cal", EventViewSet)




urlpatterns = [
    path("", include(router.urls))
]
