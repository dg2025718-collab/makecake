import streamlit as st
import streamlit.components.v1 as components
import time

# 페이지 설정
st.set_page_config(
    page_title="나만의 케이크 만들기",
    page_icon="🎂",
    layout="wide"
)

# 세션 상태 초기화
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'ingredients' not in st.session_state:
    st.session_state.ingredients = {"밀가루": 0, "설탕": 0, "계란": 0, "버터": 0, "우유": 0, "베이킹파우더": 0}
if 'flavor_addon' not in st.session_state:
    st.session_state.flavor_addon = None
if 'dough_quality' not in st.session_state:
    st.session_state.dough_quality = None
if 'cake_baked' not in st.session_state:
    st.session_state.cake_baked = False
if 'cream_flavor' not in st.session_state:
    st.session_state.cream_flavor = None
if 'whip_count' not in st.session_state:
    st.session_state.whip_count = 0
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
st.markdown('<p style="text-align:center; font-size:1.2rem; color:#666;">✨ 직접 반죽부터 데코까지! 세상에 하나뿐인 케이크! ✨</p>', unsafe_allow_html=True)

# 진행 단계 표시
steps = ["🥣 반죽 만들기", "🔥 오븐 굽기", "🥛 생크림 휘핑", "🍓 데코레이션", "🎉 완성!"]
cols = st.columns(5)
for idx, (col, step_name) in enumerate(zip(cols, steps)):
    with col:
        if idx <= st.session_state.step:
            st.markdown(f'<div class="progress-step active-step">{step_name}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="progress-step inactive-step">{step_name}</div>', unsafe_allow_html=True)

st.markdown("---")

