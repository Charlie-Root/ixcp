# Generated by Django 3.1.1 on 2020-09-12 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_peers_resourceasn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peers',
            name='peer_asn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.resourceasn'),
        ),
    ]
