
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import operator
import pandas as pd

# Doesn't process in parallel now, might do it later
def Process():
    source=input("Enter source file name no need to put .csv\n")
    destination=input("Enter the destination file without .csv\n")

    print("\nThe default content column should be named 'Content', if its not please change it and continue\n" )

    source = source + ".csv" # add csv to source name 
    destination = destination + ".csv" # add csv to destination name

    analyzer  = SentimentIntensityAnalyzer() # Initializing vaderSentiment
    df = pd.read_csv(source) # Pandas DataFrame
    lines = df['Content'] # Get the content coloumn
    data = [] # Data store list
    counter = 0 # counter 

    # looping through all lines
    for line in lines:
        vs = analyzer.polarity_scores(str(line)) # Analyze and get the sentiment
        sentiment = max(vs.items(), key=operator.itemgetter(1))[0] # get the sentiment with max value

        data.append([sentiment, line]) # Append to the data store list
        
        if(counter % 1000 == 0): # print counter after every 1000 lines
            print(counter)
        
        counter = counter + 1

    # save data
    pd.DataFrame(data).to_csv(destination)

def main():
    key = "n"
    while(key == "n"):
        Process()
        key = input("Enter n to process another file or any other key to quit")

if __name__ == '__main__':
    main()
