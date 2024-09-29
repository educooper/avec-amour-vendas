from django import forms
from django.forms import inlineformset_factory
from .models import Cliente, Endereco, Pagamento, Pedido, Item

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'complemento', 'cidade', 'estado', 'cep']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'cpf','rg','instagram','telegram']

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['tipo', 'sinal', 'total', 'status']

class PedidoForm(forms.ModelForm):
    itens = forms.ModelMultipleChoiceField(
        queryset=Item.objects.filter(status=True),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Pedido
        fields = ['cliente', 'valor_total', 'itens']

# Formset para o Cliente e Endereço
ClienteFormSet = inlineformset_factory(
    Cliente, Endereco, form=EnderecoForm, extra=1
)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['descricao', 'valor', 'custo', 'peso', 'altura', 'largura', 'comprimento', 'estoque', 'status']
