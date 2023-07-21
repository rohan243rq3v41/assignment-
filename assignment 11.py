import tkinter as tk
import webbrowser

def open_faq():
    source = source_var.get()

    if source == "Instagram Ads":
        url = "https://www.example.com/instagram_faq"
    elif source == "YouTube Ads":
        url = "https://www.example.com/youtube_faq"
    else:
        url = "https://www.example.com/general_faq"

    print("Navigating to:", url)
    webbrowser.open(url)

def create_gui():
    root = tk.Tk()
    root.title("Course Enquiry Form")

    label_course = tk.Label(root, text="Enter the course you are interested in:")
    label_course.pack()

    entry_course = tk.Entry(root)
    entry_course.pack()

    label_source = tk.Label(root, text="Where did you come to know about the course?")
    label_source.pack()

    # Create a variable to store the selected source
    source_var = tk.StringVar()
    source_var.set("Instagram Ads")

    # Create a dropdown menu for the source options
    source_options = ["Instagram Ads", "YouTube Ads", "Other"]
    dropdown_source = tk.OptionMenu(root, source_var, *source_options)
    dropdown_source.pack()

    button_submit = tk.Button(root, text="Submit", command=open_faq)
    button_submit.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
