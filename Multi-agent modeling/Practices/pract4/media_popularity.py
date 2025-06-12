import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

# Параметры симуляции
NUM_AGENTS = 150  # Количество агентов
BASE_PROB_SUBSCRIBE = {
    "Telegram": 0.06,  # Базовая вероятность подписки на Telegram
    "TV": 0.04,       # Базовая вероятность подписки на TV
    "X": 0.05         # Базовая вероятность подписки на X
}
BASE_PROB_SWITCH = {
    "Telegram": 0.02,  # Базовая вероятность переключения на Telegram
    "TV": 0.015,       # Базовая вероятность переключения на TV
    "X": 0.018        # Базовая вероятность переключения на X
}
PROB_RECOMMEND = 0.12  # Базовая вероятность рекомендации СМИ
SANCTIONS_FACTOR = 0.333  # Множитель для вероятностей X при санкциях (1/3)
OBSERVATION_PERIOD = 180  # Срок наблюдения в днях

# Размеры прямоугольной области
WIDTH = 10
HEIGHT = 10

# День наблюдения
day_count = 0

# Инициализация уровня цифровизации и состояния санкций
digitalization_level = 0.5
sanctions_active = False

# Создание популяции агентов
agents = []
for i in range(NUM_AGENTS):
    agent = {
        "media": "none",  # Тип СМИ: "none", "Telegram", "TV" или "X"
        "x": random.random() * WIDTH,  # Фиксированная x-координата
        "y": random.random() * HEIGHT  # Фиксированная y-координата
    }
    agents.append(agent)

# Инициализация данных для графика
num_none = []       # Количество неподписанных агентов
num_telegram = []   # Количество подписчиков Telegram
num_tv = []         # Количество подписчиков TV
num_x = []          # Количество подписчиков X

# Функция для пересчета вероятностей на основе уровня цифровизации и санкций
def update_probabilities(digitalization, sanctions):
    prob_subscribe = {}
    prob_switch = {}
    
    # Модификация вероятностей подписки
    tv_boost = (1 - digitalization) * 0.1
    digital_boost = digitalization * 0.1
    
    prob_subscribe["TV"] = min(BASE_PROB_SUBSCRIBE["TV"] + tv_boost, 0.15)
    prob_subscribe["Telegram"] = max(BASE_PROB_SUBSCRIBE["Telegram"] - tv_boost / 2 + digital_boost / 2, 0.01)
    prob_subscribe["X"] = max(BASE_PROB_SUBSCRIBE["X"] - tv_boost / 2 + digital_boost / 2, 0.01)
    
    # Модификация вероятностей переключения
    prob_switch["TV"] = min(BASE_PROB_SWITCH["TV"] + tv_boost / 2, 0.1)
    prob_switch["Telegram"] = max(BASE_PROB_SWITCH["Telegram"] - tv_boost / 4 + digital_boost / 4, 0.005)
    prob_switch["X"] = max(BASE_PROB_SWITCH["X"] - tv_boost / 4 + digital_boost / 4, 0.005)
    
    # Применение санкций к X
    prob_recommend_x = PROB_RECOMMEND
    if sanctions:
        prob_subscribe["X"] *= SANCTIONS_FACTOR
        prob_switch["X"] *= SANCTIONS_FACTOR
        prob_recommend_x *= SANCTIONS_FACTOR
    
    return prob_subscribe, prob_switch, prob_recommend_x

# Инициализация вероятностей
prob_subscribe, prob_switch, prob_recommend_x = update_probabilities(digitalization_level, sanctions_active)

# Функция обновления для анимации
def update(frame):
    global day_count, prob_subscribe, prob_switch, prob_recommend_x
    
    # Пересчет вероятностей
    prob_subscribe, prob_switch, prob_recommend_x = update_probabilities(digitalization_level, sanctions_active)

    # Обновление агентов
    for agent in agents:
        if agent["media"] == "none":
            # Неподписанный агент может подписаться
            for media, prob in prob_subscribe.items():
                if random.random() < prob:
                    agent["media"] = media
                    break
        else:
            # Подписанный агент может переключиться
            for media, prob in prob_switch.items():
                if media != agent["media"] and random.random() < prob:
                    agent["media"] = media
                    break
            # Подписанный агент может порекомендовать свое СМИ
            recommend_prob = prob_recommend_x if agent["media"] == "X" else PROB_RECOMMEND
            if random.random() < recommend_prob:
                other_agent = random.choice(agents)
                if other_agent["media"] != agent["media"]:
                    other_agent["media"] = agent["media"]

    # Подсчет количества агентов по типам СМИ
    num_none.append(len([agent for agent in agents if agent["media"] == "none"]))
    num_telegram.append(len([agent for agent in agents if agent["media"] == "Telegram"]))
    num_tv.append(len([agent for agent in agents if agent["media"] == "TV"]))
    num_x.append(len([agent for agent in agents if agent["media"] == "X"]))

    # Отображение агентов
    ax1.cla()
    ax1.set_xlim(0, WIDTH)
    ax1.set_ylim(0, HEIGHT)
    for agent in agents:
        if agent["media"] == "none":
            ax1.scatter(agent["x"], agent["y"], c="gray", label="None" if "None" not in ax1.get_legend_handles_labels()[1] else "")
        elif agent["media"] == "Telegram":
            ax1.scatter(agent["x"], agent["y"], c="blue", label="Telegram" if "Telegram" not in ax1.get_legend_handles_labels()[1] else "")
        elif agent["media"] == "TV":
            ax1.scatter(agent["x"], agent["y"], c="red", label="TV" if "TV" not in ax1.get_legend_handles_labels()[1] else "")
        elif agent["media"] == "X":
            ax1.scatter(agent["x"], agent["y"], c="green", label="X" if "X" not in ax1.get_legend_handles_labels()[1] else "")

    # Отображение графика
    ax2.cla()
    ax2.plot(num_none, label="Неподписанные", c="gray")
    ax2.plot(num_telegram, label="Telegram", c="blue")
    ax2.plot(num_tv, label="TV", c="red")
    ax2.plot(num_x, label="X", c="green")
    ax2.set_xlabel("День")
    ax2.set_ylabel("Количество агентов")
    ax2.legend(loc='upper right', fontsize=8, framealpha=0.3)

    day_count += 1
    if day_count >= OBSERVATION_PERIOD:
        plt.close()
        return

# Создание фигуры и осей
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
plt.subplots_adjust(bottom=0.3)

# Создание ползунка
ax_slider = plt.axes([0.15, 0.15, 0.65, 0.03])
slider = Slider(ax_slider, 'Уровень цифровизации', 0.0, 1.0, valinit=digitalization_level)

# Создание кнопки
ax_button = plt.axes([0.8, 0.05, 0.1, 0.04])
button = Button(ax_button, 'Санкции', hovercolor='0.975')

# Обработчик ползунка
def update_slider(val):
    global digitalization_level
    digitalization_level = slider.val
slider.on_changed(update_slider)

# Обработчик кнопки
def toggle_sanctions(event):
    global sanctions_active
    sanctions_active = not sanctions_active
    button.label.set_text('Санкции (вкл)' if sanctions_active else 'Санкции (выкл)')
button.on_clicked(toggle_sanctions)

# Создание анимации
ani = animation.FuncAnimation(fig, update, interval=100, save_count=OBSERVATION_PERIOD)
plt.show()