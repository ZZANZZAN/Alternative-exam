import pandas as pd
from tkinter import Tk, END, LabelFrame, Text, Label, Frame, Button, LEFT
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from numpy import abs as np_abs
from numpy.fft import rfft
import soundfile as sf
import numpy as np
import os
import ffmpeg
from pydub import AudioSegment

sc = StandardScaler()
len_spectr = 250 #длина спектра
data = pd.read_csv(os.getcwd() + "\music_library.csv", sep = ';')
X = data.iloc[:, 0:len_spectr].values #спектры взятые из файла
y = data.iloc[:, 255].values 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50) #распределение полученных данных на тестовые и тренировочные
X_train = sc.fit_transform(X_train) #подготовка входных данных для обучения случайного леса
regressor = RandomForestClassifier(n_estimators=200, random_state=1) #создание случайного леса
regressor.fit(X_train, y_train) #обучение случайного леса

def Audio_processing_and_output():
    s = text.get(1.0, END)
    s = s[0: len(s)-1]
    key = True
    if s[1] != ':':
        s = os.getcwd() + "\\" + s
    if s[len(s)-3:len(s)] == 'mp3':
        AudioSegment.from_mp3(s).export(os.getcwd() + '/formatfile.wav', format="wav")
        s = 'formatfile.wav'
    if os.path.exists(s):
        len_part = 390000 #число, которое в итоге позволяет взять примерно равный 10 секундам отрывок
        music_sig, samplerate = sf.read(s) #поиск входного файла в дериктории где лежит программа и получение информации о файле
        for i_on_sig in range (0, int(len(music_sig)/len_part)): #цикл где программа делит входной файл на примерно равные части в 10 сек
            sig = music_sig[i_on_sig*len_part:(i_on_sig+1)*len_part]
            N = int(len(sig)/1024)*1024
            spectrum_array = [0]*512
            for i in range(0, N-1, 1024):
                time_array = [0]*1024
                for j in range(0, 1023):
                    time_array[j] = sig[j+i][0]
                spectrum = rfft(time_array, 1024) #взятие БПФ из полученного отрывка
                spectrum_abc = np_abs(spectrum) #взятие амплитудного спектра 
                for j in range(0, 511):
                    spectrum_array[j] += spectrum_abc[j]
            for j in range(0, 511):
                spectrum_array[j] = spectrum_array[j]/int(len(sig)/1024)
            y = np.array(spectrum_array)/N
            if key == False:
                a += [y[0:len_spectr]]
            if key == True: 
                a = [y[0:len_spectr]]
                key = False
        Test = a[0:len_spectr]   
        Test = sc.transform(Test) #подготовка полученных данных к прогонке через случайный лес    
        y_pred_test = regressor.predict(Test)

        arr = y_pred_test
        num = arr[0]
        N = len(arr)
        max_frq = 1
        for i in range(N-1):
            frq = 1
            for k in range(i+1,N):
                if arr[i] == arr[k]:
                    frq += 1
            if frq > max_frq:
                max_frq = frq
                num = arr[i]
        if num == 0: label['text'] = 'Хипхоп'
        if num == 6: label['text'] = 'Электроника'
        if num == 2: label['text'] = 'Джаз'
        if num == 3: label['text'] = 'Рок'
        if num == 4: label['text'] = 'Классика'
    else: label['text'] = 'Невозможно найти файл или файла не существует'
 
def deleteText():
    text.delete(1.0, END)
    label['text'] = ''
 
root = Tk()
root.title("Определитель жанра 1.4")
f_top = LabelFrame (root)
f_top = LabelFrame(text="Путь к файлу или имя файла(Желательно использование форматов wav или flac):")
f_top.pack(padx = 10, pady = 10)
text = Text(f_top, width=50, height=1)
text.pack()

label = Label(f_top)
label.pack() 

frame = Frame()
frame.pack()
 
b_get = Button(frame, text="Определить жанр", command=Audio_processing_and_output)
b_get.pack(side=LEFT)
 
b_delete = Button(frame, text="Удалить", command=deleteText)
b_delete.pack(side=LEFT)

root.mainloop()
