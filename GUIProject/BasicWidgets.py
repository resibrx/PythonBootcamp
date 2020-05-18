import ipywidgets as widgets
from IPython.display import display

w = widgets.IntSlider()
display(w)

#close widgets
w.close()

v = widgets.IntSlider()
display(w)
v.value
v.value = 50
v.max = 2000

a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)
#link both widgets together
mylink = widgets.jslink((a,'value'),(b,'value'))
anotherlink = widgets.jslinkt((a,'value'),(b,'max'))
#remove the linking
mylink.unlink()
