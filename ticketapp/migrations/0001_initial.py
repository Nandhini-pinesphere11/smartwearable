# Generated by Django 5.0 on 2023-12-13 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_mobile_no', models.CharField(max_length=15)),
                ('customer_email_id', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='PickupRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.CharField(max_length=20, unique=True)),
                ('product_name', models.CharField(max_length=255)),
                ('variant_no', models.CharField(max_length=50)),
                ('problem_category', models.CharField(max_length=100)),
                ('problem_description', models.TextField()),
                ('date_of_purchase', models.DateField()),
                ('invoice_copy', models.FileField(upload_to='invoice_copies/')),
                ('issue_voice', models.FileField(upload_to='issue_voices/')),
                ('front_image', models.FileField(upload_to='front_images/')),
                ('back_image', models.FileField(upload_to='back_images/')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(max_length=255)),
                ('address_line_2', models.CharField(blank=True, max_length=255, null=True)),
                ('landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=10)),
                ('customer_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ticketapp.customerdetails')),
            ],
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='ticket_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ticketapp.pickuprequest'),
        ),
    ]