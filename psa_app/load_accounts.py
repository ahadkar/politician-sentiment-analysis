# Created by Aditya Hadkar

import csv, sqlite3, time

db_filename = "db.sqlite3"

# Loads all the politicians from a csv file in a db.sqlite3 database.


def parse(filename):

    sql = """
    insert into psa_politician (twitter_id, screen_name, description, created_at, location, is_verified, latest_following_count, latest_status_count, tags)
    values (:\ufeffid, :screen_name, :description, :created_at, :location, :is_verified, :latest_following_count, :latest_status_count, :array_agg)
    """

    start_time = time.time()

    with open(filename, 'rt') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            cursor.executemany(sql, csv_reader)

            print("Elapsed: {} seconds".format(round(time.time() - start_time, 4)))
            print("Finished loading.")

        """
        dialect = csv.Sniffer().sniff(csv_file.read(), delimiters=';,')
        csv_file.seek(0)
        reader = csv.DictReader(csv_file)

        for line in reader:
            print(line)
            #pol_name = line["\ufeffid"]
            #print(pol_name)
        """


def main():
    
    # The file is not included in the repository to save bandwidth
    # for source control.

    parse('pol_accounts.csv')


if __name__ == '__main__':
    main()


