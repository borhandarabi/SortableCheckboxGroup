---
tags: [gradio-custom-component, CheckboxGroup]
title: gradio_sortablecheckboxgroup
short_description: SortableCheckboxGroup
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: space.py
---

# `gradio_sortablecheckboxgroup`
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  

SortableCheckboxGroup

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
        gr.Markdown("""
        - **Drag and Drop**: Drag items with mouse and drop them in the desired position
        - **Arrow Keys**: Click on an item and use ↑ and ↓ keys to move it
        - **Arrow Buttons**: Use the ↑ and ↓ buttons next to each item to move it
        - **Enter or Space Key**: Use to select and move an item
        """)

if __name__ == "__main__":
    demo.launch() 
```

## `SortableCheckboxGroup`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>choices</code></td>
<td align="left" style="width: 25%;">

```python
Sequence[
        str | int | float | tuple[str, str | int | float]
    ]
    | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">A list of string or numeric options to select from. An option can also be a tuple of the form (name, value), where name is the displayed name of the checkbox button and value is the value to be passed to the function, or returned by the function.</td>
</tr>

<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
Sequence[str | float | int]
    | str
    | float
    | int
    | Callable
    | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Default selected list of options. If a single choice is selected, it can be passed in as a string or numeric type. If a function is provided, the function will be called each time the app loads to set the initial value of this component.</td>
</tr>

<tr>
<td align="left"><code>type</code></td>
<td align="left" style="width: 25%;">

```python
Literal["value", "index"]
```

</td>
<td align="left"><code>"value"</code></td>
<td align="left">Type of value to be returned by component. "value" returns the list of strings of the choices selected, "index" returns the list of indices of the choices selected.</td>
</tr>

<tr>
<td align="left"><code>sortable</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True, allows reordering of selected items to set priority.</td>
</tr>

<tr>
<td align="left"><code>show_order</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True, shows the priority order section by default.</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">the label for this component, displayed above the component if `show_label` is `True` and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component corresponds to.</td>
</tr>

<tr>
<td align="left"><code>info</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">additional component description, appears below the label in smaller font. Supports markdown / HTML syntax.</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
Timer | float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Continously calls `value` to recalculate it if `value` is a function (has no effect otherwise). Can provide a Timer whose tick resets `value`, or a float that provides the regular interval for the reset Timer.</td>
</tr>

<tr>
<td align="left"><code>inputs</code></td>
<td align="left" style="width: 25%;">

```python
Component | Sequence[Component] | set[Component] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Components that are used as inputs to calculate `value` if `value` is a function (has no effect otherwise). `value` is recalculated any time the inputs change.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If True, will display label.</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will place the component in a container - providing some extra padding around the border.</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left">Minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If True, choices in this checkbox group will be checkable; if False, checking will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will be hidden.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.</td>
</tr>

<tr>
<td align="left"><code>key</code></td>
<td align="left" style="width: 25%;">

```python
int | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the SortableCheckboxGroup changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `input` | This listener is triggered when the user changes the value of the SortableCheckboxGroup. |
| `select` | Event listener for when the user selects or deselects the SortableCheckboxGroup. Uses event data gradio.SelectData to carry `value` referring to the label of the SortableCheckboxGroup, and `selected` to refer to state of the SortableCheckboxGroup. See EventData documentation on how to use this event data |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Is passed, passes the list of checked checkboxes as a `list[str | int | float]` or their indices as a `list[int]` into the function, depending on `type`.
- **As input:** Should return, expects a `list[str | int | float]` of values or a single `str | int | float` value, the checkboxes with these values are checked.

 ```python
 def predict(
     value: list[str | int | float] | list[int | None]
 ) -> list[str | int | float] | str | int | float | None:
     return value
 ```
 
