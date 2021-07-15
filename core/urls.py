from django.urls import path, include
from .views import (
    DashboardView,
    ItemCreateView,
    ItemDetailView,
    ItemUpdateView,
    ItemDeleteView,
    PurchaseItemCreateView,
    PurchaseItemDetailView,
    PurchaseItemUpdateView,
    PurchaseItemDeleteView,
    SellItemCreateView,
    SellItemDetailView,
    SellItemUpdateView,
    SellItemDeleteView
    ) # or from .views import * :/

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard-view'),
    # item
    path('i/add/', ItemCreateView.as_view(), name='add-item'),
    path('i/<str:slug>/', ItemDetailView.as_view(), name='detail-item'),
    path('i/<str:slug>/update/', ItemDeleteView.as_view(), name='update-item'),
    path('i/<str:slug>/delete/', ItemDeleteView.as_view(), name='delete-item'),
    # purchase
    path('p/add/', PurchaseItemCreateView.as_view(), name='add-purchase'),
    path('p/<str:slug>/', PurchaseItemDetailView.as_view(), name='detail-purchase'),
    path('p/<str:slug>/update/', PurchaseItemDeleteView.as_view(), name='update-purchase'),
    path('p/<str:slug>/delete/', PurchaseItemDeleteView.as_view(), name='delete-purchase'),
    # sell
    path('s/add/', SellItemCreateView.as_view(), name='add-sell'),
    path('s/<str:slug>/', SellItemDetailView.as_view(), name='detail-sell'),
    path('s/<str:slug>/update/', SellItemUpdateView.as_view(), name='update-sell'),
    path('s/<str:slug>/delete/', SellItemDeleteView.as_view(), name='delete-sell'),

]