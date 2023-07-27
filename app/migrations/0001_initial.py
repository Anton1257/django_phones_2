# Generated by Django 4.2.3 on 2023-07-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Phone",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image", models.ImageField(upload_to="phones/")),
                ("release_date", models.DateField()),
                ("lte_exists", models.BooleanField()),
                ("slug", models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
