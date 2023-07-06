import csv

#define variables
months = 0
net_pl = 0
prev_pl = 0
diff = []
dates = []

#open data file
with open('PyBank/Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #read in header
    csv_header = next(csvreader)
    for row in csvreader:
        #create list of dates
        dates.append(row[0])
        #sum net profit/loss
        net_pl = net_pl + int(row[1])
        #create list of consecutive difference in profit/loss
        if months != 0: 
            diff.append(int(row[1]) - prev_pl)
        #sum months
        months += 1
        #assign new previous profit/loss
        prev_pl = int(row[1])
    
#create output variables
max_diff = max(diff)
min_diff = min(diff)
avg_change = sum(diff) / (months - 1)
inc_date = dates[diff.index(max_diff) + 1]
dec_date = dates[diff.index(min_diff) + 1]

#print results to terminal
print('Financial Analysis')
print('--------------------------')
print(f'Total Months: {months}')
print(f'Total: ${net_pl}')
print(f'Average Change: ${round(avg_change,2)}')
print(f'Greatest Increase in Profits: {inc_date} (${max_diff})')
print(f'Greatest Decrease in Profits: {dec_date} (${min_diff})')

#print results to text file
with open('PyBank/PyBank.txt','w') as text:
    text.write('Financial Analysis')
    text.write('\n--------------------------')
    text.write(f'\nTotal Months: {months}')
    text.write(f'\nTotal: ${net_pl}')
    text.write(f'\nAverage Change: ${round(avg_change,2)}')
    text.write(f'\nGreatest Increase in Profits: {inc_date} (${max_diff})')
    text.write(f'\nGreatest Decrease in Profits: {dec_date} (${min_diff})')