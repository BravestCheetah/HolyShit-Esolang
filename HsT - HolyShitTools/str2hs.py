import customtkinter as ctk

# Initialize customtkinter
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Main application window
app = ctk.CTk()
app.title("HolyShitTools - Str2hs")
app.geometry("1000x600")


# Grid configuration
app.grid_columnconfigure((0, 2), weight=1)
app.grid_columnconfigure(1, weight=0)
app.grid_rowconfigure(0, weight=1)

# Input Text Area
input_text = ctk.CTkTextbox(app, wrap="word", font=("Courier", 14))
input_text.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="nsew")

# Output Text Area
output_text = ctk.CTkTextbox(app, wrap="word", font=("Courier", 14))
output_text.grid(row=0, column=2, padx=(10, 20), pady=20, sticky="nsew")

# Convert function
def convert():
    input_value = input_text.get("1.0", "end").strip()

    output = "c"
    for char in input_value:
        if char == '\n': char_value = 10
        else: char_value = ord(char)
        char_code = f"~{char_value}[?s%c]s@cr"
        output += char_code

    output_text.delete("1.0", "end")
    output_text.insert("1.0", output)

# Convert Button
convert_button = ctk.CTkButton(app, text="Convert!", command=convert)
convert_button.grid(row=0, column=1, padx=10, pady=20, sticky="ns")

# Run the app
app.mainloop()
