#GUI Imports
from dearpygui.core import *
from dearpygui.simple import *

#SMS Spam Filter Imports
import random
import pandas as pd
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')

#function Imports
from functions import categorize_words, predict, pre_process

#check button results
def check_spam(sender, data, pred = []):
    with window("Simple SMS Spam Filter"):
        #Frame 2 Widgets
        if pred == []:
            #executed only once, when no prior prediction is detected
            print('no prior prediction detected')
            add_spacing(count=12, name="spacing4")
            add_separator(name="sep")
            add_spacing(count=12, name="spacing5")
            input_value = get_value("Input")
            input_value = pre_process(input_value)
            input_value, text_colour = predict(input_value)
            pred.append(str(input_value))
            add_text(pred[-1], color=text_colour) #display prediction
        else:
            #executed each time the button is clicked
            print('prior prediction detected, updating text...')
            hide_item(pred[-1]) #hide previous prediction
            input_value = get_value("Input")
            input_value = pre_process(input_value)
            input_value, text_colour = predict(input_value)
            pred.append(str(input_value))
            add_text(pred[-1], color=text_colour) #display current prediction

#Pre-determined Window Settings
set_main_window_size(540, 720)
set_global_font_scale(1.25)
set_theme("Gold")

#Start Window object
with window("Simple SMS Spam Filter", width=520, height=677):
    set_window_pos("Simple SMS Spam Filter",0,0)

    #Frame 1 Widgets
    add_drawing("Frame1", width=520, height=290)
    add_separator()
    add_spacing(count=12, name="spacing1")
    add_text("Please enter an SMS message of your choice to check if it's spam or not", wrap=480, color=[232,163,33])
    set_style_window_padding(30.00, 30.00)
    add_spacing(count=12, name="spacing2")

    add_input_text("Input", width=415, default_value="type message here!")
    add_spacing(count=12, name="spacing3")

    add_button("Check", callback=check_spam)

draw_image("Frame1", 'logo_spamFilter.png', [-75, 300], pmax=[50, 300], uv_min=[0, 0], uv_max=[1, 1], tag="logo")

#End Window Object
start_dearpygui()
