from random import uniform

import pylab as p

from data import critics


def display_critics(name1, name2):
    """
    plot the two critics' movie scores.
    
    @param name1 (str): the name of a critic
    @param name2 (str): the name of a critic 
    """
    movies1 = critics.get(name1, None)
    movies2 = critics.get(name2, None)
    si_names = [n for n in movies1 if movies2.has_key(n)]

    _init_plot()
    p.xlabel(name1)
    p.ylabel(name2)
    for m_name in si_names:
        score1 = movies1[m_name]
        score2 = movies2[m_name]
        r = uniform(0, 0.2)
        p.plot(score1, score2 + r, 'D')
        p.text(score1, score2 + r, m_name)
    p.show()


def display_all_critics():
    for name1 in critics:
        for name2 in critics:
            if name1 == name2:
                continue
            display_critics(name1, name2)


def display_movies(movie1, movie2):
    """
    plot the two critics' movie scores.

    @param name1 (str):
    @param name2 (str): the name of a critic
    """

    _init_plot()
    p.xlabel(movie1)
    p.ylabel(movie2)

    critic_names = [name for name, scores in critics.items() if scores.has_key(movie1) and scores.has_key(movie2)]
    for c_name in critic_names:
        a_score = critics[c_name][movie1]
        b_score = critics[c_name][movie2]

        p.plot(a_score + uniform(0, 0.1), b_score + uniform(0, 0.1), '^')
        p.text(a_score, b_score + uniform(0, 0.3), c_name.split(' ')[0])

    p.show()


def display_all_movies():
    movie_names = []
    for movies in critics.values():
        for movie_name in movies:
            if movie_name not in movie_names:
                movie_names.append(movie_name)

    for name1 in movie_names:
        for name2 in movie_names:
            if name1 == name2:
                continue
            display_movies(name1, name2)


def _init_plot():
    p.figure(1)
    p.grid()
    p.xlim(0, 6)
    p.ylim(0, 6)
    p.xticks(p.arange(0, 6, 0.5), p.arange(0, 6, 0.5))
    p.yticks(p.arange(0, 6, 0.5), p.arange(0, 6, 0.5))