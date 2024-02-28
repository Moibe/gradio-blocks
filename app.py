import gradio as gr

get_local_storage = """
    function() {
      globalThis.setStorage = (key, value)=>{
        localStorage.setItem(key, JSON.stringify(value))
      }
       globalThis.getStorage = (key, value)=>{
        return localStorage.getItem(key)
      }
       const text_inputAMLO =  getStorage('text_input')
       const dropdown =  getStorage('dropdown')
       const local_data =  getStorage('local_data')
       globalThis.MOI = "Moisés"
       return [text_inputAMLO, dropdown, local_data, MOI];
      }
    """


def predict(text_input, dropdown):
    return {
        "text": text_input,
        "dropdown": dropdown,
        "something_else": [text_input] * 3 + [dropdown],
    }


with gr.Blocks() as block:
    text_input = gr.Text(label="Input183")
    dropdown = gr.Dropdown(["first", "second", "third"], type="index")
    local_data = gr.JSON({}, label="Local Storage")

    dropdown.change(None, dropdown, None, _js="(v)=>{ setStorage('dropdown',v) }")
    text_input.change(None, text_input, None, _js="(v)=>{ getStorage('text_input') }")
    local_data.change(None, local_data, None, _js="(v)=>{ setStorage('local_data',v) }")
    btn = gr.Button("Set New Data")
    btn.click(fn=predict, inputs=[text_input, dropdown], outputs=[local_data])
    valores = block.load(
        None,
        inputs=None,
        outputs=[text_input, dropdown, local_data],
        _js=get_local_storage,
    )
block.launch(debug=True)

# Accede al valor de MOI
moi = valores[3]

# Imprime el valor de MOI
print(f"MOI: {moi}")