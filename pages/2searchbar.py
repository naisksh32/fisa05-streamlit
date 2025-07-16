import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# text를 입력받아 해당 텍스트와 일치하면 그 이미지를 화면에 출력하는 검색창을 적어주세요
txt = st.text_input('애니메이션 리스트')

for i in range(len(ani_list)):
    if (txt in ani_list[i]) and (txt != ''):
        st.image(img_list[i])
    else:
        break
        st.text('일치하는 값이 없습니다.')
