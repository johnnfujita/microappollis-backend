# Generated by Django 3.0.8 on 2020-08-21 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('generic_vendor_profiles', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodNetStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_quantity', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=16)),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=16)),
                ('manufactor', models.CharField(default='', max_length=100)),
                ('unit_price', models.DecimalField(decimal_places=3, max_digits=14)),
                ('is_infinite', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductGenericClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generic_product_classes', to='generic_vendor_profiles.GlobalSegment')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, unique=True)),
                ('measure_unit', models.CharField(max_length=3)),
                ('is_branded', models.BooleanField(blank=True, default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by_vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_created', to='generic_vendor_profiles.VendorData')),
                ('parent_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_products', to='product_generic_catalog.ProductGenericClass')),
            ],
        ),
        migrations.CreateModel(
            name='FoodProductDisplaySection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('parent_section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_sections', to='product_generic_catalog.FoodProductDisplaySection')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='generic_vendor_profiles.VendorData')),
            ],
        ),
        migrations.CreateModel(
            name='FoodProductAvailable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='products')),
                ('details', models.CharField(blank=True, default='', max_length=250)),
                ('is_displayed', models.BooleanField(blank=True, default=True)),
                ('StoredFood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_generic_catalog.FoodNetStorage', unique=True)),
                ('displayed_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product_generic_catalog.FoodProductDisplaySection')),
            ],
        ),
        migrations.AddField(
            model_name='foodnetstorage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_generic_catalog.ProductInstance'),
        ),
    ]
