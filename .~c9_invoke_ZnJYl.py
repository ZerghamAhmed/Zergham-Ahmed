from cs50 import get_string
from sys import argv
import sys
import csv
import pandas as pd
import cs50
from nltk.tokenize import sent_tokenize



def main():

    # make dictionary of comparisons and open csv
    db = pd.read_csv("concreq.csv")

    courses = ["LS 1a", "LS 1b", "LS 2", "LPSA"]

   # request.form.get("")

    # create a comparisons counter

    # List of the best concentrations


    # iterate over each of the concentrations
    for col in db.columns:
        count = 0
        best = []
        # check for comparison
        common = set(courses).intersection(set(db[col]))
        #print(common)
        # if len of this comparison is greater than zero than input best concentration
        if len(common) > count:
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