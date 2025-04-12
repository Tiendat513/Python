import sys
from collections import Counter
sys.stdin = open('CPHONE.INP')
sys.stdout = open('CPHONE.OUT', 'w')
n = int(sys.stdin.readline())
votes = [int(input()) for _ in range(n)]
vote_counts = Counter(votes)
max_votes = max(vote_counts.values())
winners = []
for id, count in vote_counts.items():
    if count == max_votes:
        winners.append(id)
winners.sort()
for i in  range(len(winners)):
    print(str(winners[i])) 
    
