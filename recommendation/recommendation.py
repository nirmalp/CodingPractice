critics={'Lisa Rose':{'Lady in the Winter':2.5,'Snakes on a Plane':3.5,'Just My Luck':3.0,'Superman Returns':3.5,'You, Me and Dupree':2.5,'The Night Listener':3.0},
		 'Gene Seymour':{'Lady in the Winter':3.0,'Snakes one a Plane':3.5,'Just My Luck':1.5,'Superman Returns':5.0,'The Night Listener':3.0,
		 'You, Me and Dupree':3.5},
		 'Michael Phillips':{'Lady in the Winter':2.5,'Snakes in a Plane':3.0,'Superman Returns':3.5,'The Night Listener':4.0},
		 'Claudia Puig':{'Snakes in a Plane':3.5,'Just My Luck':3.0,'The Night Listener':4.5,'Superman Returns':4.0,'You, Me and Dupree':2.5},
		 'Mick LaSalle':{'Lady in the Water':3.0, 'Snakes on a Plane':4.0, 'Just My Luck': 2.0,'Superman Returns':3.0,'The Night Listener':3.0,
		 'You, Me and Dupree':2.0},
		 'Toby':{'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


from math import sqrt
def sim_distance(prefs, person1, person2):
	#Get List of shared items
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1
	
	if len(si)==0: 
		return 0

	sum_of_squares= sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
	return 1/(1+sum_of_squares)

def sim_pearson(prefs, person1, person2):
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1
	n=len(si)
	if len(si)==0:
		return 0
	
	sum1=sum([prefs[person1][item] for item in si])
	sum2 = sum([prefs[person2][item] for item in si])
	sum1Sq = sum([pow(prefs[person1][item],2) for item in si])
	sum2Sq = sum([pow(prefs[person2][item],2) for item in si])
	# return 1
	psum = sum([prefs[person1][item]*prefs[person2][item] for item in si])
	#Pearson score
	num=psum-(sum1*sum2/n)
	den = sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den==0:
		return 0
	r=num/den
	return r

# print(sim_pearson(critics,'Lisa Rose','Gene Seymour'))

#print val

def top_Matches(self prefs,person,n=5,similarity=sim_pearson):
	print(prefs[person])
	scores=sim_pearson(perfs,person,'Lisa Rose')
	#print(scores)
	# scores=[similarity(perfs,person,other) for other in prefs]
	# scores.sort()
	# scores.reverse()
	# return scores[0:n]
	
top_Matches(critics,'Toby',n=3)
