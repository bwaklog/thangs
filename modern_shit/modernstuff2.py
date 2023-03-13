import tkinter
import tkintermapview

root = tkinter.Tk()
root.geometry('800x600')
root.title("map_view_example")

map_widget = tkintermapview.TkinterMapView(
    root, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

map_widget.set_position(12.91906, 77.68962)
map_widget.set_zoom(17)

home = "Adarsh Palm Retreat,Tower - 4 C & D Block ,Bengaluru ,Karnataka"
map_widget.set_address(
    "Adarsh Palm Retreat,Tower - 4 C & D Block ,Bengaluru ,Karnataka")


root.mainloop()
