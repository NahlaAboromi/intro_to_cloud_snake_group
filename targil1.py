import ipywidgets as widgets
from IPython.display import display

with open('/content/drive/My Drive/students.txt', 'r') as file:
    students = list({line.split(',')[0] for line in file.readlines()})

dropdown = widgets.Dropdown(
    options=students,
    value=students[0] if students else '',
    description='Choose Student:',
)

button = widgets.Button(description="Show Details")
output = widgets.Output()

txt1 = widgets.Text(description="Name:")
txt2 = widgets.Text(description="Family:")
txt3 = widgets.Text(description="Email:")
txt4 = widgets.Text(description="Courses:")
txt5 = widgets.Text(description="Link:")
txt6 = widgets.Text(description="Favorits:")
button2 = widgets.Button(description="Update")

# פריסה מסודרת
form_items = [
    widgets.HBox([dropdown, button]),
    txt1,
    txt2,
    txt3,
    txt4,
    txt5,
    widgets.HBox([txt6, button2])
]

form = widgets.VBox(form_items)
display( form, output)

def show_student_details(b=None):
    output.clear_output()
    selected_student = dropdown.value

    with open('/content/drive/My Drive/students.txt', 'r') as file:
        found = False
        for line in file:
            if line.startswith(selected_student + ','):
                details = line.strip().split(',')
                name = details[0]
                family = details[1]
                email = details[2]
                courses = details[3:-1]
                link = details[-1]

                txt1.value = name
                txt2.value = family
                txt3.value = email
                txt4.value = ', '.join(courses)
                txt5.value = link
                txt6.value = ""

                found = True
                break
        if not found:
            display(widgets.Label(value="Student not found."))
        else:
            button2.on_click(update_favorits)

def update_favorits(b):
    selected_student = dropdown.value
    favorits = txt6.value
    with open('/content/drive/My Drive/students.txt', 'a') as file:
        file.write(f"{selected_student},Favorits,{favorits}\n")
    print("Favorits updated successfully!")

button.on_click(show_student_details)