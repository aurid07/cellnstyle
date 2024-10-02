# Generated by Django 5.1.1 on 2024-09-29 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_repaircategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=255)),
                ('reviewer_image', models.ImageField(upload_to='reviews/')),
                ('review_text', models.TextField()),
                ('review_link', models.URLField()),
                ('display_on_website', models.BooleanField(default=False)),
            ],
        ),
    ]
