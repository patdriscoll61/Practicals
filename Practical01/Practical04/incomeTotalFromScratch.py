
months = int(input("How many months? "))
income_list = []
total = 0

for i in range(months):
    income = float(input("Enter income for month {}: ".format(i+1)))
    income_list.append(income)
print("Income Report")
print("-------------")
for i in range(len(income_list)):
    total += income_list[i]
    print("Month {} - Income: $  {} Total: $ {}".format(i+1,income_list[i],total) )
