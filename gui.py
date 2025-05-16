# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
#
# # Create the main window (root)
# root = tk.Tk()
# root.title("File Upload GUI")
# root.geometry("400x200")  # Set window size
#
# # Function to open file dialog and upload a file
# def upload_file():
#     # Open a file dialog to select a file
#     file_path = filedialog.askopenfilename(
#         title="Select a file",
#         filetypes=(("Image files", "*.jpg;*.jpeg;*.png;*.bmp"),  # Add more file types if needed
#                    ("All files", "*.*"))
#     )
#     if file_path:
#         # Display the file path in the label
#         file_label.config(text=f"File Selected: {file_path}")
#     else:
#         # Display a message if no file is selected
#         messagebox.showwarning("No File Selected", "Please select a file to upload")
#
# # Create a label to show the file path after selection
# file_label = tk.Label(root, text="No file selected", wraplength=300)
# file_label.pack(pady=20)
#
# # Create the upload button
# upload_button = tk.Button(root, text="Upload File", command=upload_file)
# upload_button.pack(pady=10)
#
#####################################################################################

# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
#
# # Create the main window (root)
# root = tk.Tk()
# root.title("File Upload GUI")
# root.geometry("400x200")  # Set window size
#
# # Function to open file dialog and upload a file
# def upload_file():
#     # Open a file dialog to select a file
#     file_path = filedialog.askopenfilename(
#         title="Select a file",
#         filetypes=(("Image files", "*.jpg;*.jpeg;*.png;*.bmp"),  # Add more file types if needed
#                    ("All files", "*.*"))
#     )
#     if file_path:
#         # Display the file path in the label
#         file_label.config(text=f"File Selected: {file_path}")
#     else:
#         # Display a message if no file is selected
#         messagebox.showwarning("No File Selected", "Please select a file to upload")
#
# # Create a label to show the file path after selection
# file_label = tk.Label(root, text="No file selected", wraplength=300)
# file_label.pack(pady=20)
#
# # Create the upload button
# upload_button = tk.Button(root, text="Upload File", command=upload_file)
# upload_button.pack(pady=10)
#
# # Run the main event loop
# root.mainloop()  # Keep the window running

#####################################################################################################################################

# import tkinter as tk
# from tkinter import filedialog, ttk
#
# class FileUploader(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.title("File Upload")
#         self.geometry("600x400")
#
#         # File upload area
#         self.upload_frame = tk.Frame(self, relief=tk.RAISED, borderwidth=2, width=300, height=200)
#         self.upload_frame.pack(pady=20)
#
#         self.upload_label = tk.Label(self.upload_frame, text="Drag files to upload", width=25, height=10)
#         self.upload_label.pack()
#
#         # Choose file button
#         self.choose_file_button = tk.Button(self, text="Choose File", command=self.browse_files)
#         self.choose_file_button.pack(pady=10)
#
#         # Uploading area
#         self.uploading_label = tk.Label(self, text="Uploading")
#         self.uploading_label.pack()
#
#         self.upload_list_frame = tk.Frame(self)
#         self.upload_list_frame.pack(pady=10)
#
#         # File list (Progress bar simulation)
#         self.file_list = []
#
#     def browse_files(self):
#         filenames = filedialog.askopenfilenames(initialdir="/", title="Select File")
#         if filenames:
#             self.add_files(filenames)
#
#     def add_files(self, filenames):
#         for filename in filenames:
#             file_frame = tk.Frame(self.upload_list_frame)
#             file_frame.pack(fill="x", pady=2)
#
#             file_name_label = tk.Label(file_frame, text=filename.split("/")[-1], width=20)
#             file_name_label.pack(side="left")
#
#             progress = ttk.Progressbar(file_frame, orient="horizontal", length=200, mode="determinate")
#             progress.pack(side="left", padx=5)
#             progress["value"] = 50  # Simulate progress for now
#
#             self.file_list.append((filename, progress))
#
# if __name__ == "__main__":
#     app = FileUploader()
#     app.mainloop()
############################################################################################################################

