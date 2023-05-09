# Generated by Django 3.2.18 on 2023-05-09 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire_store', models.DateTimeField(auto_created=True, blank=True, null=True)),
                ('stampin_reg', models.DateTimeField(auto_created=True, blank=True, null=True)),
                ('name_store', models.CharField(blank=True, max_length=50, null=True)),
                ('level_store', models.IntegerField(blank=True, null=True)),
                ('dle_flg', models.BooleanField(default=False)),
                ('user_id_main', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_zone', models.CharField(blank=True, max_length=50, null=True)),
                ('dle_flg', models.BooleanField(default=False)),
                ('id_store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.store')),
            ],
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_table', models.CharField(blank=True, max_length=50, null=True)),
                ('dle_flg', models.BooleanField(default=False)),
                ('id_store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.store')),
                ('id_zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.zone')),
            ],
        ),
        migrations.CreateModel(
            name='StaffStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('dle_flg', models.BooleanField(default=False)),
                ('role_staff_id', models.IntegerField(blank=True, null=True)),
                ('id_store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.store')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_menu', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('img', models.CharField(blank=True, max_length=50, null=True)),
                ('type_menu_id', models.IntegerField(blank=True, null=True)),
                ('status_id', models.BooleanField(default=False)),
                ('dle_flg', models.BooleanField(default=False)),
                ('id_store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.store')),
            ],
        ),
    ]
