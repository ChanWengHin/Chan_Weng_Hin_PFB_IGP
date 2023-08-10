#writing custom function called "coh_function()"
def coh_function():
    """
    - If the business' cash only increases everyday, the function will indicate this and state the highest cash surplus and the day in which it occured
    - If the busienss' cash is fluctuating (not always increasing everyday), the function will state all the cash deficits and the days in which they occur respectively. It will also state the highest cash deficit and the day in which it occured
    - This function does not require any parameters
    """
    #from pathlib modlule, import the Path class
    from pathlib import Path
    #import csv module
    import csv

    # create a file path to csv file.
    file_path= Path.cwd()/"csv_reports"/"cash_on_hand.csv"

    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty lists to store day and cash on hand
        coh_list=[] 

        # append day and cash on hand into the "coh_list" list
        for row in reader:
            #get the day, and cash on hand for each record
            #and append the "coh_list" list
            coh_list.append([row[0], row[1]])

    #creating empty dictionary "coh_dict"
    coh_dict= {}
    #starting for loop
    for cash_on_hand in coh_list:
        #convert the day into integer
        day = int(cash_on_hand[0])
        #change amount to float
        amount = float(cash_on_hand[1])
        #write dictionary with "day" as key and "amount" as value
        coh_dict[day] = amount

    #creating empty dictionary "coh_diff"
    coh_diff= {}
    #starting for loop for day 1 to day 90
    for day in range(1, len(coh_dict)):
        #calculate difference between current day and previous day net profit and round the calculated value to 2 decimal places
        difference= (coh_dict[day]) - (coh_dict[day - 1])
        difference= round(difference, 2)
        #write dictionary with "day" as key and "difference" as value
        coh_diff[day] = difference

    coh_deficit= []
    coh_surplus=[]
    #starting for loop
    for day in coh_diff:
        #add deficit values to the "coh_deficit" list and surplus values to the "coh_surplus" list
        if coh_diff[day] <= 0:
            coh_deficit.append(coh_diff[day])
        else:
            coh_surplus.append(coh_diff[day])

    #create a file path to text file.
    file_path= Path.cwd()/"project_group"/"summary_report.txt"

    #if there are cash deficits, state all deficits and the days which they occur
    #also, state the highest deficit and the day which it occured
    if len(coh_deficit) > 0:
        for day in coh_diff:
            if coh_diff[day] <= 0:
                #open the file "summary_report.txt" for appending with UTF-8 encoding and append the message stating all deficits and the days which they occur
                with file_path.open(mode= "a", encoding= "UTF-8") as file:
                    file.write(f'[CASH DEFICIT] DAY: {day}, AMOUNT: USD{abs(coh_diff[day])}\n')
        coh_deficit.sort()
        highest_deficit= coh_deficit[0]
        for day in coh_diff:
            if coh_diff[day] == highest_deficit:
                #open the file "summary_report.txt" for appending with UTF-8 encoding and state the highest deficit and the day which it occured
                with file_path.open(mode= "a", encoding= "UTF-8") as file:
                    file.write(f'[HIGHEST CASH DEFICIT] DAY: {day}, AMOUNT: USD{abs(coh_diff[day])}\n')

    #if cash on hand always increases everyday, write the message saying so
    #also, state the highest cash surplus and the day which it occured
    else:
        #open the file "summary_report.txt" for appending with UTF-8 encoding and write the message saying cash on hand always increases everyday
        with file_path.open(mode= "a", encoding= "UTF-8") as file:
            file.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        coh_surplus.sort(reverse= True)
        highest_surplus= coh_surplus[0]
        for day in coh_diff:
            if coh_diff[day] == highest_surplus:
                #open the file "summary_report.txt" for appending with UTF-8 encoding and state the highest cash surplus and the day which it occured
                with file_path.open(mode= "a", encoding= "UTF-8") as file:
                    file.write(f'[HIGHEST CASH SURPLUS] DAY: {day}, AMOUNT: USD{coh_diff[day]}\n')
