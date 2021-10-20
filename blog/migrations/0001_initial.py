# Generated by Django 3.2.6 on 2021-10-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('blog_detail', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='blogs/')),
                ('blog_type', models.CharField(choices=[('travel', 'travel'), ('love', 'love'), ('life-style', 'life-style'), ('technology', 'technology'), ('illustration', 'illustration'), ('design', 'design'), ('restaurant', 'restaurant')], max_length=15)),
                ('blog_description', models.TextField(max_length=200)),
            ],
        ),
    ]