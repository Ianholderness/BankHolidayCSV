import sys # used for excepting prams
import os.path # used to checking if file exists
import requests # xmlhttp request
import csv # writing csv file
import json  # dealing with return request


def GetBHDates(url, pmin):
    responce = requests.get(url).json()
    # split the arry to the new bh only
    data = responce['england-and-wales']['events']
    # checks if the file alread exists 
    if os.path.isfile("BH.csv"):
    # removed the file
        os.remove("BH.csv")
    # Creates the CSV file with write permissions
    f = csv.writer(open("BH.csv", "w", newline='', encoding='utf-8'), delimiter='\t', lineterminator='\n')

    #Write headder
    f.writerow(["Date"])
    # Loops through each data point in the json data 
    for i in data:
    # Checks if the date is less than the min date 
        if i['date'] > pmin and  i['date'] < pmax:
    # Writes the BH date to the file
            f.writerow(i['date'] )

if __name__ == "__main__":

    pmin = sys.argv[1] #Start date
    pmax = sys.argv[2] #End Date
    url = 'https://www.gov.uk/bank-holidays.json' # Url for Gov website with BH
    GetBHDates(url, pmin) # Function call