# import tkinter as tk
# from tkinter import filedialog, Label
# from PIL import Image, ImageTk
# import tensorflow as tf
# import numpy as np
#
# # Define class labels
# class_labels = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']
#
# # Load your pre-trained VGG model
# model = tf.keras.models.load_model('E:/ML Dataset/BrainTumor/final_vgg19_brain_tumor.keras', compile=False)
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
#
# class TumorPredictionApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.title("Brain Tumor Prediction")
#         self.geometry("500x600")
#
#         self.image_label = Label(self, text="Please upload an MRI scan")
#         self.image_label.pack(pady=20)
#
#         self.upload_button = tk.Button(self, text="Upload Image", command=self.upload_image)
#         self.upload_button.pack(pady=10)
#
#         self.result_label = tk.Label(self, text="")
#         self.result_label.pack(pady=20)
#
#         self.image_display = tk.Label(self)
#         self.image_display.pack(pady=20)
#
#     def upload_image(self):
#         # Open file dialog to choose an image
#         file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
#         if file_path:
#             # Load and display the image
#             img = Image.open(file_path)
#             img = img.resize((224, 224))  # Resize image to match VGG model input size
#             img_display = ImageTk.PhotoImage(img)
#
#             # Update image label
#             self.image_display.config(image=img_display)
#             self.image_display.image = img_display
#
#             # Convert image to array for model prediction
#             img_array = np.array(img)
#             img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
#             img_array = img_array / 255.0  # Normalize image
#
#             # Make prediction
#             prediction = model.predict(img_array)
#             predicted_class = class_labels[np.argmax(prediction)]
#
#             # Display the result
#             self.result_label.config(text=f"Predicted Tumor Type: {predicted_class}")
#
# if __name__ == "__main__":
#     app = TumorPredictionApp()
#     app.mainloop()
#################################################################################################################################

import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np

# Define class labels
class_labels = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']

# Load your pre-trained VGG model
# model = tf.keras.models.load_model('E:/ML Dataset/BrainTumor/final_vgg19_brain_tumor.keras', compile=False)
model = tf.keras.models.load_model('E:/ML Dataset/BrainTumor/final_vgg19_brain.keras', compile=False)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

class TumorPredictionApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window title and dimensions
        self.title("Brain Tumor Prediction")
        self.geometry("500x600")
        self.config(bg="#2c2f33")  # Dark background

        # Styling variables
        self.font_style = ("Helvetica", 14, "bold")
        self.text_color = "#ffffff"  # White text
        self.button_color = "#7289da"  # Minimalistic button color
        self.button_text_color = "#ffffff"
        self.label_color = "#99aab5"  # Slightly lighter label color

        # Upload Image label
        self.image_label = Label(self, text="Please upload an MRI scan", font=self.font_style, fg=self.label_color, bg="#2c2f33")
        self.image_label.pack(pady=20)

        # Upload Button
        self.upload_button = tk.Button(self, text="Upload Image", command=self.upload_image, font=self.font_style,
                                       bg=self.button_color, fg=self.button_text_color, bd=0, activebackground="#677bc4", activeforeground=self.text_color)
        self.upload_button.pack(pady=10)

        # Prediction Result label
        self.result_label = tk.Label(self, text="", font=("Helvetica", 16, "bold"), fg=self.text_color, bg="#2c2f33")
        self.result_label.pack(pady=20)

        # Area to display the uploaded image
        self.image_display = tk.Label(self, bg="#2c2f33")
        self.image_display.pack(pady=20)

    def upload_image(self):
        # Open file dialog to choose an image
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            # Load and display the image
            img = Image.open(file_path)
            img = img.resize((224, 224))  # Resize image to match VGG model input size
            img_display = ImageTk.PhotoImage(img)

            # Update image label
            self.image_display.config(image=img_display)
            self.image_display.image = img_display

            # Convert image to array for model prediction
            img_array = np.array(img)
            img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
            img_array = img_array / 255.0  # Normalize image

            # Make prediction
            prediction = model.predict(img_array)
            predicted_class = class_labels[np.argmax(prediction)]

            # Display the result
            self.result_label.config(text=f"Predicted Tumor Type: {predicted_class}")

if __name__ == "__main__":
    app = TumorPredictionApp()
    app.mainloop()
