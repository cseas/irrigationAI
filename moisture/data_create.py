import pandas as pd

l = []
import random
while len(l) < 680:
    # float
	l.append(random.uniform(237.8, 266.9).__round__(1))
    # integer
    # l.append(random.randint(117, 155))

df = pd.DataFrame(l)
# print(len(l))
# print(l)

#Stores the data in excel file
# writer = pd.ExcelWriter('keywords_extracted.csv', engine='xlsxwriter')
# df.to_excel(writer, sheet_name='Sheet1')
# writer.save()

df.to_csv("water_required.csv")