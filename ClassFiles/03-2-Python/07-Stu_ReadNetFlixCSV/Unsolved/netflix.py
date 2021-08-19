# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
nf_file_path = os.path.join('..','Resources','netflix_ratings.csv')


# Open the CSV
with open(nf_file_path,'r') as csvfile:

    # Loop through looking for the video
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        if row[0] == video:
             print(f"{row[0]} is rated {row[1]} with a rating of {row[5]}")
             break
    # print(csv_header)
