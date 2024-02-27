import gradio as gr 

from transformers import pipeline

#pipe = pipeline("translation", model="t5-base")

get_local_storage = """
    function() {
      globalThis.setStorage = (key, value)=>{
        localStorage.setItem(key, JSON.stringify(value))
      }
       globalThis.getStorage = (key, value)=>{
        return JSON.parse(localStorage.getItem(key))
      }
       const text_input =  getStorage('text_input')
       return text_input;
      }
    """


def translate(text):
    return text

with gr.Blocks() as demo:
    with gr.Row(): 
        with gr.Column():
            english = gr.Textbox(label="English text")
            text_input = gr.Text(label="Input va allá")
            text_input.change(None, text_input, None, _js="(v)=>{ setStorage('text_input',v) }")
            translate_btn = gr.Button(value="Translate")
        with gr.Column():
            german = gr.Textbox(label="German Text")

    translate_btn.click(translate, inputs=english, outputs=german)
    examples = gr.Examples(examples=["I went to the supermarket yesterday.", "Helen is a good swimmer."],
                        inputs=[english])

demo.load(
        None,
        inputs=None,
        outputs=text_input,
        _js=get_local_storage,
    )
demo.launch(debug=True)
