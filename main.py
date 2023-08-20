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
    [sg.Column([[sg.Image(filename='images/placeholder_image (Small).png')]], element_justification='center')],
    [sg.ProgressBar(100, orientation='h', size=(40, 20), key='-PROGRESS-')],
]


window = sg.Window("ComicVine Cover Downloader", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'OK':
        selected_folder = values['-FOLDER-']
        comic_vine_link = values['-LINK-']

        progress_bar = window['-PROGRESS-']
        progress_bar.update(0)  # Set initial progress to 0%

        all_images = downloader.get_images(comic_vine_link)
        total_images = len(all_images)

        downloader.download_image(selected_folder, all_images)  # Download all images

        sg.popup_quick_message("Download completed", background_color=bg_color, text_color=text_color)
        break


window.close()
