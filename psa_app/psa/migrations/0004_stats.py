# Generated by Django 2.1.3 on 2018-12-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psa', '0003_tweet_sentiment_polarity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive_tweet_count', models.IntegerField(default=0)),
                ('negative_tweet_count', models.IntegerField(default=0)),
                ('neutral_tweet_count', models.IntegerField(default=0)),
                ('gm_average_positivity_score', models.FloatField(default=0.0)),
                ('gm_average_negativity_score', models.FloatField(default=0.0)),
                ('most_positive_tweet', models.CharField(max_length=1000)),
                ('most_positive_tweet_id', models.BigIntegerField(default=0)),
                ('most_negative_tweet', models.CharField(max_length=1000)),
                ('most_negative_tweet_id', models.BigIntegerField(default=0)),
            ],
        ),
    ]
