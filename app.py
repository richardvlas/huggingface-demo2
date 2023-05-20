from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]['summary_text']
    return summary

with gr.Blocks() as demo:
    textbox = gr.inputs.Textbox(lines=5, label="Input Text")
    label = gr.outputs.Textbox(label="Output Summary")
    gr.Interface(fn=predict, inputs=textbox, outputs=label, title="Summarizer", description="Summarize your text!").launch()

# Path: Dockerfile

