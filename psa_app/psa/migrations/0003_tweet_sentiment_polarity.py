# Generated by Django 2.1.3 on 2018-12-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psa', '0002_auto_20181206_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='sentiment_polarity',
            field=models.CharField(default='neutral', max_length=100),
        ),
    ]
