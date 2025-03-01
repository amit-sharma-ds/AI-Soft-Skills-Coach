from questions_generator import generate_dynamic_question_and_answer
from text_processing import analyze_text, evaluate_response
from voice_processing import analyze_speech

import streamlit as st

def reset_session_state():
    st.session_state.current_question = None
    st.session_state.ideal_answer = None
    st.session_state.user_response = ""

st.sidebar.header("Profile Information")
experience_level = st.sidebar.selectbox("Experience Level", ["Fresher", "Experienced"], on_change=reset_session_state)
domain = st.sidebar.selectbox("Domain", ["General", "Technical", "Managerial"], on_change=reset_session_state)

st.title("AI Soft Skills Coach")
st.subheader("Mock Interview")

if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "ideal_answer" not in st.session_state:
    st.session_state.ideal_answer = None
if "user_response" not in st.session_state:
    st.session_state.user_response = ""


if st.button("Generate Question"):
    question, ideal_answer = generate_dynamic_question_and_answer(domain, experience_level)
    if question and ideal_answer:
        st.session_state.current_question = question
        st.session_state.ideal_answer = ideal_answer
        st.session_state.user_response = ""

if st.session_state.current_question:
    st.write(f"**Question:** {st.session_state.current_question}")

    # Streamlit text_area
    user_response = st.text_area(
        "Type Your Answer:",
        value=st.session_state.get("user_response", ""),
        key="user_response",
        max_chars=200
    )

    st.markdown("""
        <style>
        textarea {
            -webkit-user-modify: read-write-plaintext-only !important;
            autocomplete: off !important;
            width: 80%;
            height: 150px;
            font-size: 16px;
        }
        </style>

        <button id="start-btn" style="position: absolute; bottom: 10; right: 0; font-size: 20px;">🎙️</button>
        
        <script>
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            const recognition = new SpeechRecognition();
            recognition.lang = 'en-US';
            recognition.continuous = true;

            const textArea = document.getElementById('custom-text-area');
            const startBtn = document.getElementById('start-btn');

            startBtn.onclick = () => {
                recognition.start();
                startBtn.innerText = "🎙️ Listening...";
                startBtn.style.backgroundColor = "red";
            };

            recognition.onresult = (event) => {
                let transcript = '';
                for (let i = event.resultIndex; i < event.results.length; ++i) {
                    if (event.results[i].isFinal) {
                        transcript += event.results[i][0].transcript + " ";
                    }
                }
                textArea.value = transcript;
            };

            recognition.onend = () => {
                startBtn.innerText = "🎙️ Start Speech Recognition";
                startBtn.style.backgroundColor = "lightblue";
            };

            recognition.onerror = (event) => {
                console.error("Speech Recognition Error: ", event.error);
            };
        </script>

    """, unsafe_allow_html=True)

    if st.button("Analyze Response"):
        st.subheader("Feedback:")
        with st.spinner("Evaluating your response, please wait..."):
            user_response = st.session_state.user_response.strip()

            if user_response:
                ideal_answer = st.session_state.ideal_answer
                text_analysis = analyze_text(user_response, [ideal_answer])
                for comment in text_analysis['feedback']:
                    st.write(f"- {comment}")
                
                                

                if text_analysis['relevance'] >= 0.75:
                    st.write("Good job! Your answer is similar to the expected response.")
                else:
                    st.write(f"For relevant answer please go through this: {ideal_answer}")
        
            else:
                st.warning("Please provide a response for analysis.")
else:
    st.info("Click 'Generate Question'.")
