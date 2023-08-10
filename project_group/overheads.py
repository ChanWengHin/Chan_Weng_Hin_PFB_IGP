#writing custom function called "overhead_function()"
def overhead_function():
    """
    - This function will return the highest overhead catagory and its weightage
    - This function does not require any parameters
    """
    #from pathlib modlule, import the Path class
    from pathlib import Path
    #import csv module
    import csv

    # create a file path to csv file.
    file_path= Path.cwd()/"csv_reports"/"overheads.csv"

    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty lists to store expense category and expense percentage
        overheads=[] 

        # append expense category and expense percentage into the "overheads" list
        for row in reader:
            #get the expense category and expense percentage for each record
            #and append the "overheads" list
            overheads.append([row[0], row[1]])

    #create empty list "percentage_summary"
    percentage_summary= []
    #starting for loop
    for expenses in overheads: 
        expense_type = expenses[0]
        #replace percentage stored as string as a float value
        expenses[1]= float(expenses[1])
        percentage = expenses[1]
        #add percentage expense from each category to the "percentage_summary" list
        percentage_summary.append(percentage)
    #sort values in "percentage_summary" in decending order
    percentage_summary.sort( reverse=True)
    #extracting the highest percentage in "percentage_summary" and saving it to the "highest_percentage" variable
    highest_percentage= percentage_summary[0]

    #starting for loop
    for expenses in overheads:
        #look for the expense category that has the highest expense percentage stored in "highest_percentage" variable
        if expenses[1] == highest_percentage:
            print(f'Highest overhead category is {expenses[0]} at {highest_percentage}%')
