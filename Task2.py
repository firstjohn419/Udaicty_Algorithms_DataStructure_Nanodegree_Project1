"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#I've found all call records had happended in September 2016 from the csv
longest_call_time = 0
longest_calling_phone_number = ""

for call_record in calls:
 	if int(call_record[3]) > longest_call_time:
#	 	print(int(call_record[3]))
 		longest_calling_phone_number = call_record[0]
 		longest_call_time = int(call_record[3])

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(str(longest_calling_phone_number), longest_call_time))