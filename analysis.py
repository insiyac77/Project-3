# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    # changing the noise to 0 will guarantee the agent crosses as it will never fall off the bridge
    answerNoise = 0
    return answerDiscount, answerNoise

def question3a():
    # prefer the close exit and risking cliff
    # we want a myopic (low discount) factor with low noise (will be unlikely to take high path)
    # and a negative living reward to make it extra myopic (knows its dying)
    answerDiscount = 0.1
    answerNoise = 0
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    # prefer close exit but avoid cliff
    # still want myopic but now we should increase noise to dissuade taking the cliff path
    # also don't want too myopic or it will prioritize the close one too much
    # still want a negative living reward
    answerDiscount = 0.3
    answerNoise = 0.3
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    # prefer far exit and risk cliff
    # want far sighted, but low noise
    # and positive living reward to encourage exiting later
    answerDiscount = 0.8
    answerNoise = 0
    answerLivingReward = 1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    # prefer far exit but avoid cliff
    # want far sighted, noise, positive living reward
    answerDiscount = 0.8
    answerNoise = 0.3
    answerLivingReward = 1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    # avoid both exits and cliff
    # want high discount, extremely high noise, negative living reward
    answerDiscount = 0.5
    answerNoise = 0.9
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question6():
    answerEpsilon = None
    answerLearningRate = None
    return 'NOT POSSIBLE'
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
