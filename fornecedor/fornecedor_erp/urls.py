from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'fornecedores', views.FornecedorViewSet)
router.register(r'compras', views.CompraViewSet)

urlpatterns = [
  path('cadastrarFornecedor', views.cadastrarFornecedor),
  path('listarFornecedores', views.listarFornecedores),
  path('excluirFornecedor/<int:id>', views.excluirFornecedor),
  path('editarFornecedor/<int:id>', views.editarFornecedor),
  path('cadastrarCompra', views.cadastrarCompra),
  path('listarCompras', views.listarCompras),
  path('excluirCompra/<int:id>', views.excluirCompra),
  path('editarCompra/<int:id>', views.editarCompra),
  path('logout/', views.logout_view),
]

urlpatterns += router.urls