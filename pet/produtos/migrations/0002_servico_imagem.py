# Generated by Django 5.1.7 on 2025-03-31 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produtos/'),
        ),
    ]
