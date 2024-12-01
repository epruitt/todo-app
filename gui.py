import time

import functions
import FreeSimpleGUI as sg

sg.theme("System Default")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box= sg.InputText(tooltip="Enter to-do", key='todo')
add_btn= sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos(),key='todos',
                    enable_events=True,size=[45,10])
edit_btn = sg.Button("Edit")
complete_btn = sg.Button("Complete")
exit_btn=sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout =[[clock],
                            [label],
                            [input_box,add_btn],
                            [list_box,edit_btn, complete_btn],
                            [exit_btn]],
                   font =('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value= time.strftime(" %a - %B %d, %Y - %I:%M %p  "))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value = '')
            except IndexError:
                sg.popup("Please select a to-do first", font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos =functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a to-do first", font=('Helvetica', 20))
        case "Exit":
            break

        case 'todos':
            window['todo'].update(value = values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()