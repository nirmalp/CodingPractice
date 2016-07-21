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

#Returns best match for a person
def top_Matches(
	prefs,
	person,
	n=5,
	similarity=sim_pearson
	):
	scores = [(similarity(prefs, person, other), other) for other in prefs 
			if other!=person]
	#print(scores)
	scores.sort()
	scores.reverse()
	return scores[0:n]

def getRecommendation(prefs, person, similarity=sim_pearson):
	totals={}
	simSums={}
	for other in prefs:
		if other==person:
			continue
		sim=similarity(prefs,person,other)
		# ignore scores of zero or lower
		if sim<=0:
			continue
		for item in prefs[other]:
			#only scores movies that person haven't seen
			if item not in prefs[person] or prefs[person][item]==0:
				totals.setdefault(item,0)
				totals[item]+=sim*prefs[other][item]
				simSums.setdefault(item,0)
				simSums[item]+=sim
	rankings = [(total/simSums[item],item) for item,total in totals.items()]
	rankings.sort()
	rankings.reverse()
	return rankings

def transformPerfs(prefs):
	result={}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item,{})
			result[item][person]=prefs[person][item]
	return result

def calculateSimilarItems(prefs, n=10):
	result={}
	itemPrefs=transformPerfs(prefs)
	c=0
	for item in itemPrefs:
		c+=1
		if c%100==0: print("%d %d",c,len(itemPrefs))
		scores= top_Matches(itemPrefs, item, n=n, similarity=sim_distance)
		result[item]=scores
	return result


def getRecommendationItems(prefs, itemMatch,user):
	userRatings=prefs[user]
	scores={}
	totalSim={}
	#Loop over items rated by the user
	for(item,rating) in userRatings.items():
		for(similarity,item2) in itemMatch[item]:
			if item2 in userRatings: continue
			scores.setdefault(item2,0)
			scores[item2]+=similarity*rating
			totalSim.setdefault(item2,0)
			totalSim[item2]+=similarity
	rankings=[(score/totalSim[item],item) for item,score in scores.items()]
	rankings.sort()
	rankings.reverse()
	return rankings
#print(top_Matches(transformPerfs(critics),'Just My Luck'))
itemsim=calculateSimilarItems(critics)
print(getRecommendationItems(critics,itemsim,'Toby'))
#print(top_Matches(critics,'Lisa Rose',n=3))
#print(getRecommendation(critics,'Toby'))
#print(sim_pearson(critics,'Toby','Claudia Puig'))