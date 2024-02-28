import gradio as gr

get_local_storage = """
    function() {
      globalThis.setStorage = (key, value)=>{
        localStorage.setItem(key, JSON.stringify(value))
      }
       globalThis.getStorage = (key, value)=>{
        obtencion = localStorage.getItem(key)
        console.log("Dentro de getStorage:", obtencion)
        return localStorage.getItem(key)
      }
       
       return [text_input, local_data];
      }
    """


def predict(text_input):
    return "Hola mundo, éste es el resultado."

with gr.Blocks() as block:
    tokens_label = gr.Label("Etiqueta")
    
    text_input = gr.Text(label="Input183")
    resultadoFinal = gr.Text(label="ResulAquí")

    text_input.change(None, text_input, None, _js="(v)=>{ getStorage('text_input') }")
    resultadoFinal.change(None, local_data, None, _js="(v)=>{ setStorage('local_data',v) }")
    btn = gr.Button("Enviar")
    btn.click(fn=predict, inputs=[text_input], outputs=[resultadoFinal])
    valores = block.load(
        None,
        inputs=None,
        outputs=[text_input, local_data],
        _js=get_local_storage,
    )
block.launch(debug=True)