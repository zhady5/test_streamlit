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


# Применение пользовательского CSS
st.markdown("""
<style>
    .reportview-container {
        background-color: white;
    }
    .main {
        background-color: white;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        background-color: #ffb347;
        padding: 2rem;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    
    /* Медиа-запрос для мобильных устройств */
    @media (max-width: 768px) {
        .stApp {
            padding: 1rem;
        }
    }

    h1, h2, h3, h4 {
        font-family: 'Open Sans', sans-serif;
        color: #333;
        font-weight: 600;
    }
    p {
        font-family: 'Open Sans', sans-serif;
        color: #666;
        font-size: 14px;
        line-height: 1.6;
    }
    .metric-card {
        background-color: #f5dfbf;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .metric-value {
        font-size: 18px;
        font-weight: 600;
        color: #333;
    }
    .stSelectbox {
        background-color: #f5dfbf;
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
    ax.grid(False)

# Настройка стиля графиков
#plt.style.use('seaborn')
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
sns.set_palette(sns.color_palette(colors))
sns.set(rc={"axes.facecolor": "#ffb347", "figure.facecolor": "#ffb347"})
#sns.axes_style("ticks")
#sns.despine()

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

