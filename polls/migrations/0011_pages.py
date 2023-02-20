# Generated by Django 2.2.12 on 2021-02-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0010_auto_20210216_0836"),
    ]

    operations = [
        migrations.CreateModel(
            name="pages",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Тема")),
                ("href", models.TextField(verbose_name="Ссылка")),
            ],
            options={
                "verbose_name": "Загрузка/выгрузка",
            },
        ),
    ]
