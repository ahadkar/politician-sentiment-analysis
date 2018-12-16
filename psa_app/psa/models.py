# Created by Aditya Hadkar

from django.db import models
from django.forms import ModelForm
from django.db.models import Max

# Create your models here.


class Politician(models.Model):

	twitter_id = models.BigIntegerField(default=0)
	screen_name = models.CharField(max_length=1000)
	description = models.CharField(max_length=2000)
	created_at = models.DateTimeField(auto_now_add=False, blank=True)
	location = models.CharField(max_length=1000)
	is_verified = models.BooleanField(default=False)
	latest_following_count = models.IntegerField(default=0)
	latest_status_count = models.IntegerField(default=0)
	tags = models.CharField(max_length=200, blank=True)
	average_positivity_score = models.FloatField(default=0)

	def tweet_url(self):
		return "psa/tweets?screen_name=" + self.screen_name

	def paginated_tweet_url(self):
		return "psa/tweets?screen_name=" + self.screen_name + "&page"

	def processed_tags(self):

		tag_list = self.tags.replace("{", "")
		tag_list = tag_list.replace("}", "")

		tag_list = tag_list.split(",")

		new_tags = []

		for tag in tag_list:
			new_tags.append(tag.capitalize())

		new_tags = list(set(new_tags))

		return new_tags

	def is_location_valid(self):

		if len(self.location) > 0:
			return True

		return False


class Tweet(models.Model):
	
	tweet_id = models.BigIntegerField(default=0)
	user_id = models.BigIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=False, blank=True)
	tweet_text = models.CharField(max_length=1000)
	hashtag_entities = models.CharField(max_length=1000)
	url_entities = models.URLField(max_length=2000)
	favorite_count = models.IntegerField(default=0)
	retweet_count = models.IntegerField(default=0)
	quoted_status_id = models.BigIntegerField(default=0)
	in_reply_to_status_id = models.BigIntegerField(default=0)
	sentiment_score = models.FloatField(default=0.0)
	sentiment_polarity = models.CharField(max_length=100, default='neutral')
	topics = models.CharField(max_length=100000, default='unknown')

	def polarity(self):

		if float(self.sentiment_score) >= 0.05:
			return "Positive"

		elif -0.05 < float(self.sentiment_score) < 0.05:
			return "Neutral"

		elif float(self.sentiment_score) <= -0.05:
			return "Negative"

		return "Neutral"

	def top_topic(self):

		tweet_topic = TweetTopic.objects.filter(tweet_id=self.tweet_id).order_by('-topic_coverage')[0]

		tweet_topic.topic_id += 1
		tweet_topic.topic_coverage = round(tweet_topic.topic_coverage * 100)

		return tweet_topic

	def sentiment_score_percentage(self):

		return round(self.sentiment_score * 100)


class Topics(models.Model):

	topics = models.CharField(max_length=100000, default='')
	topic_id = models.IntegerField(default=0)

	def topic_distribution(self):
		split_topics = self.topics.split(" + ")

		processed_topics = []

		for sp_topic in split_topics:
			sp_topic.replace("\"", "")
			sp_topic.replace("*", "-")

			processed_topics.append(sp_topic)

		return processed_topics


class TweetTopic(models.Model):

	topic_id = models.IntegerField(default=0)
	topic_coverage = models.FloatField(default=0.0)
	tweet_id = models.BigIntegerField(default=0)
	user_id = models.BigIntegerField(default=0)


class Stats(models.Model):

	positive_tweet_count = models.IntegerField(default=0)
	negative_tweet_count = models.IntegerField(default=0)
	neutral_tweet_count = models.IntegerField(default=0)
	gm_average_positivity_score = models.FloatField(default=0.0)
	gm_average_negativity_score = models.FloatField(default=0.0)
	most_positive_tweet = models.CharField(max_length=1000)
	most_positive_tweet_id = models.BigIntegerField(default=0)
	most_negative_tweet = models.CharField(max_length=1000)
	most_negative_tweet_id = models.BigIntegerField(default=0)

	total_tweet_count = 0
	stats_type = ""

	def positive_tweet_percentage(self):

		if self.total_tweet_count > 0:
			return round(((self.positive_tweet_count / self.total_tweet_count) * 100)) #float("{0:.0f}".format()

		return 0.0

	def negative_tweet_percentage(self):

		if self.total_tweet_count > 0:
			return round(((self.negative_tweet_count / self.total_tweet_count) * 100)) #float("{0:.0f}".format()

		return 0.0

	def neutral_tweet_percentage(self):

		if self.total_tweet_count > 0:
			return int(((self.neutral_tweet_count / self.total_tweet_count) * 100)) #float("{0:.0f}".format())

		return 0.0


