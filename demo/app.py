
import gradio as gr
from gradio_sortablecheckboxgroup import SortableCheckboxGroup


example = SortableCheckboxGroup().example_value()

demo = gr.Interface(
    lambda x:x,
    SortableCheckboxGroup(),  # interactive version of your component
    SortableCheckboxGroup(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()
