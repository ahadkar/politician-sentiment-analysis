'''
For each politician, retrieve the sentiment scores of the tweets they posted,
and compute the average score.
'''
import sqlite3

def compute_average():
    # retrieve all the politician twitter id from psa_politician
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    cursor.execute('''SELECT twitter_id FROM psa_politician''')
    all_id = cursor.fetchall()
    all_id_list = [i[0] for i in all_id]

    # for each id, retrieve sentiment scores
    for id in all_id_list:
        cursor.execute('''SELECT sentiment_score FROM psa_tweet WHERE user_id = ?''', (id,))
        scores = cursor.fetchall()
        scores_list = [i[0] for i in scores]

        # compute the average and update the database
        scores_size = len(scores_list)
        if scores_size == 0:
            average = 0
        else:
            average = sum(scores_list) / scores_size
        cursor.execute('''UPDATE psa_politician SET average_positivity_score = ? WHERE twitter_id = ?''', (average, id))

    db.commit()
    db.close()

if __name__ == "__main__":
    compute_average()
