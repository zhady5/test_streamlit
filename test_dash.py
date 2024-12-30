import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Создание контейнера для всего содержимого
container = st.container()

# Настраиваем стили для фона и отступов
container.markdown(
    f"""
    <style>
        .css-1v4kyyz {{
            background-color: #ffb347 !important;
            margin-left: 10% !important;  /* Отступ слева */
            margin-right: 10% !important; /* Отступ справа */
            padding: 0 !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Заголовок
container.title("Мой Дашборд")

# Генерируем случайные данные для графиков
np.random.seed(42)
data = pd.DataFrame({
    'x': range(100),
    'y1': np.random.normal(loc=0, scale=1, size=100).cumsum(),
    'y2': np.random.normal(loc=0, scale=1, size=100).cumsum(),
    'y3': np.random.normal(loc=0, scale=1, size=100).cumsum(),
    'y4': np.random.normal(loc=0, scale=1, size=100).cumsum(),
    'y5': np.random.normal(loc=0, scale=1, size=100).cumsum(),
    'y6': np.random.normal(loc=0, scale=1, size=100).cumsum()
})

# Индикаторы
col1, col2, col3, col4 = container.columns(4)
with col1:
    container.metric(label="Индикатор 1", value=np.random.randint(500))
with col2:
    container.metric(label="Индикатор 2", value=np.random.randint(200))
with col3:
    container.metric(label="Индикатор 3", value=np.random.randint(300))
with col4:
    container.metric(label="Индикатор 4", value=np.random.randint(400))

# Разделение на три строки для графиков
row1, row2, row3 = container.columns((1, 1, 1))

# Первый ряд графиков
with row1:
    fig1, ax1 = plt.subplots()
    sns.lineplot(x=data['x'], y=data['y1'], ax=ax1)
    container.pyplot(fig1)
    
    fig2, ax2 = plt.subplots()
    sns.barplot(x=data['x'], y=data['y2'], ax=ax2)
    container.pyplot(fig2)

# Второй ряд графиков
with row2:
    fig3, ax3 = plt.subplots()
    sns.scatterplot(x=data['x'], y=data['y3'], ax=ax3)
    container.pyplot(fig3)
    
    fig4, ax4 = plt.subplots()
    sns.histplot(data['y4'], kde=True, ax=ax4)
    container.pyplot(fig4)

# Третий ряд графиков
with row3:
    fig5, ax5 = plt.subplots()
    sns.boxplot(y=data['y5'], ax=ax5)
    container.pyplot(fig5)
    
    fig6, ax6 = plt.subplots()
    sns.kdeplot(data['y6'], shade=True, ax=ax6)
    container.pyplot(fig6)

# Дополнительное описание
container.write("""
### Описание данных
Это тестовые данные, которые были сгенерированы случайным образом для демонстрации возможностей дашборда.
""")
