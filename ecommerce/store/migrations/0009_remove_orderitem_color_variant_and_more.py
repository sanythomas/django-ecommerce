# Generated by Django 4.1.2 on 2022-12-29 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_orderitem_color_variant_orderitem_size_variant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='color_variant',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='size_variant',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='color_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.colorvariant'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='size_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.sizevariant'),
        ),
    ]