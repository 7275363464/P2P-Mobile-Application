import configparser
import json
import sqlite3
import anvil
from anvil.tables import app_tables
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.material_resources import dp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.spinner import MDSpinner
from borrower_extend_loan import ExtensionLoansRequest
from borrower_view_transaction_history import TransactionBH
from borrower_application_tracker import ALLLoansAPT
from borrower_dues import BorrowerDuesScreen
from new_loan_request import NewloanScreen
from borrower_viewloan import DashboardScreenVLB
from borrower_foreclosure import LoansDetailsB
from kivy.uix.modalview import ModalView
from kivymd.uix.spinner import MDSpinner
from kivy.clock import Clock
from kivy.animation import Animation
from kivymd.uix.label import MDLabel
from kivy.factory import Factory

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)

user_helpers = """
<WindowManager>:
    DashboardScreen:
    ProfileScreen:
    EditScreen:
<DashboardScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Borrower Dashboard"
            elevation: 2
            pos_hint: {'top': 1}
            right_action_items: [["wallet", lambda x: root.go_to_wallet()], ["logout", lambda x: root.logout()]]
            title_align: 'center'  # Center-align the title
            md_bg_color: 0.043, 0.145, 0.278, 1

        MDBoxLayout:
            size_hint: 1, 1
            orientation: "vertical"
            spacing: dp(5)
            padding: dp(5)

            MDBoxLayout:
                orientation: "horizontal"
                pos_hint: {"top": 1}
                size_hint_y: 0.15

                MDIcon:
                    icon: 'account'
                    halign: 'center'
                    valign: 'middle'
                    size_hint_x: None
                    width: dp(34)
                    spacing: dp(30)
                    padding: dp(30)
                    theme_text_color: 'Custom'
                    text_color: 0.043, 0.145, 0.278, 1
                    size: dp(180), dp(180)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_touch_down:  root.go_to_profile() if self.collide_point(*args[1].pos) else None
                    canvas.before:
                        Color:
                            rgba: 174/255, 214/255, 241/255, 1
                        Ellipse:
                            size: self.size
                            pos: self.pos

                MDBoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    pos_hint: {"center_y": 0.5}
                    padding: dp(5)

                    MDLabel:
                        id: username
                        text: "Welcome"
                        bold: True
                        font_size: dp(20)
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        id: date
                        text: "Joined Date:"
                        font_size: dp(15)
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        id: limit
                        text: "Credit Limit:"
                        font_size: dp(15)
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        id: balance
                        text: "Available Balance:"
                        font_size: dp(15)
                        size_hint_y: None
                        height: self.texture_size[1]

            MDBoxLayout:
                orientation: "vertical"
                size_hint_y:0.47

                MDCard:
                    pos_hint:{"top": 1}

                    MDGridLayout:
                        cols: 2
                        spacing: dp(20)  # Equal gap between cards
                        padding: dp(20)  # Proper padding around the grid
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: dp(70)
                            md_bg_color: "#ffffff"
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 1.5
                                    rectangle: (self.x, self.y, self.width,self.height)
                            # Card 1
                            MDCard:
                                md_bg_color: "#ffffff"  # Customize background color
                                orientation: "vertical"
                                padding:dp(9), dp(3)
                                on_release: root.go_to_newloan_screen()

                                MDIcon:
                                    icon: 'newspaper'
                                    halign: 'center'
                                    valign: 'middle'
                                    size_hint_x: None
                                    width: dp(24)
                                    theme_text_color: 'Custom'
                                    text_color: 0.043, 0.145, 0.278, 1
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                                MDLabel:
                                    text: "New Loan Requests"
                                    font_size:dp(12)
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                    halign: "center"  # Center-align the label text
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: dp(70)
                            md_bg_color: "#ffffff"
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 1.5
                                    rectangle: (self.x, self.y, self.width,self.height)
                            MDCard:
                                md_bg_color: "#ffffff"  # Customize background color
                                orientation: "vertical"
                                padding:dp(9), dp(3)
                                on_release: root.go_to_view_loan_screen()

                                MDIcon:
                                    icon: 'bank'
                                    halign: 'center'
                                    valign: 'middle'
                                    size_hint_x: None
                                    width: dp(24)
                                    theme_text_color: 'Custom'
                                    text_color: 0.043, 0.145, 0.278, 1
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}



                                MDLabel:
                                    text: "View Loans"
                                    font_size:dp(12)
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                    halign: "center"
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: dp(70)
                            md_bg_color: "#ffffff"
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 1.5
                                    rectangle: (self.x, self.y, self.width,self.height)
                            MDCard:
                                md_bg_color: "#ffffff"  # Customize background color
                                orientation: "vertical"
                                padding:dp(9), dp(3)
                                on_release: root.go_to_dues_screen()


                                MDIcon:
                                    icon: 'calendar-today'
                                    halign: 'center'
                                    valign: 'middle'
                                    size_hint_x: None
                                    width: dp(24)
                                    theme_text_color: 'Custom'
                                    text_color: 0.043, 0.145, 0.278, 1
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                                MDLabel:
                                    text: "Today's Dues"
                                    font_size:dp(12)
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                    halign: "center"
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: dp(70)
                            md_bg_color: "#ffffff"
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 1.5
                                    rectangle: (self.x, self.y, self.width,self.height)
                            MDCard:
                                md_bg_color: "#ffffff"  # Customize background color
                                orientation: "vertical"
                                padding:dp(9), dp(3)
                                on_release: root.go_to_app_tracker()

                                MDIcon:
                                    icon: 'progress-check'
                                    halign: 'center'
                                    valign: 'middle'
                                    size_hint_x: None
                                    width: dp(24)
                                    theme_text_color: 'Custom'
                                    text_color: 0.043, 0.145, 0.278, 1
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                                MDLabel:
                                    text: "Application Tracker"
                                    font_size:dp(12)
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                    halign: "center"

                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: dp(70)
                            md_bg_color: "#ffffff"
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 1.5
                                    rectangle: (self.x, self.y, self.width,self.height)
                            MDCard:
                                md_bg_color: "#ffffff"  # Customize background color
                                orientation: "vertical"
                                padding:dp(9), dp(3)
                                on_release: root.go_to_transaction_history()
                                MDIcon:
                                    icon: 'history'
                                    halign: 'center'
                                    valign: 'middle'
                                    size_hint_x: None
                                    width: dp(24)
                                    theme_text_color: 'Custom'
                                    text_color: 0.043, 0.145, 0.278, 1
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                                MDLabel:
                                    text: "View Transaction History"
                                    font_size:dp(12)
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                    halign: "center"

                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: dp(70)
                            md_bg_color: "#ffffff"
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 1.5
                                    rectangle: (self.x, self.y, self.width,self.height)
                            MDCard:
                                md_bg_color: "#ffffff"  # Customize background color
                                orientation: "vertical"
                                padding:dp(9), dp(3)
                                on_release: root.go_to_fore_closer_details()

                                MDIcon:
                                    icon: 'file-document-outline'
                                    halign: 'center'
                                    valign: 'middle'
                                    size_hint_x: None
                                    width: dp(24)
                                    theme_text_color: 'Custom'
                                    text_color: 0.043, 0.145, 0.278, 1
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                                MDLabel:
                                    text: "Loan Foreclose"
                                    font_size:dp(12)
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                    halign: "center"

                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: dp(70)
                            md_bg_color: "#ffffff"
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 1.5
                                    rectangle: (self.x, self.y, self.width,self.height)
                            MDCard:
                                md_bg_color: "#ffffff"  # Customize background color
                                orientation: "vertical"
                                padding:dp(9), dp(3)
                                on_release:root.go_to_extend()

                                MDIcon:
                                    icon: 'clock'
                                    halign: 'center'
                                    valign: 'middle'
                                    size_hint_x: None
                                    width: dp(24)
                                    theme_text_color: 'Custom'
                                    text_color: 0.043, 0.145, 0.278, 1
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                                MDLabel:
                                    text: "Extended Loan Request"
                                    font_size:dp(12)
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                    halign: "center"



<ProfileScreen>
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "View Profile"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding:dp(10)
                spacing:dp(25)
                size_hint_y: None
                height: self.minimum_height
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)
                    BoxLayout:
                        id: box1
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(500)
                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Name:"
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: name
                                text: ""
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Email:"
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: email
                                text: ""
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Mobile No::"
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: mobile_no
                                text: ""
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Date Of Birth::"
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: dob
                                text: ""
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "City:"
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: city
                                text: ""
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Gender:"
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: gender
                                text: ""
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Marrital Status:"
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: marrital_status
                                text: ""
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"

                        MDFloatLayout:
                            MDRaisedButton:
                                text: "Edit Profile"
                                md_bg_color: 0.043, 0.145, 0.278, 1
                                font_name: "Roboto-Bold"
                                size_hint: 0.4, None
                                height: dp(50)
                                on_release:root.on_edit()
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                font_size:dp(15)
<EditScreen>
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "View Profile"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding:dp(10)
                spacing:dp(25)
                size_hint_y: None
                height: self.minimum_height
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)
                    BoxLayout:
                        id: box1
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(500)
                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Name:"
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDTextField:
                                id: name
                                text: ""
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Email:"
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: email
                                text: ""
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Mobile No::"
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDTextField:
                                id: mobile_no
                                text: ""
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Date Of Birth::"
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: dob
                                text: ""
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "City:"
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDTextField:
                                id: city
                                text: ""
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Gender:"
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            Spinner:
                                id: gender
                                text: "Select Gender"
                                multiline: False
                                size_hint: None, None
                                size: "180dp", "45dp"

                                halign: "center"
                                background_color: 1, 1, 1, 0
                                color: 0, 0, 0, 1
                                canvas.before:
                                    Color:
                                        rgba: 0, 0, 0, 1
                                    Line:
                                        width: 0.7
                                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                        MDFloatLayout:
                            MDRaisedButton:
                                text: "Save"
                                md_bg_color: 0.043, 0.145, 0.278, 1
                                font_name: "Roboto-Bold"
                                size_hint: 0.4, None
                                height: dp(50)
                                on_release:root.save_edited_data()
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                font_size:dp(15)
"""


