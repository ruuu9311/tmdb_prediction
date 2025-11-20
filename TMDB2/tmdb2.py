import requests
import json
import tkinter as tk

api_key ='d3fdedf6c9f7a259e9d16c5b93a0d13b'

root = tk.Tk()
root.title('The Movie Database')
root.geometry('500x500')

label_movie = tk.Label(root, text='Movie ID')
label_movie.pack(pady=(15,5))
entry_movie = tk.Entry(root, width=25)
entry_movie.pack()

show_variable = tk.StringVar()
show_area = tk.Label(root, 
                     textvariable=show_variable,
                     font = ('Helvetica', 32),
                     bg = "lightyellow",
                     justify='left')
show_area.pack(pady=20,padx=20,fill='both',expand=True)

#movie_id = '500'
#api_key ='d3fdedf6c9f7a259e9d16c5b93a0d13b'

def print_movie():
    movie_id = entry_movie.get()
    print('Movie ID = ',movie_id)
    print('-'*30)
button_print = tk.Button(root, text='Print', command=print_movie) 
button_print.pack(pady=15)

#response = requests.get(url)
#data = response.json()
#show_variable.set(json.dumps(data, indent=4))

def print_revenue():
    movie_id = entry_movie.get()
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    #api_key ='d3fdedf6c9f7a259e9d16c5b93a0d13b'
    response = requests.get(url)
    data = response.json()
    revenue_value = data.get('revenue')
    print('Revenue = ', revenue_value)
    print('-'*30)
    show_variable.set(revenue_value)
    #show_variable.set(json.dumps(data, indent=4))
button_revenue = tk.Button(root, text='Revenue', command=print_revenue) 
button_revenue.pack(pady=15)

#print(response)
#data = response.json()
#print(data,type(data))
#trial = data.get('adult')
#print(trial)






root.mainloop()