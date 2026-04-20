import streamlit as st
import json
from app.mcq_generator import generate_mcqs
  
# Page config
st.set_page_config(page_title="MCQ Generator", page_icon="🧠")

# Title
st.title("🧠 MCQ Generator")
st.write("Generate Multiple Choice Questions using AI")

# Inputs
topic = st.text_input("Enter Topic", placeholder="e.g. Machine Learning")
num_questions = st.number_input("Number of Questions", min_value=1, max_value=20, value=5)

# Button
if st.button("Generate MCQs"):
    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:
        with st.spinner("Generating MCQs..."):
            try:
                result = generate_mcqs(topic, num_questions)

                # Convert string → JSON
                mcqs = json.loads(result)

                st.success("MCQs Generated Successfully!")

                # Display MCQs
                for i, mcq in enumerate(mcqs, 1):
                    st.markdown(f"### Q{i}. {mcq['question']}")

                    options = mcq["options"]
                    for idx, option in enumerate(options):
                        st.write(f"{chr(65+idx)}. {option}")

                    st.info(f"✅ Correct Answer: {mcq['answer']}")
                    st.markdown("---")

            except json.JSONDecodeError:
                st.error("❌ Error parsing JSON. Check prompt format.")
                st.write(result)

            except Exception as e:
                st.error(f"❌ Error: {e}")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit + OpenAI 🚀")
            
            
            
            
            
            
            
            
            
            
            
            