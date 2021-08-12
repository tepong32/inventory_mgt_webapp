from django.urls import path, include
from .views import (
    DashboardView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    AddPPurchase,
    PPurchaseDetail,
    UpdatePPurchase,
    DeletePPurchase,
    AddPSell,
    # PSellDetail,
    UpdatePSell,
    DeletePSell,
    ) # or from .views import * :/

urlpatterns = [
    # overview
    path('', DashboardView.as_view(), name='dashboard-view'),

    ### products
    path('add-product/', ProductCreateView.as_view(), name='add-product'),
    path('product/<str:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<str:slug>/update/', ProductUpdateView.as_view(), name='update-product'),
    path('product/<str:slug>/delete/', ProductDeleteView.as_view(), name='delete-product'),
    # product purchases
    path('product/<str:slug>/purchase/add-entry', AddPPurchase.as_view(), name='add-ppurchase'),
    path('product/<str:slug>/', PPurchaseDetail.as_view(), name='ppurchase-detail'),
    path('product/<str:slug>/purchase/update-entry/', UpdatePPurchase.as_view(), name='ppurchase-update'),
    path('product/<str:slug>/purchase/delete-entry/', DeletePPurchase.as_view(), name='ppurchase-delete'),
    # product sells
    path('product/<str:slug>/sell/add-entry', AddPSell.as_view(), name='add-psell'),
    # path('product/<str:slug>/', PSellDetail.as_view(), name='psell-detail'),
    path('product/<str:slug>/sell/update-entry/', UpdatePSell.as_view(), name='psell-update'),
    path('product/<str:slug>/sell/delete-entry/', DeletePSell.as_view(), name='psell-delete'),


    # ### services
    # path('add-service/', ServiceCreateView.as_view(), name='add-service'),
    # path('service/<str:slug>/', ServiceDetailView.as_view(), name='service-detail'),
    # path('service/<str:slug>/update/', ServiceUpdateView.as_view(), name='update-service'),
    # path('service/<str:slug>/delete/', ServiceDeleteView.as_view(), name='delete-service'),
    # # service purchases
    # path('service/<str:slug>/purchase/add-entry', AddPSEntry.as_view(), name='spurchase-add'),
    # path('service/<str:slug>/purchase/update-entry/', UpdatePSEntry.as_view(), name='spurchase-update'),
    # path('service/<str:slug>/purchase/delete-entry/', DeletePSEntry.as_view(), name='spurchase-delete'),
    # # service sells
    # path('service/<str:slug>/sell/add-entry', AddSSEntry.as_view(), name='ssell-add'),
    # path('service/<str:slug>/sell/update-entry/', UpdateSSEntry.as_view(), name='ssell-update'),
    # path('service/<str:slug>/sell/delete-entry/', DeleteSSEntry.as_view(), name='ssell-delete'),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)