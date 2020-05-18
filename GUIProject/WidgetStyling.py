import ipywidgets as widgets
from IPython.display import display

w =widgets.IntSlider()
display(w)

w.layout.margin = 'auto'
w.layout.height = '75px'

x = widgets.IntSlider(value=15,description='New Slider')
display(x)
x.layout = w.layout

#bootstrap look
widgets.Button(description = 'Ordinary Button', button_style='danger')

b1 = widgets.Button(description='NEW')
b1.style.button_color = 'lightgreen'
b1

b2 = widgets.Button()
b2.style = b1.style
b2

s1 = widgets.IntSlider(description='My Handle')
s1.style.handle_color = 'blue'
s1
