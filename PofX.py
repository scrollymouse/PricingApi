# v2.0 9.27.20
# Scrollymouse
# w/ alpha_vantage API
###########################################
#Requirements : 

import alpha_vantage
from alpha_vantage.timeseries import TimeSeries

import time
import datetime

##########################################
# UPDATE YOUR KEY HERE
API_KEY = ('xxxxxxxxx')

def CallPrice():
    TimeStamp = datetime.datetime.now()
    
    DateStamp = TimeStamp.strftime('%Y-%m-%d-%s')
    
    # alpha vantage call
    ts = TimeSeries(key=API_KEY)
    
    #tickers = [] hard coded for max of 5 for free tier
    tickers = ['pypl', 'atvi','goog', 'abt', 'gld']    
    
    print ('Pricing begins...')
    print ("\n") 
    for i in tickers: 
        
        data, meta_data = ts.get_intraday(symbol= i ,interval='60min', outputsize='compact')

        # PRINT OUTPUT
        # Hard coded KEY:       
        
        # grabs prior day
        DailyArray = (data['2020-10-01 17:00:00'])
        
        # grabs only the closing price
        DailyArrayClose = (DailyArray['4. close']) 
                
        print ('Close Price For:   ' , i  ,  DailyArrayClose)
        
        # Appends ticker, price to csv, saves here:
        loggs= open("/Users/xxx/Desktop/v3nv/Logs/AlphaPricing" + str(TimeStamp) + ".csv", "a+")
        
        loggs.write(i + ',' + DailyArrayClose + "\n") 
    
    
    print ("\n")     
    print ('Task complete.', TimeStamp)    
        
##########################################

CallPrice()


#END
        
