from cs50 import get_string
from sys import argv
import sys
import csv
import pandas as pd
import cs50
from nltk.tokenize import sent_tokenize



def main():

    # make dictionary of comparisons and open csv
    conc_to_cour = {}
    db = pd.read_csv("concreq.csv")

    courses = ["MATH 21b", "MATH 21a", "MATH 1b", "COMPSCI 50", "COMPSCI 51", "STAT 110"]

    # create a comparisons counter
    count = 0
    # List of the best concentrations
    best = []

    # iterate over each of the concentrations
    for col in db.columns:
        # check for comparison
        common = set(courses).intersection(set(db[col]))
        #print(common)
        # if len of this comparison is greater than zero than input best concentration
        if len(common) >= count:
            count = len(common)
            best.append(col)

    print(count, best)

    # for concentration in concentrations:
    #     fulfilled = 0
    #     common = set(courses).intersection(set(concentrations))
    #     if (len(common) > 0):
    #         fulfilled = len(common)
    #         matches.append(fulfilled)

    # best = max(matches)

    # for match in matches:
    #     if match == best:
    #         print(f'Based on the courses you have taken, your best-fit concentration match is {concnames[match]}!') # return concentration

    # MATH.fulfilled = set(courses.split('\n')).intersection(APMTH.split('\n'))
    # return APMTH.fulfilled.count()

    # APMTH.fulfilled.count()
    # ASTRON.fulfilled.count()

    # max(APMTH.fulfilled.count(), APMTH.fulfilled.count())



    # with open('concreq.csv', "r") as csv_file:
    # csv_reader = csv.reader(csv_file, delimiter=',')
    # line_count = 0
    # for row in csv_reader:
    #     if line_count == 0:
    #         print(f'Column names are {", ".join(row)}')
    #         line_count += 1
    #     else:
    #         print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
    #         line_count += 1
    # print(f'Processed {line_count} lines.')



    # courses = request.form.get("course")

    # https://realpython.com/python-csv/


        # for course in courses:
        #     for concentration in concentrations:
        #         for requirement in requirements:
                    #https://stackoverflow.com/questions/3748063/what-is-the-syntax-to-insert-one-list-into-another-list-in-python

if __name__ == "__main__":
    main()