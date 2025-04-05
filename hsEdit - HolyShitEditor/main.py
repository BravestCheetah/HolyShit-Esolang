import subprocess, threading, os, importlib.util, tkinter.messagebox
import customtkinter as ctk

class ProcessManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("HsEdit | Holy-Shit esolang Official Code Editor")
        self.geometry("600x500")
        ctk.set_appearance_mode("dark")

        self.process = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)

        self.code_area = ctk.CTkTextbox(self, wrap="word")
        self.code_area.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)
        self.code_area.bind("<KeyRelease>", lambda event: self.save_code())

        self.output_text = ctk.CTkTextbox(self, wrap="word", height=5, state="disabled")
        self.output_text.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

        self.run_button = ctk.CTkButton(self, text="Run", fg_color="green", command=self.toggle_process)
        self.run_button.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

        self.input_entry = ctk.CTkEntry(self, placeholder_text="Enter code input...", state="disabled")
        self.input_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=5)
        self.input_entry.bind("<Return>", self.send_input)

        with open(os.path.join("data", "code.crap"), "r") as f:
            self.code_area.insert("end", f.read())


    def save_code(self):
        content = self.code_area.get("1.0", "end-1c")
        with open(os.path.join("data", "code.crap"), "w") as f:
            f.write(content)

    def toggle_process(self):
        if self.process and self.process.poll() is None:
            self.stop_process()
        else:
            self.clear_output()
            self.start_process()

    def start_process(self):
        if self.process is None or self.process.poll() is not None:
            self.process = subprocess.Popen(
                ["HolyShit", "data\\code.crap"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            threading.Thread(target=self.read_output, daemon=True).start()
            threading.Thread(target=self.monitor_process, daemon=True).start()
            self.run_button.configure(text="Stop", fg_color="red")
            self.input_entry.configure(state="normal")

    def read_output(self):
        while self.process and self.process.poll() is None:
            output = self.process.stdout.readline()
            if output:
                self.output_text.configure(state="normal")
                self.output_text.insert("end", f"Output >>    {output}" if output != "\n" else output)
                self.output_text.see("end")
                self.output_text.configure(state="disabled")

    def send_input(self, event=None):
        if self.process and self.process.stdin:
            code_input = self.input_entry.get() + "\n"
            try:
                self.process.stdin.write(code_input)
                self.process.stdin.flush()
                self.input_entry.delete(0, "end")
                self.output_text.configure(state="normal")
                self.output_text.insert("end", f"Input >>    {code_input}")
                self.output_text.see("end")
                self.output_text.configure(state="disabled")
            except OSError:
                self.input_entry.configure(state="disabled")

    def stop_process(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process.wait()
            self.process = None
            self.output_text.configure(state="normal")
            self.output_text.insert("end", "\n[Process Terminated]\n")
            self.output_text.configure(state="disabled")
            self.run_button.configure(text="Run", fg_color="green")
            self.input_entry.configure(state="disabled")

    def monitor_process(self):
        self.process.wait()
        self.process = None
        self.output_text.configure(state="normal")
        self.output_text.insert("end", "\n[Process Ended]\n")
        self.output_text.configure(state="disabled")
        self.run_button.configure(text="Run", fg_color="green")
        self.input_entry.configure(state="disabled")

    def clear_output(self):
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.configure(state="disabled")

def is_hs_installed():
    try:
        import holyshit_eso
        return True
    except ImportError:
        return False

if __name__ == "__main__":
    if is_hs_installed():
        app = ProcessManager()
        app.mainloop()
    
    else:
        tkinter.messagebox.showerror("Package Error", "The holyshit-eso package is not installed, check the github for installaion intructions.")
