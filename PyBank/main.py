import os
import csv

path = os.path.join('Resources', 'budget_data.csv')

def read_a_csv(csvpath):
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        data = []
        for row in csvreader:
            data.append(row)

    return data

def total_months(data):
    # row_number = 0
    # for row in data:
    #     row_number += 1
    # return row_number
    return len(data)

def total_profit_loss(data):
    profit_loss = 0
    for row in data:
        profit_loss += int(row[1])
    return profit_loss

def change_in_profit(data):
    first_month_profit = int(data[0][1])
    last_month_profit = int(data[-1][1])
    return first_month_profit - last_month_profit

def change_in_profit_list(data):
    changes_in_profit = []
    first_row = int(data[0][1])
    for row in data[1:]:
        current_row = int(row[1])
        change = current_row - first_row
        changes_in_profit.append(change)
        first_row = current_row
    return changes_in_profit

def avg_of_list(list_of_numbers):
    return sum(list_of_numbers) / len(list_of_numbers)

def greatest_inc_dec(list_of_changes):
    greatest_inc = max(list_of_changes)
    greatest_dec = min(list_of_changes)
    return [greatest_inc, greatest_dec]



data = read_a_csv(path)
print("Financial Analysis")
print("-------------------------")
print("Total Months: ", total_months(data))
print(f"Total: ${total_profit_loss(data)}")
changes = change_in_profit_list(data)
print(f"Average Change: S{round(avg_of_list(changes), 2)}")
print(f"Greatest increase and decrease: {greatest_inc_dec(changes)}")
