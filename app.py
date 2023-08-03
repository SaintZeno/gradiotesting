# gradio quickstart app
import gradio as gr

def greet(name):
    # greet function that takes in a name and returns a greeting
    # with the name in it
    # if name is not string the raise ValueError
    if not isinstance(name, str):
        raise ValueError("Name must be a string!")
    else: 
        return "Hello " + name + "!"


def basic_interface():
    # run greet function on single input 
    # and return a single output to the app.
    gr.Interface(fn=greet, 
                 inputs="text", 
                 outputs="text").launch()

# gradio interface requirements are 
# fn: function to wrap UI around
# inputs: components to use for the input (text, image, audio)
# outputs: components to use for the output (text, image, audio)
# to run the interface use gr.interface(fn, inputs, outputs).launch()

# basic gradio interface with text box inputs with 2 lines 
# and a placeholder called "what's your name?" and text box 
# outputs with 2 lines and a placeholder called "output"
def basic_interface():
    inputs = gr.Textbox(lines=2, placeholder="What's your name?")
    outputs = gr.Textbox(lines=2, placeholder="Output here")
    gr.Interface(fn=greet, inputs=inputs, outputs=outputs).launch()

# function called greet2 which accepts 3 different positional arguments: name, age, and city
def greet2(name, age, city):
    # greeting variable equal to 
    # if age > 80 then greeting is "you're old but cool"
    # else if age <= 80 then greeting is "you're not old but still cool"
    # else greeting is "you're not old and you're not cool"
    greeting = f"{name} you're neat!" if age <= 80 else f"{name} you're cool!"
    # good_city variable equal to
    # if city != 'good-town' then good_city is false
    # else good_city is true
    good_city = city == "good-town"
    # return the greeting variable and the good_city variable
    return greeting, good_city

# basic gradio interface with multiple input and output components
def multiple_interface():
    # start list 
    # text box with 1 line, placeholder is "input your name", label is "Name"
    # slider from 0 to 150
    # text box with 1 lines and "input city youre currently in" placeholder
    # end list
    inputs = [gr.Textbox(lines=1, label= 'NAME BRO!', placeholder="Input your name"),
              gr.Slider(0,150, label='YOUR AGE??'),
              gr.Textbox(lines=1, label='CURRENT CITY!!',placeholder="Input the city you're currently in")]
    outputs = [gr.Textbox(lines=1, label='Greeting', placeholder="Yo"),
               gr.Textbox(lines=1, label='Good Town?',placeholder="Maybe!")
               ]
    gr.Interface(fn=greet2, inputs=inputs, outputs=outputs).launch()




if __name__ == "__main__":
    
    multiple_interface()

    

