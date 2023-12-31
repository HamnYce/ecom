# Generated by Django 4.2.4 on 2023-08-28 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_userprofile_gender'),
        ('products', '0004_alter_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile', to_field='username'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('owner', 'name')},
        ),
    ]
