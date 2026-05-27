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
    
    flavors = {
        "바닐라": {"emoji": "🤍", "color": "#FFF8DC", "desc": "부드럽고 클래식한 맛"},
        "초콜릿": {"emoji": "🤎", "color": "#8B4513", "desc": "진하고 달콤한 맛"},
        "딸기": {"emoji": "🩷", "color": "#FFB6C1", "desc": "상큼하고 사랑스러운 맛"},
        "말차": {"emoji": "💚", "color": "#9ACD32", "desc": "은은하고 고급스러운 맛"}
    }
    
    for col, (flavor, info) in zip([col1, col2, col3, col4], flavors.items()):
        with col:
            st.markdown(f"""
            <div style="background:{info['color']}; padding:20px; border-radius:15px; text-align:center; min-height:150px;">
                <h1>{info['emoji']}</h1>
                <h3>{flavor}</h3>
                <p>{info['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"{flavor} 선택!", key=f"flavor_{flavor}", use_container_width=True):
                st.session_state.cake_flavor = flavor
                st.success(f"🎉 {info['emoji']} {flavor} 반죽을 만들었어요!")
    
    if st.session_state.cake_flavor:
        st.markdown(f"### ✅ 선택한 맛: **{flavors[st.session_state.cake_flavor]['emoji']} {st.session_state.cake_flavor}**")
        
        with st.expander("🥄 반죽 만드는 과정 보기"):
            st.markdown("""
            1. 🥚 계란을 풀어주세요
            2. 🧈 버터와 설탕을 섞어요
            3. 🌾 밀가루를 체에 쳐서 넣어요
            4. 🥛 우유를 조금씩 부어가며 섞어요
            5. ✨ 부드러운 반죽 완성!
            """)
        
        if st.button("➡️ 오븐에 넣기!", use_container_width=True, type="primary"):
            st.session_state.step = 1
            st.rerun()

# ============ STEP 1: 오븐에 굽기 ============
elif st.session_state.step == 1:
    st.markdown("## 🔥 Step 2. 오븐에서 굽기")
    st.markdown(f"### {st.session_state.cake_flavor} 반죽을 오븐에 넣어요! 🎵")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        temperature = st.slider("🌡️ 오븐 온도 (°C)", 150, 220, 180)
        bake_time = st.slider("⏰ 굽는 시간 (분)", 20, 50, 30)
    
    with col2:
        st.markdown(f"""
        <div style="text-align:center; padding:30px; background:linear-gradient(135deg, #FFE4B5, #FFA500); border-radius:20px;">
            <h1 style="font-size:5rem;">🔥♨️🔥</h1>
            <h2>오븐 설정</h2>
            <h3>🌡️ {temperature}°C  |  ⏰ {bake_time}분</h3>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("🔥 굽기 시작!", use_container_width=True, type="primary"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        cake_visual = st.empty()
        
        stages = ["🥣", "🍞", "🎂"]
        messages = ["반죽이 부풀고 있어요...", "노릇노릇 익어가고 있어요...", "거의 다 됐어요!"]
        
        for i in range(101):
            progress_bar.progress(i)
            stage_idx = min(i // 34, 2)
            status_text.markdown(f"### {messages[stage_idx]} ({i}%)")
            cake_visual.markdown(f"<div class='cake-display'>{stages[stage_idx]}</div>", unsafe_allow_html=True)
            time.sleep(0.03)
        
        # 결과 판정
        if 170 <= temperature <= 200 and 25 <= bake_time <= 40:
            st.success("🎉 완벽하게 구워졌어요! 황금빛 케이크 빵 완성!")
            st.session_state.cake_baked = "perfect"
        elif temperature > 200 or bake_time > 40:
            st.warning("😅 조금 탔지만 먹을 만해요!")
            st.session_state.cake_baked = "burnt"
        else:
            st.info("🤔 조금 덜 익었지만 부드러워요!")
            st.session_state.cake_baked = "soft"
        
        st.balloons()
    
    if st.session_state.cake_baked:
        if st.button("➡️ 생크림 만들러 가기!", use_container_width=True, type="primary"):
            st.session_state.step = 2
            st.rerun()

# ============ STEP 2: 생크림 만들기 ============
elif st.session_state.step == 2:
    st.markdown("## 🥛 Step 3. 생크림 만들기")
    st.markdown("### 어떤 크림으로 케이크를 덮을까요? 🍦")
    
    cream_options = {
        "화이트 생크림": {"emoji": "🤍", "color": "#FFFFFF", "desc": "순백의 깔끔한 크림"},
        "초코 생크림": {"emoji": "🍫", "color": "#D2691E", "desc": "진한 초콜릿 크림"},
        "딸기 생크림": {"emoji": "🍓", "color": "#FFB6C1", "desc": "달콤한 핑크 크림"},
        "레몬 생크림": {"emoji": "🍋", "color": "#FFFACD", "desc": "상큼한 옐로우 크림"},
        "블루베리 크림": {"emoji": "🫐", "color": "#9370DB", "desc": "신비로운 보라 크림"}
    }
    
    cols = st.columns(5)
    for col, (cream, info) in zip(cols, cream_options.items()):
        with col:
            st.markdown(f"""
            <div style="background:{info['color']}; padding:15px; border-radius:15px; text-align:center; min-height:150px; border: 2px solid #ddd;">
                <h1>{info['emoji']}</h1>
                <h4>{cream}</h4>
                <p style="font-size:0.8rem;">{info['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"선택!", key=f"cream_{cream}", use_container_width=True):
                st.session_state.cream_flavor = cream
    
    if st.session_state.cream_flavor:
        st.success(f"✅ {cream_options[st.session_state.cream_flavor]['emoji']} {st.session_state.cream_flavor}을(를) 선택했어요!")
        
        st.markdown("### 🌀 크림을 휘핑해주세요!")
        whip_count = st.slider("휘핑 횟수 🥄", 0, 100, 0)
        
        if whip_count < 30:
            st.info("🥛 아직 묽어요... 더 휘핑해주세요!")
        elif whip_count < 70:
            st.warning("🍦 조금 더! 거의 다 됐어요!")
        else:
            st.success("✨ 완벽한 크림 완성! 부드럽고 폭신폭신해요!")
            if st.button("➡️ 데코레이션 하러 가기!", use_container_width=True, type="primary"):
                st.session_state.step = 3
                st.rerun()

# ============ STEP 3: 데코레이션 ============
elif st.session_state.step == 3:
    st.markdown("## 🍓 Step 4. 케이크 꾸미기")
    st.markdown("### 마음껏 데코레이션을 추가해보세요! 🎨")
    
    decorations_list = {
        "딸기": "🍓", "블루베리": "🫐", "체리": "🍒", "포도": "🍇",
        "초콜릿": "🍫", "쿠키": "🍪", "마카롱": "🧁", "사탕": "🍬",
        "별": "⭐", "하트": "💖", "꽃": "🌸", "리본": "🎀",
        "촛불": "🕯️", "왕관": "👑", "무지개": "🌈", "반짝이": "✨"
    }
    
    st.markdown("### 🎁 데코 아이템을 클릭해서 추가하세요!")
    
    cols = st.columns(8)
    for idx, (name, emoji) in enumerate(decorations_list.items()):
        with cols[idx % 8]:
            if st.button(f"{emoji}\n{name}", key=f"deco_{name}", use_container_width=True):
                st.session_state.decorations.append(emoji)
                st.rerun()
    
    st.markdown("---")
    
    # 메시지 입력
    st.markdown("### 💌 케이크에 메시지를 적어보세요!")
    st.session_state.cake_message = st.text_input("메시지 입력", value=st.session_state.cake_message, placeholder="예: Happy Birthday! 🎉", max_chars=30)
    
    # 현재 케이크 미리보기
    st.markdown("### 👀 현재 케이크 미리보기")
    
    cake_base = "🎂"
    flavor_emoji = {"바닐라": "🤍", "초콜릿": "🤎", "딸기": "🩷", "말차": "💚"}
    cream_emoji_map = {"화이트 생크림": "🤍", "초코 생크림": "🍫", "딸기 생크림": "🍓", "레몬 생크림": "🍋", "블루베리 크림": "🫐"}
    
    decoration_display = " ".join(st.session_state.decorations) if st.session_state.decorations else "아직 데코가 없어요!"
    
    st.markdown(f"""
    <div style="text-align:center; padding:30px; background:linear-gradient(135deg, #FFF0F5, #FFE4E1); border-radius:20px;">
        <h3>🍰 {st.session_state.cake_flavor} 케이크 + {st.session_state.cream_flavor}</h3>
        <div style="font-size:5rem;">{cake_base}</div>
        <div style="font-size:2rem; margin:20px 0;">{decoration_display}</div>
        <h2 style="color:#FF69B4;">💌 {st.session_state.cake_message if st.session_state.cake_message else '메시지를 입력해주세요'}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 데코 초기화", use_container_width=True):
            st.session_state.decorations = []
            st.rerun()
    with col2:
        if st.button("✅ 완성하기!", use_container_width=True, type="primary"):
            st.session_state.step = 4
            st.rerun()

# ============ STEP 4: 완성! ============
elif st.session_state.step == 4:
    st.markdown("## 🎉 케이크 완성! 🎉")
    st.balloons()
    st.snow()
    
    cake_base = "🎂"
    decoration_display = " ".join(st.session_state.decorations) if st.session_state.decorations else ""
    
    st.markdown(f"""
    <div style="text-align:center; padding:50px; background:linear-gradient(135deg, #FFB6C1, #FFD700, #FF69B4); border-radius:30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
        <h1 style="color:white; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🌟 나만의 특별한 케이크 🌟</h1>
        <div style="font-size:10rem; margin:30px 0;">{cake_base}</div>
        <div style="font-size:3rem; margin:20px 0; background:white; padding:20px; border-radius:20px;">{decoration_display}</div>
        <h2 style="color:white; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">💌 {st.session_state.cake_message if st.session_state.cake_message else 'Sweet Cake!'} 💌</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📋 케이크 레시피 카드")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"🍰 **빵 맛**\n\n{st.session_state.cake_flavor}")
    with col2:
        st.info(f"🥛 **크림**\n\n{st.session_state.cream_flavor}")
    with col3:
        st.info(f"🎨 **데코 개수**\n\n{len(st.session_state.decorations)}개")
    
    # 평가
    score = 60 + len(st.session_state.decorations) * 3
    if st.session_state.cake_message:
        score += 10
    score = min(score, 100)
    
    st.markdown(f"### 🏆 케이크 점수: {score}점")
    st.progress(score / 100)
    
    if score >= 90:
        st.success("🌟 환상적인 케이크예요! 파티시에 자격증 발급! 👨‍🍳")
    elif score >= 70:
        st.success("😊 정말 멋진 케이크네요!")
    else:
        st.info("🍰 소박하지만 정성 가득한 케이크!")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 다시 만들기", use_container_width=True, type="primary"):
            st.session_state.step = 0
            st.session_state.cake_flavor = None
            st.session_state.cake_baked = False
            st.session_state.cream_flavor = None
            st.session_state.decorations = []
            st.session_state.cake_message = ""
            st.rerun()
    with col2:
        if st.button("📸 자랑하기", use_container_width=True):
            st.success("🎉 친구들에게 자랑해보세요! 화면을 캡처해보세요!")

# 푸터
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#999; padding:20px;">
    <p>🎂 Made with 💖 for 당곡고등학교 학생들 🍰</p>
    <p>✨ Powered by Streamlit ✨</p>
</div>
""", unsafe_allow_html=True)
