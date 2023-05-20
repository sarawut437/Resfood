# Generated by Django 3.2.18 on 2023-05-20 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LookUpType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_code', models.CharField(blank=True, max_length=50, null=True)),
                ('dle_flg', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LookUpValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_code', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('dle_flg', models.BooleanField(default=False)),
                ('att1', models.CharField(blank=True, max_length=50, null=True)),
                ('att2', models.CharField(blank=True, max_length=50, null=True)),
                ('att3', models.JSONField(blank=True, null=True)),
                ('type_code_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.lookuptype')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('frist_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('id_card', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('dle_flg', models.BooleanField(default=False)),
                ('role_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.lookupvalue')),
            ],
        ),
    ]
