from django.urls import path

from core.views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),

]
