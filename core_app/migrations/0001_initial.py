# Generated by Django 4.1 on 2022-08-16 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudiAndVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Аудио и видео')),
            ],
        ),
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Аккумулятор')),
            ],
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Камера')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='ComputingResources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Вычислительные ресурсы')),
            ],
        ),
        migrations.CreateModel(
            name='ContentsOfDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Комплект поставки')),
            ],
        ),
        migrations.CreateModel(
            name='DimensionsAndWeight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Размеры и вес')),
            ],
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Дисплей')),
            ],
        ),
        migrations.CreateModel(
            name='DisplayAndBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Дисплей и корпус')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Поддержка сетей')),
            ],
        ),
        migrations.CreateModel(
            name='SecureAuthentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Безопасная аутентификация')),
            ],
        ),
        migrations.CreateModel(
            name='WaterAndDustProtection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Защита от воды и пыли')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('memory', models.CharField(choices=[('64', '64'), ('128', '128'), ('254', '254'), ('508', '508')], default=None, max_length=3, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='catalog,photo')),
                ('audi_and_video', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.audiandvideo')),
                ('battery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.battery')),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.camera')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.color')),
                ('computing_resources', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.computingresources')),
                ('contents_of_delivery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.contentsofdelivery')),
                ('dimensions_and_weight', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.dimensionsandweight')),
                ('display', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.display')),
                ('display_and_body', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.displayandbody')),
                ('network_support', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.networksupport')),
                ('secure_authentication', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.secureauthentication')),
                ('water_and_dust_protection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.wateranddustprotection')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]