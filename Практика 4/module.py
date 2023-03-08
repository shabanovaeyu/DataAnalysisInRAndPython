import pandas as pd

ok = 'Correct'
no = 'Incorrect'

items = pd.read_csv('items.csv', sep=';', decimal=',')
groups = pd.read_csv('groups.csv', sep=';')
names = pd.read_csv('names.csv', sep=',')

answer_41 = names.rename(columns={'Сокращенное название категории': 'Категория(сокр.)'})

rows = [
        ['Вафли с фр-ми начинками', 3.2, 2.8, 80.9], 
        ['Вафли с жировыми начинками', 3.4, 30.2, 64.7], 
        ['Пирожное трубочка с кремом', 1.7, 25.2, 50.9],
        ['Пирожное воздушное', 3.1, 16.3, 68.5], 
        ['Пряники', 5.8, 6.5, 71.6], 
        ['Торт ассорти', 4.7, 15, 36], 
        ['Торт Прага', 4.6, 26.5, 65.1]
        ]

answer_51 = items.copy()

for row in rows:
    answer_51.loc[len(answer_51)] = row

answer_61 = pd.merge(answer_51, groups, on=['Товар'], how='inner')
answer_61 = pd.merge(answer_61, answer_41, on=['Категория'], how='inner')

answer_71 = answer_61.copy()
answer_71['Калорийность'] = answer_71['Белки'] * 4 + answer_71['Жиры'] * 9 + answer_71['Углеводы'] * 4
answer_71['Калорийность(Дж)'] = answer_71['Калорийность'] * 4.1868

df = answer_71.copy()

selection_81 = df.loc[df['Категория'] == 'Сладости']
selection_82 = df.loc[df['Калорийность'] > 700]
selection_83 = df.loc[df['Белки'] == 0]
selection_84 = df.loc[df['Категория'].isin(['Сладости', 'Орехи', 'Яйца'])]
selection_85 = df.loc[(df['Белки'] >= 5) & ((df['Белки'] <= 10))]
selection_86 = df.loc[(df['Калорийность']>=500) & (df['Калорийность'] <= 550)]
selection_87 = df.loc[(df['Категория'] == 'Колбаса') & (df['Белки'] > 20)]
selection_88 = df.loc[(df['Категория'].isin(['Колбаса', 'Яйца'])) & (df['Белки'] > 15)]
selection_89 = df.loc[(df['Белки'] > 20 ) & (df['Жиры'] < 10)]
selection_810 = df.loc[(df['Белки'] == 0) & (df['Углеводы'] == 0)]
selection_811 = df.loc[(df['Белки'] == 0) & (df['Жиры'] == 0)]
selection_812 = df.loc[(df['Калорийность'] >= 400) & (df['Калорийность'] <= 500) & (df['Углеводы'] == 0)]

check_dict = {
              'task 1.1': items,
              'task 1.2': groups,
              'task 1.3': names,
              'task 2.1': len(items),
              'task 2.2': len(groups),
              'task 2.3': len(names),
              'task 3.1': items.columns,
              'task 3.2': groups.columns,
              'task 3.3': names.columns,
              'task 4.1': answer_41,
              'task 5.1': answer_51,
              'task 6.1': answer_61,
              'task 7.1': answer_71,
              'task 8.1': selection_81,
              'task 8.2': selection_82,
              'task 8.3': selection_83,
              'task 8.4': selection_84,
              'task 8.5': selection_85,
              'task 8.6': selection_86,
              'task 8.7': selection_87,
              'task 8.8': selection_88,
              'task 8.9': selection_89,
              'task 8.10': selection_810,
              'task 8.11': selection_811,
              'task 8.12': selection_812,
              }

comparable = ['task 2.1', 'task 2.2', 'task 2.3']

def check(task_number, answer):
    if task_number in comparable:
        if check_dict[task_number] == answer:
            print(ok)
        else:
            print(no)
    else:
        if check_dict[task_number].equals(answer):
            print(ok)
        else:
            print(no)










