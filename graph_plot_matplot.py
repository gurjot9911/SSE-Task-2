import matplotlib.pyplot as plt
import numpy as np

x = np.array([2020,2021,2022,2023,2024])
y1 = np.array([20,25,50,15,40])
y2 = np.array([30,55,10,18,35])
y3 = np.array([22,42,31,58,26])

plt.title ("Random Graph",fontsize=20,family="Arial",fontweight="bold",color="#45089A")

plt.xlabel("Year",fontsize=15,family="Arial",fontweight="bold",color="#24D009")
plt.ylabel("Value",fontsize=15,family="Arial",fontweight="bold",color="#24D009")

line_style = dict(
    mec = "#d90928",
    mfc = "#d90928",
    markersize = 12,
    linewidth = 2,
    marker = "."
)

plt.tick_params(axis="both",color = "#03273E")
plt.plot(x,y2,**line_style,color = "#9A085B")
plt.plot(x,y1,**line_style,color = "#045733")
plt.plot(x,y3,**line_style,color = "#e8a30e")

plt.xticks(x)

plt.show()