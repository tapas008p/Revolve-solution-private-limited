import numpy as np
import pandas as pd
import pickle

def total_number_of_days_flight_data_cover():
    """
    returns the total number of days in given csv file.
    """
    data = pickle.load(open('flights.pkl','rb'))
    data['days'] = data['year'].astype(str)+'-'+data['month'].astype(str)+'-'+data['day'].astype(str)
    return len(pd.unique(data['days']))




########################################################################
def number_of_departure_cities():
    """
    returns the  departure cities that the flights database cover.
    """
    data = pickle.load(open('flights.pkl','rb'))
    data1 = pickle.load(open('airports.pkl','rb'))
    d = data[['origin','dest']]
    e = data1[['IATA_CODE','CITY']]
    d.columns=['IATA_CODE','DEST']
    f = pd.merge(d,e,on='IATA_CODE')
    return len(pd.unique(f['CITY']))




#########################################################################

def manufacturer_with_most_delays():
    """
    returns the manufacturer of the plane, which has done most amount of delay.
    """
    data = pickle.load(open('flights.pkl','rb'))
    data2 = pickle.load(open('planes.pkl','rb'))    
    k=pd.merge(data,data2,on='tailnum')
    k['delay'] = k['dep_delay']+k['arr_delay']
    kk = k[['manufacturer','delay']]
    kkk = kk.groupby(['manufacturer']).sum()
    kkk = kkk.sort_values(by=['delay'],ascending=False)
    kkk = kkk.reset_index()
    kkk.columns=['manufacturer','con']
    return kkk['manufacturer'][0]




###################################################################################

def two_most_connected_cities():
    """
    return two most connected cities from flights database.
    """
    data = pickle.load(open('flights.pkl','rb'))
    data1 = pickle.load(open('airports.pkl','rb'))
    d = data[['origin','dest']]
    e = data1[['IATA_CODE','CITY']]
    d.columns=['IATA_CODE','DEST']
    f = pd.merge(d,e,on='IATA_CODE')
    f.columns = ['origin','IATA_CODE','ORIGIN_CITY']
    g = pd.merge(f,e,on='IATA_CODE')
    g.columns = ['origin','dest','origin_city','dest_city']
    g['con'] = g['origin_city'] + '-' + g['dest_city']
    b =pd.DataFrame(g['con'].value_counts())
    b = b.reset_index()
    b.columns=['cities','con']
    return b['cities'][0]

    
if __name__ == "__main__":
    print(total_number_of_days_flight_data_cover())
    print( number_of_departure_cities())
    print(manufacturer_with_most_delays())
    print(two_most_connected_cities())
    
    
    