'''
Created on 2014. 8. 1.

@author: a141890
'''
from matplotlib.colors import cnames
from matplotlib.pyplot import xlabel, ylabel, xlim, ylim, bar, pie
from numpy import pi
from pprint import pprint
from pylab import figure, plot, array, show, savefig, FigureCanvasBase, arange, \
    grid, hold, axis, legend, xticks, yticks, subplot, title, text
from scipy import sin, cos, tan

def basic(save=False):
    """
    Shows up a simple plot
    
    Symbols
     - 'o'
     - '^'
     - 's'
     - '+'
     - 'x'
     - 'D'
     
    Line Styles
     - '-'
     - '--'
     - '-.'
     - ':'
    """
    figure(1)
    y = array([3,2,5,4,9])
    plot(y, 'D--')
    if not save: 
        show()
    else:
        savefig('example.png')


def list_available_file_types():
    pprint(FigureCanvasBase.filetypes)
    
def list_available_colors():
    pprint(cnames)
    
def show_multiple_plots():
    """
    plot(multiple arguments)
    """
    figure(1)
    x = arange(5)
    y = array([3,2,5,4,9])
    t= array([10,11,9,4,13])
    plot(x, y, 'o-', t, '^:')
    grid()
    show()
    
def show_multiple_plots2():
    """
    hold method
    """
    figure(1)
    hold(True)
    x = arange(5)
    y = array([3,2,5,4,9])
    plot(x, y, 'o:', color='yellowgreen')
    
    y= array([10,11,9,4,13])
    plot(y, 's--', color='#ff0000')
    grid()
    show()


def show_sin_cos_graph():
    figure(1)
    hold(True)
    title('Sin Cos')
    s = arange(0, 2*pi, 0.1)
    plot(sin(s), 'o:', label='sin')
    plot(cos(s), '^--', label='cos')
    legend()
    grid()
    
    l = len(s)
    xticks([0, l/4, l/2, l*3/4, l], [0, 'pi/2 (90)', 'pi (180)', 'pi*3/2 (270)', '2*pi (360)'])
    show()
    
def control_axis():
    """
    axis('auto')
    axis('equal')
    axis('tight')
    axis('scaled')
    """
    figure(1)
    R = 2
    I = arange(0, 2*pi, 0.01)
    hold(True)
    plot(sin(I)*R, cos(I)*R, '-')
    grid()
    axis('scaled')
    show()

def text_example():
    """
    the list of arguments used in text function
    
     - fontsize : large, medium, small, 50 <-- Actual font size
     - va       : (vertical alignment) top, baseline, bottom, center
     - ha       : (horizontal alignment) center, left, right
    """
    data = {'C': {'x': 2, 'y': 8},
            'C++': {'x': 4, 'y': 9},
            'python': {'x': 7, 'y': 2},
            'ruby': {'x': 5, 'y': 3},
            'javascript': {'x': 9, 'y': 2},
            'C#': {'x': 8, 'y': 6},
            'Java': {'x': 9, 'y': 6}}
    
    figure(1)
    title('Programming Language')
    hold(True)
    for name, point in data.items():
        x = point['x']
        y = point['y']
        plot(x, y, 'o')
        text(x, y, "%s\n(%d, %d)"%(name, x, y), fontsize='large', va='bottom', ha='left')
        
    xlabel('Popularity')
    ylabel('Dificulty to learn')
    axis('scaled')
    xlim(0, 10)
    ylim(0, 10)
    xticks(arange(0, 11))
    yticks(arange(0, 11))
    grid()
    show()

def show_bar():
    data = {'Chang Min': 110,
            'Sang Won': 100,
            'Byung Du': 50,
            'Jung Ah': 60,
            'Ga Ram': 20,
            'Eun Hae': 10}
    
    figure(1)
    title('TOEFL Scores')
    
    count =1
    for name, height in data.items():
        bar(count, height, color='#333333')
        text(count, height, name, va='bottom')
        count += 1
        
    ylim(0, 120)
    grid()
    yticks(arange(0, 120, 10))
    show()
    
def show_piechart():
    data = {'Germany': 89,
            'Korean' : 76,
            'Italian': 60,
            'Polish': 40,
            'Japanese': 125,
            'China': 955,
            'English': 360}
    
    figure(1)
    title('Language Popularity')
    
    countries = [p for p in data.keys()]
    popularities = [p for p in data.values()]
    pie(popularities, labels=countries, shadow=True)
    show()

if __name__ == "__main__":
    basic()
    #list_available_file_types()
    #list_available_colors()
    #show_multiple_plots2()
    #show_sin_cos_graph()
    #control_axis()
    #text_example()
    #show_bar()
    #show_piechart()
    
    
    
    
    
    
    
    
    