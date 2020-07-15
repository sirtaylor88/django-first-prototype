from django.urls import path
from .views import (
    CourseShowView,
    CourseIndexView,
    CourseNewView,
    CourseEditView,
    CourseDeleteView,
)

app_name = "courses"
urlpatterns = [
    path("", CourseIndexView.as_view(), name="courses-index"),
    path("new/", CourseNewView.as_view(), name="courses-new"),
    path("<int:id>/", CourseShowView.as_view(), name="courses-show"),
    path("<int:id>/edit/", CourseEditView.as_view(), name="courses-edit"),
    path("<int:id>/delete/", CourseDeleteView.as_view(), name="courses-delete"),
]
