# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 19:07:52 2024

@author: polas
"""

import streamlit as st 
import math
from datetime import  date, datetime
from dateutil.relativedelta import relativedelta

background_image = """
<style>
[data-testid="stAppViewContainer"]  {
    background-image: url("https://img5.pic.in.th/file/secure-sv1/smsk-1e26f337bb6ec6813.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)



st.markdown("<h1 style='text-align: center; color: black ; font-size: 40px ;'>Sakhon Nubmed</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black ; font-size: 19px ;'><em>Good precise Good using</em></h1>", unsafe_allow_html=True)





today = date.today()
yr = today.strftime("%Y")
mt= today.strftime("%m")
dy= today.strftime("%d")
interval1 = 0
interval2 = 0 
interval3 = 0 


def convert_to_int(a) :
    if int(a) == float(a):
        return int(a)
    else:
        return math.ceil(a)

listofdate=["01", "02", "03", "04", "05", "06", "07", "08", "09","10", "11", "12","13", "14", "15",
 "16", "17", "18", "19", "20", "21", "22", "23", "24","25", "26", "27","28", "29", "30", "31"]
listofmonth = ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
               "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]



        
st.subheader("นัดแบบเจาะจงวัน",divider=True) 

col1, col2, col3, col4, col5, col6  = st.columns([1,2,1,1,2,1])

with col1:
    date1 = st.selectbox("วันที่",(listofdate),index=int(dy)-1, key ='date1')
    
with col2:
    month1 =  st.selectbox( "เดือน", (listofmonth),index=int(mt)-1, key='month1')
    
with col3:
    year1 = st.text_input( "พ.ศ.", value= int(yr)+543, key='year1')   
    
with col4:
    date2 = st.selectbox("นัดวันที่",(listofdate),index=int(dy)-1, key='date2')
    
with col5:
    month2 =  st.selectbox( "เดือน",(listofmonth),index=int(mt)-1, key='month2')    

with col6:
    year2 = st.text_input( "พ.ศ.", value= int(yr)+543, key='year2')   

col12, col22, col32, col42, col52  = st.columns([0.5,0.5,1,1,1])  

with col12:
    fre1 = st.write("กินยาวันละ")
    
with col22:
    med1 = st.text_input("**", key='med1',value="1", label_visibility= "collapsed")

with col32:
    fre11 = st.write("เม็ด/แคปซูล")
    
with col42:
    today1 = st.checkbox("นับรวมวันนี้ด้วย", key='today1')
    
with col52:
    but1 = st.button("คำนวณ", key='calculate1')
    
if but1:
    first_date1 = datetime.strptime(f'{date1}/{listofmonth.index(month1)+1}/{int(year1)-543}', "%d/%m/%Y")
    second_date1 = datetime.strptime(f'{date2}/{listofmonth.index(month2)+1}/{int(year2)-543}', "%d/%m/%Y")
    if today1:
        interval1 = int((second_date1 - first_date1).days)+1
        sum1 = st.code(f"ควรจ่ายยา {convert_to_int(interval1*float(med1))} เม็ด/แคปซูล") 
    else:
        interval1 = int((second_date1 - first_date1).days)
        sum1 = st.code(f"ควรจ่ายยา {convert_to_int(interval1*float(med1))} เม็ด/แคปซูล") 
    


st.subheader("นัดไม่เจาะจงวัน",divider=True) 
    
col1b, col2b, col3b, col4b, col5b, col6b, col7b  = st.columns([1,2,1,1,1.2,1,1])

with col1b:
    date2 = st.selectbox("วันที่",(listofdate),index=int(dy)-1, key ='date22')
    
with col2b:
    month2 =  st.selectbox( "เดือน",(listofmonth),index=int(mt)-1, key='month22')
    
with col3b:
    year2 = st.text_input( "พ.ศ.", value= int(yr)+543, key='year22') 

with col4b:
    nudday = st.number_input("นัดเป็นวัน", format= "%0f",  key='nudday')
    
with col5b:
    nudwk = st.number_input("นัดเป็นสัปดาห์", format= "%0f", key='nudwk')
    
with col6b:
    nudmt = st.number_input("นัดเป็นเดือน", format= "%0f",key='nudmt')
    
with col7b:
    nudyr = st.number_input("นัดเป็นปี", format= "%0f", key='nudyr')



col2b3, col2b4, col2b5, col2b6, col2b7 =st.columns([0.5,0.5,1,1,1])   

with col2b3:
       fre1b = st.write("กินยาวันละ") 

with col2b4:
       med2 = st.text_input("**", key='med2',value="1", label_visibility= "collapsed")
       
with col2b5:
      fre1c = st.write("เม็ด/แคปซูล")

with col2b6:
      today2 = st.checkbox("นับรวมวันนี้ด้วย", key='today2')
 
with col2b7:
       but22 = st.button("คำนวณ", key='calculate2')     
       
if but22:
    
    first_date2 = datetime.strptime(f'{date2}/{listofmonth.index(month2)+1}/{int(year2)-543}', "%d/%m/%Y") 
    wkday = first_date2.weekday()
    if today2:
           
           if  int(nudday) == 0:
               second_date2 = first_date2+relativedelta(days = int(nudday), weeks =int(nudwk), months = int(nudmt), years= int(nudyr), weekday=wkday   )
               resecond_date2 = second_date2.strftime("%d/%m/%Y")
               interval2 = int((second_date2 - first_date2).days)+1
               sum2 = st.code(f"ตรงกับวันที่ {resecond_date2} ควรจ่ายยา {convert_to_int(interval2*float(med2))} เม็ด/แคปซูล") 
           
           else:
              second_date2 = first_date2+relativedelta(days = int(nudday), weeks =int(nudwk), months = int(nudmt), years= int(nudyr)  )
              resecond_date2 = second_date2.strftime("%d/%m/%Y")
              interval2 = int((second_date2 - first_date2).days)+1
              sum2 = st.code(f"ตรงกับวันที่ {resecond_date2} ควรจ่ายยา {convert_to_int(interval2*float(med2))} เม็ด/แคปซูล")  
    else:
        
        
          if  int(nudday) == 0:
              second_date2 = first_date2+relativedelta(days = int(nudday), weeks =int(nudwk), months = int(nudmt), years= int(nudyr), weekday=wkday   )
              resecond_date2 = second_date2.strftime("%d/%m/%Y")
              interval2 = int((second_date2 - first_date2).days)
              sum2 = st.code(f"ตรงกับวันที่ {resecond_date2} ควรจ่ายยา {convert_to_int(interval2*float(med2))} เม็ด/แคปซูล") 
          
          else:
             second_date2 = first_date2+relativedelta(days = int(nudday), weeks =int(nudwk), months = int(nudmt), years= int(nudyr)  )
             resecond_date2 = second_date2.strftime("%d/%m/%Y")
             interval2 = int((second_date2 - first_date2).days)
             sum2 = st.code(f"ตรงกับวันที่ {resecond_date2} ควรจ่ายยา {convert_to_int(interval2*float(med2))} เม็ด/แคปซูล")  
    
            
st.subheader("เช็คว่ากินยาครบหรือไม่",divider=True) 



col1c, col2c, col3c, col4c, col5c, col6c  = st.columns([1,1,0.8,1,1,0.8])

with col1c:
    date3 = st.selectbox("นัดครั้งที่แล้ววันที่",(listofdate),index=int(dy)-1, key ='date3')
    
with col2c:
    month3 =  st.selectbox( "เดือน", (listofmonth),index=int(mt)-1, key='month3')
    
with col3c:
    year3 = st.text_input( "พ.ศ.", value= int(yr)+543, key='year3') 
    
with col4c:
    date4 = st.selectbox("วันที่จะคำนวณ",(listofdate),index=int(dy)-1, key ='date4')
    
with col5c:
    month4 =  st.selectbox( "เดือน",(listofmonth),index=int(mt)-1, key='month4')
    
with col6c:
    year4 = st.text_input( "พ.ศ.", value= int(yr)+543, key='year4')   
    
col1c1, col2c1, col3c1, col4c1, col5c1, col6c1, col7c1, col8c1 = st.columns([0.5,0.6,1,1,0.5,0.5,1.5,1])

with col1c1:
    frea = st.write("นัดที่แล้ว")

with col2c1:
    nubmed = st.number_input("**", format= "%0f",key='nubmed', label_visibility= "collapsed")
    
with col3c1:
   frec = st.write("เม็ด/แคปซูล")  

with col4c1:
    freb = st.write("กินยาวันละ") 
    
with col5c1:
    med3 =  st.text_input("**", key='med3',value="1", label_visibility= "collapsed")
    
with col6c1:
    fred = st.write("เม็ด/แคปซูล") 
 
with col7c1:
    today3 = st.checkbox("นับรวมวันนี้ด้วย", key='today3')

with col8c1:
    but3 = st.button("คำนวณ", key='calculate3')
       
if but3:
        first_date3 = datetime.strptime(f'{date3}/{listofmonth.index(month3)+1}/{int(year3)-543}', "%d/%m/%Y")
        second_date3 = datetime.strptime(f'{date4}/{listofmonth.index(month4)+1}/{int(year4)-543}', "%d/%m/%Y")
        if today3:
            interval3 = int((second_date3 - first_date3).days)+1
            sum3 = st.code(f"{ float(nubmed) - (interval3*float(med3)) } เม็ด/แคปซูล") 
        else:
            interval3 = int((second_date3 - first_date3).days)
            sum3 = st.code(f"ควรเหลือยา { float(nubmed) - (interval3*float(med3))} เม็ด/แคปซูล") 

    




