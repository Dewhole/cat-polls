# Generated by Django 2.2.12 on 2021-02-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0004_auto_20210211_0621"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="company",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Компания"
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание (Вы купили)"
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="facture",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Фактура"
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="factureDate",
            field=models.DateField(blank=True, null=True, verbose_name="Дата фактуры"),
        ),
        migrations.AlterField(
            model_name="users",
            name="phone",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Телефон"
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="phoneCompany",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Телефон Организации"
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="phoneMobile",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Мобильный Телефон"
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="rating1",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Ответ 1"
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="rating2",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Ответ 2"
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="rating3",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Ответ 3"
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="rating4",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Ответ 4"
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="rating5",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Ответ 5"
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="rating6",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Ответ 6"
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="unswer1",
            field=models.TextField(blank=True, null=True, verbose_name="Примечание 1"),
        ),
        migrations.AlterField(
            model_name="users",
            name="unswer2",
            field=models.TextField(blank=True, null=True, verbose_name="Примечание 2"),
        ),
        migrations.AlterField(
            model_name="users",
            name="unswer3",
            field=models.TextField(blank=True, null=True, verbose_name="Примечание 3"),
        ),
        migrations.AlterField(
            model_name="users",
            name="unswer4",
            field=models.TextField(blank=True, null=True, verbose_name="Примечание 4"),
        ),
        migrations.AlterField(
            model_name="users",
            name="unswer5",
            field=models.TextField(blank=True, null=True, verbose_name="Примечание 5"),
        ),
        migrations.AlterField(
            model_name="users",
            name="unswer6",
            field=models.TextField(blank=True, null=True, verbose_name="Примечание 6"),
        ),
    ]
