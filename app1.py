import streamlit as st
import random
import requests
from datetime import date
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Omid Merati | Developer Portfolio",
    page_icon="💻",
    layout="wide"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #020617 100%);
        color: white;
    }

    h1, h2, h3 {
        color: white;
    }

    .hero-box {
        padding: 3rem;
        border-radius: 25px;
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin-bottom: 2rem;
    }

    .card {
        padding: 1.5rem;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.12);
        margin-bottom: 1rem;
    }

    .highlight {
        color: #38bdf8;
        font-weight: 700;
    }

    .small-text {
        color: #cbd5e1;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)


def load_lottie(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None


lottie_coding = load_lottie("https://assets2.lottiefiles.com/packages/lf20_1pxqjqps.json")


# HERO SECTION
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="hero-box">
        <h1>Hi, I'm Omid Merati 👋</h1>
        <p class="small-text">
        I’m an aspiring Python developer building practical projects in automation, AI and problem-solving.
        I enjoy turning ideas into working tools — from smart assistants to games and productivity scripts.
        </p>
        <h3><span class="highlight">Currently building:</span> Smart Fridge AI Assistant</h3>
    </div>
    """, unsafe_allow_html=True)

with col2:
    if lottie_coding:
        st_lottie(lottie_coding, height=260, key="coding")


# QUICK STATS
st.subheader("🚀 What I’m focused on")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>Python</h3>
        <p>Building practical apps, scripts and problem-solving projects.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>AI & Automation</h3>
        <p>Exploring how AI can make everyday tasks smarter and easier.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>Web Development</h3>
        <p>Learning HTML, CSS and JavaScript to build better user experiences.</p>
    </div>
    """, unsafe_allow_html=True)


# INTERACTIVE PROJECT SECTION
st.subheader("🧠 Explore My Projects")

project = st.selectbox(
    "Choose a project:",
    [
        "Smart Fridge AI Assistant",
        "Alien Invasion Game",
        "Save Christmas Puzzle Solver",
        "Mac File Organiser"
    ]
)

if project == "Smart Fridge AI Assistant":
    st.success("A Raspberry Pi + camera-based AI assistant that recognises fridge items and suggests meals.")
    st.write("**Tech used:** Python, Raspberry Pi, image recognition, automation")

elif project == "Alien Invasion Game":
    st.success("A Python arcade game built with Pygame.")
    st.write("**Features:** Movement, collision detection, scoring system, game loop")

elif project == "Save Christmas Puzzle Solver":
    st.success("An algorithmic puzzle project using pairing, comparison and distance calculations.")
    st.write("**Focus:** Problem-solving, logic, data handling")

elif project == "Mac File Organiser":
    st.success("A script that organises files and removes duplicates.")
    st.write("**Focus:** Automation, file handling, productivity")


# FUN FACT BUTTON
fun_facts = [
    "🤖 I’m building a Smart Fridge AI Assistant using a Raspberry Pi Camera.",
    "🎮 I built an Alien Invasion game in Python.",
    "🧹 I created a script to organise files on my Mac.",
    "🧠 I enjoy solving algorithmic problems and turning ideas into working projects."
]

if st.button("🎲 Show me a random fact"):
    st.info(random.choice(fun_facts))


# SKILLS
st.subheader("🛠 Skills")

col1, col2 = st.columns(2)

with col1:
    st.write("**Programming**")
    st.progress(80)
    st.write("Python, Git, GitHub, problem-solving")

with col2:
    st.write("**Currently Learning**")
    st.progress(45)
    st.write("HTML, CSS, JavaScript, frontend design")


# CONTACT
st.subheader("🔗 Find Me Online")

st.markdown("""
[GitHub](https://github.com/Omid25-dot)  
[LinkedIn](https://www.linkedin.com/in/omid-merati)
""")

st.caption(f"Last updated · {date.today().strftime('%B %Y')}")


