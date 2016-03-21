# Jack Ryan
# 2/25/2016
# CSE 30151
# music_generator.py
# Goal: support at least first and second order music generation

import random

def build_markov_dict(s):
	# Builds up a dictionary using input string
	# e.g. {A -> [A, A, B, C, A], B -> [A, B, A, C, C], ...}
	markov_dict = {}
	for i in xrange(0, len(s)-1):
		if not s[i] in markov_dict:
			# If the character is not a key yet, initialize value to list with next char
			markov_dict[s[i]] = [s[i+1]]
		else:
			markov_dict[s[i]].append(s[i+1])
	return markov_dict

def build_charset(notes):
	char_set = set()
	for char in notes:
		char_set.add(char)
	sorted_set = sorted(char_set)
	return sorted_set
def build_fo_adjlist(notes):
	# Builds a first order Markov chain
	markov_dict = build_markov_dict(notes)
	sorted_set = build_charset(notes)
	adjlist = [None] * len(sorted_set)
	i = 0
	for char in sorted_set:
		if char not in markov_dict:
			adjlist[i] = []
		else:
			adjlist[i] = markov_dict[char]
		i += 1
	return adjlist

#TODO
def build_second_order(notes):
	m_dict = {}
	for i in xrange(0, len(notes)-2):
		current_pair=(notes[i]+notes[i+1])
		m_dict.setdefault(current_pair,[]).append(notes[i+2])
	return m_dict


def generate_score(markov_dict):
	most_freq = max(markov_dict, key= lambda x: len(markov_dict[x]))
	current = most_freq
	score = [current]
	i = 0
	while (current in markov_dict) and i < 100:
		char = random.choice(markov_dict[current])
		score.append(char)
		current = char
		i += 1
	return " ".join(score)

def generate_score_second_order(markov_dict):
	most_freq = max(markov_dict, key= lambda x: len(markov_dict[x]))
	current = most_freq
	score = [current[0], current[1]]#contains the first an second elements
	i = 0
	while (current in markov_dict) and i < 100:
		char = random.choice(markov_dict[current])
		score.append(char)
		current = score[len(score)-2]+score[len(score)-1] #current is the last two elements in in the list
		i += 2 
	return " ".join(score)


## Main ##

frequency_map = {'C': 261.63,'D': 293.66,'E': 329.63,'F':349.23,'G':392.00,'A':440.00,'B':493.88}
# Using middle C octave for simplicity, can easily be extended to support 'C4', 'E2', etc

print "Enter the string of notes to be used in this Markov music generator:",
notes = raw_input()

adj_list = build_fo_adjlist(notes)
charset = build_charset(notes)


print "\nFirst-order adjacency list representing transitions on current musical note\n"
for i in xrange(0, len(adj_list)):
	print charset[i] + ": " + str(adj_list[i])

print "\nGenerating 20 musical scores based on Markov first-order music generation model...\n"

markov_dict = build_markov_dict(notes)

score_list = []

for i in xrange(0, 20):
	score = generate_score(markov_dict)
	score_list.append(score)
	print str(i) + ": " + score + "\n"


#SECOND ORDER ----
print "\nsecond-order adjacency list representing transitions on current musical note\n"

s= build_second_order(notes)
for key, value in s.iteritems():
	print "key: "+key + " values: "+ str(value)

score_list = []

for i in xrange(0, 20):
	score = generate_score_second_order(s)
	score_list.append(score)
	print str(i) + ": " + score + "\n"





