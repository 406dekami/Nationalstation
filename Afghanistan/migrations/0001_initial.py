# Generated by Django 5.0 on 2023-12-22 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AfghanistanPopulation",
            fields=[
                ("year", models.IntegerField(blank=True, db_column="Year", null=True)),
                (
                    "population",
                    models.IntegerField(blank=True, db_column="Population", null=True),
                ),
                (
                    "yearly_change",
                    models.FloatField(
                        blank=True, db_column="Yearly %  Change", null=True
                    ),
                ),
                (
                    "yearly_change_0",
                    models.IntegerField(
                        blank=True, db_column="Yearly Change", null=True
                    ),
                ),
                (
                    "migrants_net_field",
                    models.IntegerField(
                        blank=True, db_column="Migrants (net)", null=True
                    ),
                ),
                (
                    "median_age",
                    models.FloatField(blank=True, db_column="Median Age", null=True),
                ),
                (
                    "fertility_rate",
                    models.FloatField(
                        blank=True, db_column="Fertility Rate", null=True
                    ),
                ),
                (
                    "density_p_km2_field",
                    models.IntegerField(
                        blank=True, db_column="Density (P/Km²)", null=True
                    ),
                ),
                (
                    "urban_pop_field",
                    models.FloatField(blank=True, db_column="Urban Pop %", null=True),
                ),
                (
                    "urban_population",
                    models.IntegerField(
                        blank=True, db_column="Urban Population", null=True
                    ),
                ),
                (
                    "country_s_share_of_world_pop",
                    models.FloatField(
                        blank=True, db_column="Country's Share of World Pop", null=True
                    ),
                ),
                (
                    "world_population",
                    models.FloatField(
                        blank=True, db_column="World Population", null=True
                    ),
                ),
                (
                    "afghanistanglobal_rank",
                    models.IntegerField(
                        blank=True,
                        db_column="AfghanistanGlobal Rank",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
            options={
                "verbose_name": "浏览阿富汗人口信息 ",
                "verbose_name_plural": "阿富汗人口信息管理(不可修改)",
                "db_table": "afghanistan_population",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Submission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("submit_time", models.DateTimeField()),
            ],
            options={
                "verbose_name": "浏览网站用户提交信息",
                "verbose_name_plural": "网站用户反馈信息(不可修改)",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("ip_address", models.CharField(max_length=100)),
                ("submit_time", models.DateTimeField()),
            ],
            options={
                "verbose_name": "浏览网站用户信息",
                "verbose_name_plural": "网站用户信息(不可修改)",
            },
        ),
    ]
