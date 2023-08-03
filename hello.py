# gradio quickstart script
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

if __name__ == "__main__":
    gr.Interface(fn=greet, 
                 inputs="text", 
                 outputs="text").launch()


