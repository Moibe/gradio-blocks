import gradio as gr

get_local_storage = """
    function() {
      globalThis.setStorage = (key, value)=>{
        localStorage.setItem(key, value)
      }
       globalThis.getStorage = (key, value)=>{
        obtencion = localStorage.getItem(key)
        console.log("Dentro de getStorage:", obtencion)
        return obtencion
      }

       if (!localStorage.getItem('tokens')) {
        localStorage.setItem('tokens', 5);
        }

        const legado = localStorage.getItem('tokens');

        return legado;
       
      }
    """

def predict(text_input, tokens_label):
   
    tokens_texto = int(tokens_label) - 1
    resultado_texto = "Hola " + text_input + ", éste es el resultado." 
    print("Tokens_Label:", tokens_label)

    if tokens_texto > 0:
        
        print("Saldo Positivo")
        return tokens_texto, resultado_texto, gr.Button(interactive=True)

    else:
    
        print("Saldo negativo")
        return tokens_texto, resultado_texto, gr.Button(interactive=False)

with gr.Blocks() as block:

    tokens_label = gr.Text(label="Tokens Disponibles", interactive = False)
    text_input = gr.Text(label="Tu Nombre:")
    resultadoFinal = gr.Text(label="Resultado")
    
    #text_input.change(None, tokens_label, tokens_label, js="(v)=>{ getStorage('text_input',v) }")
    tokens_label.change(None, tokens_label, None, js="(v)=>{ setStorage('tokens',v) }")

    #resultadoFinal.change(None, text_input, resultadoFinal, js="(v)=>{ getStorage('text_input') }")
    btn = gr.Button("Enviar", icon="aiicon.png", interactive = True)
    btn.click(fn=predict, inputs=[text_input, tokens_label], outputs=[tokens_label, resultadoFinal, btn])
 
    block.load(
        None,
        inputs=None,
        outputs=[tokens_label],
        js=get_local_storage,
    )
block.launch(debug=True)