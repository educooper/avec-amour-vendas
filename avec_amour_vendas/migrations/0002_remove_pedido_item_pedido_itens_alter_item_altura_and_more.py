# Generated by Django 4.1 on 2024-10-08 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avec_amour_vendas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='item',
        ),
        migrations.AddField(
            model_name='pedido',
            name='itens',
            field=models.ManyToManyField(related_name='pedidos', to='avec_amour_vendas.item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='altura',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='comprimento',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='largura',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='peso',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='status',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='avec_amour_vendas.cliente'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor_frete',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
