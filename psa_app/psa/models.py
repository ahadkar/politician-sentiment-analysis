# Created by Aditya Hadkar

from django.db import models

# Create your models here.

class Politician(models.Model):
	
	twitter_id 				= models.BigIntegerField(default=0)
	screen_name 			= models.CharField(max_length=1000)
	description 			= models.CharField(max_length=2000)
	created_at 				= models.DateTimeField(auto_now_add=False, blank=True)
	location 				= models.CharField(max_length=1000)
	is_verified 			= models.BooleanField(default=False)
	latest_following_count 	= models.IntegerField(default=0)
	latest_status_count 	= models.IntegerField(default=0)
	tags 					= models.CharField(max_length=200, blank=True)
		

class Tweet(models.Model):
	
	tweet_id 				= models.BigIntegerField(default=0)
	user_id 				= models.BigIntegerField(default=0)
	created_at 				= models.DateTimeField(auto_now_add=False, blank=True)
	tweet_text 				= models.CharField(max_length=1000)
	hashtag_entities		= models.CharField(max_length=1000)
	url_entities 			= models.URLField(max_length=2000)
	favorite_count 			= models.IntegerField(default=0)
	retweet_count 			= models.IntegerField(default=0)
	quoted_status_id 		= models.BigIntegerField(default=0)
	in_reply_to_status_id	= models.BigIntegerField(default=0)

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



		
