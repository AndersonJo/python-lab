# -*- coding:utf-8 -*-
__author__ = 'a141890'

from math import sqrt
from data import get_all_movie_names


def euclidean_distance(prefs, person1, person2):
    # Get the list of shared_items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]: si[item] = 1

    # if they have no ratings in common, return 0
    if len(si) == 0: return 0

    # Add up the squares of all the differences
    sum_of_squares = sqrt(sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                               for item in prefs[person1] if item in prefs[person2]]))
    return 1 / (1 + sum_of_squares)


# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs, p1, p2):
    # Get the list of mutually rated items
    si = []
    for item in prefs[p1]:
        if item in prefs[p2]:
            si.append(item)

    # if they are no ratings in common, return 0
    if not si:
        return 0

    # Sum calculations
    n = len(si)

    # Sums of all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # Sums of the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # Sum of the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # Calculate r (Pearson score)
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0: return 0

    r = num / den

    return r


# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def top_matches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]


def display_top_matchers(data, name):
    top_matchers = top_matches(data, name, n=10)
    movie_names = get_all_movie_names()

    out = "{critic:<15} {sim:<20}"
    for m_name in movie_names:
        word = m_name.split(' ')[0]
        out += " {"+ word +":<10}"

    args = {}
    args['critic'] = 'Critic'
    args['sim'] = 'Sim'
    for m_name in movie_names:
        args[m_name.split(' ')[0]] = m_name[:10]
    print out.format(**args)

    for sim, critic_name in top_matchers:
        args = {}
        args['critic'] = critic_name[:15]
        args['sim'] = sim
        for m_name in movie_names:
            score = data[critic_name].get(m_name, '')
            args[m_name.split(' ')[0]] = ''
            if score:
                args[m_name.split(' ')[0]] = str(score) + "("+ str(round(sim * score, 2)) + ")"



        print out.format(**args)



# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def get_recommendations(prefs, person, similarity=sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        # don't compare me to myself
        if other == person:
            continue
        sim = similarity(prefs, person, other)

        # ignore scores of zero or lower
        if sim <= 0:
            continue


        data1 = prefs[person]
        data2 = prefs[other]

        for item in prefs[other]:
            # only score movies I haven't seen yet
            if item not in data1 or data1[item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                totals[item] += data2[item] * sim
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # Create the normalized list
    rankings = [(total / simSums[item], item) for item, total in totals.items()]

    # Return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings
