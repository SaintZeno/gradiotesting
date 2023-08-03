# gradio quickstart app
import gradio as gr
from diffusers import DiffusionPipeline

pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", 
                                             safety_checker=None)
pipeline.to('cuda')
    

def text_2_img(text):
    # use pipeline to generate image from text
    # get image from pipeline
    image = pipeline(text+'; best quality').images[0]
    # return image
    return image


demo = gr.Interface(fn=text_2_img, 
                    inputs=gr.Textbox(label='Create an image with text!', 
                                      placeholder= 'your text here', 
                                      lines=4),
                    outputs="image", 
                    title="Text to Image Generator"
                    )

demo.launch()

    

