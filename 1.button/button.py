# 需要安裝 nicegui package , 
# >pip install nicegui

from nicegui import ui
#建立一個最簡單的按鈕，按下按鈕後會顯示訊息
button = ui.button('Click me')
button.on_click(lambda: ui.notify('Button clicked!'))

# 使用 AWSG (非同步 web server interface) 啟動 GUI
ui.run()