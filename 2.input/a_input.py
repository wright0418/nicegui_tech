from nicegui import ui
name = ""
password = ""

def get_input(e):
    global name, password
    if e.sender.props['label'] == 'Enter your name:':
        name = e.value
    elif e.sender.props['label'] == 'Enter your passwaor:':
        password = e.value
    print(f'Name: {name}, Password: {password}')


ui.input('Enter your name:',on_change= get_input)
ui.input('Enter your passwaor:',on_change= get_input , password=True , password_toggle_button=True)

ui.run()