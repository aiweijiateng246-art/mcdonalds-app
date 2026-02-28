import streamlit as st
import random

# メニューデータ
if 'menu_data' not in st.session_state:
    st.session_state.menu_data = {
        "チーズバーガー": "マス、ケチャ、オニ、ピ、チーズ、10",
        "ダブルチーズバーガー": "マス、ケチャ、オニ、ピク×2、チーズ、10、チーズ、10",
        "HB":"マス、ケチャ、オニ、ピ、10",
        "エグチ":"マス、ケチャ、オニ、ピク、たまちー、肉",
        # ここにどんどん追加していきます
    }

# 状態管理（現在の問題と回答表示フラグ）
if 'current_item' not in st.session_state:
    st.session_state.current_item = random.choice(list(st.session_state.menu_data.keys()))
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False

st.title("🍔 マックメニュー暗記アプリ")

# 問題表示
st.subheader(f"問題：{st.session_state.current_item}")

# 答えを見るボタン
if st.button("答えを見る"):
    st.session_state.show_answer = True

# 答えの表示
if st.session_state.show_answer:
    st.success(f"答え：{st.session_state.menu_data[st.session_state.current_item]}")
    
    # 次の問題へボタン
    if st.button("次の問題へ"):
        st.session_state.current_item = random.choice(list(st.session_state.menu_data.keys()))
        st.session_state.show_answer = False
        st.rerun()

st.sidebar.write("全メニューを覚えたら、君もマネージャー級！")
