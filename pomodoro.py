import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk, Style

# Set the default time for work and breaks:
WORK_TIME = 25 * 60
SHORT_BREAK_TIME = 5 * 60
LONG_BREAK_TIME = 15 * 60

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Pomodoro Timer")
        self.style = Style(theme="simplex")
        self.style.theme_use()

        self.timer_label = tk.Label(self.root, text="", font=("TkDefaultFont", 40))
        self.timer_label.pack(pady=20)

        self.start_button = ttk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        # Initialize work_time and break_time correctly
        self.work_time = WORK_TIME  # Change: Ensure proper variable initialization
        self.break_time = SHORT_BREAK_TIME  # Change: Ensure proper variable initialization
        self.is_work_time = True  # Change: Initialize as a boolean
        self.pomodoros_completed = 0
        self.is_running = False

        self.update_timer_display()  # Change: Initialize the timer label display correctly
        self.root.mainloop()

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()

    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False

    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.is_work_time = False  # Change: Correctly toggle the boolean
                    self.pomodoros_completed += 1
                    self.break_time = LONG_BREAK_TIME if self.pomodoros_completed % 4 == 0 else SHORT_BREAK_TIME
                    messagebox.showinfo(
                        "Great job!" if self.pomodoros_completed % 4 == 0 else "Good job!",
                        "Take a long break now!" if self.pomodoros_completed % 4 == 0 else "Time for a short break!"
                    )
            else:
                self.break_time -= 1
                if self.break_time == 0:
                    self.is_work_time = True  # Change: Correctly toggle the boolean
                    self.work_time = WORK_TIME
                    messagebox.showinfo("Work time", "Get back to work now!")

            self.update_timer_display()  # Change: Update the timer display
            self.root.after(1000, self.update_timer)

    def update_timer_display(self):  # Change: Add method to update timer display
        minutes, seconds = divmod(self.work_time if self.is_work_time else self.break_time, 60)
        self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))

PomodoroTimer()
