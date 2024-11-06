from django.urls import path
from portfolio_app.views import IndexView
from . import views

urlpatterns = [
    path('', IndexView, name='index'),
    path('thank',views.thank, name = 'thank' ),
]