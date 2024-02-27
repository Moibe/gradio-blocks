import gradio as gr

get_local_storage = """
    function() {
      globalThis.setStorage = (key, value)=>{
        localStorage.setItem(key, JSON.stringify(value))
      }
       globalThis.getStorage = (key, value)=>{
        return JSON.parse(localStorage.getItem(key))
      }
       const text_input =  getStorage('text_input')
       const dropdown =  getStorage('dropdown')
       const local_data =  getStorage('local_data')
       return [text_input, dropdown, local_data];
      }
    """


def predict(text_input, dropdown):
    return {
        "text": text_input,
        "dropdown": dropdown,
        "something_else": [text_input] * 3 + [dropdown],
    }


with gr.Blocks() as block:
    text_input = gr.Text(label="Input182")
    dropdown = gr.Dropdown(["first", "second", "third"], type="index")
    local_data = gr.JSON({}, label="Local Storage")

    dropdown.change(None, dropdown, None, _js="(v)=>{ setStorage('dropdown',v) }")
    text_input.change(None, text_input, None, _js="(v)=>{ setStorage('text_input',v) }")
    local_data.change(None, local_data, None, _js="(v)=>{ setStorage('local_data',v) }")
    btn = gr.Button("Set New Data")
    btn.click(fn=predict, inputs=[text_input, dropdown], outputs=[local_data])
    block.load(
        None,
        inputs=None,
        outputs=[text_input, dropdown, local_data],
        _js=get_local_storage,
    )
block.launch(debug=True)
