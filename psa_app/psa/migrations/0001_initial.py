# Generated by Django 2.1.3 on 2018-11-22 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_id', models.BigIntegerField(default=0)),
                ('screen_name', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=2000)),
                ('created_at', models.DateTimeField(blank=True)),
                ('location', models.CharField(max_length=1000)),
                ('is_verified', models.BooleanField(default=False)),
                ('latest_following_count', models.IntegerField(default=0)),
                ('latest_status_count', models.IntegerField(default=0)),
                ('tags', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_state', models.CharField(choices=[('None', 'None'), ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AK', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'NorthDakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='None', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.BigIntegerField(default=0)),
                ('user_id', models.BigIntegerField(default=0)),
                ('created_at', models.DateTimeField(blank=True)),
                ('tweet_text', models.CharField(max_length=1000)),
                ('hashtag_entities', models.CharField(max_length=1000)),
                ('url_entities', models.URLField(max_length=2000)),
                ('favorite_count', models.IntegerField(default=0)),
                ('retweet_count', models.IntegerField(default=0)),
                ('quoted_status_id', models.BigIntegerField(default=0)),
                ('in_reply_to_status_id', models.BigIntegerField(default=0)),
            ],
        ),
    ]
