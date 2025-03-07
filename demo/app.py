#!/usr/bin/env python3

import gradio as gr
import sys
import os

# Adding project path to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.gradio_sortablecheckboxgroup import SortableCheckboxGroup

# Simple demo
with gr.Blocks() as demo:
    
    with gr.Group():
        gr.Markdown("## Simple Example")
        checkbox_group = SortableCheckboxGroup(
            choices=["Option 1", "Option 2", "Option 3", "Option 4"], 
            value=["Option 1", "Option 3"],
            label="Sortable Options",
            sortable=True
        )
        
        output = gr.Textbox(label="Result", value="Selected options with priority order: ['Option 1', 'Option 3']")
        
        def on_change(value):
            return f"Selected options with priority order: {value}"
        
        checkbox_group.change(on_change, checkbox_group, output)
    
    with gr.Group():
        gr.Markdown("## Keyboard Shortcuts Guide")
        gr.Markdown("""
        - **Drag and Drop**: Drag items with mouse and drop them in the desired position
        - **Arrow Keys**: Click on an item and use ↑ and ↓ keys to move it
        - **Arrow Buttons**: Use the ↑ and ↓ buttons next to each item to move it
        - **Enter or Space Key**: Use to select and move an item
        """)

if __name__ == "__main__":
    demo.launch() 