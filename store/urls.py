from django.urls import path
from . import views

urlpatterns = [
    path('category/',views.store,name='category'),
    path('category/<slug:category_slug>/',views.store,name='products_by_category')
]