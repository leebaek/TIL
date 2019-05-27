lunch = {
    '양자강' : '02-557-4211',
    '감밥카페' : '02-553-3181',
    '순남시래기' : '02-588-0887'
}

# 1. f-string
# with open('lunch.csv', 'w', encoding='utf-8') as f:
#     for item in lunch.items(): # .items() : [('양자강', '02-557-4211'), (...), (...)]
#         f.write(f'{item[0]},{item[1]}\n')

# 2. join()
# with open('lunch.csv', 'w', encoding='utf-8') as f:
#     for item in lunch.items(): # .items() : [('양자강', '02-557-4211'), (...), (...)]
#         f.write(','.join(item)+'\n')
        # 'a'.join(('양자강', '02-557-4211', '역삼동'))
        # => 양자강a02-557-4211a역삼동

# 3. csv
import csv
with open('lunch.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item)