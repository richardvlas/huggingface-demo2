import gradio as gr
from transformers import pipeline

# Load the text summarization pipeline
summarizer = pipeline("summarization", model="EleutherAI/gpt-j-6B")

def summarize_text(input_text):
    # Use the summarization pipeline to generate a summary
    summary = summarizer(input_text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Create the Gradio interface
iface = gr.Interface(fn=summarize_text, 
                     inputs="text", 
                     outputs="text", 
                     title="Text Summarization", 
                     description="Enter some text and get a summary of it.")

iface.launch()
