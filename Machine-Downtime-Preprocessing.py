# =============================================================================
# Machine Downtime -  Preprocessing
# =============================================================================

#Importing libraries
import pandas as pd                    #For data manipulation
import numpy as np                     #For numerical calculations - numerical python
import matplotlib.pyplot as plt        #For visualization
import seaborn as sns                  #Advanced data vizualization

# Read the data into spyder

data = pd.read_csv(r"E:\360digiTMG-Project\Machine Downtime.csv")

# Copy data to another dataframe
data.head()
machine_data = data.copy()

machine_data.info()

machine_data.dtypes


#from datetime import datetime

#date_format = "%d-%m-%Y"
  
#machine_data['Date'] = pd.to_datetime(machine_data['Date'], format=date_format).dt.date

# null values

machine_data.isna().sum()

# Since there is no relation between missing values in columns we are removing missing values

machine_data = machine_data.dropna()

# We get to know from EDA that , "Assembly line no column is no longer required ,Since it is highly related with machine_id

machine_data = machine_data.drop("Assembly_Line_No",axis = "columns")

pd.set_option("display.max_columns",20)
pd.set_option("display.max_rows",3000)

machine_data.head()

machine_data.describe()

machine_data.Date.value_counts()
print(type(machine_data.Date.value_counts()))

# Checking for outliers

sns.boxplot(x = machine_data.Hydraulic_Pressure)
sns.boxplot(x = machine_data.Coolant_Pressure)
sns.boxplot(x = machine_data.Air_System_Pressure)
sns.boxplot(x = machine_data.Coolant_Temperature)
sns.boxplot(x = machine_data.Hydraulic_Oil_Temperature)
sns.boxplot(x = machine_data.Spindle_Bearing_Temperature)
sns.boxplot(x = machine_data.Spindle_Vibration)
sns.boxplot(x = machine_data.Tool_Vibration)
sns.boxplot(x = machine_data.Spindle_Speed)
sns.boxplot(x = machine_data.Voltage)
sns.boxplot(x = machine_data.Torque)
sns.boxplot(x = machine_data.Cutting)


# Out of all these , Air_System_Pressure,Hydraulic_Oil_Temperature,Spindle_Bearing_Temperature
#Spindle_Vibration , Voltage, Tool_Vibration has outliers

def get_iqr_values(df, column_name):
    median = df[column_name].mean()
    q1 = df[column_name].quantile(0.25)
    q3 = df[column_name].quantile(0.75)
    iqr = q3 - q1
    max_quantile = q3 + (1.5 * iqr)
    min_quantile = q1 - (1.5 * iqr)
    return median, q1, q3, max_quantile, min_quantile

def remove_outliers(df, column):
    _, _, _, maximum, minimum = get_iqr_values(df, column)
    df_out = df[(df[column] > minimum) & (df[column] < maximum)]
    return df_out

#number_outliers = machine_data.shape[0] - df_out.shape[0]
#print('Number of outliers:', number_outliers)
# Removing outliers present in dataset
machine_data = remove_outliers(machine_data,"Air_System_Pressure")
machine_data = remove_outliers(machine_data,"Hydraulic_Oil_Temperature")
machine_data = remove_outliers(machine_data,"Spindle_Bearing_Temperature")
machine_data = remove_outliers(machine_data,"Spindle_Vibration")
machine_data = remove_outliers(machine_data,"Voltage")
machine_data = remove_outliers(machine_data,"Tool_Vibration")

# Removing duplicate values from dataset
machine_data = machine_data.drop_duplicates()


# converting categorical variables to contineous variables by getting dummy variables

machine = pd.get_dummies(machine_data,drop_first = True)


# Transformation

Hydraulic_Pressure = pd.DataFrame({"1. Before":machine_data["Hydraulic_Pressure"], "2. After":np.log(machine_data["Hydraulic_Pressure"])})
Hydraulic_Pressure.hist()

Coolant_Pressure = pd.DataFrame({"1. Before":machine_data["Coolant_Pressure"], "2. After":np.log(machine_data["Coolant_Pressure"])})
Coolant_Pressure.hist()

Air_System_Pressure = pd.DataFrame({"1. Before":machine_data["Air_System_Pressure"], "2. After":np.log(machine_data["Air_System_Pressure"])})
Air_System_Pressure.hist()

Coolant_Temperature = pd.DataFrame({"1. Before":machine_data["Coolant_Temperature"], "2. After":np.log(machine_data["Coolant_Temperature"])})
Coolant_Temperature.hist()

Spindle_Bearing_Temperature = pd.DataFrame({"1. Before":machine_data["Spindle_Bearing_Temperature"], "2. After":np.log(machine_data["Spindle_Bearing_Temperature"])})
Spindle_Bearing_Temperature.hist()

Spindle_Vibration = pd.DataFrame({"1. Before":machine_data["Spindle_Vibration"], "2. After":np.log(machine_data["Spindle_Vibration"])})
Spindle_Vibration.hist()

Tool_Vibration  = pd.DataFrame({"1. Before":machine_data["Tool_Vibration"], "2. After":np.log(machine_data["Tool_Vibration"])})
Tool_Vibration.hist()

Spindle_Speed = pd.DataFrame({"1. Before":machine_data["Spindle_Speed"], "2. After":np.log(machine_data["Spindle_Speed"])})
Spindle_Speed.hist()

Voltage = pd.DataFrame({"1. Before":machine_data["Voltage"], "2. After":np.log(machine_data["Voltage"])})
Voltage.hist()

Torque = pd.DataFrame({"1. Before":machine_data["Torque"], "2. After":np.log(machine_data["Torque"])})
Torque.hist()

Cutting = pd.DataFrame({"1. Before":machine_data["Cutting"], "2. After":np.log(machine_data["Cutting"])})
Cutting.hist()


machine_data.to_csv(r"E:\360digiTMG-Project\processed_file.csv")


z









