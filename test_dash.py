
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Установка цвета фона и стиля страницы
st.set_page_config(
    page_title="Мой Дашборд",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Применение пользовательского CSS для изменения цвета фона и стилей
st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stPlotlyChart {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Заголовок
st.title("Мой Дашборд")

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
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Индикатор 1", value=np.random.randint(500))
with col2:
    st.metric(label="Индикатор 2", value=np.random.randint(200))
with col3:
    st.metric(label="Индикатор 3", value=np.random.randint(300))
with col4:
    st.metric(label="Индикатор 4", value=np.random.randint(400))

# Разделение на три строки для графиков
row1, row2, row3 = st.columns((1, 1, 1))

# Функция для создания и отображения графика
def plot_chart(data, x, y, kind, ax):
    if kind == 'line':
        sns.lineplot(x=data[x], y=data[y], ax=ax)
    elif kind == 'bar':
        sns.barplot(x=data[x], y=data[y], ax=ax)
    elif kind == 'scatter':
        sns.scatterplot(x=data[x], y=data[y], ax=ax)
    elif kind == 'hist':
        sns.histplot(data[y], kde=True, ax=ax)
    elif kind == 'box':
        sns.boxplot(y=data[y], ax=ax)
    elif kind == 'kde':
        sns.kdeplot(data[y], shade=True, ax=ax)
    ax.set_title(f"{kind.capitalize()} Plot")
    ax.set_xlabel(x)
    ax.set_ylabel(y)

# Первый ряд графиков
with row1:
    fig1, ax1 = plt.subplots()
    plot_chart(data, 'x', 'y1', 'line', ax1)
    st.pyplot(fig1)
    
    fig2, ax2 = plt.subplots()
    plot_chart(data, 'x', 'y2', 'bar', ax2)
    st.pyplot(fig2)

# Второй ряд графиков
with row2:
    fig3, ax3 = plt.subplots()
    plot_chart(data, 'x', 'y3', 'scatter', ax3)
    st.pyplot(fig3)
    
    fig4, ax4 = plt.subplots()
    plot_chart(data, 'x', 'y4', 'hist', ax4)
    st.pyplot(fig4)

# Третий ряд графиков
with row3:
    fig5, ax5 = plt.subplots()
    plot_chart(data, 'x', 'y5', 'box', ax5)
    st.pyplot(fig5)
    
    fig6, ax6 = plt.subplots()
    plot_chart(data, 'x', 'y6', 'kde', ax6)
    st.pyplot(fig6)

# Дополнительное описание
st.write("""
### Описание данных
Это тестовые данные, которые были сгенерированы случайным образом для демонстрации возможностей дашборда.
""")
```
