import customtkinter as ctk
from PIL import Image
import os

class SocialAppComponents:
    def __init__(self, root):
        self.root = root

    def create_heading(self, container, text):
        heading = ctk.CTkLabel(
            container,
            text=text,
            text_color=("#1a1a1a", "#eeeeee"),
            font=ctk.CTkFont(size=22, weight="bold")
        )
        return heading

    def create_nav_button(self, container, text, icon_path=None, icon_only=False, **kwargs):
        img = None
        if icon_path and os.path.exists(icon_path):
            img = ctk.CTkImage(light_image=Image.open(icon_path), size=(20, 20))

        button_settings = {
            "text": "" if icon_only else text,
            "image": img,
            "compound": "left",
            "corner_radius": 10,
            "width": 40 if icon_only else 140,
            # Standard tuple colors: (Light Mode, Dark Mode)
            "fg_color": ("#1f538d", "#1f538d"),
            "text_color": ("#eeeeee", "#ffffff"),
            "hover_color": ("#367cbb", "#14375e")
        }

        button_settings.update(kwargs)

        button = ctk.CTkButton(container, **button_settings)
        return button

    def create_text_input(self, container, label_text, placeholder, is_password=False):
        frame = ctk.CTkFrame(container, fg_color="transparent")

        label = ctk.CTkLabel(frame, text=label_text, text_color=("#333333", "#bbbbbb"))
        label.pack(anchor="w")

        entry = ctk.CTkEntry(
            frame,
            placeholder_text=placeholder,
            show="*" if is_password else "",
            border_color=("#1f538d", "#5dade2"),  # Navy in light, Sky blue in dark
            border_width=2
        )
        entry.pack(fill="x")
        return frame

    def create_frame_card(self, container, title=None, **kwargs):
        card_args = {
            "corner_radius": 15,
            "fg_color": ("#f2f2f2", "#252525"),  # Subtle light/dark contrast
            "border_width": 1,
            "border_color": ("#dcdcdc", "#3d3d3d")
        }
        card_args.update(kwargs)

        card_frame = ctk.CTkFrame(container, **card_args)

        if title:
            title_label = ctk.CTkLabel(
                card_frame,
                text=title.upper(),
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color=("#666666", "#888888")  # Muted label color
            )
            title_label.pack(anchor="w", padx=15, pady=(10, 5))

        return card_frame