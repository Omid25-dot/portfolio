import streamlit as st
import random
import requests
from datetime import date
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="Omid Merati | My Portfolio",
    page_icon="💻",
    layout="centered"
)




st.markdown("""
<style>
    .main {
        background-color:#f4f6f8;
    }
    h1, h2, h3 {
        color:#003366;
    }
</style>
""", unsafe_allow_html=True)




def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottie("https://assets2.lottiefiles.com/packages/lf20_1pxqjqps.json")


col1, col2 = st.columns([2, 1])
with col1:
    st.title("👋 Hi, I'm Omid Merati")
    st.write("""
    I’m an aspiring Python developer who’s been building up my skills through hands on projects and problem-solving.
I love finding smart, practical ways to use tech to make life easier whether that’s through automation or AI.
Right now, I’m working on a **Smart Fridge AI Assistant** that uses a Raspberry Pi Camera to recognise what’s inside a fridge and suggests meals based on the items that are in the fridge.
This page gives a quick, interactive look at some of the things I’ve worked on and why I think I’d be a great fit for JP Morgan.
    """)
with col2:
    st_lottie(lottie_coding, height=180, key="coding")


fun_facts = [
"🤖 I’m working on a Smart Fridge AI Assistant that uses a Raspberry Pi Camera to spot what’s in the fridge and suggest meals based on it.",
    "🎄 I built a puzzle solving algorithm on Advent of Code that helped 'Elvish historians save Christmas' a fun project that tested my problem-solving and creativity.",
    "🕵️‍♂️ You’ll usually find me deep in PyCharm, trying to make my code behave.",
    "💻 I built a little script that sorted all my files on my Mac and deleted duplicates."
]
if st.button("🎲 Click for a Random Fun Fact"):
    st.info(random.choice(fun_facts))


topic = st.selectbox(
    "Pick a topic to explore:",
    ["Technical Skills", "Projects", "Certifications", "Hobbies"]
)

if topic == "Technical Skills":
    st.write("**Programming Languages:** Python (proficient)")
    st.write("**Version Control:** Git & GitHub")
    st.write("**Core Strengths:** Problem solving, algorithmic thinking, and building practical solutions.")
    st.progress(80)

elif topic == "Projects":
    st.write("• **Smart Fridge AI Assistant** – I'm currently working on a Ai Assistant which runs on python code through a Raspberry Pi and a camera")
    st.write("• **Alien Invasion Game** – Python arcade game built with Pygame featuring movement, collision detection, and scoring.")
    st.write("• **Save Christmas Puzzle Solver** – Algorithmic project to reconcile lists of location IDs and optimise pairings.")

elif topic == "Certifications":
    st.write("• **Machine Learning with Python – FreeCodeCamp**")
    st.write("• **Git and GitHub – Udemy**")

elif topic == "Hobbies":
    st.write("• Muay Thai and boxing building discipline and focus through training.")
    st.write("• Fitness and learning about AI, automation, and emerging tech.")
    st.write("• Exploring how code can make everyday tasks smarter and simpler.")


with st.expander("💻 My Projects in Detail"):
    st.write("- **Smart Fridge AI Assistant** – currently in development, uses a Raspberry Pi Camera and image recognition to detect fridge items, it suggests recipes and tracks food coming in and out of your fride.")
    st.write("- **Alien Invasion Game** – Python arcade style project where players defend against alien ships; implemented movement, collision detection, and scoring.")
    st.write("- **Save Christmas: Location ID Puzzle Solver** – solved a logistics-based matching puzzle using algorithmic pairing and distance calculation.")

with st.expander("🎓 Certifications"):
    st.write("• **Machine Learning with Python – FreeCodeCamp**")
    st.write("• **Git and GitHub – Udemy**")




st.header("🔗 Find Me Online")
st.markdown("[GitHub](https://github.com/Omid25-dot)  |  [LinkedIn](https://www.linkedin.com/in/omid-merati)")

st.caption(f"Last updated · {date.today().strftime('%B %Y')}")


