import gradio as gr
from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text):
    summarized = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]
    return summarized["summary_text"]

with gr.Interface(summarize_text, 
                  inputs=gr.inputs.Textbox(lines=10, placeholder="Enter text to summarize..."),
                  outputs=gr.outputs.Textbox(placeholder="Summary will appear here...")) as iface:
    iface.launch()
