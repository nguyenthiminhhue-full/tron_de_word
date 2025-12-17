# APP HỌC TẬP SỐ TOÁN 10 – GDPT 2018 (KẾT NỐI TRI THỨC VỚI CUỘC SỐNG)
# Công nghệ: Streamlit + GeoGebra + Google Sheet
# Mục tiêu: Học tập kiến tạo – phát triển năng lực số – đánh giá thường xuyên

import streamlit as st
import random
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# ================== CẤU HÌNH TRANG ==================
st.set_page_config(
    page_title="📘 Học tập số Toán 10 – GDPT 2018",
    page_icon="📐",
    layout="wide"
)

# ================== KẾT NỐI GOOGLE SHEET ==================
# Thầy/Cô tạo Google Sheet và Service Account trước

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# credentials = Credentials.from_service_account_file(
#     "credentials.json", scopes=SCOPES
# )
# gc = gspread.authorize(credentials)
# sheet = gc.open("DanhGiaThuongXuyen_Toan10").sheet1

# ================== DỮ LIỆU LÝ THUYẾT (GDPT 2018) ==================

LY_THUYET = {
    "Mệnh đề – Tập hợp": {
        "muc_tieu": "Hình thành tư duy logic, năng lực mô hình hóa toán học",
        "noi_dung": """
        🔹 **Mệnh đề**: khẳng định đúng hoặc sai.
        🔹 **Tập hợp**: nhóm các đối tượng xác định.
        📌 Liên hệ thực tiễn: phân loại học sinh theo CLB.
        """
    },
    "Hàm số bậc nhất": {
        "muc_tieu": "Phát triển năng lực sử dụng công cụ toán học và CNTT",
        "noi_dung": """
        🔹 Dạng: y = ax + b (a ≠ 0)
        🔹 Đồ thị: đường thẳng.
        📌 Ứng dụng: chi phí – quãng đường – thời gian.
        """
    }
}

# ================== CÂU HỎI TƯƠNG TÁC ==================

CAU_HOI = [
    {
        "question": "Đồ thị hàm số y = 2x + 1 có dạng gì?",
        "options": ["Đường thẳng", "Parabol", "Đường tròn", "Elip"],
        "answer": "Đường thẳng",
        "nang_luc": "Mô hình hóa toán học"
    }
]

# ================== MENU ==================
st.sidebar.title("📚 Chức năng")
menu = st.sidebar.radio(
    "",
    [
        "📖 Lý thuyết (GDPT 2018)",
        "📐 GeoGebra trực quan",
        "🎮 Trò chơi Toán học",
        "📝 Luyện đề",
        "📊 Điểm danh – Đánh giá"
    ]
)

# ================== LÝ THUYẾT ==================
if menu == "📖 Lý thuyết (GDPT 2018)":
    st.title("📖 Lý thuyết Toán 10 – GDPT 2018")
    bai = st.selectbox("Chọn bài học", list(LY_THUYET.keys()))
    st.info(f"🎯 Mục tiêu năng lực: {LY_THUYET[bai]['muc_tieu']}")
    st.markdown(LY_THUYET[bai]["noi_dung"])

# ================== GEOGEBRA ==================
elif menu == "📐 GeoGebra trực quan":
    st.title("📐 Khám phá Toán học với GeoGebra")
    st.markdown("Tương tác trực tiếp để **tự khám phá kiến thức**")
    st.components.v1.iframe(
        "https://www.geogebra.org/material/iframe/id/mk8k9w8f/width/800/height/500/border/888888",
        height=520
    )

# ================== TRÒ CHƠI ==================
elif menu == "🎮 Trò chơi Toán học":
    st.title("🎮 Trò chơi – học mà chơi")
    cau = random.choice(CAU_HOI)
    st.subheader(cau["question"])
    choice = st.radio("Chọn đáp án", cau["options"])
    if st.button("✅ Kiểm tra"):
        if choice == cau["answer"]:
            st.success("🎉 Chính xác! Bạn đang phát triển năng lực: " + cau["nang_luc"])
        else:
            st.error("❌ Chưa đúng, hãy thử lại!")

# ================== LUYỆN ĐỀ ==================
elif menu == "📝 Luyện đề":
    st.title("📝 Luyện đề – Đánh giá thường xuyên")
    score = 0
    for i, cau in enumerate(CAU_HOI, 1):
        st.markdown(f"**Câu {i}: {cau['question']}**")
        ans = st.radio("", cau["options"], key=i)
        if ans == cau["answer"]:
            score += 1
    if st.button("📤 Nộp bài"):
        st.success(f"🎯 Kết quả: {score}/{len(CAU_HOI)}")

# ================== ĐIỂM DANH – ĐÁNH GIÁ ==================
elif menu == "📊 Điểm danh – Đánh giá":
    st.title("📊 Đánh giá thường xuyên (GDPT 2018)")
    ten = st.text_input("Họ tên học sinh")
    lop = st.text_input("Lớp")
    muc_do = st.slider("Mức độ hiểu bài", 1, 5, 3)
    if st.button("📥 Ghi nhận"):
        # sheet.append_row([ten, lop, muc_do])
        st.success("✅ Đã lưu đánh giá (mô phỏng)")

# ================== FOOTER ==================
st.markdown("---")
st.caption("🚀 App học tập số Toán 10 | Học tập kiến tạo | Phát triển năng lực số | GDPT 2018")
