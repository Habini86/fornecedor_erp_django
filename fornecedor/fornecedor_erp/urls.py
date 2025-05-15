from django.urls import path
from . import views

urlpatterns = [
  path('cadastrarFornecedor', views.cadastrarFornecedor),
  path('listarFornecedores', views.listarFornecedores),
  path('excluirFornecedor/<int:id>', views.excluirFornecedor),
  path('editarFornecedor/<int:id>', views.editarFornecedor),
  path('cadastrarCompra', views.cadastrarCompra),
  path('listarCompras', views.listarCompras),
  path('excluirCompra/<int:id>', views.excluirCompra),
  path('editarCompra/<int:id>', views.editarCompra),
]