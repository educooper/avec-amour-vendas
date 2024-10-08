from django import forms
from django.forms import inlineformset_factory
from .models import Cliente, Endereco, Pagamento, Pedido, Item

CANAL_VENDA_CHOICES = [
        ('instagram', 'Instagram'),
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
        ('ecommerce', 'E-commerce'),
        ('indicacao', 'Indicação'),
    ]

MODALIDADE_FRETE_CHOICES = [
        ('economica', 'Econômica'),
        ('rapida', 'Rápida'),
        ('retirada', 'Retirada'),
    ]

STATUS_FRETE_CHOICES = [
        ('cotado', 'Cotado'),
        ('pendente', 'Pendente'),
        ('enviado', 'Enviado'),
        ('recusado', 'Recusado'),
        ('extraviado', 'Extraviado'),
        ('entregue', 'Entregue'),
    ]

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'rua', 'numero', 'complemento', 'cidade', 'estado']
        apagar = forms.BooleanField(widget=forms.HiddenInput(), required=False) # ocultando campo bool APAGAR

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'cpf','instagram','telegram']

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['tipo', 'sinal', 'total', 'status']

class PedidoForm(forms.ModelForm):
    itens = forms.ModelMultipleChoiceField(
        queryset=Item.objects.filter(status=True),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),  # Alterado para Select Multiple
        required=True  # Se necessário, ou defina como False se não obrigatório
    )

    canal_venda = forms.ChoiceField(
        choices=CANAL_VENDA_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    tipo_frete = forms.ChoiceField(
        choices=MODALIDADE_FRETE_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    status_frete = forms.ChoiceField(
        choices=STATUS_FRETE_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    class Meta:
        model = Pedido
        fields = ['tipo_frete','valor_frete','status_frete','rastreio_frete','valor_total','canal_venda']

# Formset para o Cliente e Endereço -    //  'cliente', 'itens'  , 'quantidade',
ClienteFormSet = inlineformset_factory(
    Cliente, Endereco, form=EnderecoForm, extra=1
)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['descricao', 'valor', 'custo', 'peso', 'altura', 'largura', 'comprimento', 'estoque', 'status']
