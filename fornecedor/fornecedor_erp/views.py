from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Fornecedor, Compra 
from django.utils import timezone

from .serializers import FornecedorSerializer, CompraSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django.shortcuts import redirect
@login_required
def logout_view(request):
    logout(request)
    return redirect('/admin')

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permission_classes = [permissions.IsAuthenticated]

@login_required
def cadastrarFornecedor(request):
    if request.method == "POST":
        nome_razao = request.POST.get("nome_razao")
        cnpj_cpf = request.POST.get("cnpj_cpf")
        telefone = request.POST.get("telefone")
        email = request.POST.get("email")
        endereco = request.POST.get("endereco")
        status = request.POST.get("status")

        fornecedor = Fornecedor(
            nome_razao=nome_razao,
            cnpj_cpf=cnpj_cpf,
            telefone=telefone,
            email=email,
            endereco=endereco,
            status=status
        )
        fornecedor.save()
        
        return HttpResponseRedirect("/fornecedor/listarFornecedores")
    
    return render(request, "cadastrarForcenedor.html")

@login_required  
def listarFornecedores(request):
    
    fornecedores = Fornecedor.objects.all().distinct()

    return render(request, "listarFornecedores.html", {"fornecedores" : fornecedores})
  
@login_required
def excluirFornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    
    fornecedor.delete()
    
    return HttpResponseRedirect("/fornecedor/listarFornecedores")

@login_required
def editarFornecedor(request, id):
    idFornecedor = id
    if request.method == "POST":
        nome_razao = request.POST.get("nome_razao")
        cnpj_cpf = request.POST.get("cnpj_cpf")
        telefone = request.POST.get("telefone")
        email = request.POST.get("email")
        endereco = request.POST.get("endereco")
        status = request.POST.get("status")
        
        fornecedor = Fornecedor.objects.get(id=idFornecedor)
        
        # Atualizar os campos do fornecedor existente
        fornecedor.nome_razao = nome_razao
        fornecedor.cnpj_cpf = cnpj_cpf
        fornecedor.telefone = telefone
        fornecedor.email = email
        fornecedor.endereco = endereco
        fornecedor.status = status

        # Salvar as alterações
        fornecedor.save()
        
        return HttpResponseRedirect("/fornecedor/listarFornecedores")
        
    fornecedor = Fornecedor.objects.get(id=idFornecedor)
    
    return render(request, "editarFornecedor.html", {"fornecedor": fornecedor})
  
from datetime import datetime

@login_required
def cadastrarCompra(request):
    fornecedores = Fornecedor.objects.all()
    if request.method == "POST":
        descricao = request.POST.get("descricao")
        data = request.POST.get("data")  # formato: YYYY-MM-DD
        hora = request.POST.get("hora")  # formato: HH:MM
        fornecedor_id = request.POST.get("fornecedor")

        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
        # Junta data e hora em um datetime
        if data and hora:
            data_hora_str = f"{data} {hora}"
            data_compra = datetime.strptime(data_hora_str, "%Y-%m-%d %H:%M")
        else:
            data_compra = timezone.now()

        compra = Compra(
            descricao=descricao,
            data=data_compra,
            fornecedor=fornecedor
        )
        compra.save()
        return HttpResponseRedirect("/fornecedor/listarCompras")
    return render(request, "cadastrarCompra.html", {"fornecedores": fornecedores})
  
@login_required
def listarCompras(request):
    
    compras = Compra.objects.all().distinct()

    return render(request, "listarCompras.html", {"compras" : compras})

@login_required  
def excluirCompra(request, id):
    compra = Compra.objects.get(id=id)
    
    compra.delete()
    
    return HttpResponseRedirect("/fornecedor/listarCompras")

@login_required
def editarCompra(request, id):
    from datetime import datetime
    compra = Compra.objects.get(id=id)
    fornecedores = Fornecedor.objects.all()
    if request.method == "POST":
        descricao = request.POST.get("descricao")
        data = request.POST.get("data")  # formato: YYYY-MM-DD
        hora = request.POST.get("hora")  # formato: HH:MM
        fornecedor_id = request.POST.get("fornecedor")

        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
        # Junta data e hora em um datetime
        if data and hora:
            data_hora_str = f"{data} {hora}"
            data_compra = datetime.strptime(data_hora_str, "%Y-%m-%d %H:%M")
        else:
            data_compra = timezone.now()

        compra.descricao = descricao
        compra.data = data_compra
        compra.fornecedor = fornecedor
        compra.save()
        return HttpResponseRedirect("/fornecedor/listarCompras")
    return render(request, "editarCompra.html", {"compra": compra, "fornecedores": fornecedores})