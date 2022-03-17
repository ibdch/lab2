import pandas as pd
import matplotlib.pyplot as plt

# подготовка данных
data = pd.read_csv('oks.csv',sep=r'\s*,\s*', header=0, encoding='utf8', engine='python')
x = data['Дата'].to_numpy()
y = data['Стоимость'].to_numpy()
# даем название осям и графику
plt.xlabel('Дата')
plt.ylabel('Стоимость')
plt.title('Динамика изменения цен товара')
# Используем Matplotlib, чтобы нарисовать линейную диаграмму
plt.plot(x, y)
plt.show()

