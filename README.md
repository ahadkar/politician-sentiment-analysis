# Politician Sentiment Analysis

## Summary

This is a project for UIUC CS410 Text Retrieval and Analysis class.

In this project we extract meaningful topics from a corpus of tweets for US politicians to create topic model. Futher we analyze the topic coverage for each politician's corpus of tweets. The tweets are then analyzed for positive/ negative/ neutral sentiment.

**This project requires Python 3.6 to run.**

**The project used [this dataset available on data.world](https://data.world/bkey/politician-tweets)**

**Contribution of Each Team Member**
* Aditya:
* Yujia:
* Qian: Researched the appropriate toolkit of sentiment analysis. Implemented the sentiment analysis for each tweet and politician. Wrote the two files in sentiment directory: tweet_sentiment.py, politician_average.py and relative documentations.

## Required Python Frameworks

* [Django](https://www.djangoproject.com/)
```bash
pip install django
```

* VirtualEnv is required to run the virtual environment. Install this by using:
```bash
pip install virtualenv
```

* [Spacy](https://spacy.io/)
```bash
pip install spacy
```

* [NLTK](https://www.nltk.org/index.html)
```bash
pip install nltk
```

* [Vader Sentiment](https://github.com/cjhutto/vaderSentiment)
```bash
pip install vaderSentiment
```

* [Gensim](https://radimrehurek.com/gensim/install.html)
```bash
pip install gensim
```

## Running the app

1. Clone or download the repository files.
2. [Download the database](https://drive.google.com/file/d/1du9vzxirOis5uVF-34k4JcQneT8NgYrr/view?usp=sharing) required to run the app.
3. Navigate to the project directory **politician-sentiment-analysis** and run the following command to activate the virtual environment.

```bash
source env/bin/activate
```

*Note: Windows users should activate the environment by running:*
```bash
source env/scripts/activate
```

4. You will see the command prompt with the environment name **env**.

```bash
env
```

5. Use ```cd psa_app``` to navigate to the *psa_app* sub directory.

6. Next, enter the following command to start the runserver for the environment.

```bash
python manage.py runserver
```

7. On a successful build the command prompt will print:

```
System check identified no issues (0 silenced).
November 21, 2018 - 22:03:33
Django version 2.1.3, using settings 'psa_app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
8. Finally, start the development server by going to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.


## Sentiment Analysis Implementation

In our project, we use [VADER](https://github.com/cjhutto/vaderSentiment) to perform the sentiment analysis. VADER (Valence Aware Dictionary and Sentiment Reasoner) is a lexicon and rule-based sentiment analysis tool. It is specifically attuned to sentiments expressed in social media.

In the pre-processing step, we first clean the tweets, including:

1. remove stock market tickers like $GE
2. remove old style retweet text "RT"
3. remove URLs
4. remove the hash # sign

Then we use TweetTokenizer from nltk.tokenize to tokenize the tweets.
We use stopwords from nltk.corpus to remove the stop words.
We also stem words using WordNetLemmatizer from nltk.stem.wordnet.

An optimization: At first we used Porter stemmer. But it stems word too much that VADER analyzer cannot recognize the word. For Example, it stems "happy" to "happi", and VADER gives 0 score for this word. It means it is neutral, which apparently is not accurate. After some research, we choose WordNet Lemmatizer as the stemmer, and it performed much better.

After pre-processing, we use VADER sentiment intensity analyzer to do the sentiment analysis. We get sentiment score of each tweet, and retrieve the compound score. Then we classify tweets into different polarities like positive/negative/neutral according to the typical thresholds.

At last, we loop over all the politicians and compute the average sentiment score for each politician. 
All the sentiment scores, polarities, and average score of each politician are stored in the database.



To perform sentiment analysis on tweets from the database:

1. Install nltk and VADER analyzer in command line

```bash
pip install nltk
pip install vaderSentiment
```

2. Copy the database db.sqlite3 to directory psa_app/sentiment
3. Run tweet_sentiment.py
4. Run politician_average.py

Then an updated database with all the sentiment information is available.