# ============ STEP 0: 빵 반죽 직접 만들기 ============
if st.session_state.step == 0:
    st.markdown("## 🥣 Step 1. 반죽 직접 만들기")
    st.markdown("### 재료를 직접 넣어가며 반죽을 완성해보세요! 👩‍🍳")
    
    st.info("💡 **레시피 가이드**: 밀가루 3컵, 설탕 2컵, 계란 3개, 버터 1컵, 우유 2컵, 베이킹파우더 1스푼이 적당해요!")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🧂 재료 추가하기")
        
        ingredients_info = {
            "밀가루": {"emoji": "🌾", "unit": "컵", "ideal": 3},
            "설탕": {"emoji": "🍬", "unit": "컵", "ideal": 2},
            "계란": {"emoji": "🥚", "unit": "개", "ideal": 3},
            "버터": {"emoji": "🧈", "unit": "컵", "ideal": 1},
            "우유": {"emoji": "🥛", "unit": "컵", "ideal": 2},
            "베이킹파우더": {"emoji": "🧂", "unit": "스푼", "ideal": 1}
        }
        
        for ing, info in ingredients_info.items():
            c1, c2, c3 = st.columns([2, 1, 1])
            with c1:
                st.markdown(f"#### {info['emoji']} {ing}: **{st.session_state.ingredients[ing]}{info['unit']}**")
            with c2:
                if st.button(f"➕ 추가", key=f"add_{ing}", use_container_width=True):
                    st.session_state.ingredients[ing] += 1
                    st.rerun()
            with c3:
                if st.button(f"➖ 빼기", key=f"sub_{ing}", use_container_width=True):
                    if st.session_state.ingredients[ing] > 0:
                        st.session_state.ingredients[ing] -= 1
                        st.rerun()
        
        st.markdown("### 🎨 맛 추가하기 (선택)")
        flavor_cols = st.columns(4)
        flavors = {"바닐라": "🤍", "초콜릿": "🍫", "딸기": "🍓", "말차": "🍵"}
        for col, (flavor, emoji) in zip(flavor_cols, flavors.items()):
            with col:
                if st.button(f"{emoji}\n{flavor}", key=f"flavor_{flavor}", use_container_width=True):
                    st.session_state.flavor_addon = flavor
                    st.rerun()
        
        if st.session_state.flavor_addon:
            st.success(f"✅ {flavors[st.session_state.flavor_addon]} {st.session_state.flavor_addon} 맛 선택!")
    
    with col2:
        st.markdown("### 🥣 현재 반죽 상태")
        
        total = sum(st.session_state.ingredients.values())
        
        # 반죽 시각화
        bowl_content = ""
        for ing, count in st.session_state.ingredients.items():
            if count > 0:
                bowl_content += ingredients_info[ing]['emoji'] * count + " "
        
        if not bowl_content:
            bowl_content = "텅 비어있어요... 재료를 넣어주세요!"
        
        st.markdown(f"""
        <div style="text-align:center; padding:30px; background:linear-gradient(135deg, #FFF8DC, #FFE4B5); border-radius:20px; min-height:300px;">
            <h1 style="font-size:5rem;">🥣</h1>
            <div style="font-size:1.5rem; padding:20px; background:white; border-radius:15px; min-height:100px;">
                {bowl_content}
            </div>
            <h3>총 재료: {total}개</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # 반죽 평가
        st.markdown("### 📊 레시피 정확도")
        
        score = 0
        feedback = []
        for ing, info in ingredients_info.items():
            diff = abs(st.session_state.ingredients[ing] - info['ideal'])
            if diff == 0:
                score += 100 / 6
                feedback.append(f"✅ {info['emoji']} {ing}: 완벽!")
            elif diff == 1:
                score += 70 / 6
                feedback.append(f"🟡 {info['emoji']} {ing}: 살짝 아쉬워요")
            else:
                feedback.append(f"❌ {info['emoji']} {ing}: 양이 맞지 않아요")
        
        st.progress(int(score) / 100)
        st.markdown(f"**점수: {int(score)}점**")
        
        with st.expander("📝 자세한 평가 보기"):
            for fb in feedback:
                st.markdown(fb)
        
        if score >= 80:
            st.session_state.dough_quality = "perfect"
            st.success("🎉 완벽한 반죽이에요! 다음 단계로!")
        elif score >= 50:
            st.session_state.dough_quality = "good"
            st.info("😊 괜찮은 반죽이에요!")
        else:
            st.session_state.dough_quality = "bad"
            st.warning("😅 재료를 더 신경써서 넣어주세요!")
        
        if total > 0:
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("🔄 다시 만들기", use_container_width=True):
                    st.session_state.ingredients = {"밀가루": 0, "설탕": 0, "계란": 0, "버터": 0, "우유": 0, "베이킹파우더": 0}
                    st.session_state.flavor_addon = None
                    st.rerun()
            with col_b:
                if st.button("➡️ 오븐에 넣기!", use_container_width=True, type="primary"):
                    st.session_state.step = 1
                    st.rerun()

# ============ STEP 1: 오븐에 굽기 ============
elif st.session_state.step == 1:
    st.markdown("## 🔥 Step 2. 오븐에서 굽기")
    flavor_text = f" ({st.session_state.flavor_addon} 맛)" if st.session_state.flavor_addon else ""
    st.markdown(f"### 반죽{flavor_text}을 오븐에 넣어요! 🎵")
    
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
            cake_visual.markdown(f"<div style='text-align:center; font-size:8rem;'>{stages[stage_idx]}</div>", unsafe_allow_html=True)
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

# ============ STEP 2: 생크림 휘핑 (마우스 인터랙션) ============
elif st.session_state.step == 2:
    st.markdown("## 🥛 Step 3. 생크림 휘핑하기")
    st.markdown("### 크림 맛을 선택하고 마우스로 직접 휘핑해보세요! 🌀")
    
    # 크림 선택
    cream_options = {
        "화이트 생크림": {"emoji": "🤍", "color": "#FFFFFF"},
        "초코 생크림": {"emoji": "🍫", "color": "#D2691E"},
        "딸기 생크림": {"emoji": "🍓", "color": "#FFB6C1"},
        "레몬 생크림": {"emoji": "🍋", "color": "#FFFACD"},
        "블루베리 크림": {"emoji": "🫐", "color": "#9370DB"}
    }
    
    cols = st.columns(5)
    for col, (cream, info) in zip(cols, cream_options.items()):
        with col:
            if st.button(f"{info['emoji']}\n{cream}", key=f"cream_{cream}", use_container_width=True):
                st.session_state.cream_flavor = cream
                st.rerun()
    
    if st.session_state.cream_flavor:
        st.success(f"✅ {cream_options[st.session_state.cream_flavor]['emoji']} {st.session_state.cream_flavor} 선택!")
        
        st.markdown("---")
        st.markdown("### 🌀 마우스로 휘핑해주세요!")
        st.info("💡 **사용법**: 휘핑 영역에서 **마우스를 누른 상태로 위아래로 흔들어주세요!** 빠르게 흔들수록 카운트가 빨리 올라가요!")
        
        # 마우스 인터랙션 휘핑 컴포넌트
        cream_color = cream_options[st.session_state.cream_flavor]['color']
        cream_emoji = cream_options[st.session_state.cream_flavor]['emoji']
        
        whip_html = f"""
        <div style="text-align:center; font-family: Arial;">
            <div id="whipArea" style="
                width: 100%;
                height: 400px;
                background: linear-gradient(135deg, #FFE4E1, #FFF0F5);
                border: 4px dashed #FF69B4;
                border-radius: 20px;
                cursor: grab;
                position: relative;
                user-select: none;
                overflow: hidden;
            ">
                <div id="bowl" style="
                    position: absolute;
                    bottom: 20px;
                    left: 50%;
                    transform: translateX(-50%);
                    font-size: 6rem;
                ">🥣</div>
                
                <div id="whisk" style="
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    font-size: 5rem;
                    pointer-events: none;
                    transition: transform 0.1s;
                ">🥄</div>
                
                <div id="cream" style="
                    position: absolute;
                    bottom: 80px;
                    left: 50%;
                    transform: translateX(-50%);
                    font-size: 3rem;
                    opacity: 0;
                ">{cream_emoji}</div>
                
                <div id="instructions" style="
                    position: absolute;
                    top: 20px;
                    left: 50%;
                    transform: translateX(-50%);
                    color: #FF69B4;
                    font-weight: bold;
                    font-size: 1.2rem;
                ">⬇️ 여기를 클릭하고 위아래로 흔들어주세요! ⬆️</div>
            </div>
            
            <div style="margin-top: 20px;">
                <h2 style="color: #FF69B4;">🌀 휘핑 카운트: <span id="count" style="font-size: 3rem;">0</span> 회</h2>
                <div style="
                    width: 100%;
                    background: #f0f0f0;
                    border-radius: 20px;
                    overflow: hidden;
                    height: 30px;
                    margin: 10px 0;
                ">
                    <div id="progressBar" style="
                        width: 0%;
                        height: 100%;
                        background: linear-gradient(90deg, #FFB6C1, #FF69B4);
                        transition: width 0.3s;
                        text-align: center;
                        color: white;
                        line-height: 30px;
                        font-weight: bold;
                    ">0%</div>
                </div>
                <h3 id="statusText" style="color: #666;">🥛 묽은 상태 - 더 휘핑해주세요!</h3>
                <button id="saveBtn" onclick="saveCount()" style="
                    padding: 15px 40px;
                    font-size: 1.2rem;
                    background: linear-gradient(135deg, #FF69B4, #FFB6C1);
                    color: white;
                    border: none;
                    border-radius: 15px;
                    cursor: pointer;
                    font-weight: bold;
                    margin-top: 20px;
                ">✅ 휘핑 완료하기!</button>
            </div>
        </div>
        
        <script>
            let count = 0;
            let isDragging = false;
            let lastY = 0;
            let direction = 0; // 0: 없음, 1: 아래로, -1: 위로
            let lastDirection = 0;
            
            const whipArea = document.getElementById('whipArea');
            const whisk = document.getElementById('whisk');
            const countDisplay = document.getElementById('count');
            const progressBar = document.getElementById('progressBar');
            const statusText = document.getElementById('statusText');
            const cream = document.getElementById('cream');
            
            function updateStatus() {{
                const percent = Math.min(count, 100);
                progressBar.style.width = percent + '%';
                progressBar.textContent = percent + '%';
                
                if (count < 30) {{
                    statusText.textContent = '🥛 묽은 상태 - 더 휘핑해주세요!';
                    statusText.style.color = '#666';
                    cream.style.opacity = (count / 30) * 0.3;
                }} else if (count < 70) {{
                    statusText.textContent = '🍦 거의 다 됐어요! 조금 더!';
                    statusText.style.color = '#FFA500';
                    cream.style.opacity = 0.5;
                    cream.style.fontSize = '4rem';
                }} else if (count < 100) {{
                    statusText.textContent = '✨ 부드러운 크림 완성 중!';
                    statusText.style.color = '#FF69B4';
                    cream.style.opacity = 0.8;
                    cream.style.fontSize = '5rem';
                }} else {{
                    statusText.textContent = '🎉 완벽한 크림 완성! 다음 단계로!';
                    statusText.style.color = '#32CD32';
                    cream.style.opacity = 1;
                    cream.style.fontSize = '6rem';
                }}
            }}
            
            function handleStart(e) {{
                isDragging = true;
                whipArea.style.cursor = 'grabbing';
                const y = e.touches ? e.touches[0].clientY : e.clientY;
                lastY = y;
            }}
            
            function handleMove(e) {{
                if (!isDragging) return;
                e.preventDefault();
                
                const rect = whipArea.getBoundingClientRect();
                const x = (e.touches ? e.touches[0].clientX : e.clientX) - rect.left;
                const y = (e.touches ? e.touches[0].clientY : e.clientY) - rect.top;
                
                // 휘퍼 위치 업데이트
                whisk.style.left = x + 'px';
                whisk.style.top = y + 'px';
                whisk.style.transform = 'translate(-50%, -50%) rotate(' + (count * 10) + 'deg)';
                
                const currentY = e.touches ? e.touches[0].clientY : e.clientY;
                const deltaY = currentY - lastY;
                
                if (Math.abs(deltaY) > 10) {{
                    const currentDirection = deltaY > 0 ? 1 : -1;
                    
                    if (lastDirection !== 0 && currentDirection !== lastDirection) {{
                        // 방향이 바뀌면 카운트 증가 (위아래 흔들기)
                        count++;
                        countDisplay.textContent = count;
                        updateStatus();
                        
                        // 효과음 느낌
                        countDisplay.style.transform = 'scale(1.3)';
                        setTimeout(() => {{
                            countDisplay.style.transform = 'scale(1)';
                        }}, 100);
                    }}
                    
                    lastDirection = currentDirection;
                    lastY = currentY;
                }}
            }}
            
            function handleEnd() {{
                isDragging = false;
                whipArea.style.cursor = 'grab';
                lastDirection = 0;
            }}
            
            whipArea.addEventListener('mousedown', handleStart);
            whipArea.addEventListener('mousemove', handleMove);
            whipArea.addEventListener('mouseup', handleEnd);
            whipArea.addEventListener('mouseleave', handleEnd);
            
            whipArea.addEventListener('touchstart', handleStart);
            whipArea.addEventListener('touchmove', handleMove);
            whipArea.addEventListener('touchend', handleEnd);
            
            countDisplay.style.transition = 'transform 0.1s';
            
            function saveCount() {{
                if (count < 100) {{
                    alert('아직 휘핑이 부족해요! 100번 이상 흔들어주세요! 현재: ' + count + '회');
                    return;
                }}
                // Streamlit에 값 전달
                window.parent.postMessage({{
                    type: 'streamlit:setComponentValue',
                    value: count
                }}, '*');
                alert('🎉 휘핑 완료! ' + count + '회 휘핑했어요! 아래 버튼을 눌러 다음 단계로 가세요!');
            }}
        </script>
        """
        
        components.html(whip_html, height=700)
        
        st.markdown("### 휘핑이 끝나셨나요?")
        whip_done = st.checkbox("✅ 휘핑을 100번 이상 했어요!")
        
        if whip_done:
            st.success("🎉 완벽한 크림 완성!")
            if st.button("➡️ 데코레이션 하러 가기!", use_container_width=True, type="primary"):
                st.session_state.whip_count = 100
                st.session_state.step = 3
                st.rerun()

# ============ STEP 3: 데코레이션 (케이크 위에 직접 올리기) ============
elif st.session_state.step == 3:
    st.markdown("## 🍓 Step 4. 케이크 꾸미기")
    st.markdown("### 데코를 선택하면 케이크 위에 올라가요! 🎨")
    
    decorations_list = {
        "딸기": "🍓", "블루베리": "🫐", "체리": "🍒", "포도": "🍇",
        "초콜릿": "🍫", "쿠키": "🍪", "마카롱": "🧁", "사탕": "🍬",
        "별": "⭐", "하트": "💖", "꽃": "🌸", "리본": "🎀",
        "촛불": "🕯️", "왕관": "👑", "무지개": "🌈", "반짝이": "✨"
    }
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🎁 데코 선택")
        st.caption("클릭하면 케이크 위에 올라가요!")
        
        deco_cols = st.columns(4)
        for idx, (name, emoji) in enumerate(decorations_list.items()):
            with deco_cols[idx % 4]:
                if st.button(f"{emoji}", key=f"deco_{name}", use_container_width=True, help=name):
                    st.session_state.decorations.append(emoji)
                    st.rerun()
        
        st.markdown("### 💌 메시지")
        st.session_state.cake_message = st.text_input("케이크 메시지", value=st.session_state.cake_message, placeholder="Happy Birthday! 🎉", max_chars=30)
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🔄 데코 초기화", use_container_width=True):
                st.session_state.decorations = []
                st.rerun()
        with col_b:
            if len(st.session_state.decorations) > 0 and st.session_state.decorations[-1:]:
                if st.button("↩️ 마지막 취소", use_container_width=True):
                    st.session_state.decorations.pop()
                    st.rerun()
    
    with col2:
        st.markdown("### 🎂 내 케이크")
        
        # 크림 색상
        cream_colors = {
            "화이트 생크림": "#FFFFFF",
            "초코 생크림": "#D2691E",
            "딸기 생크림": "#FFB6C1",
            "레몬 생크림": "#FFFACD",
            "블루베리 크림": "#9370DB"
        }
        cream_color = cream_colors.get(st.session_state.cream_flavor, "#FFFFFF")
        
        # 케이크 빵 색상
        bread_colors = {
            "바닐라": "#FFE4B5",
            "초콜릿": "#8B4513",
            "딸기": "#FFB6C1",
            "말차": "#9ACD32"
        }
        bread_color = bread_colors.get(st.session_state.flavor_addon, "#FFE4B5")
        
        # 데코를 케이크 위에 배치
        deco_html = ""
        positions = [
            (50, 25), (30, 30), (70, 30), (20, 40), (80, 40),
            (40, 22), (60, 22), (35, 38), (65, 38), (50, 35),
            (25, 28), (75, 28), (45, 32), (55, 32), (15, 35), (85, 35)
        ]
        
        for idx, deco in enumerate(st.session_state.decorations):
            pos = positions[idx % len(positions)]
            deco_html += f'<div style="position:absolute; left:{pos[0]}%; top:{pos[1]}%; font-size:2.5rem; transform:translate(-50%,-50%); z-index:{10+idx};">{deco}</div>'
        
        message_html = ""
        if st.session_state.cake_message:
            message_html = f'<div style="position:absolute; bottom:25%; left:50%; transform:translate(-50%,-50%); font-size:1.5rem; font-weight:bold; color:#FF1493; text-shadow: 2px 2px 4px white; z-index:50; background:rgba(255,255,255,0.8); padding:5px 15px; border-radius:15px;">{st.session_state.cake_message}</div>'
        
        cake_html = f"""
        <div style="position:relative; width:100%; height:500px; background:linear-gradient(135deg, #FFF0F5, #FFE4E1); border-radius:20px; overflow:hidden;">
            <!-- 케이크 상단 (크림) -->
            <div style="position:absolute; bottom:15%; left:15%; right:15%; height:35%; background:{cream_color}; border-radius:50% 50% 10px 10px / 30% 30% 10px 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); border: 3px solid #fff;">
            </div>
            
            <!-- 케이크 빵 (중간) -->
            <div style="position:absolute; bottom:5%; left:12%; right:12%; height:25%; background:{bread_color}; border-radius:10px; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
            </div>
            
            <!-- 접시 -->
            <div style="position:absolute; bottom:2%; left:8%; right:8%; height:5%; background:#ddd; border-radius:50%; box-shadow: 0 5px 15px rgba(0,0,0,0.3);">
            </div>
            
            <!-- 데코레이션 -->
            {deco_html}
            
            <!-- 메시지 -->
            {message_html}
        </div>
        """
        
        st.markdown(cake_html, unsafe_allow_html=True)
        
        st.markdown(f"**🎨 올린 데코: {len(st.session_state.decorations)}개**")
        
        if st.button("✅ 완성하기!", use_container_width=True, type="primary"):
            st.session_state.step = 4
            st.rerun()

# ============ STEP 4: 완성! ============
elif st.session_state.step == 4:
    st.markdown("## 🎉 케이크 완성! 🎉")
    st.balloons()
    st.snow()
    
    # 크림 색상
    cream_colors = {
        "화이트 생크림": "#FFFFFF",
        "초코 생크림": "#D2691E",
        "딸기 생크림": "#FFB6C1",
        "레몬 생크림": "#FFFACD",
        "블루베리 크림": "#9370DB"
    }
    cream_color = cream_colors.get(st.session_state.cream_flavor, "#FFFFFF")
    
    bread_colors = {
        "바닐라": "#FFE4B5",
        "초콜릿": "#8B4513",
        "딸기": "#FFB6C1",
        "말차": "#9ACD32"
    }
    bread_color = bread_colors.get(st.session_state.flavor_addon, "#FFE4B5")
    
    # 데코 배치
    deco_html = ""
    positions = [
        (50, 25), (30, 30), (70, 30), (20, 40), (80, 40),
        (40, 22), (60, 22), (35, 38), (65, 38), (50, 35),
        (25, 28), (75, 28), (45, 32), (55, 32), (15, 35), (85, 35)
    ]
    
    for idx, deco in enumerate(st.session_state.decorations):
        pos = positions[idx % len(positions)]
        deco_html += f'<div style="position:absolute; left:{pos[0]}%; top:{pos[1]}%; font-size:3rem; transform:translate(-50%,-50%); z-index:{10+idx};">{deco}</div>'
    
    message_html = ""
    if st.session_state.cake_message:
        message_html = f'<div style="position:absolute; bottom:25%; left:50%; transform:translate(-50%,-50%); font-size:2rem; font-weight:bold; color:#FF1493; text-shadow: 2px 2px 4px white; z-index:50; background:rgba(255,255,255,0.9); padding:10px 20px; border-radius:20px;">{st.session_state.cake_message}</div>'
    
    final_cake_html = f"""
    <div style="position:relative; width:100%; height:600px; background:linear-gradient(135deg, #FFB6C1, #FFD700, #FF69B4); border-radius:30px; overflow:hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
        <h1 style="text-align:center; color:white; padding:20px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🌟 나만의 특별한 케이크 🌟</h1>
        
        <!-- 케이크 상단 (크림) -->
        <div style="position:absolute; bottom:15%; left:15%; right:15%; height:35%; background:{cream_color}; border-radius:50% 50% 10px 10px / 30% 30% 10px 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.3); border: 3px solid #fff;">
        </div>
        
        <!-- 케이크 빵 -->
        <div style="position:absolute; bottom:5%; left:12%; right:12%; height:25%; background:{bread_color}; border-radius:10px; box-shadow: 0 5px 15px rgba(0,0,0,0.3);">
        </div>
        
        <!-- 접시 -->
        <div style="position:absolute; bottom:2%; left:8%; right:8%; height:5%; background:#fff; border-radius:50%; box-shadow: 0 5px 15px rgba(0,0,0,0.3);">
        </div>
        
        {deco_html}
        {message_html}
    </div>
    """
    
    st.markdown(final_cake_html, unsafe_allow_html=True)
    
    st.markdown("### 📋 케이크 레시피 카드")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.info(f"🍰 **빵 맛**\n\n{st.session_state.flavor_addon or '플레인'}")
    with col2:
        st.info(f"🥛 **크림**\n\n{st.session_state.cream_flavor}")
    with col3:
        st.info(f"🌀 **휘핑**\n\n{st.session_state.whip_count}회")
    with col4:
        st.info(f"🎨 **데코**\n\n{len(st.session_state.decorations)}개")
    
    # 평가
    score = 50
    if st.session_state.dough_quality == "perfect":
        score += 20
    elif st.session_state.dough_quality == "good":
        score += 10
    
    if st.session_state.cake_baked == "perfect":
        score += 15
    
    score += min(len(st.session_state.decorations) * 2, 15)
    
    if st.session_state.cake_message:
        score += 5
    
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
            st.session_state.ingredients = {"밀가루": 0, "설탕": 0, "계란": 0, "버터": 0, "우유": 0, "베이킹파우더": 0}
            st.session_state.flavor_addon = None
            st.session_state.dough_quality = None
            st.session_state.cake_baked = False
            st.session_state.cream_flavor = None
            st.session_state.whip_count = 0
            st.session_state.decorations = []
            st.session_state.cake_message = ""
            st.rerun()
    with col2:
        if st.button("📸 자랑하기", use_container_width=True):
            st.success("🎉 화면을 캡처해서 친구들에게 자랑해보세요!")

# 푸터
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#999; padding:20px;">
    <p>🎂 Made with 💖 for 당곡고등학교 학생들 🍰</p>
    <p>✨ Powered by Streamlit ✨</p>
</div>
""", unsafe_allow_html=True)
