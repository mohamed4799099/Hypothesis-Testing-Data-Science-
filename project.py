import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
State = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
def get_list_of_university_towns():
    
    State=[]
    RegionName=[]
    L=[]
    K=[]
    o=[]
    u=0
    #State.append('Alabama[edit]')
    K='Alabama'

    file = pd.read_fwf('university_towns.txt')
    file.replace('\n','')
    for i in file['Alabama[edit]']:
        if i[-6:] == '[edit]':
            K=i[:-6]
            #State.append(K[0])
            u=u+1
            continue    
        if '(' in i:
            if u==0:
                u=u+1
            #L=i.split('(')
            o=i[:i.index('(')-1]
            RegionName.append(o)
            State.append(K)
            L=[]
            continue
        else:
            State.append(K)
            RegionName.append(i)
    #State[220]='Massachusetts'
    #State[225]='Massachusetts'
    #State[262]='Minnesota'
    #State[268]='Minnesota'
    
    '''
    
    m=0
    state1=pd.Series(State)
    state2=state1.str.split('[',n=1,expand=True)
    state2.drop(1,axis=1,inplace=True)
    r=file['Alabama[edit]'].str.split('(',n=1,expand=True)
    r=r[0].str.split('[',n=1,expand=True)
    r.drop(1,axis=1,inplace=True) ### the region name 
    r.rename(columns={0:'RegionName'},inplace=True)### the region name
    f=pd.concat([state2,r['RegionName']],axis=1)
    f.drop(f.index[5:616],axis=0,inplace=True)
    '''

    
    state1=pd.Series(State)
    r=pd.Series(RegionName)
    state1=state1.to_frame()
    f=pd.concat([state1,r],axis=1)
    f.columns=['State','RegionName']
    return f
    
    ################
    def get_recession_start():
    file=pd.read_excel('gdplev.xls')
    file.drop([0,1,2,3,4,5,6],axis=0,inplace=True)
    file.reset_index(inplace=True)
    file.drop(['index','Unnamed: 3'],axis=1,inplace=True)
    file.drop(file.columns[-1],axis=1,inplace=True)
    file.columns=['years','GDP in billions of current dollars','GDP in billions of chained 2009 dollars','quarters','GDP1 in billions of current dollars','GDP1 in billions of chained 2009 dollars']
    m=file # dh kda gwah l data frame l original copy
    f=file[file['quarters'] > '1999q4']
    f.drop(['years','GDP in billions of current dollars','GDP in billions of chained 2009 dollars'],axis=1,inplace=True)
    f.reset_index(inplace=True)
    f.drop(['index'],axis=1,inplace=True)
    f['GDP1 in billions of current dollars']=f['GDP1 in billions of current dollars'].astype('int64')
    for i in range(2, len(f)):
          if (f.iloc[i-2,1] > f.iloc[i-1,1]) and (f.iloc[i-1,1] > f.iloc[i,1]):
                return f.iloc[i-2,0]
############
def get_recession_end():
    file=pd.read_excel('gdplev.xls')
    file.drop([0,1,2,3,4,5,6],axis=0,inplace=True)
    file.reset_index(inplace=True)
    file.drop(['index','Unnamed: 3'],axis=1,inplace=True)
    file.drop(file.columns[-1],axis=1,inplace=True)
    file.columns=['years','GDP in billions of current dollars','GDP in billions of chained 2009 dollars','quarters','GDP1 in billions of current dollars','GDP1 in billions of chained 2009 dollars']
    m=file # dh kda gwah l data frame l original copy
    f=file[file['quarters'] > '1999q4']
    f.drop(['years','GDP in billions of current dollars','GDP in billions of chained 2009 dollars'],axis=1,inplace=True)
    f.reset_index(inplace=True)
    f.drop(['index'],axis=1,inplace=True)
    f['GDP1 in billions of current dollars']=f['GDP1 in billions of current dollars'].astype('int64')
    start=get_recession_start()
    start_index = f[f['quarters'] == start].index.tolist()[0]
    f=f.iloc[start_index:]
    
    for i in range(2,len(f)):
        if (f.iloc[i-2][1] < f.iloc[i-1][1]) and (f.iloc[i-1][1] < f.iloc[i][1]):
            return f.iloc[i][0]

    #############
    def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3'''
    file=pd.read_excel('gdplev.xls')
    file.drop([0,1,2,3,4,5,6],axis=0,inplace=True)
    file.reset_index(inplace=True)
    file.drop(['index','Unnamed: 3'],axis=1,inplace=True)
    file.drop(file.columns[-1],axis=1,inplace=True)
    file.columns=['years','GDP in billions of current dollars','GDP in billions of chained 2009 dollars','quarters','GDP1 in billions of current dollars','GDP1 in billions of chained 2009 dollars']
    m=file # dh kda gwah l data frame l original copy
    f=file[file['quarters'] > '1999q4']
    f.drop(['years','GDP in billions of current dollars','GDP in billions of chained 2009 dollars'],axis=1,inplace=True)
    f.reset_index(inplace=True)
    f.drop(['index'],axis=1,inplace=True)
    f['GDP1 in billions of current dollars']=f['GDP1 in billions of current dollars'].astype('int64')
    start=get_recession_start()
    end=get_recession_end()  
    start_index = f[f['quarters'] == start].index.tolist()[0]
    end_index = f[f['quarters'] == end].index.tolist()[0]
    f=f.iloc[start_index:end_index+1]
    a=f['GDP1 in billions of current dollars'].min()
    
    
    return str(list(f[f['GDP1 in billions of current dollars']==a]['quarters'])[0])
    
    
    
  ###########
  def convert_housing_data_to_quarters():
    c=pd.read_csv('City_Zhvi_AllHomes.csv')
    s=list(c['State'])
    c['State']=c['State'].replace(State,regex=True)
    st=c['State']
    rg=c['RegionName']
    c.drop(c.columns[0],axis=1,inplace=True)
    c.drop(c.columns[0:50],axis=1,inplace=True)
    c.columns=pd.to_datetime(c.columns,errors='coerce')
    res=c.resample('Q',axis=1).mean()
    res=res.rename(columns=lambda col: '{}q{}'.format(col.year,col.quarter))
    res.index=[st,rg]
    return res
#########

def run_ttest():

    unitowns = get_list_of_university_towns()
    bottom = get_recession_bottom()
    start = get_recession_start()
    hdata = convert_housing_data_to_quarters()
    bstart = hdata.columns[hdata.columns.get_loc(start) -1]
    
    hdata['ratio'] = hdata[bottom] - hdata[bstart]
    hdata = hdata[[bottom,bstart,'ratio']]
    hdata = hdata.reset_index()
    unitowns_hdata = pd.merge(hdata,unitowns,how='inner',on=['State','RegionName'])
    unitowns_hdata['uni'] = True
    hdata2 = pd.merge(hdata,unitowns_hdata,how='outer',on=['State','RegionName',bottom,bstart,'ratio'])
    hdata2['uni'] = hdata2['uni'].fillna(False)

    ut = hdata2[hdata2['uni'] == True]
    nut = hdata2[hdata2['uni'] == False]

    t,p = ttest_ind(ut['ratio'].dropna(),nut['ratio'].dropna())
    
    different = True if p < 0.01 else False

    better = "non-university town" if ut['ratio'].mean() < nut['ratio'].mean() else "university town"

    return different, p, better

run_ttest()
