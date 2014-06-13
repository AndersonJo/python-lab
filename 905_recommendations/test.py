'''
Created on May 20, 2014

@author: a141890
'''
from clusters import blogs
from recommendations import sim_distance, sim_pearson, topMatches


top = topMatches(blogs, 'Wonkette', similarity=sim_distance)[:10]
top2 = topMatches(blogs, 'Wonkette', similarity=sim_pearson)[:10]

top.sort(key=lambda x: -x[1])
top2.sort(key=lambda x: -x[1])
print top
print top2

for i1, i2 in zip(top, top2):
    print "%-60s %-60s"% (i1[0], i2[0])