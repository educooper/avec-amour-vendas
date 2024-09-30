from django.shortcuts import render, redirect
from .forms import ClienteForm, PagamentoForm, PedidoForm, ClienteFormSet, ItemForm
from .models import Pedido, Cliente, Item

def criar_pedido(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        endereco_formset = ClienteFormSet(request.POST)
        pagamento_form = PagamentoForm(request.POST)
        pedido_form = PedidoForm(request.POST)
        
        if cliente_form.is_valid() and endereco_formset.is_valid() and pagamento_form.is_valid() and pedido_form.is_valid():
            cliente = cliente_form.save()
            endereco_formset.instance = cliente
            endereco_formset.save()
            pagamento = pagamento_form.save()
            pedido = pedido_form.save(commit=False)
            pedido.cliente = cliente
            pedido.pagamento = pagamento
            pedido.save()
            pedido_form.save_m2m()  # Salva os itens selecionados
            return redirect('lista_pedidos')
    else:
        cliente_form = ClienteForm()
        endereco_formset = ClienteFormSet()
        pagamento_form = PagamentoForm()
        pedido_form = PedidoForm()
    
    return render(request, 'pedido_form.html', {
        'cliente_form': cliente_form,
        'endereco_formset': endereco_formset,
        'pagamento_form': pagamento_form,
        'pedido_form': pedido_form,
    })


def cadastrar_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_itens')  # Redireciona para uma página de listagem de itens
    else:
        form = ItemForm()

    return render(request, 'cadastrar_item.html', {'form': form})

def lista_itens(request):
    itens = Item.objects.all()  # Busca todos os itens no banco de dados
    return render(request, 'lista_itens.html', {'itens': itens})



