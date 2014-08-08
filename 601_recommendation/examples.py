# -*- coding:utf-8 -*-
'''
Created on 2014. 8. 8.

@author: a141890
'''
from pprint import pprint

from plots import *
from recommendations import euclidean_distance, sim_pearson, get_recommendations, display_top_matchers


def euclidean_distance_score():
    """
    Euclidean Distance Score 를 이용하여
    Toby와 Mick의 취향이 얼마나 같은지 알아보자

    a^2 + b^2 = c^2
    을 이용하여 Euclidean Distance Score 함수를 만들어라

    sqrt(E(x-y)^2) = Euclidean Distance Score
    """
    # display_movies('You, Me and Dupree', 'Snakes on a Plane') # Basic Euclidean Distance

    # display_critics('Jack Matthews', 'Gene Seymour')
    # display_critics('Jack Matthews', 'Toby')
    print 'Jack Matthews', 'Toby :', euclidean_distance(critics, 'Jack Matthews', 'Toby')
    print 'Jack Matthews', 'Gene Seymour :', euclidean_distance(critics, 'Jack Matthews', 'Gene Seymour')
    print 'Jack Matthews', 'Chang :', euclidean_distance(critics, 'Jack Matthews', 'Chang')


def person_correlation_score():
    """
    Pearson Correlation Score

    - Best Fit Line
        Jack하고 Gene의 그래프와
        Jack하고 Toby의 그래프를 비교하자

    - Grade Inflation 을 극복한다
        Chang 하고 Jack 을 비교해보자..
        Euclidean Distance 사용시와 비교


    """
    display_critics('Jack Matthews', 'Chang')
    print 'Jack Matthews', 'Toby :', sim_pearson(critics, 'Jack Matthews', 'Toby')
    print 'Jack Matthews', 'Gene Seymour :', sim_pearson(critics, 'Jack Matthews', 'Gene Seymour')
    print 'Jack Matthews', 'Chang :', sim_pearson(critics, 'Jack Matthews', 'Chang')


def recommend():
    """
    total = E(score*similarity)
    simSums = E(similarity)
    score = total/simSums

    """
    display_top_matchers(critics, 'Toby')
    pprint(get_recommendations(critics, 'Toby'))


if __name__ == '__main__':
    pass








     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    