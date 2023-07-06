import csv

#define variables
votes = 0
candidates = []
candidate_votes = [0,0,0]

#open data file
with open('PyPoll/Resources/election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #store header
    csv_header = next(csvreader)
    for row in csvreader:
        #sum number of votes
        votes += 1
        #create list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])
        #Tally vote for particular candidate
        candidate_votes[candidates.index(row[2])] += 1

#calculate percentages
candidate_percents = [0,0,0]
for i in range(len(candidate_votes)):
    candidate_percents[i] = candidate_votes[i] / votes * 100
#determine winner
winner = candidates[candidate_votes.index(max(candidate_votes))]

#print results to terminal
print('Election Results')
print('--------------------------')
print(f'Total Votes: {votes}')
print('--------------------------')
print(f'{candidates[0]}: {round(candidate_percents[0],3)}% ({candidate_votes[0]})')
print(f'{candidates[1]}: {round(candidate_percents[1],3)}% ({candidate_votes[1]})')
print(f'{candidates[2]}: {round(candidate_percents[2],3)}% ({candidate_votes[2]})')
print('--------------------------')
print(f'Winner: {winner}')

#print results to text file
with open('PyPoll/PyPoll.txt','w') as text:
    text.write('Election Results')
    text.write('\n--------------------------')
    text.write(f'\nTotal Votes: {votes}')
    text.write('\n--------------------------')
    text.write(f'\n{candidates[0]}: {round(candidate_percents[0],3)}% ({candidate_votes[0]})')
    text.write(f'\n{candidates[1]}: {round(candidate_percents[1],3)}% ({candidate_votes[1]})')
    text.write(f'\n{candidates[2]}: {round(candidate_percents[2],3)}% ({candidate_votes[2]})')
    text.write('\n--------------------------')
    text.write(f'\nWinner: {winner}')