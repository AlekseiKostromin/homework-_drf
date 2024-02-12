from django.urls import path
from rest_framework import routers

from lms import views, apps
from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = LmsConfig.name

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='create_lesson'),
    path('lesson/', LessonListAPIView.as_view(), name='all_lessons'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='view_lesson'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update_lesson'),
    path('lesson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete_lesson'),
    ] + router.urls
