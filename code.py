# --------------
#Importing the modules
import pandas as pd
import numpy as np
from scipy.stats import mode 

weather=pd.read_csv(path)
#Code for categorical variable
def categorical(df):
    """ Extract names of categorical column
    
    This function accepts a dataframe and returns categorical list,
    containing the names of categorical columns(categorical_var).
    
    Keyword arguments:
    df - Pandas dataframe from which the columns name will be extracted
        
    Returns:
    categorical_var - List of categorical features
    """
    categorical_var=[]
    categorical_var.append(df.select_dtypes(include='object'))
    return categorical_var
c=categorical(weather)

#Code for numerical variable
def numerical(df):
    """ Extract names of numerical column
    
    This function accepts a dataframe and returns numerical list,
    containing the names of numerical columns(numerical_var).
        
    Keyword arguments:
    df - Pandas dataframe from which the columns name will be extracted
    
    Returns:
    numerical_var - List of numerical features
    """
    numerical_var=[]
    numerical_var.append(df.select_dtypes(include='number'))

    return numerical_var
n=numerical(weather)



#code to check distribution of variable
def clear(df,col,val):
    """ Check distribution of variable
    
    This function accepts a dataframe,column(feature) and value which returns count of the value,
    containing the value counts of a variable(value_counts)
    
    Keyword arguments:
    df - Pandas dataframe
    col - Feature of the datagrame
    val - value of the feature
    
    Returns:
    value_counts - Value count of the feature 
    """
    return (df[col]==val).value_counts()
value=clear(weather,'Weather','Cloudy')
value



#Code to check instances based on the condition
def instances_based_condition(df,col1,val1,col2,val2):
    """ Instances based on the condition
    
    This function accepts a dataframe, 2 columns(feature) and 2 values which returns the dataframe
    based on the condition.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - First feature of the dataframe on which you want to apply the filter
    val1 - Value to be filtered on the first feature
    col2 - Second feature of the dataframe on which you want to apply the filter
    val2 - Value to be filtered on second feature
    
    Returns:
    instance - Generated dataframe
    """
    w=df[df[col1]>val1]
    instance=w[w[col2]==val2]
    return instance
    
    
wind_speed_35_vis_25=instances_based_condition(weather,'Wind Spd (km/h)',35,'Visibility (km)',25)
wind_speed_35_vis_25



# Code to calculate different aggreagted values according to month

import datetime
def agg_values_ina_month(df,date_col,agg_col, agg):
    """  Aggregate values according to month
    
    This function accepts a dataframe, 2 columns(feature) and aggregated funcion(agg) which returns the Pivot 
    table with different aggregated value of the feature with an index of the month.
     
    Keyword arguments:
    df - Pandas dataframe which has the data.
    date_col - Date feature of the dataframe on which you want to apply to_datetime conversion
    agg_col - Feature of the dataframe on which values will be aggregated.
    agg - The function to be used for aggregating the df (eg. 'mean', 'min', 'max').
    
    Returns:
    aggregated_value - Generated pivot table
    """
    df['Month'] = pd.DatetimeIndex(df[date_col]).month
    aggregated_value=df.pivot_table(index=df['Month'],values=agg_col,aggfunc=agg)
    return aggregated_value

aggregated_value=agg_values_ina_month(weather,'Date/Time','Temp (C)','mean')
aggregated_value

# Code to group values based on the feature
def group_values(df,col1,agg1):
    """ Agrregate values by grouping
    
    This function accepts a dataframe, 1 column(feature) and aggregated function(agg1) which groupby the 
    datframe based on the column.
   
   Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - The function to be used for aggregating the df (eg. 'mean', 'min', 'max').
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
    """
    mean_weather=df.groupby(col1)[['Date/Time','Temp (C)','Dew Point Temp (C)','Rel Hum (%)','Wind Spd (km/h)','Visibility (km)','Stn Press (kPa)']].agg(agg1)
    return mean_weather
mean_weather=group_values(weather,'Weather','mean')
mean_weather


# function for conversion 
def convert(df,celsius):
    """ Convert temperatures from celsius to fahrenhheit
    
    This function accepts a dataframe, 1 column(feature) which returns the dataframe with converted values from 
    celsius to fahrenhheit.
         
    Keyword arguments:
    df - Pandas dataframe which has the data.
    celsius - Temperature feature of the dataframe which you want to convert to fahrenhheit
    
    Returns:
    converted_temp - Generated dataframe with Fahrenhheit temp.
    
    
    """
    converted_temp=(df[celsius]*1.8)+32
    return converted_temp
converted_temp=convert(weather,"Temp (C)")
converted_temp

# Load the weather_2012 data csv file and store it in weather variable. The path of the dataset has been stored in the variable `path` for you.



# As you have now loaded the weather data you might want to check the categorical and numerical variables. You can check it by calling categorical and numerical function. 




#You might be interested in checking the distribution of a specific value like the number of times the weather was exactly Cloudy in the given column. Feel free to check on other values.
#You can check it by calling the function clear with respective parameters.
#By using index of the value or name of the value you can check the number of count




# Now suppose you want to check some instances based on a specific condition like when the wind speed was above 35 and visibility was 25. You can dicretly check it by calling the function instances_based_condition with respective parameters.




#You have temperature data and want to calculate the mean temperature recorded by month.You can generate a pivot table which contains the aggregated values(like mean, max ,min, sum, len) recoreded by month. 
#You can call the function agg_values_ina_month with respective parameters. 



# To groupby based on a column like you want to groupby on Weather column and then aggregate the mean values of each column for different types of weather using mean. You can call the function group_values.
# Feel free to try on diffrent aggregated functions like max, min, sum, len



# You have a temperature data and wanted to convert celsius temperature into fahrehheit temperatures you can call the function convert.


