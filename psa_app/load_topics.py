# Created by Aditya Hadkar

import csv, sqlite3, time

db_filename = "db.sqlite3"


def parse(filename):
    SQL = """
    insert into psa_tweettopic (topic_id, tweet_id, user_id, topic_coverage)
    values (:topic_id, :tweet_id, :user_id, :topic_coverage)
    """

    start_time = time.time()

    with open(filename, 'rt') as csv_file:
        csv_reader = csv.DictReader(csv_file)

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

    parse('topics.csv')


if __name__ == '__main__':
    main()


