import gradio as gr
from transformers import pipeline

# Load the summarization model from Hugging Face
summarizer = pipeline("summarization")

# Define the summarization function
def summarize_text(input_text):
    summarized = summarizer(input_text, max_length=100, min_length=30, do_sample=False)[0]
    return summarized["summary_text"]

# Create the Gradio interface
iface = gr.Interface(
    fn=summarize_text,
    inputs=gr.inputs.Textbox(lines=10, placeholder="Enter text to summarize..."),
    outputs=gr.outputs.Textbox(placeholder="Summary will appear here...")
)

# Run the interface
iface.launch()
