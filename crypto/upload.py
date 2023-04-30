 #streamlit run ~/Downloads/upload.py

import streamlit as st
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
from plotly import graph_objs as go
import plotly.graph_objects as px
from PIL import Image
from matplotlib import pyplot as plt

figure=plt.figure()

image = Image.open('C:\Users\sdnak\crypto\logo.jpg')
st.image(image, width = 700)

st.write("<h1 style='text-align: center'>Crypto Visualizer App</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>CRYPTO: <strong>MONEY</strong> without <strong>BORDERS</strong></h2>", unsafe_allow_html=True)
st.markdown ("---", unsafe_allow_html=True) 
st.markdown("""
*A cryptocurrency past data visualizer app is a web application designed to help users analyze
 historical data of various cryptocurrencies.The app provides graphical representations of data,
 such as charts, graphs, and heatmaps, that enable investors to understand trends and patterns 
 in the performance of different cryptocurrencies. Users can compare multiple cryptocurrencies
side-by-side and explore historical data over a specified period of time.
A cryptocurrency past data visualizer app provides investors with a valuable 
tool for making informed investment decisions and managing their portfolios more effectively.*
""")
st.markdown ("---", unsafe_allow_html=True) 
# coverting the date format



#def date_converter(date_list, format_string="%Y-%m-%d"):
#    converted_dates = []
 #   for date in date_list:
  #      converted_date = datetime.strptime(date, format_string)
   #     converted_dates.append(converted_date)
    #return converted_dates

#def date_converter(date_col):
 #   result=list()
  #  values=date_col.values
   # for value in values:
    #    result.append(str(value).split("T")[0])
     #   return result

st.markdown("<h1 style='text-align: center; '>Data visualizer</h1>", unsafe_allow_html=True) 
st.markdown ("---", unsafe_allow_html=True) 
#add multiple files
files_names=list()  #to get names of file an empty list is created
files=st.file_uploader ("Upload Multiple Files", type= ["csv"], accept_multiple_files=True)
for file in files:
    files_names.append(file.name)
selected_files=st.multiselect("select files", options=files_names)

if files:
   
        if selected_files:
            option=st.radio("select entity against date", options=["none","open","high","low","close"])
            if option !="none":
                for file in files:
                        if file.name in selected_files:
                              crypto_data = pd.read_csv(file, index_col=0)
                              #print(crypto_data["date"].values)
                              item=list(crypto_data[option]) 
                              #item=(crypto_data[option])
                              dates =(crypto_data["date"])
                              index = np.arange(len(dates))


                              plt.plot(dates, item, label=file.name, marker='o') #o is for circulare marker and label is for scale graph
                              plt.gcf().autofmt_xdate()
                              plt.xlabel('date')
                              plt.ylabel(option)
                              plt.title(option+" chart")
                              plt.grid(True)
                              plt.legend()  #to show the label


                              fig = go.Figure(data=[go.Bar(x=dates, y=item)])
                              st.plotly_chart(fig)
                           
 
                              #plt.gcf().autofmt_xdate()
                              #plt.xlabel('date')
                              #plt.ylabel(option)
                              #plt.title(option+" chart")
                              #plt.grid(True)
                              #plt.legend() 
                            
st.write(figure)
            