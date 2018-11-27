# Created by Aditya Hadkar

import csv, sqlite3, time

db_filename = "db.sqlite3"

def parse(filename):    

    SQL = """
    insert into psa_tweet (tweet_id, user_id, created_at, tweet_text, hashtag_entities, url_entities, favorite_count, retweet_count, quoted_status_id, in_reply_to_status_id)
    values (:id, :user_id, :created_at, :tweet_text, :hashtag_entities, :url_entities, :favorites_count, :retweet_count, :quoted_status_id, :in_reply_to_status_id)
    """

    start_time = time.time()

    with open(filename, 'rt') as csvfile:

        csv_reader = csv.DictReader(csvfile)

        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            cursor.executemany(SQL, csv_reader)

            print("Elapsed: {} seconds".format(round(time.time() - start_time, 4)))
            print("Finished loading.")

        """
        dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=';,')
        csvfile.seek(0)
        reader = csv.DictReader(csvfile)

        for line in reader:
            print(line)
            #pol_name = line["\ufeffid"]
            #print(pol_name)
        """

def main():
    
    # The file is not included in the repository to save bandwidth
    # for source control.
    
    parse('pol_tweets.csv')

if __name__ == '__main__':
    main()


