from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Coffee Geeks Cafe")
window.geometry('600x600')

tab_control = ttk.Notebook(window)

## color wheel
## visit this website for more nice 'flat' color options
## https://flatuicolors.com/

mintleaf = "#00b894"
robinsegg = "#00cec9"
pure_apple = "#6ab04c"

style = ttk.Style()

style.theme_create( "tabtheme", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
    "TNotebook.Tab": {
        "configure": {"padding": [45, 8], "background": mintleaf}, # the 45 and 8 represent the width and height of the tab's padding
        "map": {"background": [("selected", robinsegg)],
                "expand": [("selected", [2, 2, 1, 0])]}}})
style.theme_use("tabtheme")

# TAB 1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Staff Manager")

## ROW 0 ##

# This is the code inside the frame of tab 1
label_frame = LabelFrame(tab1)
label_frame.grid(column=0, row=0, pady=10)


#lbl1 = Label(tab1, text='Staff', font=("Courier", 30), padx=10, pady=10)
lbl1 = Label(label_frame, text='Staff', font=("Courier", 30), padx=10, pady=10)
lbl1.grid(column=0, row=0)
tab_control.tab(tab1, padding=10) # this line keeps the labels and frames padded away from the widget's edge
## END ROW 0 ##


## ROW 2 ##




def get_employees():

    staff = ["Joe", "Vince", "Andria", "Brendan"]
    tempstring = ""
    staff_frame = ttk.Labelframe(tab1)
    for emp in staff:
        tempstring += emp + '\n'
    temp_label = ttk.Label(staff_frame, text=tempstring)
    temp_label.grid(column=0, row=2)
    staff_frame.grid(column=0, row=2)


style.configure('TButton', background=pure_apple, padding=6)
view_employees = ttk.Button(tab1, text="View Employees", command=get_employees)
view_employees.grid(column=0, row=1)

def get_managers():

    managers = ["Kathryn", "Gabriela"]
    tempstring = ""
    staff_frame = ttk.Labelframe(tab1)
    var = StringVar()
    for emp in managers:
        tempstring += emp + '\n'
    temp_label = ttk.Label(staff_frame, text=tempstring)
    temp_label.grid(column=0, row=2)
    staff_frame.grid(column=0, row=2)


style.configure('TButton', background=pure_apple, padding=6, relief=RAISED)
view_managers = ttk.Button(tab1, text="View Managers", command=get_managers)
view_managers.grid(column=1, row=1)

## END ROW 2 ##

style.configure('TButton', background=pure_apple, padding=6, relief=RAISED)
add_staff = ttk.Button(tab1, text="Add a Staff Member", command=get_managers)
add_staff.grid(column=2, row=1)


## ROW 3##

footer_frame = LabelFrame(tab1)
footer_frame.grid(column=0, columnspan=3, row=4, pady=10)
made_by_label = Label(footer_frame, text="Coded with ❤️ by the fine folks @ ¯\_(ツ)_/¯", pady=10)
made_by_label.grid(column=0, row=4)

## END ROW 3 ##












# TAB 2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Inventory Manager")

lbl2 = Label(tab2, text='Inventory', font=("Courier", 30), padx=10, pady=10)
lbl2.grid(column=0, row=0)
tab_control.tab(tab2, padding=10)


tab_control.pack(expand=1, fill='both')
window.mainloop()
