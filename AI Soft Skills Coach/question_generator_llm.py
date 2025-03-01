from transformers import AutoModelForCausalLM, AutoTokenizer
import streamlit as st

@st.cache_resource
def generate_dynamic_question_and_answer(domain, experience_level):
    # Load LLaMA model and tokenizer
    model_name = "meta-llama/Llama-2-7b-chat-hf"
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Define the prompt
    prompt = f"Generate an interview question and ideal answer for a {experience_level} candidate in the {domain} domain."

    # Encode the prompt for the model
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate the output
    output = model.generate(
        input_ids,
        max_length=100,
        temperature=0.8,
        num_return_sequences=1,  # Generate one sequence
        top_p=1,
        do_sample=True  # Enable sampling
    )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(generated_text)

    if '\n' in generated_text:
        question, ideal_answer = generated_text.split('\n', 1)
    else:
        question = generated_text
        ideal_answer = "No answer generated."

    return question.strip(), ideal_answer.strip()
