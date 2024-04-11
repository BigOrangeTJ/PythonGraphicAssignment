import matplotlib.pyplot as plot

# set up your lists
numlist = [8, 6, 5, 3]
namelist = ['Freshmen', 'Sophomores', 'Juniors', 'Seniors']
colors = ['#3443E0', '#34E065', '#E03434', '#E0BB34']  # Using Hex for custom colors
explodelist = [0.0, 0., 0.0, 0.4]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colors, shadow=True,
         explode=explodelist, startangle=0)
plot.title("Richard Partridge\nPie Chart", size=15)  # Add a title with initials and larger font
plot.text(-1.3, 1.1, "RP2", size=30,  # Add initials in text box in the upper left corner
          ha="center", va="center",
          bbox=dict(boxstyle="round",
                    ec= '#42548B',
                    fc= '#3FA3E1',))
plot.axis('equal')
plot.savefig('PartridgePieChart.png')