class DashboardScreen(Screen):
    Builder.load_string(user_helpers)

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)
        log_email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search(email_user=log_email)
        credit = app_tables.fin_borrower.search(email_id=log_email)
        wallet = app_tables.fin_wallet.search(user_email=log_email)
        print(log_email)

        email_user = []
        name_list = []
        date = []
        limit = []
        balance = []

        for i in profile:
            email_user.append(i['email_user'])
            name_list.append(i['full_name'])
        for i in wallet:
            balance.append(i['wallet_amount'])
        for i in credit:
            limit.append(i['credit_limit'])
        for i in log_email:
            if 'signed_up' in i:  # Check if 'signed_up' key exists in the dictionary
                date.append(i['signed_up'])
        # Check if 'logged' is in the status list
        if log_email in email_user:
            log_index = email_user.index(log_email)
            self.ids.username.text = f"Welcome {name_list[log_index]}"
        else:
            # Handle the case when 'logged' is not in the status list
            self.ids.username.text = "User welcome to P2P"

        # Access the first element of the lists to avoid square brackets
        self.ids.limit.text = f"Credit Limit : {limit[0] if limit else ''}"
        self.ids.date.text = f"Joined Date : {date[0] if date else ''}"
        self.ids.balance.text = f"Available Balance : {balance[0] if balance else ''}"

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerLanding'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def go_to_newloan_screen(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_request_action(modal_view), 2)

    def perform_loan_request_action(self, modal_view):
        # Cancel the animation
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager

        self.manager.add_widget(Factory.NewloanScreen(name='NewloanScreen'))
        self.manager.current = 'NewloanScreen'

    def go_to_view_loan_screen(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_view_loan_screen_action(modal_view), 2)

    def perform_view_loan_screen_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()

        self.manager.add_widget(Factory.DashboardScreenVLB(name='DashboardScreenVLB'))
        self.manager.current = 'DashboardScreenVLB'

    def go_to_transaction_history(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size=dp(50), bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching transaction history)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_transaction_history_action(modal_view), 2)

    def perform_transaction_history_action(self, modal_view):
        # Dismiss the modal view
        modal_view.dismiss()

        # Get the ScreenManager
        sm = self.manager

        # Create a new instance of the TransactionBH screen
        transaction_bh_screen = TransactionBH(name='TransactionBH')

        # Add the TransactionBH screen to the existing ScreenManager
        sm.add_widget(transaction_bh_screen)

        # Switch to the TransactionBH screen
        sm.current = 'TransactionBH'

    def go_to_app_tracker(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_app_tracker_action(modal_view), 2)

    def perform_app_tracker_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager

        self.manager.add_widget(Factory.ALLLoansAPT(name='ALLLoansAPT'))
        self.manager.current = 'ALLLoansAPT'

    def go_to_extend(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_extend_action(modal_view), 2)

    def perform_extend_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()

        self.manager.add_widget(Factory.ExtensionLoansRequest(name='ExtensionLoansRequest'))
        self.manager.current = 'ExtensionLoansRequest'

    def go_to_fore_closer_details(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_fore_closer_details_action(modal_view), 2)

    def perform_fore_closer_details_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()

        self.manager.add_widget(Factory.LoansDetailsB(name='LoansDetailsB'))
        self.manager.current = 'LoansDetailsB'

    def go_to_loan_details(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_details_action(modal_view), 2)

    def perform_loan_details_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager

        self.manager.add_widget(Factory.LoansDetails(name='LoansDetails'))
        self.manager.current = 'LoansDetails'

    def logout(self):
        # Clear user data
        with open("emails.json", "r+") as file:
            user_data = json.load(file)
            # Check if user_data is a dictionary
            if isinstance(user_data, dict):
                for email, data in user_data.items():
                    if isinstance(data, dict) and data.get("logged_status", False):
                        data["logged_status"] = False
                        data["user_type"] = ""
                        break
                # Move the cursor to the beginning of the file
                file.seek(0)
                # Write the updated data back to the file
                json.dump(user_data, file, indent=4)
                # Truncate any remaining data in the file
                file.truncate()

        # Switch to MainScreen
        self.manager.current = 'MainScreen'

    def go_to_profile(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_profile_action(modal_view), 2)

    def perform_profile_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager

        self.manager.add_widget(Factory.ProfileScreen(name='ProfileScreen'))
        self.manager.current = 'ProfileScreen'

    def go_to_wallet(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_wallet(modal_view), 2)

    def perform_wallet(self, modal_view):
        from borrower_wallet import WalletScreen
        modal_view.dismiss()
        # Get the existing ScreenManager

        self.manager.add_widget(Factory.WalletScreen(name='WalletScreen'))
        self.manager.current = 'WalletScreen'

    def go_to_dues_screen(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="25sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_request_action(modal_view), 2)

    def perform_request_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        self.manager.add_widget(Factory.DuesScreen(name='DuesScreen'))
        self.manager.current = 'DuesScreen'

        # # Create a new instance of the LoginScreen
        # login_screen = BorrowerDuesScreen(name='DuesScreen')
        #
        # # Add the LoginScreen to the existing ScreenManager
        # sm.add_widget(login_screen)
        #
        # # Switch to the LoginScreen
        # sm.current = 'BorrowerDuesScreen'

    def help_module(self):
        from help_module import HelpScreen
        self.manager.add_widget(Factory.HelpScreen(name='HelpScreen'))
        self.manager.current = 'HelpScreen'


class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refresh_profile_data()  # Initial data retrieval
        Clock.schedule_interval(self.refresh_profile_data, 0)  # Schedule data refresh every 60 seconds

    def refresh_profile_data(self, dt=None):
        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)
        name = []
        email1 = []
        mobile_no = []
        dob = []
        city = []
        gender = []
        marrital_status = []
        for row in data:
            name.append(row['full_name'])
            email1.append(row['email_user'])
            mobile_no.append(row['mobile'])
            dob.append(row['date_of_birth'])
            city.append(row['city'])
            gender.append(row['gender'])
            marrital_status.append(row['marital_status'])
        if email in email1:
            index = email1.index(email)
            self.ids.name.text = str(name[index])
            self.ids.email.text = str(email1[index])
            self.ids.mobile_no.text = str(mobile_no[index])
            self.ids.dob.text = str(dob[index])
            self.ids.city.text = str(city[index])
            self.ids.gender.text = str(gender[index])
            self.ids.marrital_status.text = str(marrital_status[index])

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def refresh(self):
        pass

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('profile')

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id):
        self.ids[image_id].source = path  # Set the source of the Image widget
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False

    def on_edit(self):
        self.manager.add_widget(Factory.EditScreen(name='EditScreen'))
        self.manager.current = 'EditScreen'

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreen'


class EditScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        gender_data = app_tables.fin_gender.search()
        gender_list = []
        for i in gender_data:
            gender_list.append(i['gender'])
        self.unique_gender = []
        for i in gender_list:
            if i not in self.unique_gender:
                self.unique_gender.append(i)
        print(self.unique_gender)
        if len(self.unique_gender) >= 1:
            self.ids.gender.values = ['Select a Gender'] + self.unique_gender
        else:
            self.ids.gender.values = ['Select a Gender']

        email = self.get_email()
        data = app_tables.fin_user_profile.search()
        name = []
        email1 = []
        mobile_no = []
        dob = []
        city = []
        gender = []
        for row in data:
            name.append(row['full_name'])
            email1.append(row['email_user'])
            mobile_no.append(row['mobile'])
            dob.append(row['date_of_birth'])
            city.append(row['city'])
            gender.append(row['gender'])
        if email in email1:
            index = email1.index(email)
            self.ids.name.text = str(name[index])
            self.ids.email.text = str(email1[index])
            self.ids.mobile_no.text = str(mobile_no[index])
            self.ids.dob.text = str(dob[index])
            self.ids.city.text = str(city[index])
            self.ids.gender.text = str(gender[index])

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def save_edited_data(self):
        # Retrieve the edited data from the UI
        name = self.ids.name.text
        email = self.ids.email.text
        mobile_no = self.ids.mobile_no.text
        dob = self.ids.dob.text
        city = self.ids.city.text
        gender = self.ids.gender.text

        # Update the database with the edited data
        # Replace 'update_profile_data' with your actual database update function
        success = self.update_profile_data(name, email, mobile_no, dob, city, gender)

        if success:
            # If the update was successful, reload the profile data
            self.reload_profile_data()
            # self.show_validation_error("Database Update Sucessfully.")
            # If the update was successful, navigate back to the dashboard screen
            self.manager.add_widget(Factory.DashboardScreen(name='DashboardScreen'))
            self.manager.current = 'DashboardScreen'

        else:
            # Handle the case where the update failed (e.g., display an error message)
            self.on_back_button_press()

    def reload_profile_data(self):
        # Refresh the data in the ProfileScreen
        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)
        name = []
        email1 = []
        mobile_no = []
        dob = []
        city = []
        gender = []
        for row in data:
            name.append(row['full_name'])
            email1.append(row['email_user'])
            mobile_no.append(row['mobile'])
            dob.append(row['date_of_birth'])
            city.append(row['city'])
            gender.append(row['gender'])
        if email in email1:
            index = email1.index(email)
            self.ids.name.text = str(name[index])
            self.ids.email.text = str(email1[index])
            self.ids.mobile_no.text = str(mobile_no[index])
            self.ids.dob.text = str(dob[index])
            self.ids.city.text = str(city[index])
            self.ids.gender.text = str(gender[index])

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def update_profile_data(self, name, email, mobile_no, dob, city, gender):
        user_profiles = app_tables.fin_user_profile.search(email_user=email)

        # Check if any user profile exists
        if user_profiles:
            # Assuming there should be only one row per unique email address,
            # we retrieve the first matching row
            user_profile = user_profiles[0]

            # Update the user's profile data
            user_profile.update(full_name=name,
                                email_user=email,
                                mobile=mobile_no,
                                gender=gender,
                                city=city,
                                date_of_birth=dob
                                )
            return True
        else:
            # Handle the case where the user's profile does not exist
            return False

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('profile')

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id):
        self.ids[image_id].source = path  # Set the source of the Image widget
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ProfileScreen'

    def on_back_button_press(self):
        self.manager.current = 'ProfileScreen'


class MyScreenManager(ScreenManager):
    pass
