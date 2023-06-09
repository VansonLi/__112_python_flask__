import requests
import pandas as pd
import streamlit as st

url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
response = requests.request('GET',url)
if response.status_code == 200:
    print('連線成功')
    all_data = response.json()
    print(type(all_data))
else:
    print(f'連線失敗:{response.status_code}')

dataFrame = pd.DataFrame(data=all_data,columns=['sna','tot','sbi','sarea','mday','ar','bemp','act'])
mask = dataFrame['sbi'] <= 3
mask_dataFrame = dataFrame[mask]
st.dataframe(mask_dataFrame)
