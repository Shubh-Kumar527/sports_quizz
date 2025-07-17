import streamlit as st
import random
from google import generativeai as genai

# Configure Gemini API key
GEMINI_API_KEY = 'AIzaSyCQGt3DkRf6BrkVV9HGWmtl9JrjdI6gEtA'
genai.configure(api_key=GEMINI_API_KEY)

# Initialize model
model = genai.GenerativeModel('models/gemini-1.5-flash')

# App title
st.title('🇫🇷 Welcome to the French Quiz 🇫🇷')

# Question list
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

# Only select a random question once
if 'question' not in st.session_state:
    st.session_state.question = random.choice(question_list)

# Show question
st.subheader("Question:")
st.write(st.session_state.question)

# User input
a = st.text_input('Enter your answer:')

# Check answer and display feedback
if a:
    prompt = f"Please check and evaluate this answer:\nQuestion: {st.session_state.question}\nAnswer: {a}\nIs it correct? Provide feedback."
    response = model.generate_content(prompt)
    st.write("### Feedback:")
    st.write(response.text)
