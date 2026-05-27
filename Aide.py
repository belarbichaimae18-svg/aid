# =========================================================
# APPLICATION STREAMLIT - CARTE DE VŒUX AÏD AL-ADHA
# Thème : élégante, féminine, style ingénieure
# Exécution :
#   1) pip install streamlit
#   2) streamlit run app.py
# =========================================================

import streamlit as st
from datetime import datetime

# =========================
# CONFIGURATION PAGE
# =========================
st.set_page_config(
    page_title="تهنئة عيد الأضحى",
    page_icon="🌙",
    layout="centered"
)

# =========================
# STYLE CSS
# =========================
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#fff5f5,#ffeaea,#fff0f6);
    font-family: 'Arial';
}

.main-box{
    background: rgba(255,255,255,0.88);
    padding: 45px;
    border-radius: 30px;
    text-align:center;
    box-shadow: 0 10px 40px rgba(0,0,0,0.15);
    border: 2px solid #ffd6e7;
}

.title{
    font-size:48px;
    color:#d63384;
    font-weight:bold;
}

.subtitle{
    font-size:22px;
    color:#6c757d;
    margin-bottom:25px;
}

.message{
    font-size:28px;
    color:#444;
    line-height:2.2;
    direction: rtl;
}

.hearts{
    font-size:35px;
    animation: pulse 1.5s infinite;
}

.footer{
    margin-top:30px;
    font-size:20px;
    color:#999;
}

.signature{
    margin-top:25px;
    font-size:24px;
    color:#d63384;
    font-weight:bold;
    letter-spacing:1px;
}

@keyframes pulse{
    0%{transform:scale(1);}
    50%{transform:scale(1.1);}
    100%{transform:scale(1);}
}

.gold-line{
    height:4px;
    background: linear-gradient(to right,#f7d794,#f3a683,#f8c291);
    border-radius:20px;
    margin:25px 0;
}

</style>
""", unsafe_allow_html=True)

# =========================
# CONTENU
# =========================
st.markdown("""
<div class="main-box">

<div class="hearts">
💖 🌸 ✨ 🌙 🕌 ✨ 🌸 💖
</div>

<div class="title">
عيد أضحى مبارك
</div>

<div class="gold-line"></div>

<div class="message">

بمناسبة عيد الأضحى المبارك 🌙✨<br><br>

أتقدم بأصدق عبارات التهاني والتبريكات،<br>
راجيةً من الله أن يجعل هذا العيد مليئًا<br>
بالفرح، والطمأنينة 🤍<br><br>

كل عام وأنتم بخير،<br>
🌸<br><br>

مهندسة بأحلام كبيرة وقلب مليء بالنور 💖

</div>

<div class="signature">
CHAIMAE BELARBI ✨
</div>

<div class="gold-line"></div>

<div class="hearts">
🌷 💕 🌙 ✨  ✨ 🌙 💕 🌷
</div>

<div class="footer">
Eid Al-Adha Mubarak ✨
</div>

</div>
""", unsafe_allow_html=True)

# =========================
# BOUTON
# =========================
if st.button("🎉 اضغط لرؤية مفاجأة"):
    st.balloons()
    st.success("✨ عيد سعيد مليء بالأفراح والنجاح ✨")