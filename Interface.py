import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import pickle

file_name = "xgb_final.pkl"
# load
xgb_model_loaded = pickle.load(open(file_name, "rb"))

import tkinter as tk

# tkinter GUI
root= tk.Tk() 
root.title("Prediction of Pullout Interaction Coefficient of Geogrid")

canvas1 = tk.Canvas(root, width = 550, height = 500)
canvas1.configure(background='#e9ecef')
canvas1.pack()

#adding a label to the root window
label0 = tk.Label(root, text='Developed by Dr. Aali Pant and Prof. G. V. Ramana',font=('Futura Md Bt', 13, 'bold'),bg='#e9ecef')
canvas1.create_window(20, 20, anchor="w", window=label0)
label_phd = tk.Label(root, text='Indian Institute of Technology Delhi',font=('Futura Md Bt',12),bg='#e9ecef')
canvas1.create_window(20, 50, anchor="w",window=label_phd)
label_city = tk.Label(root, text='New Delhi, India',font=('Futura Md Bt',12),bg='#e9ecef')
canvas1.create_window(20, 80, anchor="w",window=label_city)
label_mail = tk.Label(root, text='Email: aali.pant@gmail.com',font=('Futura Md Bt',12),bg='#e9ecef')
canvas1.create_window(20, 110, anchor="w",window=label_mail)


label_input = tk.Label(root, text='Input Parameters',font=('Futura Md Bt',12,'bold','italic','underline'),bg='#e9ecef')
canvas1.create_window(20, 140, anchor="w",window=label_input)

# New_Normal_Stress label and input box
label1 = tk.Label(root, text='Normal Stress, kPa: ',font=('Futura Md Bt',12),bg='#e9ecef')
canvas1.create_window(20, 170, anchor="w",window=label1)

entry1 = tk.Entry (root) # create 1st entry box
canvas1.create_window(480, 170, window=entry1)

# New_D50 label and input box
label2 = tk.Label(root, text='D50, mm: ',font=('Futura Md Bt',12),bg='#e9ecef')
canvas1.create_window(20, 200, anchor="w",window=label2)

entry2 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(480, 200, window=entry2)

# New_FC label and input box
label3 = tk.Label(root, text='Fines Content, %: ',font=('Futura Md Bt',12),bg='#e9ecef')
canvas1.create_window(20, 230, anchor="w",window=label3)

entry3 = tk.Entry (root) # create 3rd entry box
canvas1.create_window(480, 230, window=entry3)

# New_Length of geogrid label and input box
label4 = tk.Label(root, text='Length of geogrid, mm: ',font=('Futura Md Bt',12),bg='#e9ecef')
canvas1.create_window(20, 260, anchor="w",window=label4)

entry4 = tk.Entry (root) # create 4th entry box
canvas1.create_window(480, 260, window=entry4)

# New_Spacing between geogrid longitudinal members label and input box
label5 = tk.Label(root, text='Spacing between geogrid longitudinal members, mm: ',font=('Futura Md Bt',12),bg='#e9ecef')
canvas1.create_window(20, 290, anchor="w",window=label5)

entry5 = tk.Entry (root) # create 5th entry box
canvas1.create_window(480, 290, window=entry5)

# New_Spacing between geogrid transverse members label and input box
label6 = tk.Label(root, text='Spacing between geogrid longitudinal members, mm: ',font=('Futura Md Bt',12),bg='#e9ecef')
canvas1.create_window(20, 320, anchor="w",window=label6)

entry6 = tk.Entry (root) # create 6th entry box
canvas1.create_window(480, 320, window=entry6)

# New_Ultimate Tensile Strength of Geogrid label and input box
label7 = tk.Label(root, text='Ultimate strength of geogrid, kN/m: ',font=('Futura Md Bt',12),bg='#e9ecef')
canvas1.create_window(20, 350, anchor="w",window=label7)

entry7 = tk.Entry (root) # create 7th entry box
canvas1.create_window(480, 350, window=entry7)

label0000 = tk.Label(root, text='Output',font=('Futura Md Bt',12,'bold','italic','underline'),bg='#e9ecef')
canvas1.create_window(20, 410, anchor="w",window=label0000)

label_out = tk.Label(root, text='Pullout Interaction Coefficient',font=('Futura Md Bt',12),bg='#e9ecef')
canvas1.create_window(20, 450, anchor="w",window=label_out)

#entry_out = tk.Entry (root) # create box for output
#canvas1.create_window(480, 450, window=entry_out)

def values(): 
    global New_normal_stress_MPa #our 1st input variable
    New_normal_stress_MPa = float(entry1.get())/1000 
    
    global New_D50 #our 2nd input variable
    New_D50 = float(entry2.get())

    global New_FC #our 3rd input variable
    New_FC = float(entry3.get())/100

    global New_L_mm #our 4th input variable
    New_L_mm = float(entry4.get())/1000

    global New_sL #our 5th input variable
    New_sL = float(entry5.get())/1000

    global New_sT #our 6th input variable
    New_sT = float(entry6.get())/1000

    global New_Tult_N_mm #our 7th input variable
    New_Tult_N_mm = float(entry7.get())/1000
    
    data = np.array([[New_normal_stress_MPa ,New_D50,New_FC,New_L_mm,New_sL,New_sT,New_Tult_N_mm]])
    Input_data = pd.DataFrame(data, columns=['normal_stress_MPa','D50','FC','L_mm','sL','sT','Tult_N_mm'])

    
    Prediction_result  = np.around(xgb_model_loaded.predict(Input_data),2)
    label_Prediction = tk.Label(root, text = str(Prediction_result).lstrip('[').rstrip(']') ,bg='white')
    canvas1.create_window(450, 450, anchor="w", window=label_Prediction)
    
button1 = tk.Button (root, text= 'Predict',command=values, bg='white') # button to call the 'values' command above 
canvas1.create_window(450, 385, anchor="w",window=button1)

root.mainloop()