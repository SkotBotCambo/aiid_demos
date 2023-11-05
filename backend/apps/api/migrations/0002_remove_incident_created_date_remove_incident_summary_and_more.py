# Generated by Django 4.2.6 on 2023-10-29 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="incident",
            name="created_date",
        ),
        migrations.RemoveField(
            model_name="incident",
            name="summary",
        ),
        migrations.AddField(
            model_name="incident",
            name="algd_deployer",
            field=models.CharField(default="", max_length=1000),
        ),
        migrations.AddField(
            model_name="incident",
            name="algd_developer",
            field=models.CharField(default="", max_length=1000),
        ),
        migrations.AddField(
            model_name="incident",
            name="algd_harm",
            field=models.CharField(default="", max_length=1000),
        ),
        migrations.AddField(
            model_name="incident",
            name="date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Incident Date"
            ),
        ),
        migrations.AddField(
            model_name="incident",
            name="description",
            field=models.CharField(default="", max_length=10000),
        ),
        migrations.AddField(
            model_name="incident",
            name="incident_id",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="incident",
            name="title",
            field=models.CharField(default="", max_length=1000),
        ),
        migrations.CreateModel(
            name="Reports",
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
                ("authors", models.CharField(default="", max_length=300)),
                (
                    "date_downloaded",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Date downloaded"
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Date report was modified"
                    ),
                ),
                (
                    "date_published",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Date report was published"
                    ),
                ),
                (
                    "date_submitted",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Date report was submitted"
                    ),
                ),
                ("description", models.CharField(max_length=5000)),
                ("epoch_date_downloaded", models.DateTimeField(blank=True, null=True)),
                ("epoch_date_modified", models.DateTimeField(blank=True, null=True)),
                ("epoch_date_published", models.DateTimeField(blank=True, null=True)),
                ("epoch_date_submitted", models.DateTimeField(blank=True, null=True)),
                ("image_url", models.CharField(default="", max_length=1000)),
                ("language", models.CharField(default="", max_length=7)),
                ("report_number", models.IntegerField()),
                ("source_domain", models.CharField(default="", max_length=1000)),
                ("submitters", models.CharField(default="", max_length=1000)),
                ("text", models.CharField(default="", max_length=100000)),
                ("title", models.CharField(default="", max_length=1000)),
                ("url", models.CharField(default="", max_length=1000)),
                ("incident", models.ManyToManyField(to="api.incident")),
            ],
        ),
    ]