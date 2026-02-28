import streamlit as st
import random

# メニューデータ
if 'menu_data' not in st.session_state:
    st.session_state.menu_data = {
        "チーズバーガー": "マス、ケチャ、オニ、ピ、チーズ、10",
        "ダブルチーズバーガー": "マス、ケチャ、オニ、ピク×2、チーズ、10、チーズ、10",
        "HB（ハンバーガー）": "マス、ケチャ、オニ、ピ、10",
        "エグチ": "マス、ケチャ、オニ、ピク、たまちー、肉",
        "TMB（テリヤキ）": "Mスイート、レタス、てりやき＋ソース",
        "テリCFO": "Mスイート、レタス、Mチキ＋ソース",
        "チキチー": "Mスイート、細レタス、クリスプ、チーズ",
        "マックチキン": "レモン、細レタス、クリスプ",
        "チキンフィレオ": "オーロラ、オニオン、レタス、Mチキ",
        "FOF（フィレオフィッシュ）": "タルタル、FOF、ハーフチーズ",
        "BM（ビッグマック）": "BMソース、オニオン、細レタス、ピ×２、10、BMソース、オニオン、細レタス、チーズ、10、ヒール",
        "Mチキ（補足）": "シャカチキ、チキンフィレオ、てりやきチキンに使用",
        "クリスプ（補足）": "マックチキン、チキチーに使用",
    }

# 状態管理
if 'current_item' not in st.session_state:
    st.session_state.current_item = random.choice(list(st.session_state.menu_data.keys()))
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'history' not in st.session_state:
    st.session_state.history = []
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = "クイズ"

# サイドバーでモード切替
st.sidebar.title("設定")
mode = st.sidebar.radio("モード選択", ["クイズで暗記", "一覧を眺める"])

# --- 一覧表示モード ---
if mode == "一覧を眺める":
    st.title("📖 メニュー中身一覧")
    st.write("これを見て完璧に叩き込みましょう！")
    
    # テーブル形式で表示
    items_list = [{"メニュー名": k, "中身": v} for k, v in st.session_state.menu_data.items()]
    st.table(items_list)

# --- クイズモード ---
else:
    st.title("🍔 マックメニュー暗記クイズ")
    
    st.info(f"問題：{st.session_state.current_item}")

    if not st.session_state.show_answer:
        if st.button("答えを見る"):
            st.session_state.show_answer = True
            st.rerun()

    if st.session_state.show_answer:
        st.success(f"答え：{st.session_state.menu_data[st.session_state.current_item]}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("次の問題へ"):
                st.session_state.history.append(st.session_state.current_item)
                st.session_state.current_item = random.choice(list(st.session_state.menu_data.keys()))
                st.session_state.show_answer = False
                st.rerun()
        with col2:
            if len(st.session_state.history) > 0:
                if st.button("一つ前の問題に戻る"):
                    prev_item = st.session_state.history.pop()
                    st.session_state.current_item = prev_item
                    st.session_state.show_answer = False
                    st.rerun()

    st.sidebar.divider()
    st.sidebar.write(f"現在の学習数: {len(st.session_state.history)} 問")
