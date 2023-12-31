# Generated by Django 4.1.7 on 2023-05-30 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fotograf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Malzeme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malzeme_adi', models.CharField(max_length=200)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_adi', models.CharField(max_length=200)),
                ('resim', models.CharField(max_length=100)),
                ('vakit', models.CharField(default=0, max_length=100)),
                ('kisilik', models.CharField(default=0, max_length=100)),
                ('defter', models.CharField(default=0, max_length=200)),
                ('anasayfa', models.BooleanField(default=False)),
                ('kalori', models.CharField(default=0, max_length=100)),
                ('tarif', models.CharField(default=0, max_length=5000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.category')),
            ],
        ),
        migrations.CreateModel(
            name='Tur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TarifMalzeme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kullanilan_adet', models.PositiveIntegerField(default=1)),
                ('malzeme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.malzeme')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
        migrations.AddField(
            model_name='malzeme',
            name='tur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.tur'),
        ),
        migrations.CreateModel(
            name='KullaniciTarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KullaniciMalzeme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adet', models.PositiveIntegerField(default=1)),
                ('malzeme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.malzeme')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
