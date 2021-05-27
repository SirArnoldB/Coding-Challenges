"""
# Tournament Winner
There's an algorithms tournament taking place in which teams of programmers compete against each other to solve algorithmic problems as fast as possible. 
Teams compete in a round robin, where each team faces o against all other teams. Only two teams compete against each other at a time, and for each competition, one team is designated the home team, while the other team is the away team. 
In each competition there's always one winner and one loser; there are no ties. A team receives 3 points if it wins and 0 points if it loses. The winner of the tournament is the team that receives the most amount of points. 
Given an array of pairs representing the teams that have competed against each other and an array containing the results of each competition, write a function that returns the winner of the tournament. 
The input arrays are named competitions and results , respectively. The competitions array has elements in the form of [homeTeam, awayTeam] , where each team is a string of at most 30 characters representing the name of the team. 
The results array contains information about the winner of each corresponding competition in thecompetitions array. 
Specically, results[i] denotes the winner of competitions[i] , where a 1 in the results array means that the home team in the corresponding competition won and a 0 means that the away team won. 
It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams exactly once. It's also guaranteed that the tournament will always have at least two teams.

>>> Sample Input
competitions = [
 ["HTML", "C#"],
 ["C#", "Python"],
 ["Python", "HTML"],
]
results = [0, 0, 1]

>>> Sample Output
"Python"
// C# beats HTML, Python Beats C#, a
// HTML - 0 points
// C# - 3 points
// Python - 6 points

Solution 1
**********
"""
def tournamentWinner(competitions, results):
    team_scores = {}
    max_score = 0
    winner = ""
	
    for i in range(len(results)):
        score = results[i]
        if score == 1:
            team = competitions[i][0]
            if team in team_scores:
                team_scores[team] += 3
            else: 
                team_scores[team] = 3
        else:
            team = competitions[i][1]
            if team in team_scores:
                team_scores[team] += 3
            else: 
                team_scores[team] = 3
    for team, score in team_scores.items():
        if score > max_score:
            max_score = score 
            winner = team
    return winner


"""
Solution 2
**********
"""
# O(n) - time | O(k) - space - where n is the number of competitions, and 
# k is the number of teams 

def tournamentWinner(competitions, results):
	currentWinner = ""
	team_scores = {currentWinner: 0}
	
	for idx, competition in enumerate(competitions):
		# find the corresponding result, which corresponds to idx, from the results list
		result = results[idx]
		# decompose competition and figure out which is the home team and which is the away team
		homeTeam, awayTeam = competition
		
		# Determine the winner 
		winningTeam = homeTeam if result == 1 else awayTeam
		
		# update the winning team's score 
		updateScores(winningTeam, 3, team_scores)
		
		# update the current best team
		if team_scores[winningTeam] > team_scores[currentWinner]:
			currentWinner = winningTeam
		
	return currentWinner
# function to update the score of the current team
def updateScores(team, points, team_scores):
	if team not in team_scores:
		team_scores[team] = 0
	# update the score 
	team_scores[team] += points
