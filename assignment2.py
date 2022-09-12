import datetime 
import urllib.request
import argparse
import logging

LOG_FILENAME = 'error.log'
logging.basicConfig(filename=LOG_FILENAME,
    level=logging.DEBUG)
logging.debug('This message should go to the log file')

def downloadData(url):
    with urllib.request.urlopen(url) as response:
        url_data = response.read().decode('utf-8')
        
    return url_data

def processData(data):
    result = {}
    lines = data.split("\n")
    header = True

    for line in lines:
        if header:
            header = False
            continue
        if len(line) == 0:
            continue
        elements = line.split(",")
        id = int(elements[0])
        name = (elements[1])
        date_str = (elements[2])
        try:
            birthday = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            result[id] = (name, birthday)
        except ValueError as e:
            print (f"Error parsing {line}")

    return result

def displayPerson(id, personData):
    if id in personData:
        print ("Person {} is {} with a birthday of {}".format(id,personData[id][0],personData[id][1]))
    else:
        print ("No user found with that id")

def main(url):
    data = downloadData(url)
    personData = processData(data)
    print ('Input an ID')
    
    id = 33
    if id <= 0:
        quit()
    else:
        displayPerson(id, personData)
    
if __name__ == "__main__":
    url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
    idnum= int(input('ID'))
    my_parser = argparse.ArgumentParser(description='Assignment2 Parser')
    my_parser.add_argument('--url', type=str, required =True, help='The URL we want to download')
    args = my_parser.parse_args()
    url = args.url
    main(url)
    main(idnum)