# Generated by Django 4.1.1 on 2022-10-11 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_text', models.CharField(max_length=1000)),
                ('entry_date', models.DateTimeField(verbose_name='Päiväkirjamerkintä')),
            ],
        ),
    ]
