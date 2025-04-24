import ipywidgets as widgets
from IPython.display import display, clear_output
import json

file_path = '/content/drive/My Drive/students.json'

with open(file_path, 'r') as file:
    students = json.load(file)
student_names = [f"{student['first_name']} {student['last_name']}" for student in students]


dropdown = widgets.Dropdown(
    options=student_names,
    value=student_names[0] if student_names else '',
    description='Choose Student:',
    style={'description_width': 'initial'}
)

button_show = widgets.Button(
    description="Show Details",
    button_style='info',
    icon='search'
)

txt_name = widgets.Text(description="First Name:", disabled=True)
txt_family = widgets.Text(description="Last Name:", disabled=True)
txt_email = widgets.Text(description="Email:", disabled=True)
txt_courses = widgets.Textarea(description="Courses:", disabled=True)
txt_link = widgets.Text(description="Interesting Link:", disabled=True)
txt_favorites = widgets.Text(description="Favorites:")
btn_update = widgets.Button(
    description="Update Favorites"

)

output = widgets.Output()


form = widgets.VBox([
    widgets.HBox([dropdown, button_show]),
    widgets.VBox([
        txt_name,
        txt_family,
        txt_email,
        txt_courses,
        txt_link,
        widgets.HBox([txt_favorites, btn_update])
    ]),
    output
])


def load_students():
    with open(file_path, 'r') as f:
        return json.load(f)

def save_students(data):

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def show_student_details(b):
    with output:
        clear_output()
        selected = dropdown.value
        first, last = selected.split(' ', 1)


        for student in students:
            if student['first_name'] == first and student['last_name'] == last:
                txt_name.value = student['first_name']
                txt_family.value = student['last_name']
                txt_email.value = student['email']
                txt_courses.value = ', '.join(student['courses'])
                txt_link.value = student['interesting_link']
                txt_favorites.value = student.get('favorites', '')
                return



def update_favorites(b):

    selected_student = dropdown.value
    favorites_value = txt_favorites.value

    students_data = load_students()

    first_name, last_name = selected_student.split(' ', 1)

    for student in students_data:
        if student["first_name"] == first_name and student["last_name"] == last_name:
            student.update({"favorites": favorites_value})
            break

    save_students(students_data)

    with output:
        clear_output()
        print("✅ Favorites updated successfully!")


button_show.on_click(show_student_details)
btn_update.on_click(update_favorites)

display(form)
