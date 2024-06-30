# Generated by Django 5.0.6 on 2024-06-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructionMaterial', '0001_initial'),
        ('stages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='materials',
            field=models.ManyToManyField(blank=True, related_name='stages', to='constructionMaterial.material'),
        ),
    ]
