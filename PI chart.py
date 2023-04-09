import matplotlib.pyplot as plt 

Sports = ["Football", "Basketball", "Tennis", "Soccer", "Badminton", "Hockey"]



slices = [12, 13, 5, 8, 3, 15]

colors = ['lightcoral', 'beige', 'navajowhite', 'peachpuff', 'lightpink', 'lightskyblue']



plt.pie(slices, labels = Sports, colors=colors,
        startangle=300, shadow = True, explode = (0, 0, 0.2, 0, 0.4, 0),
        radius = 0.8, autopct = '%2.1f%%')

plt.legend()
    

plt.show()