#calling matplotlib and numpy
import numpy as np
import matplotlib.pyplot as plt

#recieving info into function in a form on numpy array 
#in this one the frequency = 5 hz and sampling time is 0.01 sec
#if i use array i need to set time range for sampling
t = np.arange(0, 1, 0.01)
# Parameters
frequency = 5        # Frequency in Hertz
sampling_rate = 0.01   # Samples per second
duration = 1          # Duration in seconds of all the sinus graph

# Generate the sine wave based on time array created before
y = np.sin(2 * np.pi * 5 * t)
#this is the normal equation for sinus: y(t)=sin(2πft)
#np.pi*2 = 2 pi = 360 degrees
#sin = sin
#frequency = how much cycles in 1 sec
#t = time base = how much time and how much sampling -
'''
i created an array and multiply it by 360 degrees and frequency,
so every sample_size i set, it will check when in time fits the
cycle of sinus according to the frequency and draw a dot
arr = np.array([1, 2, 3, 4])
print(arr * 2)  # Output: [2 4 6 8]
'''
dy_dt = np.diff(y) / np.diff(t)  # נגזרת לפי הפרש
t_derivative = t[:-1]  # טווח זמן לנגזרת (ללא הערך האחרון)

# מציאת נקודות שבהן הנגזרת משנה סימן
zero_derivative_indices = []
for i in range(len(dy_dt) - 1):
    if dy_dt[i] > 0 and dy_dt[i + 1] < 0:  # שינוי מעלה למטה -> מקסימום
        zero_derivative_indices.append(i + 1)  # שמירה של האינדקס הבא
    elif dy_dt[i] < 0 and dy_dt[i + 1] > 0:  # שינוי למטה למעלה -> מינימום
        zero_derivative_indices.append(i + 1)

time = np.arange(0, 1, 0.01*5)
y_axis = np.sin(2 * np.pi * frequency * time)

# המרת אינדקסים לזמנים וערכים
zero_derivative_times = t[zero_derivative_indices]
zero_derivative_values = y[zero_derivative_indices]

# יצירת גרף
plt.figure(figsize=(8, 4))
plt.plot(time, y_axis, label="Sine Wave")  # גרף הסינוס
plt.scatter(zero_derivative_times, zero_derivative_values, color='red', label="Extrema")  # נקודות מקסימום ומינימום
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sine Wave with Extrema')
plt.legend()
plt.grid()
plt.show()