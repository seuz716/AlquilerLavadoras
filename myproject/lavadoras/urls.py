# lavadoras/urls.py
from django.urls import path
from .views import LavadoraListView, LavadoraCreateView, LavadoraUpdateView, LavadoraDeleteView

urlpatterns = [
    path('', LavadoraListView.as_view(), name='lavadoras-list'),
    path('crear/', LavadoraCreateView.as_view(), name='lavadora-create'),
    path('editar/<int:pk>/', LavadoraUpdateView.as_view(), name='lavadora-update'),
    path('eliminar/<int:pk>/', LavadoraDeleteView.as_view(), name='lavadora-delete'),
]
