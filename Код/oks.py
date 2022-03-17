import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
# Используем Seaborn, чтобы нарисовать линейный график
df = pd.DataFrame({'x': x, 'y': y})
sns.lineplot(x="x", y="y", data=df)
plt.show()
