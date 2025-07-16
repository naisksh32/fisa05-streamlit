import streamlit as st

# 1. 버튼을 누르면 화면에 True라고 뜨는 간단한 동작 작성
a = st.button('Click')  # 버튼은 처음에 false로 기본값

st.write(a)

if st.button('클릭'):
    st.write(True)


# 2. 사진을 찍으면 다운로드 버튼으로 사진을 다운로드 받을 수 있게 작성
if image := st.camera_input('Click a Snap'):
    # 사진을 찍기 전에는 들여쓰기 안 코드를 실행하지 않습니다.
    st.download_button('Download Photo', image, 'my.png')
    # 사진을 찍어 데이터가 있으면 다운로드 버튼을 활성화