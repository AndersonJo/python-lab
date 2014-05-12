# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''
from pprint import pprint
from time import sleep
from math import sqrt

critics = {'Claudia Puig': {'Just My Luck': 3.0,
                  'Snakes on a Plane': 3.5,
                  'Superman Returns': 4.0,
                  'The Night Listener': 4.5,
                  'You, Me and Dupree': 2.5},
 'Gene Seymour': {'Just My Luck': 1.5,
                  'Lady in the Water': 3.0,
                  'Snakes on a Plane': 3.5,
                  'Superman Returns': 5.0,
                  'The Night Listener': 3.0,
                  'You, Me and Dupree': 3.5},
 'Jack Matthews': {'Lady in the Water': 3.0,
                   'Snakes on a Plane': 4.0,
                   'Superman Returns': 5.0,
                   'The Night Listener': 3.0,
                   'You, Me and Dupree': 3.5},
 'Lisa Rose': {'Just My Luck': 3.0,
               'Lady in the Water': 2.5,
               'Snakes on a Plane': 3.5,
               'Superman Returns': 3.5,
               'The Night Listener': 3.0,
               'You, Me and Dupree': 2.5},
 'Michael Phillips': {'Lady in the Water': 2.5,
                      'Snakes on a Plane': 3.0,
                      'Superman Returns': 3.5,
                      'The Night Listener': 4.0},
 'Mick LaSalle': {'Just My Luck': 2.0,
                  'Lady in the Water': 3.0,
                  'Snakes on a Plane': 4.0,
                  'Superman Returns': 3.0,
                  'The Night Listener': 3.0,
                  'You, Me and Dupree': 2.0},
 'Toby': {'Snakes on a Plane': 4.5,
          'Superman Returns': 4.0,
          'You, Me and Dupree': 1.0}}

# Returns a distance-based similarity score for person1 and person2
def sim_distance(data1, data2):
    # Get the list of shared_items
    si = {}
    for item in data1:
        if item in data2: 
            si[item] = 1

    # if they have no ratings in common, return 0
    if len(si) == 0: 
        return 0

    # Add up the squares of all the differences
    sum_of_squares = sum([pow(data1[item] - data2[item], 2) for item in si ])
    return 1 / (1 + sum_of_squares)


# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(data1, data2):
    # Get the list of mutually rated items
    si = []
    for item in data1:
        if item in data2: 
            si.append(item)

    # if they are no ratings in common, return 0
    if len(si) == 0: 
        return 0

    # Sum calculations
    n = len(si)

    # Sums of all the preferences
    sum1 = sum([data1[item] for item in si])
    sum2 = sum([data2[item] for item in si])

    # Sums of the squares
    sum1Sq = sum([pow(data1[item], 2) for item in si])
    sum2Sq = sum([pow(data2[item], 2) for item in si])

    # Sum of the products
    pSum = sum([data1[item] * data2[item] for item in si])

    # Calculate r (Pearson score)
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0: return 0

    r = num / den

    return r

def sim_manhattan(person1,person2):
    """Calculates the Manhattan distance between two critics"""
    total = 0
    ##assume person1 is the x axes and person 2 is the y axes
    for item in person1:
        if item in person2:
            total += abs(person1[item]-person2[item])
    return  1/(total+1)


# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def topMatches(data, name, n=5, similarity=sim_pearson):
    scores = [(other, similarity(data[name], data[other]))
                    for other in critics if other != name]
    scores.sort()
    scores.reverse()
    return scores[0:n]


# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(data, name, similarity=sim_pearson):
    totals = {}
    simSums = {}
    for other in data:
        # don't compare me to myself
        if other == name: continue
        sim = similarity(data[name], data[other])

        # ignore scores of zero or lower
        if sim <= 0: continue
        for item in data[other]:

            # only score movies I haven't seen yet
            if item not in data[name] or data[name][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                totals[item] += data[other][item] * sim
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # Create the normalized list
    rankings = [(total / simSums[item], item) for item, total in totals.items()]

    # Return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings

results = []