import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)

# st.bar_chart(df.rating, x=df.command)
# streamlit의 default chart는 altain라는 매서드가 없기 때문

import plotly.express as px

# Plotly Bar Chart
fig = px.bar(
    df,
    x="command",     # x축에 command
    y="rating",      # y축에 rating
    color="command", # command별 색깔 구분
    labels={"command": "x축 제목", "rating": "Rating"},
    title="Command Rating Bar Chart"
)

# ploty 차트를 streamlit으로 출력
st.plotly_chart(fig, use_container_width=True) # 현재 창 크기 모두 활용하겠다

data = 'hellow'

# 입력을 변수로 받아 출력으로 넘김
# 1. 버튼을 누르면 화면에 True라고 뜨는 간단한 동작 작성
a = st.button('Click')  # 버튼은 처음에 false로 기본값
print(a)
st.write(a)

if st.button('클릭'):
    st.write(True)
print(a)

# 2. 사진을 찍으면 다운로드 버튼으로 사진을 다운로드 받을 수 있게 작성
if image := st.camera_input('Click a Snap'):
    # 사진을 찍기 전에는 들여쓰기 안 코드를 실행하지 않습니다.
    st.download_button('Download Photo', image, 'my.png')
    # 사진을 찍어 데이터가 있으면 다운로드 버튼을 활성화

# 입력
st.data_editor(df)
st.checkbox('Option 1')

country = st.radio('Pick Country:', ['France','Germany'])
st.write(country)

st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter Article')
st.number_input('Enter required number')
st.text_area('Entered article text')
st.date_input('Select date')
st.time_input('Select Time')
st.file_uploader('File CSV uploader')
st.download_button('Download Source data', data)
st.color_picker('Pick a color')

# 출력
st.text('Tushar-Aggarwal.com')
st.markdown('[Tushar-Aggarwal.com](https://tushar-aggarwal.com)')
st.caption('Success')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Supreme Applcations by Tushar Aggarwal')
st.write(['st', 'is <', 3]) # see *
st.title('Streamlit Magic Cheat Sheets')
st.header('Developed by Tushar Aggarwal')
st.subheader('visit tushar-aggarwal.com')
st.code('for i in range(8): print(i)')
st.image('https://i.imgur.com/t2ewhfH.png')
# * optional kwarg unsafe_allow_html = True

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

for i in ani_list:
    st.header(i)

