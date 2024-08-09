# Generated by Django 5.0.3 on 2024-08-02 07:58

import django.db.models.deletion
import embed_video.fields
from django.conf import settings
from django.db import migrations, models


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
                ('cat_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Egit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('egit_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Foo_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foo_name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=400)),
                ('video', embed_video.fields.EmbedVideoField(null=True)),
                ('contact', models.CharField(default='1234', max_length=12)),
                ('timings', models.CharField(max_length=14)),
                ('rating', models.FloatField(default=0)),
                ('least_price', models.IntegerField(null=True)),
                ('keywords', models.CharField(default='spicy', max_length=1000, null=True)),
                ('category', models.ManyToManyField(to='core.category')),
                ('egit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.egit')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_photo', models.ImageField(default='unable', upload_to='static/images/menu_pics/')),
                ('name', models.CharField(max_length=200)),
                ('normal_price', models.IntegerField(default=100)),
                ('premium_price', models.IntegerField(default=100)),
                ('rating', models.FloatField(default=0)),
                ('foo_cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.foo_category')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='core.staller')),
            ],
        ),
        migrations.AddField(
            model_name='foo_category',
            name='sh_owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.staller'),
        ),
        migrations.CreateModel(
            name='Subcat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(blank=True, max_length=30, null=True)),
                ('sub_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='FooRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foo_ratings', to='core.menuitems')),
            ],
            options={
                'unique_together': {('user', 'menu')},
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('staller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='core.staller')),
            ],
            options={
                'unique_together': {('user', 'staller')},
            },
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('staller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='core.staller')),
            ],
            options={
                'unique_together': {('user', 'staller')},
            },
        ),
    ]
