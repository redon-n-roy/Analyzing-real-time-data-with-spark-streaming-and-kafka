import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from kafka import KafkaConsumer
from datetime import datetime
import time
import threading
plt_val_x=[]
plt_val_y=[]
plt_val_y2=[]
plt_val_y3=[]
plt_val_y4=[]
city_name='Chennai'

def animate(i):
    global plt_val_x, plt_val_y

    axs[0, 0].cla()
    axs[0, 1].cla()
    axs[1, 0].cla()
    axs[1, 1].cla()   
    axs[0, 0].plot(plt_val_x, plt_val_y,color='blue')
    axs[0, 0].set_title('Temperature')
    axs[0, 1].plot(plt_val_x, plt_val_y2, color='green')
    axs[0, 1].set_title('Feels like')
    axs[1, 0].plot(plt_val_x, plt_val_y3, color = 'red')
    axs[1, 0].set_title('Pressure')
    axs[1, 1].plot(plt_val_x, plt_val_y4, color = 'purple')
    axs[1, 1].set_title('Relative Humidity')


plt.style.use('fivethirtyeight')

def plot():
    count = 0
    for message in consumer:
        if(message.value['city'] == city_name):
            plt_val_x.append(int(count))
            count += 5
            plt_val_y.append(float(message.value["temp"]))
            plt_val_y2.append(float(message.value["app_temp"]))
            plt_val_y3.append(float(message.value["pres"]))
            plt_val_y4.append(float(message.value["rh"]))

consumer = KafkaConsumer('output',bootstrap_servers=['localhost:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))

plot_thread = threading.Thread(target=plot)
plot_thread.start()

time.sleep(10)
fig, axs = plt.subplots(2, 2, figsize=(12,6), num = city_name) 
ani = FuncAnimation(plt.gcf(), animate, interval=1000) 
plt.tight_layout()
plt.show()





