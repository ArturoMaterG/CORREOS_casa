from django.urls import path
from .views import DashboardHomeView,NewslettersDashboardHomeView, NewslettersCreatedViews


app_name= "dashboard"

urlpatterns = [
    path('',DashboardHomeView.as_view(),name='home'),
    path('list/',NewslettersDashboardHomeView.as_view(),name='list'),
    path('create/',NewslettersCreatedViews.as_view(),name='create')
]
