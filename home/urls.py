from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'), # this should show an overview
    path('items/', include('core.urls')), 
    # path('db/', include('core.urls')), # this one can be specifics. More on this later.
]