class PoliticianModelForm(ModelForm):
	class Meta:
		model = Politician
		fields = ['screen_name', 'description', 'location', 'is_verified', 'latest_following_count', 'tags']


class State(models.Model):
	
	"""docstring for State""" 
	NotAvailable 	= 'None'
	Alabama 		= 'AL'
	Alaska 			= 'AK'
	Arizona 		= 'AZ'
	Arkansas 		= 'AK'
	California 		= 'CA' 
	Colorado		= 'CO'
	Connecticut		= 'CT'
	Delaware		= 'DE'
	Florida			= 'FL'
	Georgia			= 'GA'
	Hawaii			= 'HI'
	Idaho			= 'ID'
	Illinois		= 'IL'
	Indiana			= 'IN'
	Iowa			= 'IA'
	Kansas			= 'KS'
	Kentucky		= 'KY'
	Louisiana 		= 'LA'
	Maine			= 'ME'
	Maryland		= 'MD'
	Massachusetts	= 'MA'
	Michigan		= 'MI'
	Minnesota		= 'MN'
	Mississippi		= 'MS'
	Missouri		= 'MO'
	Montana			= 'MT'
	Nebraska		= 'NE'
	Nevada			= 'NV'
	NewHampshire	= 'NH'
	NewJersey		= 'NJ'
	NewMexico		= 'NM'
	NewYork			= 'NY'
	NorthCarolina	= 'NC'
	NorthDakota		= 'ND'
	Ohio			= 'OH'
	Oklahoma		= 'OK'
	Oregon			= 'OR'
	Pennsylvania	= 'PA'
	RhodeIsland		= 'RI'
	SouthCarolina	= 'SC'
	SouthDakota		= 'SD'
	Tennessee		= 'TN'
	Texas			= 'TX'
	Utah			= 'UT'
	Vermont			= 'VT'
	Virginia    	= 'VA'
	Washington		= 'WA'
	WestVirginia	= 'WV'
	Wisconsin		= 'WI'
	Wyoming			= 'WY'
	State_Choices 	= (
		
		(NotAvailable, 'None'),
		(Alabama, 'Alabama'),
		(Alaska, 'Alaska'),
		(Arizona, 'Arizona'),
		(Arkansas, 'Arkansas'),
		(California, 'California'),
		(Colorado, 'Colorado'),
		(Connecticut, 'Connecticut'),
		(Delaware, 'Delaware'),
		(Florida, 'Florida'),
		(Georgia, 'Georgia'),
		(Hawaii, 'Hawaii'),
		(Idaho, 'Idaho'),
		(Illinois, 'Illinois'),
		(Indiana, 'Indiana'),
		(Iowa, 'Iowa'),
		(Kansas, 'Kansas'),
		(Kentucky, 'Kentucky'),
		(Louisiana, 'Louisiana'),
		(Maine, 'Maine'),
		(Maryland, 'Maryland'),
		(Massachusetts, 'Massachusetts'),
		(Michigan, 'Michigan'),
		(Minnesota, 'Minnesota'),
		(Mississippi, 'Mississippi'),
		(Missouri, 'Missouri'),
		(Montana, 'Montana'),
		(Nebraska, 'Nebraska'),
		(Nevada, 'Nevada'),
		(NewHampshire, 'New Hampshire'),
		(NewJersey, 'New Jersey'),
		(NewMexico, 'New Mexico'),
		(NewYork, 'New York'),
		(NorthCarolina, 'North Carolina'),
		(NorthDakota, 'NorthDakota'),
		(Ohio, 'Ohio'),
		(Oklahoma, 'Oklahoma'),
		(Oregon, 'Oregon'),
		(Pennsylvania, 'Pennsylvania'),
		(RhodeIsland, 'Rhode Island'),
		(SouthCarolina, 'South Carolina'),
		(SouthDakota, 'South Dakota'),
		(Tennessee, 'Tennessee'),
		(Texas, 'Texas'),
		(Utah, 'Utah'),
		(Vermont, 'Vermont'),
		(Virginia, 'Virginia'),
		(Washington, 'Washington'),
		(WestVirginia, 'West Virginia'),
		(Wisconsin, 'Wisconsin'),
		(Wyoming, 'Wyoming'),
	)

	selected_state = models.CharField(
		max_length=2,
		choices=State_Choices,
		default=NotAvailable,
	)

