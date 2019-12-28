# Generated by Django 3.0.1 on 2019-12-28 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarColorPrices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_price', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
            options={
                'db_table': 'car_color_prices',
            },
        ),
        migrations.CreateModel(
            name='CarColors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=50)),
                ('img_url', models.URLField(max_length=2000)),
            ],
            options={
                'db_table': 'car_colors',
            },
        ),
        migrations.CreateModel(
            name='CarModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('car_colors', models.ManyToManyField(through='price.CarColorPrices', to='price.CarColors')),
            ],
            options={
                'db_table': 'car_models',
            },
        ),
        migrations.CreateModel(
            name='CarTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'car_types',
            },
        ),
        migrations.CreateModel(
            name='CarTypePrices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='car_models', to='price.CarModels')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='car_types', to='price.CarTypes')),
            ],
            options={
                'db_table': 'car_type_prices',
            },
        ),
        migrations.AddField(
            model_name='carmodels',
            name='car_types',
            field=models.ManyToManyField(related_name='car_models', through='price.CarTypePrices', to='price.CarTypes'),
        ),
        migrations.AddField(
            model_name='carcolorprices',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='price.CarColors'),
        ),
        migrations.AddField(
            model_name='carcolorprices',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='price.CarModels'),
        ),
    ]
