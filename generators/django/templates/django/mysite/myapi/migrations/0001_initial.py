# Generated by Django 3.1.6 on 2021-02-17 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_name', models.CharField(max_length=200)),
                ('blog_text', models.TextField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
