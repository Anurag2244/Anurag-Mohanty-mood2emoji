import streamlit as st
import re
from textblob import TextBlob

st.set_page_config(
    page_title="Mood 2 Emoji - Text Mood Detector",
    page_icon = "😊",
    layout="centered"
)

inapropiate_words = {
    'hate', 'stupid', 'idiot', 'dumb', 'ugly', 'kill', 'hurt', 'terrible',
    'awful', 'horrible', 'damn', 'hell', 'sucks', 'bad', 'worst', 'loser'
}

def contain_inapro_words(text):
    text_lower = text.lower()
    words = re.findall(r'\b\w+\b', text_lower)
    return any(bad_words in words for bad_words in inapropiate_words)

def get_mood_analysis(text):
    
    if contain_inapro_words(text):
        return "😐", "Let's keep our language positive and kind!"
    
    cleaned_text = text.strip()
    if len(cleaned_text) < 2:
        return "😐", "Please share a bit more so that I can understand!"
    
    try:
        analysis = TextBlob(cleaned_text)
        polarity = analysis.sentiment.polarity

        if polarity > 0.1:
            return "😃", "Sounds positive and happy!"
        
        elif polarity < -0.1:
            return "😔", "Sounds like you might feeling down"
        
        else:
            return "🙂", "Sounds quite natural"
        
    except Exception as e:
        return "😐", "let's try again with different word"
    
def show_teacher_mode():
    st.markdown('---')
    st.subheader("How Mood2Emoji is working")

    st.markdown("""
        User Input Text -> Safety Check -> If inappropiate let's keep it positive -> TextBlob analysis(Sentiment score [-1.0 to +1.0]) -> Mood Decision [
                Score > 0.1 -> "Happy Mood",
                Score < -0.1 -> "Sad Mood",
                Otherwise -> "Sounds neutral
            ]
""")
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        Sentiment Analysis: Computer understanding emotions in text
        Polarity Score: -1.0(Positive) to +1.0(Negative)
        TextBlob: Pretrained model that knows word emotions
        Tokenization: Breaking sentences into individual words
""")
        
    with col2:
        st.markdown("""
        -Understand basic AI text processing
        -Learn about digital communication
        -Practice identifying emotions in text
        -Develop computational thinking skills
""")
        
    st.markdown("Example Analysis")
    example_text = "I love learning about computers"
    if st.button("Analyze Example Sentence"):
        emoji, exaplanation = get_mood_analysis(example_text)
        analysis = TextBlob(example_text)

        st.success(f"Sentence: {example_text}")
        st.info(f"Result {emoji}{exaplanation}")
        st.metric("Sentiment Score", f"{analysis.sentiment.polarity:.2f}")

def main():

    st.title("Mood 2 Emoji Text detector")
    st.markdown("""
    Share a sentence and I'll detect the mood!
    Perfect for students learning about computers and emotions
    """)

    teacher_mode = st.checkbox("Enable Teacher Mode", help="Show how app is working internally")

    st.markdown("Enter your text")
    user_input = st.text_area(
        "Type a sentence here:",
        placeholder="Example: I had an amazing AI session with Codingal!",
        height = 100,
        label_visibility="collapsed"
    )

    if st.button("Analyze Mood", type="primary", use_container_width=True):
        if user_input and user_input.strip():
            with st.spinner("Analyzing your text"):
                emoji, explanation = get_mood_analysis(user_input.strip())

            st.markdown("---")
            st.markdown(f"{emoji} {explanation}")

            if show_teacher_mode:
                try:
                    analysis = TextBlob(user_input.strip())
                    polarity = analysis.sentiment.analysis

                    st.info(f"Sentiment Score: {polarity:.3f}")

                    if polarity > 0.1:
                        st.success("Positive emotion detected")
                    elif polarity < -0.1:
                        st.warning("Negative emotion detected")
                    else:
                        st.info("Neutral emotion detected")

                except Exception:
                    st.info("Analysis completed")

            else:
                st.warning("Please enter some text to analyze")

    if teacher_mode:
        show_teacher_mode()

    st.markdown("---")
    st.markdown("Learning Corner")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        Try These Examples:
        "I'm so excited for the weekend!"
        "I don't understand this homework" 
        "The sky is blue today"
        "I made a new friend"
""")
        
    with col2:
        st.markdown("""
        What You're Learning:
        How computers understand language
        Emotional intelligence
        Positive communication
        Basic AI concepts
        """)

    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>"
        "Mood2Emoji - Teaching computers about human emotions"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()