from base64 import encode
import dearpygui.dearpygui as dpg
import random
import codecs




def creation():
    with dpg.window(tag = "Primary Window", label = "Guess who it is!"):
        dpg.bind_font("Default font")
        global rand
        rand = random.choice(mass)
        dpg.add_image("texture_tag"+str(rand))
        dpg.add_input_text(width=350, tag ="__input_text", hint ="Введите имя и фамилию", on_enter=True, callback=button_callback)
        dpg.add_button(label="Далее", pos = [360, 692], width=248, callback=button_callback)
        dpg.set_primary_window("Primary Window", True)

def result(res_flag):
    dpg.delete_item("Primary Window")
    with dpg.window(tag = "Res_Window"):
        dpg.bind_font("Default font")
        if(res_flag):
            dpg.add_text(default_value="Поздравляю! Вы угадали!", pos=[175,350])
            dpg.add_button(label="Далее", width=250, height=50, pos=[180,550], callback=button1_callback)
        else:
            dpg.add_text("Ой! Кажется вы что-то напутали...", pos=[140,350])
            dpg.add_button(label="Попробовать еще раз", width=250, height=50, pos=[180,550], callback=button1_callback)
    dpg.set_primary_window("Res_Window", True)
        

def button_callback():
    f = codecs.open(str(rand)+".txt", encoding='utf-8')
    str0 = next(f)
    str1 = dpg.get_value("__input_text")
    global flag
    flag = True

    if(len(str1) == len(str0)):
        for i in range(len(str0)):
            if(ord(str0[i])-848 != ord(str1[i]) and str0[i]!=str1[i]):
                flag = False
    else:
        flag = False

    if (flag):
        if(len(mass)>1):
            mass.remove(rand)
    result(flag)

def button1_callback():
    dpg.delete_item("Res_Window")
    creation()


#_______________START FROM HERE_________________#
N=6
mass = [i+1 for i in range(N)]
dpg.create_context()

with dpg.font_registry(show = False):
    with dpg.font("font.ttf", 22, id="Default font", default_font = True):
        dpg.add_font_range(0x0400, 0x044f)
        for cnt in range(0x00C0, 0x00FF):
            dpg.add_char_remap(cnt,cnt+0x0350)

for i in range(N):
    width, height, channels, data = dpg.load_image(str(i+1) + ".png")
    with dpg.texture_registry(show = False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag"+str(i+1))

  

creation()
dpg.create_viewport(title = 'Guess, who it is!', width=630, height=772, resizable = False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()