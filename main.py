import PySimpleGUI as sg
import downloader

# Set up Nord theme colors
bg_color = "#2e3440"
text_color = "#eceff4"
input_bg_color = "#3b4252"
button_bg_color = "#4c566a"
button_text_color = "#eceff4"

sg.theme_background_color(bg_color)
sg.theme_text_element_background_color(bg_color)
sg.theme_input_background_color(input_bg_color)
sg.theme_button_color((button_text_color, button_bg_color))

layout = [
    [sg.Text("Output Folder", font=("Helvetica Neue", 16), text_color=text_color)],
    [sg.InputText(key='-FOLDER-', font=("Helvetica Neue", 14), background_color=input_bg_color, text_color=text_color),
     sg.FolderBrowse(target='-FOLDER-', font=("Helvetica Neue", 14), button_color=(button_text_color, button_bg_color))],
    [sg.Text("Comic Vine Link", font=("Helvetica Neue", 16), text_color=text_color)],
    [sg.InputText(key='-LINK-', font=("Helvetica Neue", 14), background_color=input_bg_color, text_color=text_color)],
    [sg.Column(layout=[
        [sg.Button("OK", font=("Helvetica Neue", 14), button_color=(button_text_color, button_bg_color), border_width=0),
         sg.Button("Cancel", font=("Helvetica Neue", 14), button_color=(button_text_color, button_bg_color), border_width=0)],
    ], justification='center')],
    [sg.Column([[sg.Image(filename='placeholder_image (Small).png')]], element_justification='center')],
]

window = sg.Window("ComicVine Cover Downloader", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'OK':
        selected_folder = values['-FOLDER-']
        comic_vine_link = values['-LINK-']
        sg.popup(f"You selected folder: {selected_folder}\nComic Vine Link: {comic_vine_link}")
        all_images = downloader.get_images(comic_vine_link)  # Call the hello() function from downloader.py
        downloader.download_image(selected_folder, all_images)

        break

window.close()
