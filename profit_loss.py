#writing custom function called "profitloss_function()"
def profitloss_function():
    """
    - If the business' net profit only increases everyday, the function will indicate this and state the highest net profit surplus and the day in which it occured
    - If the busienss' net profit is fluctuating (not always increasing everyday), the function will state all the net profit deficits and the days in which they occur respectively. It will also state the highest net profit deficit and the day in which it occured
    - This function does not require any parameters
    """
    #from pathlib modlule, import the Path class
    from pathlib import Path
    #import csv module
    import csv

    # create a file path to csv file.
    file_path= Path.cwd()/"csv_reports"/"profit_loss.csv"

    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty lists to store day and net profit
        net_profit_list=[] 

        # append day and net profit into the "net_profit_list" list
        for row in reader:
            #get the day, and net profit for each record
            #and append the "net_profit_list" list
            net_profit_list.append([row[0], row[4]])

    #creating empty dictionary "net_profit_dict"
    net_profit_dict= {}
    #starting for loop
    for net_profit in net_profit_list:
        #convert the day into integer
        day = int(net_profit[0])
        #change amount to float
        amount = float(net_profit[1])
        #write dictionary with "day" as key and "amount" as value
        net_profit_dict[day] = amount

    #creating empty dictionary "net_profit_diff"
    net_profit_diff= {}
    #starting for loop for day 1 to day 90
    for day in range(1, len(net_profit_dict)):
        #calculate difference between current day and previous day net profit and round the calculated value to 2 decimal places
        difference= (net_profit_dict[day]) - (net_profit_dict[day - 1])
        difference= round(difference, 2)
        #write dictionary with "day" as key and "difference" as value
        net_profit_diff[day] = difference

    #create empty lists of "profit_deficit" and "profit_surplus"
    profit_deficit= []
    profit_surplus= []
    #starting for loop
    for day in net_profit_diff:
        #add deficit values to the "profit_deficit" list and surplus values to the "profit_surplus" list
        if net_profit_diff[day] <= 0:
            profit_deficit.append(net_profit_diff[day])
        else:
            profit_surplus.append(net_profit_diff[day])

    #create a file path to text file
    file_path= Path.cwd()/"summary_report.txt"

    #if there are profit deficits, state all deficits and the days which they occur
    #also, state the highest deficit and the day which it occured
    if len(profit_deficit) > 0:
        for day in net_profit_diff:
            if net_profit_diff[day] <= 0:
                #open the file "summary_report.txt" for appending with UTF-8 encoding and state all deficits and the days which they occur
                with file_path.open(mode= "a", encoding= "UTF-8") as file:
                    file.write(f'[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{abs(net_profit_diff[day])}\n')
        profit_deficit.sort()
        highest_deficit= profit_deficit[0]
        for day in net_profit_diff:
            if net_profit_diff[day] == highest_deficit:
                #open the file "summary_report.txt" for appending with UTF-8 encoding and state the highest deficit and the day which it occured
                with file_path.open(mode= "a", encoding= "UTF-8") as file:
                    file.write(f'[HIGHEST PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{abs(net_profit_diff[day])}')
    #if net profit always increases everyday, state the message saying so
    #also, state the highest net profit surplus and the day which it occured
    else:
        #open the file "summary_report.txt" for appending with UTF-8 encoding and state the message saying net profit always increases everyday
        with file_path.open(mode= "a", encoding= "UTF-8") as file:
            file.write(f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n')
        profit_surplus.sort(reverse= True)
        highest_surplus= profit_surplus[0]
        for day in net_profit_diff:
            if net_profit_diff[day] == highest_surplus:
                #open the file "summary_report.txt" for appending with UTF-8 encoding and state the highest net profit surplus and the day which it occured
                with file_path.open(mode= "a", encoding= "UTF-8") as file:
                    file.write(f'[HIGHEST NET PROFIT SURPLUS] DAY: {day}, AMOUNT: USD{net_profit_diff[day]}')
