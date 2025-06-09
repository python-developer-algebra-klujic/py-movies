import json
import tkinter as tk
from PIL import Image, ImageTk


movies = {}
# Ucitati sve filmove iz json datoteke
def load_movies():
    global movies
    try:
        with open('data/movies-250.json', 'r') as file_reader:
            movies = json.load(file_reader)
    except Exception as ex:
        print(f'Dogodila se greska {ex}!')


def load_image(event):
    global lbl_movie_poster

    selected_movie_index = lb_movies.curselection()
    if selected_movie_index:
        selected_movie_title = lb_movies.get(selected_movie_index)
        for movie in movies['movies']:
            if selected_movie_title == movie['Title']:
                image_path = f'data/thumbs/{movie['imdbID']}.jpg'

    else:
        image_path = f'data/thumbs/no_image.jpg'
    image = ImageTk.PhotoImage(image=Image.open(image_path))
    lbl_movie_poster.configure(image=image)
    lbl_movie_poster.image = image


def load_listbox():
    global lb_movies

    for index, movie in enumerate(movies['movies']):
        lb_movies.insert(index, movie['Title'])



root = tk.Tk()
root.title('Py Movies')

lbl_title = tk.Label(root, text='Py Movies', font=('Verdana', 20))
lbl_title.grid(row=0, column=0, columnspan=2, pady=10)

lbl_movie_poster = tk.Label(root)
lbl_movie_poster.grid(row=1, column=0, padx=10, pady=10)


lb_movies = tk.Listbox(root)
lb_movies.grid(row=1, column=1, padx=10, pady=10)
lb_movies.bind('<<ListboxSelect>>', load_image)


if __name__ == '__main__':
    load_movies()
    load_image(None)
    load_listbox()
    root.mainloop()
