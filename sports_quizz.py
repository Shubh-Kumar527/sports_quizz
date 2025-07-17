import streamlit as st
import random
from google import generativeai as genai

# Configure Gemini
GEMINI_API_KEY = 'AIzaSyCQGt3DkRf6BrkVV9HGWmtl9JrjdI6gEtA'
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('models/gemini-1.5-flash')

# App title
st.title("Welcome, Challenger")

st.subheader("Only the Sharpest Minds Make It to the Hall of Fame!")

# Question bank
question_list = [
    "Often played in doubles or singles, this fast-paced indoor sport uses a feathered projectile instead of a ball. It requires quick reflexes and is a staple in many Commonwealth Games. What sport is this?",
    "Known as 'the beautiful game,' this globally celebrated sport is played by two teams of eleven, but only the goalkeeper is allowed to use their hands. What is this sport commonly called in the United States?",
    "This high-speed, full-contact sport is played on a rink, involves gliding on skates, and features a black rubber puck. It’s a national obsession in Canada. Name the sport.",
    "In this precision-based Olympic discipline, competitors must account for wind and distance as they launch projectiles from a curved or compound tool. What sport is this?",
    "With origins tracing back to 19th-century England, this racquet sport features a grass, clay, or hard court and four Grand Slam tournaments annually. What sport is being described?",
    "This physically intense sport features touchdowns, field goals, and downs, and is played on a 100-yard field. What sport is it, especially popular on Thanksgiving in the U.S.?",
    "Encompassing events like hurdles, javelin, and long jump, this athletic category has its roots in ancient Greek competition. What is the general term for these combined events?",
    "With a court measuring 94 feet long, this sport involves dribbling, shooting, and defensive blocks, and features a three-point arc. What game is this?",
    "Originating in the late 19th century, this sport is known for spikes, blocks, and digs, and is played on both hardwood and sandy surfaces. What sport is it?",
    "Sometimes called 'the sport of kings,' this horseback team game requires hitting a ball into a goal using a long mallet, while riding at high speeds. What is this sport?"

]

# Initialize state
if 'asked_questions' not in st.session_state:
    st.session_state.asked_questions = []

if 'question' not in st.session_state or st.session_state.question == "":
    def pick_question():
        remaining = [q for q in question_list if q not in st.session_state.asked_questions]
        if remaining:
            q = random.choice(remaining)
            st.session_state.asked_questions.append(q)
            return q
        return None

    st.session_state.question = pick_question()

if 'feedback' not in st.session_state:
    st.session_state.feedback = ""

# Show current question
if st.session_state.question:
    st.subheader("📘 Question:")
    st.write(st.session_state.question)

    a = st.text_input("✍️ Your Answer:")

    if st.button("Check Answer") and a:
        prompt = f"""
You're a friendly and supportive tutor helping a parent answer some sports quizz
They may not know the full answer — and that's perfectly okay!

Please:
- Gently assess their answer.
- If it's close or partially right, encourage them.
- Add missing details in a simple way.
- Always use a kind and positive tone.

Question: {st.session_state.question}
Answer: {a}

What feedback would you give?
"""
        response = model.generate_content(prompt)
        st.session_state.feedback = response.text

    if st.session_state.feedback:
        st.write("### 🤖 Gemini's Feedback:")
        st.write(st.session_state.feedback)

    if st.button("🔄 Next Question"):
        # Clear old feedback and get a new question
        st.session_state.feedback = ""
        remaining = [q for q in question_list if q not in st.session_state.asked_questions]
        if remaining:
            st.session_state.question = random.choice(remaining)
            st.session_state.asked_questions.append(st.session_state.question)
        else:
            st.success("🎉 You've answered all the questions!")
            if st.button("Restart Quiz"):
                st.session_state.asked_questions = []
                st.session_state.question = ""
                st.session_state.feedback = ""

else:
    st.success("🎉 You've completed all questions!")
    if st.button("Restart Quiz"):
        st.session_state.asked_questions = []
        st.session_state.question = ""
        st.session_state.feedback = ""
