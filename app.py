import streamlit as st
import random

# メニューデータ
if 'menu_data' not in st.session_state:
    st.session_state.menu_data = {
        "チーズバーガー": "マス、ケチャ、オニ、ピ、チーズ、10",
        "ダブルチーズバーガー": "マス、ケチャ、オニ、ピク×2、チーズ、10、チーズ、10",
    }

# 状態管理（現在の問題、回答表示フラグ、履歴）
if 'current_item' not in st.session_state:
    st.session_state.current_item = random.choice(list(st.session_state.menu_data.keys()))
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("🍔 マックメニュー暗記アプリ")

# 問題表示
st.info(f"問題：{st.session_state.current_item}")

# 答えを見るボタン
if not st.session_state.show_answer:
    if st.button("答えを見る"):
        st.session_state.show_answer = True
        st.rerun()

# 答えの表示
if st.session_state.show_answer:
    st.success(f"答え：{st.session_state.menu_data[st.session_state.current_item]}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("次の問題へ"):
            # 今の問題を履歴に追加
            st.session_state.history.append(st.session_state.current_item)
            # 新しい問題をランダム選択
            all_items = list(st.session_state.menu_data.keys())
            st.session_state.current_item = random.choice(all_items)
            st.session_state.show_answer = False
            st.rerun()
            
    with col2:
        # 履歴がある場合のみ「前へ」ボタンを表示
        if len(st.session_state.history) > 0:
            if st.button("一つ前の問題に戻る"):
                # 履歴の最後を取り出して現在の問題にする
                prev_item = st.session_state.history.pop()
                st.session_state.current_item = prev_item
                st.session_state.show_answer = False
                st.rerun()

st.sidebar.header("メニューリスト")
for item in st.session_state.menu_data.keys():
    st.sidebar.write(f"・{item}")

if len(st.session_state.history) > 0:
    st.sidebar.divider()
    st.sidebar.write(f"解いた数: {len(st.session_state.history)} 問")
