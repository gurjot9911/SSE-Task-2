import matplotlib.pyplot as plt

x = [2020,2021,2022,2023,2024]
y1 = [70,80,91,75,80]
y2 = [63,55,89,90,69]
y3 = [58,57,91,63,77]

line_style = dict(
    color = "#fcfb55",
    mec = "#1c5bfc",
    mfc = "#1cfc45",
    markersize = 25,
    linewidth = 4,
    marker = "."
)

plt.plot(x,y2,**line_style)
plt.plot(x,y1,**line_style)
plt.plot(x,y3,**line_style)

plt.show()