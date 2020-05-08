"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
phone_number_list = []

for records in calls:
	phone_number_list.append(records[0])
#remove duplicates by set() and count the number elements 
print('There are {0} different telephone numbers in the records.'.format(len(set(phone_number_list))))