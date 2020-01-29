#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mayosmjs
"""
import re
import pandas as pd
import numpy as np
import emoji
import demoji 
import calendar 
import datetime
import seaborn as sns
import matplotlib.pyplot as plt


def extract_emojis(data):
    print('Extracting Emojis Please wait ❤❤❤...')
    data['Emoji_Name'] = [str(list(demoji.findall(str(data.loc[i,'Message'])).values())) for i in range(len(data))]
    data['Emoji'] = [str(list(demoji.findall(data.loc[i,'Message']).keys())) for i in range(len(data))]
    print('Successfull Extracted emojis 😊😊😊...')
    return


def read_raw_data():
    f = open('txt.txt'.format(), 'r')
    #Every text message has the same format: date - sender: message. 
    txt = re.findall('(\d+/\d+/\d+, \d+:\d+\d+ [A-Z]*) - (.*?): (.*)', f.read())
    f.close()

    #Convert list to a dataframe and name the columns
    data = pd.DataFrame(txt,columns=['Datetime','Name','Message'])
    extract_emojis(data)
    
        
    data['Datetime'] = pd.to_datetime(data['Datetime'],format="%m/%d/%y, %I:%M %p")
    data['Date'] = data['Datetime'].apply(lambda x: x.date())
    data['Time'] = data['Datetime'].apply(lambda x: x.time())
    data = data[data['Message']!='<Media omitted>']
    return data
  
 def convert_to_csv(df):
    #Convert the dataframe into a csv file
    print('Creating Dataframe ❤❤❤...')
    export_csv = df.to_csv (r'txt.csv', index = None, header=True)
    export_csv
    print('Dataframe Complete ❤❤❤...')

    return



def run_all():
    df = read_raw_data()
    convert_to_csv(df)

data = read_raw_data()
    

 
# SEE WHO SENDS MORE TEXT 
data['Name'].value_counts().plot(kind='bar', 
                   rot=0, 
                   title='#No Of Messages Sent', 
                   figsize=(15,5))    




#DAYS OF THE WEEK WHEN MOST TEXT ARE SENT
#Dow( Day of week )
data["Dow"] = data['Date'].map(lambda Date: calendar.day_name[datetime.datetime.strptime(str(Date), '%Y-%m-%d').weekday()] 
g = sns.catplot(x="Dow", kind="count", palette="ch:.25",data=data);
g.fig.set_figwidth(14)
g.fig.set_figheight(6)
g.set_xlabels(label="Days of the week")
g.set_titles("Number of messages sent per day of the week")
                               
#Emojis Mostly used
 def find_symbols(txt):
    for char in txt:
        if char in "[' ']":
            txt = txt.replace(char,'')
    return txt

data["Emoji_2"] = data['Emoji'].map(lambda Emoji: find_symbols(Emoji) )
data["Emoji_Name_2"] = data['Emoji_2'].map(lambda Emoji: find_symbols(Emoji) )
# We start with creating a new dataframe 
new_df = pd.DataFrame(data.Emoji_Name_2.str.split(',').tolist(), index=data.Name).stack()
# To do this, we will make Emoji as a column (it can't be an index since the values will be duplicate)
new_df = new_df.reset_index([0, 'Name'])
new_df.columns = ['Name', 'Emoji']
                               
# Filter empty emojis and group
new_df = new_df \
    .query('Emoji !="" ') \
    .groupby(['Emoji','Name'])\
    .size()\
    .reset_index(name="Count")\
        
g = sns.FacetGrid(new_df, col="Name",  hue="Name")
g = g.map(plt.barh, "Emoji","Count")                             
                               
                               
                               
#WHICH HOUR ARE MESSAGES MOST EXCHANGED
data["thours"] = data["Time"].map(lambda Time: Time.hour)
data['thours'].value_counts().plot(kind='bar', 
                        rot=0, 
                        title='#No Of Messages Sent', 
                        figsize=(15,5))

                             
                               
                               
                               
                            
                               


    
    
    
    
    
  


