# Generated by Django 4.0 on 2022-01-25 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('BuyerID', models.AutoField(primary_key=True, serialize=False)),
                ('Bname', models.CharField(max_length=50)),
                ('Baddress', models.CharField(max_length=50)),
                ('Bphone_number', models.BigIntegerField()),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('SellerID', models.AutoField(primary_key=True, serialize=False)),
                ('Sname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('Saddress', models.CharField(max_length=50)),
                ('Sphone_number', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('LandID', models.AutoField(primary_key=True, serialize=False)),
                ('buys', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri.buyer')),
                ('owns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('BrokerID', models.AutoField(primary_key=True, serialize=False)),
                ('Brname', models.CharField(max_length=50)),
                ('Brphone_number', models.BigIntegerField()),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('helps', models.ManyToManyField(to='agri.Buyer')),
            ],
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('AmenitiesID', models.AutoField(primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=50)),
                ('Land_area', models.BigIntegerField()),
                ('Soil_type', models.CharField(max_length=30)),
                ('Amount', models.BigIntegerField()),
                ('water_sources', models.CharField(max_length=50)),
                ('suitable_crop', models.CharField(max_length=50)),
                ('weather', models.CharField(max_length=30)),
                ('protection_type', models.CharField(max_length=50)),
                ('contains', models.ManyToManyField(to='agri.Buyer')),
                ('containss', models.ManyToManyField(to='agri.Seller')),
            ],
        ),
    ]
