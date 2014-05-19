'''
Created on May 20, 2014

@author: a141890
'''

from recommendations import critics
import matplotlib.pyplot as plt

def compare_movie(persons, movie1, movie2):
    xs = []
    ys = []
    lables = []
    for critic, movies in persons.items():
        if movie1 in movies and movie2 in movies:
            xs.append(persons[critic][movie1])
            ys.append(persons[critic][movie2])
            lables.append(critic)
        
    plt.plot(xs, ys, 'ro')
    plt.axis([0, 5, 0, 5])
    for label, x, y in zip(lables, xs, ys):
        plt.annotate(
                label, 
                xy = (x, y), xytext = (-10, 10),
                textcoords = 'offset points', ha = 'right', va = 'bottom',
                bbox = dict(boxstyle = 'round,pad=0.1', fc = 'yellow', alpha = 0.5),
                arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
    plt.show()
    


compare_movie(critics, 'You, Me and Dupree', 'Snakes on a Plane')
