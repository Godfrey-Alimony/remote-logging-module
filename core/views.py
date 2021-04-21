from django.shortcuts import render
from django.views.generic import ListView,DetailView,View
from . models import NetworkLogs, Logs


class HomeView(ListView):
	model = NetworkLogs
	template_name = "home.html"


class SysLogs(ListView):
	model = Logs
	template_name = "logs.html"

