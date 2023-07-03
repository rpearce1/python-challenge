import csv

months = 0
net_pl = 0
prev_pl = 0
diff = []
dates = []

with open('PyBank/Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    for row in csvreader:
        dates.append(row[0])
        net_pl = net_pl + int(row[1])
        if months != 0: 
            diff.append(int(row[1]) - prev_pl)
        months += 1
        prev_pl = int(row[1])
    
max_diff = max(diff)
min_diff = min(diff)
avg_change = sum(diff) / (months - 1)
inc_date = dates[diff.index(max_diff) + 1]
dec_date = dates[diff.index(min_diff) + 1]

