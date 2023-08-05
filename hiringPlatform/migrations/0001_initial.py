# Generated by Django 4.1.7 on 2023-08-04 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JobModel",
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
                (
                    "profile",
                    models.CharField(
                        choices=[
                            ("android_engineer", "Android Engineer"),
                            ("backend_engineer", "Backend Engineer"),
                            ("data_engineer", "Data Engineer"),
                            ("devops", "DevOps"),
                            ("frontend_engineer", "Frontend Engineer"),
                            ("fullstack_engineer", "Fullstack Engineer"),
                            ("ios_engineer", "iOS Engineer"),
                            ("qa_sdet", "QA / SDET"),
                        ],
                        max_length=150,
                    ),
                ),
                ("selected_roles", models.JSONField()),
                ("current_CTC", models.IntegerField()),
                ("expected_CTC", models.IntegerField()),
                ("notice_period", models.IntegerField()),
                ("curr_location", models.CharField(max_length=150)),
                (
                    "pref_location",
                    models.CharField(
                        choices=[
                            ("bengaluru", "Bengaluru"),
                            ("chennai", "Chennai"),
                            ("kolkata", "Kolkata"),
                            ("hyderabad", "Hyderabad"),
                            ("pune", "Pune"),
                            ("indore", "Indore"),
                            ("mumbai", "Mumbai"),
                            ("delhi", "Delhi"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]