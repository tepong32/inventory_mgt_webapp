from django.urls import path, include
from .views import (
    DashboardView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView
    )

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard-view'),
    path('add/', ItemCreateView.as_view(), name='add-item'),
    path('<str:slug>/', ItemDetailView.as_view(), name='item-detail'),
    path('<str:slug>/update/', ItemUpdateView.as_view(), name='update-item'),
    path('<str:slug>/delete/', ItemDeleteView.as_view(), name='delete-item'),

]