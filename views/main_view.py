import customtkinter as ctk
from views.timer_page import TimerPage
from views.video_page import VideoPage

# --- Constants
BG_COLOR = "#AC7088"
TEXT_COLOR = "#F5E8C7"
ELEMENT_COLOR = "#ECCCB2"
SHADOW_COLOR  = "#DEB6AB"
# ---

class PomodoroApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro App")
        self.geometry("1000x800")
        self.configure(fg_color=BG_COLOR)
        
        # --- Navigation
        self.nav_frame = ctk.CTkFrame(self, height=50, fg_color="transparent")
        self.nav_frame.pack(fill="both", pady=10)
        self.nav_button = ctk.CTkSegmentedButton(self.nav_frame, values=["TimerPage", "VideoPage"], 
                                                 command=self.show_frame,
                                                 fg_color=ELEMENT_COLOR,
                                                 selected_color=SHADOW_COLOR,
                                                 unselected_color=ELEMENT_COLOR,
                                                 unselected_hover_color=SHADOW_COLOR,
                                                 selected_hover_color=SHADOW_COLOR,
                                                 border_width=5,
                                                 corner_radius=20
                                                 )
        self.nav_button.set("TimerPage")
        self.nav_button.pack()
                
        # --- Main Container
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(expand=True, fill="both")
        
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Pages map
        self.frames = {}

        # Pages map init
        for PageClass in (TimerPage, VideoPage):
            page_name = PageClass.__name__
            frame = PageClass(parent=self.container)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame("TimerPage")

    # Actual page switch
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()