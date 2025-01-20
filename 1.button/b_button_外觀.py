from nicegui import ui

button = ui.button('Click me',color='red') # 這裡新增了 color='red' 參數
button.on_click(lambda: ui.notify('Button clicked!'))

"""
    https://fonts.google.com/icons 
    https://material.io/resources/icons/?style=baseline
"""
button_1 = ui.button('按鈕1',color='blue',icon = 'settings') # 這裡新增了 icon='settings' 參數
button3 = ui.button(color='blue',icon = 'settings')
# DIY 按鈕2
with ui.button('按鈕2',color='green') as button_2: # 這裡新增了 icon='delete' 參數
   ui.image('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')

# 使用 AWSG (非同步 web server interface) 啟動 GUI
ui.run()