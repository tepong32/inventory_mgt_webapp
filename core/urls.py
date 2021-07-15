from django.urls import path, include
from .views import (
    DashboardView,
    PurchaseItemCreateView,
    PurchaseItemDetailView,
    PurchaseItemUpdateView,
    PurchaseItemDeleteView,
    SellItemCreateView,
    SellItemDetailView,
    SellItemUpdateView,
    SellItemDeleteView
    )

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard-view'),
    path('p/add/', PurchaseItemCreateView.as_view(), name='add-purchase'),
    path('p/<str:slug>/', PurchaseItemDetailView.as_view(), name='detail-purchase'),
    path('p/<str:slug>/update/', PurchaseItemDeleteView.as_view(), name='update-purchase'),
    path('p/<str:slug>/delete/', PurchaseItemDeleteView.as_view(), name='delete-purchase'),
    path('s/add/', SellItemCreateView.as_view(), name='add-sell'),
    path('s/<str:slug>/', SellItemDetailView.as_view(), name='detail-sell'),
    path('s/<str:slug>/update/', SellItemUpdateView.as_view(), name='update-sell'),
    path('s/<str:slug>/delete/', SellItemDeleteView.as_view(), name='delete-sell'),

]