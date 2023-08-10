#import the "overheads", "cash_on_hand" and "profit_loss" modules
import overheads, cash_on_hand, profit_loss

#writing custom fuction called "main()" to create the output file and carry out the functions in the three imported modules
def main():
    from pathlib import Path
    # create a path object "file_path" which contains the file path to the new file "summary_report.txt" that I want to create
    file_path= Path.cwd()/"project_group"/"summary_report.txt"
    file_path.touch()
    overheads.overhead_function()
    cash_on_hand.coh_function()
    profit_loss.profitloss_function()

#activate the "main()" function
main()
