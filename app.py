from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]['summary_text']
    return summary

with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder="Enter text block to summarize here...", lines=4)
    interface = gr.Interface(fn=predict, inputs=textbox, outputs="text")
    demo.add(interface, "Summarizer", "Summarize text blocks with HuggingFace Transformers")
    
demo.launch()