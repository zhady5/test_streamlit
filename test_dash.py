import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Установка цвета фона и стиля страницы
st.set_page_config(
    page_title="Аналитический Дашборд",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Применение пользовательского CSS для стиля New York Times
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Source+Sans+Pro:wght@400;600&display=swap');
    
    .stApp {
        background-color: #ffffff;
    }
    .main {
        max-width: 900px;
        margin: 0 auto;
        padding: 0 20px;
    }
    .stMetric {
        background-color: #f8f8f8;
        padding: 20px;
        border: 1px solid #e0e0e0;
        font-family: 'Source Sans Pro', sans-serif;
    }
    .stPlotlyChart, div[data-testid="stDecoration"] {
        background-color: #ffffff;
        padding: 20px;
        border: 1px solid #e0e0e0;
    }
    h1 {
        font-family: 'Playfair Display', serif;
        font-size: 48px;
        font-weight: 700;
        color: #121212;
        margin-bottom: 30px;
        text-align: center;
    }
    h3 {
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        font-weight: 700;
        color: #121212;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    p, .stMarkdown {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 18px;
        line-height: 1.6;
        color: #333333;
    }
    .stSidebar {
        background-color: #f8f8f8;
        border-right: 1px solid #e0e0e0;
    }
    .stSidebar .stMarkdown {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# Оборачиваем содержимое в div с классом 'main'
st.markdown('<div class="main">', unsafe_allow_html=True)

# Заголовок
st.title("Аналитический Дашборд")

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
st.subheader("Ключевые Показатели")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Показатель 1", value=f"{np.random.randint(500):,}")
with col2:
    st.metric(label="Показатель 2", value=f"{np.random.randint(200):,}")
with col3:
    st.metric(label="Показатель 3", value=f"{np.random.randint(300):,}")
with col4:
    st.metric(label="Показатель 4", value=f"{np.random.randint(400):,}")

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
    ax.set_title(f"{kind.capitalize()} Plot", fontsize=16, fontweight='bold')
    ax.set_xlabel(x, fontsize=12)
    ax.set_ylabel(y, fontsize=12)
    ax.tick_params(labelsize=10)

# Настройка стиля графиков
#plt.style.use('seaborn')
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
sns.set_palette(sns.color_palette(colors))

# Графики
st.subheader("Анализ Данных")

# Первый ряд графиков
col1, col2 = st.columns(2)
with col1:
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    plot_chart(data, 'x', 'y1', 'line', ax1)
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    plot_chart(data, 'x', 'y2', 'bar', ax2)
    st.pyplot(fig2)

# Второй ряд графиков
col3, col4 = st.columns(2)
with col3:
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    plot_chart(data, 'x', 'y3', 'scatter', ax3)
    st.pyplot(fig3)

with col4:
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    plot_chart(data, 'x', 'y4', 'hist', ax4)
    st.pyplot(fig4)

# Третий ряд графиков
col5, col6 = st.columns(2)
with col5:
    fig5, ax5 = plt.subplots(figsize=(6, 4))
    plot_chart(data, 'x', 'y5', 'box', ax5)
    st.pyplot(fig5)

with col6:
    fig6, ax6 = plt.subplots(figsize=(6, 4))
    plot_chart(data, 'x', 'y6', 'kde', ax6)
    st.pyplot(fig6)

# Дополнительное описание
st.write("""
### Описание данных

Это тестовые данные, которые были сгенерированы случайным образом для демонстрации возможностей дашборда. 
Каждый график представляет различные аспекты анализа данных:

1. **Линейный график** показывает тренд изменения значений во времени.
2. **Столбчатая диаграмма** отображает сравнение категорий или групп данных.
3. **Точечная диаграмма** используется для визуализации корреляций между двумя переменными.
4. **Гистограмма** показывает распределение значений в наборе данных.
5. **Ящик с усами** отображает статистические характеристики набора данных.
6. **График плотности** показывает распределение вероятности непрерывной случайной величины.

Эти визуализации помогают лучше понять структуру и характеристики данных, выявить закономерности и аномалии.
""")

# Закрываем div с классом 'main'
st.markdown('</div>', unsafe_allow_html=True)

