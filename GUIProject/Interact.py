from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display


def func(x):
    return x

#slider
interact(func,x=10)
#checkbox
interact(func,x=True)
#textbox
interact(func,x='Hello')

#get two options
@interact(x=True,y=fixed(1.0)) #no manipulating for y
def g(x,y):
    return (x,y)


interact(func,x=widgets.IntSlider(min=-100,max=100,step=1,value=0))
interact(func,x=(-100.0,100.0,.1))

@interact(x=(0.0,20.0,0.5))
def h(x=5.0):
    return x

#dropdown menu
interact(func,x=['hi','hello','Ola'])
interact(func,x={'one':10,'two':20})

def f(a,b):
    display(a+b)
    return a+b

w = interactive(f,a=10,b=20)
display(w)
