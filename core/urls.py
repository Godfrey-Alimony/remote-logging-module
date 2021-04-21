from django.urls import path

app_name = 'core'

from .views import (
	HomeView,
	SysLogs,
)

urlpatterns = [
	path('',HomeView.as_view(),name="home"),
	path('logs/',SysLogs.as_view(),name="logs"),
]