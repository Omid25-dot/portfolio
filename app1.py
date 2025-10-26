import streamlit as st
import random
import requests
from datetime import date
from streamlit_lottie import st_lottie

# -------------------------------
# PAGE SETUP
# -------------------------------
st.set_page_config(
    page_title="Omid Merati | JP Morgan Application",
    page_icon="💻",
    layout="centered"
)

# -------------------------------
# STYLE (TRANSPARENT + CLEAN)
# -------------------------------
st.markdown("""
<style>
/* Make entire app background transparent */
[data-testid="stAppViewContainer"] {
    background-color: rgba(0, 0, 0, 0) !important;
    background: transparent !important;
}

/* Make header transparent */
[data-testid="stHeader"] {
    background: transparent !important;
}

/* Optional: remove padding if you want full-width feel */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Headings and text colours (for readability) */
h1, h2, h3, p, li {
    color: #003366;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------
# LOAD ANIMATION
# -------------------------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottie("https://assets2.lottiefiles.com/packages/lf20_1pxqjqps.json")

# -------------------------------
# HEADER
# -------------------------------
col1, col2 = st.columns([2, 1])
with col1:
    st.title("👋 Hi, I'm Omid Merati")
    st.subheader("Applicant – JP Morgan 2026 Software Engineering Apprenticeship (Glasgow)")
    st.write("""
    I’m an aspiring Python developer with a basic foundation in coding, problem-solving, and version control.  
    I’m passionate about using technology to solve real-world problems and currently working on a **Smart Fridge AI Assistant** that recognises fridge contents using a Raspberry Pi Camera.  
    This page gives a short, interactive overview of my projects and why I’d be a great fit for JP Morgan.
    """)
with col2:
    st_lottie(lottie_coding, height=180, key="coding")

# -------------------------------
# RANDOM FUN FACT
# -------------------------------
fun_facts = [
    "I'm building a Smart Fridge AI Assistant that recognises items and suggests meals using computer vision.",
    "I created an algorithmic puzzle solver that helped Elvish historians 'save Christmas' 🎄 — a fun data project mixing logic and creativity.",
    "I enjoy debugging — it’s like detective work that rewards persistence and curiosity.",
    "I once automated a repetitive task that saved hours weekly — that’s when I realised how powerful simple code can be."
]
if st.button("🎲 Click for a Random Fun Fact"):
    st.info(random.choice(fun_facts))

# -------------------------------
# DROPDOWN / SELECT BOX
# -------------------------------
topic = st.selectbox(
    "Pick a topic to explore:",
    ["Technical Skills", "Projects", "Certifications", "Hobbies"]
)

if topic == "Technical Skills":
    st.write("**Programming Languages:** Python (proficient)")
    st.write("**Version Control:** Git & GitHub")
    st.write("**Core Strengths:** Problem-solving, algorithmic thinking, and building practical solutions.")
    st.progress(80)

elif topic == "Projects":
    st.write("• **Smart Fridge AI Assistant** – Raspberry Pi & OpenCV-based system for food recognition and recipe suggestions.")
    st.write("• **Alien Invasion Game** – Python arcade game built with Pygame featuring movement, collision detection, and scoring.")
    st.write("• **Save Christmas Puzzle Solver** – Algorithmic project to reconcile lists of location IDs and optimise pairings.")

elif topic == "Certifications":
    st.write("• **Machine Learning with Python – FreeCodeCamp**")
    st.write("• **Git and GitHub – Udemy**")

elif topic == "Hobbies":
    st.write("• Muay Thai and boxing — building discipline and focus through training.")
    st.write("• Fitness and learning about AI, automation, and emerging tech.")
    st.write("• Exploring how code can make everyday tasks smarter and simpler.")

# -------------------------------
# EXPANDABLE SECTIONS
# -------------------------------
with st.expander("💻 My Projects in Detail"):
    st.write("- **Smart Fridge AI Assistant** – currently in development, uses a Raspberry Pi Camera and image recognition to detect fridge items and suggest recipes.")
    st.write("- **Alien Invasion Game** – Python arcade-style project where players defend against alien ships; implemented movement, collision detection, and scoring.")
    st.write("- **Save Christmas: Location ID Puzzle Solver** – solved a logistics-based matching puzzle using algorithmic pairing and distance calculation.")

with st.expander("🎓 Certifications"):
    st.write("• **Machine Learning with Python – FreeCodeCamp**")
    st.write("• **Git and GitHub – Udemy**")

# -------------------------------
# WHY JP MORGAN
# -------------------------------
st.header("💬 Why JP Morgan?")
st.write("""
JP Morgan’s Glasgow hub builds the technology that powers global finance.  
I’m drawn to environments where small, elegant pieces of code can have huge real-world impact.  
The apprenticeship model fits perfectly with how I learn best — through collaboration, feedback, and building things that matter.  
I’m eager to contribute to that culture while continuing to grow as a developer.
""")

# -------------------------------
# LINKS
# -------------------------------
st.header("🔗 Find Me Online")
st.markdown("[GitHub](https://github.com/Omid25-dot)  |  [LinkedIn](www.linkedin.com/in/omid-merati)")

st.caption(f"Last updated · {date.today().strftime('%B %Y')}")
