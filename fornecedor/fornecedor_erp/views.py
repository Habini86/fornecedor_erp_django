from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Fornecedor, Compra 
from django.utils import timezone

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
  
def listarFornecedores(request):
    
    fornecedores = Fornecedor.objects.all().distinct()

    return render(request, "listarFornecedores.html", {"fornecedores" : fornecedores})
  
def excluirFornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    
    fornecedor.delete()
    
    return HttpResponseRedirect("/fornecedor/listarFornecedores")

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
  
def listarCompras(request):
    
    compras = Compra.objects.all().distinct()

    return render(request, "listarCompras.html", {"compras" : compras})
  
def excluirCompra(request, id):
    compra = Compra.objects.get(id=id)
    
    compra.delete()
    
    return HttpResponseRedirect("/fornecedor/listarCompras")

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