import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import pubchempy as pcp
def get_chemical_info(chemical_name):
    try:
        compound = pcp.get_compounds(chemical_name, 'name')
        if compound:
            compound = compound[0]
            info = {
                'Name': compound.iupac_name,
                'Molecular Formula': compound.molecular_formula,
                'Molecular Weight': compound.molecular_weight,
                'Synonyms': ', '.join(compound.synonyms) if compound.synonyms else "No synonyms available"
            }
            return info
        else:
            messagebox.showwarning("Error", "Chemical not found")
    except Exception as e:
        messagebox.showwarning("Error", "No internet connection")
root = tk.Tk()
root.title("ChemExplorer")
root.geometry("1900x1100")
root.configure(bg='black')
frame = tk.Frame(root, bg='black')
frame.pack(side=tk.RIGHT, padx=10, pady=0)
label = tk.Label(root, text="| WELCOME |", bg='black', fg='cyan', font=("Arial", 30))
label.pack(padx=20, pady=20)
image = Image.open('1.jpg')
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo, bg='black')
label.pack()


label = tk.Label(root, text="《ChemExplorer》", bg='black', fg='cyan', font=("Arial", 30))
label.pack(padx=20, pady=20)


def open_chemfind():
    chemfind_window = tk.Toplevel(root)
    chemfind_window.title("Chemical Info Finder")
    chemfind_window.geometry("1900x1100")
    chemfind_window.configure(bg='black')
    title_label = tk.Label(chemfind_window, text="Chemical Info Finder", font=("Helvetica", 16), bg='black', fg='cyan')
    title_label.pack(pady=10)        
    prompt_label = tk.Label(chemfind_window, text="Enter a chemical name to get its details ", bg='black', fg='white')
    prompt_label.pack(pady=10)    
    entry = tk.Entry(chemfind_window, width=30, font=("Helvetica", 14))
    entry.pack(pady=10)
    entry.insert(0, "e.g., Water")
    def search():
        chemical_name = entry.get()
        if chemical_name:
            details = get_chemical_info(chemical_name)
            if details: 
                result = "\n".join([f"{key}: {value}" for key, value in details.items()])
                messagebox.showinfo("Chemical Info", result)
        else:
            messagebox.showwarning("Input Error", "Please enter a chemical name.")    
    search_button = tk.Button(chemfind_window, text="Search", command=search, bg='cyan', fg='black', font=("Helvetica", 12))
    search_button.pack(pady=20)
def show_aboutus():
    about_window = tk.Toplevel(root)
    about_window.title("About Us")
    about_window.geometry("1900x1100")
    about_window.configure(bg='black')
    label = tk.Label(about_window, text="Director: prashuk\n\nOur members are:", bg='black', fg='cyan', font=("Arial", 16))
    label.pack(pady=20)
btn1 = tk.Button(frame, text="Chemical Info Find", bg='cyan', fg='black', font=('Arial', 20), command=open_chemfind)
btn2 = tk.Button(frame, text="Play Chemical Game", bg='cyan', fg='black', font=('Arial', 20))
btn3 = tk.Button(frame, text="About Us", bg='cyan', fg='black', font=('Arial', 20), command=show_aboutus)
btn1.pack(fill='x', pady=(0, 10))
btn2.pack(fill='x', pady=(0, 10))
btn3.pack(fill='x')
root.mainloop()