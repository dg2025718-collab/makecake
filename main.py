import streamlit as st
import time
import random

# 페이지 설정
st.set_page_config(
    page_title="나만의 케이크 만들기",
    page_icon="🎂",
    layout="wide"
)

# 세션 상태 초기화
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'cake_flavor' not in st.session_state:
    st.session_state.cake_flavor = None
if 'cake_baked' not in st.session_state:
    st.session_state.cake_baked = False
if 'cream_flavor' not in st.session_state:
    st.session_state.cream_flavor = None
if 'decorations' not in st.session_state:
    st.session_state.decorations = []
if 'cake_message' not in st.session_state:
    st.session_state.cake_message = ""

# CSS 스타일
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 3rem;
        background: linear-gradient(90deg, #FFB6C1, #FFD700, #FF69B4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        padding: 20px;
    }
    .step-box {
        background: linear-gradient(135deg, #FFF0F5 0%, #FFE4E1 100%);
        padding: 20px;
        border-radius: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .cake-display {
        text-align: center;
        font-size: 8rem;
        padding: 30px;
        background: linear-gradient(135deg, #FFE4E1 0%, #FFF0F5 100%);
        border-radius: 30px;
        margin: 20px 0;
    }
    .progress-step {
        text-align: center;
        padding: 10px;
        border-radius: 10px;
        font-weight: bold;
    }
    .active-step {
        background: linear-gradient(135deg, #FF69B4, #FFB6C1);
        color: white;
    }
    .inactive-step {
        background: #f0f0f0;
        color: #999;
    }
</style>
""", unsafe_allow_html=True)

# 메인 타이틀
st.markdown('<h1 class="main-title">🎂 나만의 케이크 만들기 🍰</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:1.2rem; color:#666;">✨ 세상에 하나뿐인 특별한 케이크를 만들어보세요! ✨</p>', unsafe_allow_html=True)

# 진행 단계 표시
steps = ["🥣 빵 반죽", "🔥 오븐 굽기", "🥛 생크림 만들기", "🍓 데코레이션", "🎉 완성!"]
cols = st.columns(5)
for idx, (col, step_name) in enumerate(zip(cols, steps)):
    with col:
        if idx <= st.session_state.step:
            st.markdown(f'<div class="progress-step active-step">{step_name}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="progress-step inactive-step">{step_name}</div>', unsafe_allow_html=True)

st.markdown("---")

# ============ STEP 0: 케이크 빵 만들기 ============
if st.session_state.step == 0:
    st.markdown("## 🥣 Step 1. 케이크 빵 반죽하기")
    st.markdown("### 어떤 맛의 케이크 빵을 만들까요? 🤔")
    
    col1, col2, col3, col4 = st.columns(4)
