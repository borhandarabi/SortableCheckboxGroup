
import gradio as gr
from app import demo as app
import os

_docs = {'SortableCheckboxGroup': {'description': 'Creates a set of checkboxes. Can be used as an input to pass a set of values to a function or as an output to display values, a subset of which are selected.', 'members': {'__init__': {'choices': {'type': 'Sequence[\n        str | int | float | tuple[str, str | int | float]\n    ]\n    | None', 'default': 'None', 'description': 'A list of string or numeric options to select from. An option can also be a tuple of the form (name, value), where name is the displayed name of the checkbox button and value is the value to be passed to the function, or returned by the function.'}, 'value': {'type': 'Sequence[str | float | int]\n    | str\n    | float\n    | int\n    | Callable\n    | None', 'default': 'None', 'description': 'Default selected list of options. If a single choice is selected, it can be passed in as a string or numeric type. If a function is provided, the function will be called each time the app loads to set the initial value of this component.'}, 'type': {'type': 'Literal["value", "index"]', 'default': '"value"', 'description': 'Type of value to be returned by component. "value" returns the list of strings of the choices selected, "index" returns the list of indices of the choices selected.'}, 'sortable': {'type': 'bool', 'default': 'False', 'description': 'If True, allows reordering of selected items to set priority.'}, 'show_order': {'type': 'bool', 'default': 'False', 'description': 'If True, shows the priority order section by default.'}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'the label for this component, displayed above the component if `show_label` is `True` and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component corresponds to.'}, 'info': {'type': 'str | None', 'default': 'None', 'description': 'additional component description, appears below the label in smaller font. Supports markdown / HTML syntax.'}, 'every': {'type': 'Timer | float | None', 'default': 'None', 'description': 'Continously calls `value` to recalculate it if `value` is a function (has no effect otherwise). Can provide a Timer whose tick resets `value`, or a float that provides the regular interval for the reset Timer.'}, 'inputs': {'type': 'Component | Sequence[Component] | set[Component] | None', 'default': 'None', 'description': 'Components that are used as inputs to calculate `value` if `value` is a function (has no effect otherwise). `value` is recalculated any time the inputs change.'}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'If True, will display label.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container - providing some extra padding around the border.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'Relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'Minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': 'If True, choices in this checkbox group will be checkable; if False, checking will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'key': {'type': 'int | str | None', 'default': 'None', 'description': 'if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.'}}, 'postprocess': {'value': {'type': 'list[str | int | float] | str | int | float | None', 'description': 'Expects a `list[str | int | float]` of values or a single `str | int | float` value, the checkboxes with these values are checked.'}}, 'preprocess': {'return': {'type': 'list[str | int | float] | list[int | None]', 'description': 'Passes the list of checked checkboxes as a `list[str | int | float]` or their indices as a `list[int]` into the function, depending on `type`.'}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the SortableCheckboxGroup changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'input': {'type': None, 'default': None, 'description': 'This listener is triggered when the user changes the value of the SortableCheckboxGroup.'}, 'select': {'type': None, 'default': None, 'description': 'Event listener for when the user selects or deselects the SortableCheckboxGroup. Uses event data gradio.SelectData to carry `value` referring to the label of the SortableCheckboxGroup, and `selected` to refer to state of the SortableCheckboxGroup. See EventData documentation on how to use this event data'}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'SortableCheckboxGroup': []}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_sortablecheckboxgroup`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  
</div>

SortableCheckboxGroup
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_sortablecheckboxgroup
```

## Usage

```python
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
        gr.Markdown(\"\"\"
        - **Drag and Drop**: Drag items with mouse and drop them in the desired position
        - **Arrow Keys**: Click on an item and use ↑ and ↓ keys to move it
        - **Arrow Buttons**: Use the ↑ and ↓ buttons next to each item to move it
        - **Enter or Space Key**: Use to select and move an item
        \"\"\")

if __name__ == "__main__":
    demo.launch() 
```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `SortableCheckboxGroup`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["SortableCheckboxGroup"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["SortableCheckboxGroup"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, passes the list of checked checkboxes as a `list[str | int | float]` or their indices as a `list[int]` into the function, depending on `type`.
- **As output:** Should return, expects a `list[str | int | float]` of values or a single `str | int | float` value, the checkboxes with these values are checked.

 ```python
def predict(
    value: list[str | int | float] | list[int | None]
) -> list[str | int | float] | str | int | float | None:
    return value
```
""", elem_classes=["md-custom", "SortableCheckboxGroup-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          SortableCheckboxGroup: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
