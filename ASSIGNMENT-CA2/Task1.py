import csv
# declare the variable that will hold all things
list_file = []
# declare variables to store the string input into
str_packets = []
str_tx = []
str_rx = []
# read the csv file and put everything in list_file
with open('Sample for task 1.csv', newline='') as f:
    reader = csv.reader(f)
    list_file = list(reader)
# iterate over items in the list and add them to their appropriate lists
for item in list_file:
    tempItem = ''.join(item)
    temp = tempItem.split(',')
    str_packets.append(temp[2])
    str_tx.append(temp[4])
    str_rx.append(temp[6])
# pop the first element of each list because that is just the title for column
str_packets.pop(0)
str_tx.pop(0)
str_rx.pop(0)
# declare variables for final strings
int_packets = []
int_tx = []
int_rx = []
# convert each item in each string
for val in str_packets:
    int_packets.append(int(val))
for val in str_tx:
    int_tx.append(int(val))
for val in str_rx:
    int_rx.append(int(val))
# declare final list
tx_calc = []
rx_calc = []
# multiply each by each and put into final list
for i in range(len(int_packets)):
    tx_calc.append(round((int_tx[i] / int_packets[i]) * 100))
    rx_calc.append(round((int_rx[i] / int_packets[i]) * 100))
# save into file
textfile = open('Task2.tr', 'w')
for i in range(len(tx_calc)):
    text = str(rx_calc[i]) + '	' + str(tx_calc[i])
    textfile.write(text)
    textfile.write('\n')
textfile.close()