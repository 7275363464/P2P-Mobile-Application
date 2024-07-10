import json

import anvil
from anvil import tables
from anvil.tables import app_tables
from kivy.animation import Animation
from kivy.uix.popup import Popup
from kivymd.uix.list import OneLineListItem
from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.label import MDLabel
from kivy.metrics import dp

from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.factory import Factory

import server
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.properties import ListProperty, Clock, StringProperty, NumericProperty
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton, MDFlatButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
import sqlite3
from math import pow
from kivymd.uix.dialog import MDDialog, dialog
import anvil.server
from kivy.uix.spinner import Spinner
from datetime import datetime

from kivymd.uix.spinner import MDSpinner

user_helpers2 = """

<WindowManager>:
    NewloanScreen:
    
    NewloanScreen2:
    NewloanScreen3:
    MenuScreen:
        name: 'menu'
    PaymentDetailsScreen:
        name: 'payment_details'

<CustomSpinnerOption@SpinnerOption>:
    background_color:0, 0, 1, 1  
    color: 1, 1, 1, 1

<NewloanScreen>:
    name: 'NewloanScreen' 
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "New Loan Request"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding:dp(10)
                spacing:dp(15)
                size_hint_y: None
                height: self.minimum_height

                MDCard:
                    id: card
                    orientation: 'vertical'
                    size_hint: 1, None
                    height: dp(70)
                    padding: dp(15)
                    spacing: dp(3)
                    elevation: 0.4


                    MDGridLayout:
                        cols: 2
                        padding: dp(25)
                        spacing: dp(10)
                        MDLabel:
                            text: "Credit Limit" 
                            color:0.031, 0.463, 0.91, 1
                            bold:True
                            size_hint_y:None
                            height:dp(0)
                            halign: "left"
                            font_size:dp(23)
                        MDLabel:
                            id: credit_limit        
                            text: " " 
                            size_hint_y:None
                            height:dp(0)
                            halign: "left"
                            font_size:dp(20)



                MDBoxLayout:
                    id:loan_box1
                    orientation: 'vertical'
                    spacing: dp(-2)
                    padding: dp(30)
                    size_hint_y: None  # Ensure the layout fits within the ScrollView
                    height: self.minimum_height  # Dynamically adjust the height
                    canvas:
                        Color:
                            rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                        Line:
                            width: 0.7  # Border width
                            rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                    MDLabel:
                        font_size: dp(16)
                        text: "Product Group:"
                        bold: True
                        size_hint_y:None
                        height:dp(40)
                        halign: "left"

                    Spinner:
                        id: group_id1
                        text: "Select Group"
                        width: dp(200)
                        multiline: False
                        size_hint: 1, None
                        pos_hint: {'center_x':0.5, 'center_y':0.5}
                        halign: "left"
                        font_size: "15dp"
                        height: "47dp"
                        width: dp(200)

                        halign:"left"
                        background_normal: ''
                        color: 0, 0, 0, 1
                        option_cls: 'CustomSpinnerOption'  # Custom class for options
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rectangle: (self.x, self.y, self.width, self.height)
                        on_press: app.fetch_product_groups()
                        text_size: self.width - dp(20), None




                    MDLabel:
                        font_size:dp(16)
                        text: "Product Categories:"
                        bold: True
                        size_hint_y:None
                        height:dp(40)
                        halign: "left"

                    Spinner:
                        id: group_id2
                        text: "Select Categories"
                        width: dp(200)
                        multiline: False
                        size_hint: 1, None

                        height:dp(50)
                        halign:"left"
                        pos_hint: {'center_x':0.5, 'center_y':0.5}

                        background_normal: ''
                        color: 0, 0, 0, 1
                        option_cls: 'CustomSpinnerOption'  # Custom class for options
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rectangle: (self.x, self.y, self.width, self.height)
                        on_press: app.fetch_product_categories()
                        text_size: self.width - dp(20), None



                    MDLabel:
                        font_size:dp(16)
                        text: "Product Name:"
                        bold: True
                        size_hint_y:None
                        height:dp(40)
                        halign: "left"
                    Spinner:
                        id: group_id3
                        text: "Select product name"
                        width: dp(500)
                        multiline: False
                        size_hint: 1, None
                        height:dp(50)
                        halign:"left"
                        pos_hint: {'center_x':0.5, 'center_y':0.5}
                        size: "180dp", "45dp"
                        height:dp(50)
                        background_normal: ''
                        color: 0, 0, 0, 1
                        option_cls: 'CustomSpinnerOption'  # Custom class for options
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rectangle: (self.x, self.y, self.width, self.height)
                        on_press: app.fetch_product_name()
                        text_size: self.width - dp(20), None

                        on_text: app.fetch_product_description()

                    MDBoxLayout:
                        id:loan_box
                        opacity:0
                        orientation: 'vertical'
                        size_hint_y:None
                        height:dp(400)




                        MDLabel:
                            text: "Loan Amount:"
                            bold: True
                            size_hint_y:None
                            height:dp(30)
                            halign: "left"

                        MDTextField:
                            id: text_input1
                            width: dp(250)
                            multiline: False
                            mode:"rectangle"
                            hint_text: " Enter amount"
                            size_hint: 1, None

                            halign:"left"
                            height:dp(30)
                            input_type: 'number'  
                            radius: [dp(0), dp(0), dp(0), dp(0)]
                            on_touch_down: root.on_amount_touch_down()
                            on_text: root.validate_amount(text_input1,self.text)
                            background_color: 1, 1, 1, 0 
                            color: 0, 0, 0, 1
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            helper_text: ""




                        MDLabel:
                            text: "Tenure (Months):"
                            font_size:dp(16)
                            bold:True
                            size_hint_y:None
                            height:dp(40)
                            halign: "left"

                        MDTextField:
                            id: text_input2
                            size_hint_x: 0.91
                            multiline: False
                            halign:"left"
                            mode:"rectangle"
                            input_type: 'number'  
                            on_touch_down: root.on_loan_touch_down()
                            on_text: root.validate_tenure(text_input2,self.text)
                            hint_text: " Enter loan period"
                            radius: [dp(0), dp(0), dp(0), dp(0)]
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            helper_text: ""
                            helper_text_mode: "on_error"
                            size_hint: 1, None
                            height:dp(30)
                            background_color: 1, 1, 1, 0 
                            color: 0, 0, 0, 1





                        MDLabel:
                            font_size: dp(16)
                            text: "EMI Type:"
                            bold: True
                            size_hint_y:None
                            height:dp(50)
                            halign: "left"

                        Spinner:
                            id: group_id4
                            text: "Select EMI type"
                            width: dp(200)
                            multiline: False
                            halign:"left"
                            pos_hint: {'center_x':0.5, 'center_y':0.5}
                            size_hint: 1, None

                            height:dp(50)
                            background_normal: ''
                            color: 0, 0, 0, 1
                            option_cls: 'CustomSpinnerOption'  # Custom class for options
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1  
                                Line:
                                    width: 0.7
                                    rectangle: (self.x, self.y, self.width, self.height)
                            on_press: app.fetch_emi_type()
                            text_size: self.width - dp(20), None
                            disabled: not group_id4.text or group_id4.text == 'Select Categories'

                        MDLabel:
                            id: min_tenure 
                            color:1,1,1,1      
                            text: "" 
                            font_size:dp(1)
                            size_hint_y:None
                            height:dp(15)

                        MDLabel:
                            id: product_description
                            text: " "
                            font_size: dp(11)
                            size_hint_y: None
                            halign: "center"
                            padding: [dp(5), dp(5)]
                            height: self.texture_size[1] + dp(20) if self.text else 0 # Adjust height to fit content
                            canvas.before:

                                RoundedRectangle:
                                    size: self.size
                                    pos: self.pos
                                    radius: [15, 15, 15, 15]  # Adjust radius for rounded corners

                                Line:
                                    width: 0.3
                                    rectangle: (self.x, self.y, self.width, self.height)


                        MDRectangleFlatButton:
                            text: "Next"
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            on_release: root.go_to_newloan_screen1()
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "50dp"
                            font_name: "Roboto-Bold"



<NewloanScreen2>:
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "New Loan Request"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding:dp(0)
                spacing:dp(10)
                size_hint_y: None
                height: self.minimum_height


                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(10)
                    padding: dp(20)
                    size_hint_y: None
                    height: dp(730)

                    canvas.before:
                        Color:
                            rgba: 230/255, 245/255, 255/255, 1 
                        Rectangle:
                            pos: self.pos
                            size: self.size
                            # radius: [5, 5, 5, 5]
                            source: "background.jpg"

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Product Name"
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"

                        MDLabel:
                            id: product_name
                            text: ""
                            size_hint_y:None
                            height:dp(50)
                            font_size:dp(20)
                            bold: True
                            halign: "left"
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1 
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Loan Amount"
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: loan_amount
                            text: ""
                            font_size:dp(20)
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1


                    MDGridLayout:
                        cols: 2

                        MDLabel:
                            id: total_interest_label
                            text: ""  # Default text, will be updated dynamically
                            size_hint_y: None
                            height: dp(50)
                            bold: True
                            halign: "left"

                        MDLabel:
                            id: total_interest_amount
                            text: ""
                            size_hint_y: None
                            height: dp(50)
                            bold: True
                            font_size: dp(20)
                            halign: "left"
                            theme_text_color: 'Custom'
                            text_color: 140/255, 140/255, 140/255, 1

                    MDGridLayout:
                        cols: 2

                        MDLabel:
                            id: total_processing_label
                            text: ""  # Default text, will be updated dynamically
                            size_hint_y: None
                            height: dp(50)
                            bold: True
                            halign: "left"

                        MDLabel:
                            id: total_processing_fee_amount
                            size_hint_y: None
                            height: dp(50)
                            halign: "left"
                            bold: True
                            font_size: dp(20)
                            theme_text_color: 'Custom'
                            text_color: 140/255, 140/255, 140/255, 1


                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "EMI Type"
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"

                        MDLabel:
                            id: emi_type
                            text: ""
                            size_hint_y:None
                            height:dp(50)
                            font_size:dp(17)
                            bold: True
                            halign: "left"
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1        
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "EMI Tenure"
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"

                        MDLabel:
                            id: emi_tenure
                            text: ""
                            size_hint_y:None
                            height:dp(50)
                            font_size:dp(20)
                            bold: True
                            halign: "left"
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1              

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Monthly EMI"
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"

                        MDLabel:
                            id: monthly_emi
                            text: "interest"
                            size_hint_y:None
                            height:dp(50)
                            font_size:dp(20)
                            bold: True
                            halign: "left"
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Foreclosure"
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"

                        MDLabel:
                            id: foreclosure
                            text: ""
                            size_hint_y:None
                            height:dp(50)
                            font_size:dp(17)
                            bold: True
                            halign: "left"
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Total Repayment\\nAmount"
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"

                        MDLabel:
                            id: total
                            text: "interest"
                            size_hint_y:None
                            height:dp(50)
                            font_size:dp(20)
                            bold: True
                            halign: "left"
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1

                    MDGridLayout:
                        cols: 1
                        size_hint_y: None
                        height: self.minimum_height

                        MDBoxLayout:
                            size_hint_y: None
                            height: dp(50)

                            spacing: 10

                            MDLabel:
                                text: "Payment Details"
                                font_size: dp(16)
                                bold: True
                                halign: "left"

                            Button:
                                text: 'View Payment Details here'
                                background_color: 0, 0, 0, 0
                                color: 0, 0.5, 1, 1
                                font_size: '13sp'
                                size_hint: 2, None
                                size: self.texture_size
                                halign: "left"
                                pos_hint: {'center_y': 0.5}
                                on_release: root.go_to_menu_screen()


                    MDBoxLayout:
                        orientation:"horizontal"
                        size_hint_y: None
                        height: dp(50)
                        width:dp(300)
                        size_hint_x:None
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        spacing:dp(-10)

                        MDIconButton:
                            icon: "information-outline"
                            icon_size: dp(14)
                            pos_hint: {"center_y": .5}

                        MDLabel:
                            text: " The processing fees are added when you pay the total amount via EMI" 
                            color: 126/255, 126/255, 126/255, 1
                            font_size: '9sp'
                            size_hint: 2, None
                            size: self.texture_size
                            halign: "left"
                            pos_hint: {'center_y': 0.5}

                MDLabel:
                    text: " " 
                    size_hint_y:None
                    height:dp(15)
                MDFloatLayout:
                    MDRaisedButton:
                        text: "Send Request"
                        on_release: root.send_request()
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        font_size:dp(15)
                        size_hint: 0.4, None
                        height: "50dp"
                        font_name: "Roboto-Bold"
                MDLabel:
                    text: " " 
                    size_hint_y:None
                    height:dp(15)
<NewloanScreen3>:
    MDTopAppBar:
        title: "Loan Request Submitted"
        elevation: 2
        pos_hint: {'top': 1}
        title_align: 'center'
        md_bg_color: 0.043, 0.145, 0.278, 1
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDLabel:
            text: " "
        MDLabel:
            text: " "
        MDLabel:
            text: " "

        Image:
            source: "checkmark.png"
            size_hint: None, None
            size: "70dp", "70dp"
            pos_hint: {'center_x': 0.5}

        MDLabel:
            text: "Thank You"
            font_style: 'H4'
            bold: True
            halign: 'center'

        MDLabel:
            text: "Your loan request application has been received and you will be notified once it is approved."
            font_style: 'Body1'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]

        MDLabel:
            text: " "   
        MDLabel:
            text: " "
        MDLabel:
            text: " "

        MDRaisedButton:
            text: "Go Back Home"
            on_press: root.go_back_home()
            md_bg_color: 0.043, 0.145, 0.278, 1
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            size_hint: None, None
            size: "200dp", "50dp"
            pos_hint: {'center_x': 0.5}
            font_name: "Roboto-Bold"
        MDLabel:
            text: " "          
<MenuScreen>:

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)


        MDTopAppBar:
            title: "Payment Schedule Table"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            do_scroll_x: True
            do_scroll_y: True

            MDGridLayout:
                id: container
                cols: 7  # Number of columns in your table
                padding: dp(15)
                spacing: dp(40)
                size_hint_x: None
                width: dp(1400)
                size_hint_y: None
                height: self.minimum_height
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.25
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDLabel:
                    text: "Emi Number"
                    bold: True
                    font_size: dp(16)
                    halign: "left"
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            width: 1
                            rectangle: (self.x, self.y, self.width, self.height)
                    size_hint_x: None
                    width: dp(150)


                # Header row


                MDLabel:
                    text: "Beginning Balance"
                    bold: True
                    font_size: dp(16)
                    halign: "center"
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            width: 1
                            rectangle: (self.x, self.y, self.width, self.height)
                    size_hint_x: None
                    width: dp(150)

                MDLabel:
                    text: "Principal"
                    bold: True
                    font_size: dp(16)
                    halign: "center"
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            width: 1
                            rectangle: (self.x, self.y, self.width, self.height)
                    size_hint_x: None
                    width: dp(150)

                MDLabel:
                    text: "Interest Amount"
                    bold: True
                    font_size: dp(16)
                    halign: "center"
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            width: 1
                            rectangle: (self.x, self.y, self.width, self.height)
                    size_hint_x: None
                    width: dp(150)

                MDLabel:
                    text: "Processing Fee"
                    bold: True
                    font_size: dp(16)
                    halign: "center"
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            width: 1
                            rectangle: (self.x, self.y, self.width, self.height)
                    size_hint_x: None
                    width: dp(150)

                MDLabel:
                    text: "Total Payment"
                    bold: True
                    font_size: dp(16)
                    halign: "center"
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            width: 1
                            rectangle: (self.x, self.y, self.width, self.height)
                    size_hint_x: None
                    width: dp(150)



                MDLabel:
                    text: "Ending Balance"
                    bold: True
                    font_size: dp(16)
                    halign: "center"
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            width: 1
                            rectangle: (self.x, self.y, self.width, self.height)
                    size_hint_x: None
                    width: dp(150)


        MDRaisedButton:
            text: "Back"
            on_press: root.go_back()
            md_bg_color: 0.043, 0.145, 0.278, 1
            pos_hint: {'right': 1, 'y': 0.5}
            size_hint: 1, None
            height: "50dp"

"""

Builder.load_string(user_helpers2)


class NewloanScreen(Screen):
    # Add product_group, product_categories, product_description, credit_limit as attributes
    product_group = StringProperty("")
    product_categories = StringProperty("")
    product_description = StringProperty("")
    credit_limit = NumericProperty(0)

    # Define on_pre_enter method to initialize the screen
    def on_pre_enter(self, *args):

        Window.bind(on_keyboard=self.on_back_button)
        try:
            row = app_tables.fin_borrower.search()[0]
            self.credit_limit = row['credit_limit']
            self.ids.credit_limit.text = str(self.credit_limit)
        except Exception as e:
            print(f"Error: {e}")

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def refresh(self):
        pass

    def current(self):
        self.manager.current = 'DashboardScreen'

    def animate_loading_text(self, loading_label, modal_height):
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        loading_label.animation = anim

    def go_to_newloan_screen1(self):
        if (self.ids.group_id1.text == 'Select Group' or
                self.ids.group_id2.text == 'Select Categories' or
                self.ids.group_id3.text == 'Select product name'):
            self.show_dialog("Please select all fields.")
        else:
            try:
                with open('emails.json', 'r') as file:
                    emails_data = json.load(file)
                    user_email = emails_data.get('email_user')
                    print(f"User email: {user_email}")
            except Exception as e:
                print(f"Error reading emails.json: {e}")
                self.show_dialog("Unable to read user email.")
                return

            if not user_email:
                self.show_dialog("No email found in emails.json.")
                return

            selected_product_name = self.ids.group_id3.text
            print(f"Selected product name: {selected_product_name}")

            existing_loans = app_tables.fin_loan_details.search(borrower_email_id=user_email,
                                                                product_name=selected_product_name)
            existing_loan = list(existing_loans)
            print(f"Existing loans: {existing_loan}")

            if existing_loan:
                self.show_dialog(f"You already have a loan with the product {selected_product_name}."
                                 f"Cannot proceed for a new loan with the same product.")
            else:
                # Set product attributes before transitioning
                self.product_group = self.ids.group_id1.text
                self.product_categories = self.ids.group_id2.text
                self.product_description = self.ids.product_description.text

                modal_view = ModalView(size_hint=(None, None), size=(300, 100), background_color=(0, 0, 0, 0))
                loading_label = Label(text="Loading...", font_size=25)
                modal_view.add_widget(loading_label)
                modal_view.open()
                Clock.schedule_once(lambda dt: self.animate_loading_text(loading_label, modal_view.height), 0.1)
                Clock.schedule_once(lambda dt: self.performance_go_to_newloan_screen1(modal_view), 2)

    def performance_go_to_newloan_screen1(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        self.manager.add_widget(Factory.NewloanScreen2(name='NewloanScreen2'))
        self.manager.current = 'NewloanScreen2'

    def show_dialog(self, text):
        dialog = MDDialog(
            title="Warning",
            text=text,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def on_amount_touch_down(self):
        self.ids.text_input1.input_type = 'number'

    def on_loan_touch_down(self):
        self.ids.text_input2.input_type = 'number'

    def validate_amount(self, text_input, text):
        try:
            if not text:
                text_input.helper_text = ""
                text_input.error = False
                return

            amount = float(text)
            text_input.helper_text = ""

            product_name = self.ids.group_id3.text
            tenure = app_tables.fin_product_details.search(product_name=product_name)

            if tenure:
                max_amount = tenure[0]['max_amount']
                min_amount = tenure[0]['min_amount']

                if amount < float(min_amount):
                    text_input.helper_text = f"Enter amount more than {min_amount}"
                    text_input.error = True
                elif amount > float(max_amount):
                    text_input.helper_text = f"Enter amount less than {max_amount}"
                    text_input.error = True
                else:
                    text_input.error = False
            else:
                print(f"No data found for product: {product_name}")

        except ValueError:
            text_input.helper_text = "Please enter a valid number"
            text_input.error = True

        def reset_helper_text(instance_textfield, value):
            instance_textfield.helper_text = ""
            instance_textfield.error = False

        text_input.bind(on_focus=reset_helper_text)

    def go_to_lender_dashboard(self):
        self.manager.add_widget(Factory.DashboardScreen(name='DashboardScreen'))
        self.manager.current = 'DashboardScreen'

    def reset_fields(self):
        self.ids.text_input1.text = ""
        self.ids.text_input2.text = ""
        self.ids.group_id3.text = "Select EMI Type"

    def validate_tenure(self, text_input, text):
        try:
            if not text:
                text_input.helper_text = ""
                text_input.error = False
                return

            tenure = float(text)
            text_input.helper_text = ""

            product_name = self.ids.group_id3.text
            tenure_details = app_tables.fin_product_details.search(product_name=product_name)

            if tenure_details:
                max_tenure = tenure_details[0]['max_tenure']
                min_tenure = tenure_details[0]['min_tenure']

                if tenure < float(min_tenure):
                    text_input.helper_text = f"Enter tenure more than {min_tenure}"
                    text_input.error = True
                elif tenure > float(max_tenure):
                    text_input.helper_text = f"Enter tenure less than {max_tenure}"
                    text_input.error = True
                else:
                    text_input.error = False
            else:
                print(f"No tenure data found for product: {product_name}")

        except ValueError:
            text_input.helper_text = "Please enter a valid number"
            text_input.error = True

        def reset_helper_text(instance_textfield, value):
            instance_textfield.helper_text = ""
            instance_textfield.error = False

        text_input.bind(on_focus=reset_helper_text)


class NewloanScreen2(Screen):
    loan_amount = ""
    loan_tenure = ""
    emi_type = ""
    interest_rate = ""
    processing_fee = ""
    product_group = ""
    product_name = ""

    def fetch_product_details(self, product_name):
        tenure = app_tables.fin_product_details.search(product_name=product_name)
        if tenure:
            self.max_tenure = tenure[0]['max_tenure']
            self.min_tenure = tenure[0]['min_tenure']
            self.max_amount = tenure[0]['max_amount']
            self.min_amount = tenure[0]['min_amount']
            self.processing_fee = tenure[0]['processing_fee']
            self.interest_rate = tenure[0]['roi']
            print(self.interest_rate)
        else:
            self.max_tenure = self.min_tenure = self.max_amount = self.min_amount = 0
            self.processing_fee = self.interest_rate = 0
            print(f"No data found for product: {product_name}")

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)
        self.root_screen = self.manager.get_screen('NewloanScreen')

        if self.root_screen and self.root_screen.ids:
            loan_amount = float(self.root_screen.ids.text_input1.text)
            self.loan_tenure = float(self.root_screen.ids.text_input2.text)
            emi_tenure = int(self.loan_tenure)
            self.ids.emi_tenure.text = str(emi_tenure) + " " + "Months"
            self.ids.loan_amount.text = "₹" + " " + str(loan_amount)

            product_name = self.root_screen.ids.group_id3.text
            self.ids.product_name.text = str(product_name)
            self.fetch_product_details(product_name)
            tenure = app_tables.fin_product_details.search(product_name=product_name)
            roi = tenure[0]['roi']
            processing_fee = tenure[0]['processing_fee']
            foreclosure = tenure[0]['foreclose_type']
            foreclosure_months = tenure[0]['min_months']
            self.ids.total_interest_label.text = f"Interest ({str(roi)}%)"
            self.ids.total_processing_label.text = f"Processing fee ({str(processing_fee)}%)"
            if foreclosure == "Eligible":
                self.ids.foreclosure.text = f"{str(foreclosure)} after {str(foreclosure_months)} Months"
            else:
                self.ids.foreclosure.text = str(foreclosure)
            product_group = self.root_screen.product_group
            product_categories = self.root_screen.product_categories
            product_description = self.root_screen.product_description
            credit_limit = self.root_screen.credit_limit

            p = loan_amount
            t = self.loan_tenure
            monthly_interest_rate = float(self.interest_rate) / 100 / 12
            emi_denominator = ((1 + monthly_interest_rate) ** t) - 1
            if emi_denominator <= 0:
                raise ValueError("EMI calculation error: Invalid loan tenure or interest rate.")
            emi_numerator = p * monthly_interest_rate * ((1 + monthly_interest_rate) ** t)
            Monthly_EMI = emi_numerator / emi_denominator  # Resulting monthly EMI

            self.emi_type = self.root_screen.ids.group_id4.text.strip()
            self.ids.emi_type.text = str(self.emi_type)
            # Adjust calculation based on emi_type
            if self.emi_type == 'One Time':
                emi = Monthly_EMI * t
            elif self.emi_type == 'Three Months':
                emi = Monthly_EMI * 3
            elif self.emi_type == 'Six Months':
                emi = Monthly_EMI * 6
            elif self.emi_type == 'Monthly':
                emi = Monthly_EMI
            else:
                emi = 0  # Default value if emi_type is not recognized

            self.ids.monthly_emi.text = "₹" + " " + str(round(emi, 2))
            interest_amount = Monthly_EMI * t - p
            self.ids.total_interest_amount.text = "₹" + " " + str(round(interest_amount, 2))
            processing_fee_amount = (self.processing_fee / 100) * p
            self.ids.total_processing_fee_amount.text = "₹" + " " + str(round(processing_fee_amount, 2))
            total_repayment_amount = Monthly_EMI * t + interest_amount + processing_fee_amount
            self.ids.total.text = "₹" + " " + str(round(total_repayment_amount, 2))

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False

    def on_back_button_press(self):
        self.manager.current = 'NewloanScreen'

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'NewloanScreen'

    def current(self):
        self.manager.current = 'NewloanScreen'

    def animate_loading_text(self, loading_label, modal_height):
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def send_request(self):
        modal_view = ModalView(size_hint=(None, None), size=(300, 150), background_color=(0, 0, 0, 0))
        loading_label = Label(text="Loading...", font_size=25)
        modal_view.add_widget(loading_label)
        modal_view.open()
        Clock.schedule_once(lambda dt: self.animate_loading_text(loading_label, modal_view.height), 0.1)
        Clock.schedule_once(lambda dt: self.performance_send_request(modal_view), 2)

    def generate_loan_id(self):
        latest_loan = app_tables.fin_loan_details.search(tables.order_by("loan_id", ascending=False))

        if latest_loan and len(latest_loan) > 0:
            last_loan_id = latest_loan[0]['loan_id']
            counter = int(last_loan_id[2:]) + 1
        else:
            counter = 1000001
        return f"LA{counter}"

    def performance_send_request(self, modal_view):
        loan_amount_text = self.ids.loan_amount.text
        total_text = self.ids.total.text

        # Fetch interest rate and processing fee (assuming they are fetched correctly)
        roi_text = f"{self.interest_rate}%" if self.interest_rate else "0%"
        processing_fee_text = f"{self.processing_fee}%" if self.processing_fee else "0%"

        if loan_amount_text and roi_text and total_text:
            try:
                loan_amount = float(loan_amount_text.replace('₹', '').strip())
                loan_tenure = float(self.root_screen.ids.text_input2.text)
                product_name = self.root_screen.ids.group_id3.text
                product_group = self.root_screen.product_group
                product_categories = self.root_screen.product_categories
                product_description = self.root_screen.product_description
                credit_limit = self.root_screen.credit_limit

                roi = float(self.interest_rate)
                processing_fee = float(self.processing_fee)
                total_interest_amount = float(self.ids.total_interest_amount.text.replace('₹', '').strip())
                total_processing_fee_amount = float(self.ids.total_processing_fee_amount.text.replace('₹', '').strip())
                monthly_EMI = float(self.ids.monthly_emi.text.replace('₹', '').strip())
                emi_type = self.root_screen.ids.group_id4.text
                total_repayment = float(total_text.replace('₹', '').strip())
                date_of_apply = datetime.now().date()

                loan_id = self.generate_loan_id()
                email = anvil.server.call('another_method')
                customer = app_tables.fin_user_profile.search(email_user=email)
                if customer:
                    customer_id = customer[0]['customer_id']
                    borrower_name = customer[0]['full_name']
                else:
                    print("Customer not found.")
                product_id = app_tables.fin_product_details.search(product_name=product_name)
                product_id = product_id[0]['product_id']
                app_tables.fin_loan_details.add_row(
                    loan_id=str(loan_id),
                    borrower_full_name=borrower_name,
                    borrower_email_id=email,
                    borrower_customer_id=customer_id,
                    product_id=str(product_id),
                    loan_amount=float(loan_amount),
                    tenure=float(loan_tenure),
                    loan_updated_status="under process",
                    borrower_loan_created_timestamp=date_of_apply,
                    interest_rate=float(roi),
                    product_name=str(product_name),
                    total_repayment_amount=float(total_repayment),
                    remaining_amount=float(total_repayment),
                    product_description=str(product_description),
                    credit_limit=int(credit_limit),
                    total_processing_fee_amount=float(total_processing_fee_amount),
                    total_interest_amount=float(total_interest_amount),
                    monthly_emi=float(monthly_EMI),
                    emi_payment_type=str(emi_type)
                )

                # Update the labels with fetched values
                self.ids.total_interest_label.text = f"Total Interest\\nAmount ({roi_text})"
                self.ids.total_processing_label.text = f"Total Processing\\nFee Amount ({processing_fee_text})"

                modal_view.dismiss()
                self.clear_fields()
                self.manager.add_widget(Factory.NewloanScreen3(name='NewloanScreen3'))
                self.manager.current = 'NewloanScreen3'

            except ValueError as e:
                modal_view.dismiss()
                print(f"An error occurred: {e}")
        else:
            self.show_popup("Please fill in all fields before submitting.")

    def go_to_menu_screen(self):
        loan_amount = self.root_screen.ids.text_input1.text.strip()
        loan_tenure = self.root_screen.ids.text_input2.text.strip()
        emi_type = self.root_screen.ids.group_id4.text.strip()

        if not loan_amount or not loan_tenure or emi_type == 'Select EMI type':
            self.show_popup("Please enter all fields.")
        else:
            # Extract numeric value from the text
            interest_rate_text = self.ids.total_interest_amount.text.replace('₹', '').strip()
            processing_fee_text = self.ids.total_processing_fee_amount.text.replace('₹', '').strip()

            try:
                interest_rate = float(interest_rate_text)
                processing_fee = float(processing_fee_text)
            except ValueError as e:
                print(f"Error converting text to float: {e}")
                self.show_popup("Error in interest rate or processing fee format.")
                return

            # Check if MenuScreen already exists in the ScreenManager
            if 'menu' in self.manager.screen_names:
                # If it exists, get a reference to the existing MenuScreen
                menu_screen = self.manager.get_screen('menu')

                # Update the existing MenuScreen with new values
                menu_screen.update_values(loan_amount, loan_tenure, interest_rate, processing_fee, emi_type)
                self.manager.current = 'menu'  # Switch to the existing MenuScreen
            else:
                # If it doesn't exist, create a new MenuScreen and switch to it
                menu_screen = MenuScreen(name='menu', loan_amount=loan_amount, loan_tenure=loan_tenure,
                                         interest_rate=interest_rate, processing_fee=processing_fee,
                                         emi_type=emi_type)
                self.manager.add_widget(menu_screen)
                self.manager.current = 'menu'

    def clear_fields(self):
        self.root_screen.ids.text_input1.text = ""
        self.root_screen.ids.text_input2.text = ""
        self.root_screen.ids.group_id4.text = "Select EMI Type"

    def show_success_dialog(self, text):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.open_dashboard_screen(dialog),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ]
        )
        dialog.open()

    def open_dashboard_screen(self, dialog):
        dialog.dismiss()
        self.manager.current = 'DashboardScreen'


class NewloanScreen3(Screen):
    def go_back_home(self):
        self.manager.current = 'DashboardScreen'


class PaymentDetailsScreen(Screen):
    def go_to_menu_screen(self):
        self.manager.add_widget(Factory.MenuScreen(name='menu'))
        self.manager.current = 'menu'


# Register the PaymentDetailsScreen class with the Factory
Factory.register('PaymentDetailsScreen', cls=PaymentDetailsScreen)


class MenuScreen(Screen):
    def __init__(self, loan_amount=0, loan_tenure=0, interest_rate=0, processing_fee=0, emi_type="", **kwargs):
        super().__init__(**kwargs)

        self.loan_amount = float(loan_amount)
        self.loan_tenure = float(loan_tenure)
        self.interest_rate = float(interest_rate)
        self.processing_fee = float(processing_fee)
        self.emi_type = emi_type  # Assign selected EMI type
        self.update_calculation()

        if self.emi_type == 'Monthly':
            self.calculate_schedule()
        elif self.emi_type == 'One Time':
            self.calculate_one_time_payment()
        elif self.emi_type == 'Three Months':
            self.calculate_three_months_payment()
        elif self.emi_type == 'Six Months':
            self.calculate_six_months_payment()
        print(self.loan_amount)
        print(self.loan_tenure)
        print(interest_rate)
        print(processing_fee)
        print(self.emi_type)

    def update_values(self, loan_amount, loan_tenure, interest_rate, processing_fee, emi_type):
        self.loan_amount = float(loan_amount)
        self.loan_tenure = float(loan_tenure)
        self.interest_rate = float(interest_rate)
        self.processing_fee = float(processing_fee)
        self.emi_type = emi_type

        if self.emi_type == 'Monthly':
            self.calculate_schedule()
        elif self.emi_type == 'One Time':
            self.calculate_one_time_payment()
        elif self.emi_type == 'Three Months':
            self.calculate_three_months_payment()
        elif self.emi_type == 'Six Months':
            self.calculate_six_months_payment()

    def update_calculation(self):
        if self.emi_type == 'Monthly':
            self.calculate_schedule()
        elif self.emi_type == 'One Time':
            self.calculate_one_time_payment()
        elif self.emi_type == 'Three Months':
            self.calculate_three_months_payment()
        elif self.emi_type == 'Six Months':
            self.calculate_six_months_payment()
        else:
            print("Invalid EMI type")

    def calculate_schedule(self):
        container = self.ids.container
        container.clear_widgets()

        header_texts = [
            "Emi Number", "Beginning Balance", "Principal", "Interest",
            "Processing Fee", "Total Emi Payment", "Ending Balance"
        ]

        # Add header labels
        for text in header_texts:
            label = MDLabel(text=text, font_size=dp(14), halign="center", bold=True)
            container.add_widget(label)

        monthly_interest_rate = (self.interest_rate / 100) / 12
        monthly_emi = (self.loan_amount * monthly_interest_rate *
                       ((1 + monthly_interest_rate) ** self.loan_tenure)) / (
                              ((1 + monthly_interest_rate) ** self.loan_tenure) - 1)
        total_processing_fee = (self.processing_fee / 100) * self.loan_amount
        total_interest = (monthly_emi * self.loan_tenure) - self.loan_amount

        beginning_balance = self.loan_amount + total_processing_fee + total_interest
        loan_amount_beginning_balance = self.loan_amount

        for month in range(1, int(self.loan_tenure) + 1):
            monthly_interest = loan_amount_beginning_balance * monthly_interest_rate
            monthly_processing_fee = total_processing_fee / self.loan_tenure
            principal = monthly_emi - monthly_interest
            total_payment = monthly_emi + monthly_processing_fee + monthly_interest

            ending_balance = max(0, beginning_balance - total_payment)
            loan_amount_ending_balance = max(0, loan_amount_beginning_balance - principal)

            row_data = [
                f"{month}",
                f"Rs. {beginning_balance:.2f}",
                f"Rs. {principal:.2f}",
                f"Rs. {monthly_interest:.2f}",
                f"Rs. {monthly_processing_fee:.2f}",
                f"Rs. {total_payment:.2f}",
                f"Rs. {ending_balance:.2f}",
            ]

            for text in row_data:
                label = MDLabel(text=text, font_size=dp(12), halign="center")
                container.add_widget(label)

            beginning_balance = ending_balance
            loan_amount_beginning_balance = loan_amount_ending_balance

    def calculate_one_time_payment(self):
        container = self.ids.container
        container.clear_widgets()
        header_texts = [
            "Emi Number", "Beginning Balance", "Principal", "Interest",
            "Processing Fee", "Total Emi Payment", "Ending Balance"
        ]

        # Add header labels
        for text in header_texts:
            label = MDLabel(text=text, font_size=dp(14), halign="center", bold=True)
            container.add_widget(label)
        monthly_interest_rate = (self.interest_rate / 100) / 12
        total_processing_fee = (self.processing_fee / 100) * self.loan_amount

        emi_numerator = self.loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** self.loan_tenure)
        emi_denominator = ((1 + monthly_interest_rate) ** self.loan_tenure) - 1

        if emi_denominator == 0:
            return

        monthly_emi = emi_numerator / emi_denominator
        total_interest = monthly_emi * self.loan_tenure - self.loan_amount

        total_payment = monthly_emi + total_interest + total_processing_fee
        beginning_balance = monthly_emi * self.loan_tenure + total_interest + total_processing_fee

        row_data = [
            "1",
            f"Rs. {beginning_balance:.2f}",
            f"Rs. {self.loan_amount:.2f}",
            f"Rs. {total_interest:.2f}",
            f"Rs. {total_processing_fee:.2f}",
            f"Rs. {total_payment:.2f}",
            f"Rs. {0:.2f}",
        ]

        for text in row_data:
            label = MDLabel(text=text, font_size=dp(12), halign="center")
            container.add_widget(label)

    def calculate_three_months_payment(self):
        container = self.ids.container
        container.clear_widgets()

        header_texts = [
            "Emi Number", "Beginning Balance", "Principal", "Interest",
            "Processing Fee", "Total Emi Payment", "Ending Balance"
        ]

        # Add header labels
        for text in header_texts:
            label = MDLabel(text=text, font_size=dp(14), halign="center", bold=True)
            container.add_widget(label)

        monthly_interest_rate = (self.interest_rate / 100) / 12
        total_processing_fee = (self.processing_fee / 100) * self.loan_amount

        emi_numerator = self.loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** self.loan_tenure)
        emi_denominator = ((1 + monthly_interest_rate) ** self.loan_tenure) - 1

        if emi_denominator == 0:
            return

        monthly_emi = emi_numerator / emi_denominator
        total_interest = (monthly_emi * self.loan_tenure) - self.loan_amount

        beginning_balance = monthly_emi * self.loan_tenure + total_interest + total_processing_fee

        num_periods = int(self.loan_tenure // 3)
        remaining_months = int(self.loan_tenure % 3)
        loan_amount_beginning_balance = self.loan_amount

        for period in range(1, num_periods + 1):
            principal_sum = 0
            interest_sum = 0
            processing_fee_sum = 0

            for month in range(3):
                monthly_interest = loan_amount_beginning_balance * monthly_interest_rate
                principal = monthly_emi - monthly_interest

                principal_sum += principal
                interest_sum += monthly_interest
                processing_fee_sum += total_processing_fee / self.loan_tenure

            total_payment = (monthly_emi * 3) + processing_fee_sum + interest_sum

            ending_balance = max(0, beginning_balance - total_payment)
            loan_amount_ending_balance = max(0, loan_amount_beginning_balance - principal_sum)

            row_data = [
                f"{period}",
                f"Rs. {beginning_balance:.2f}",
                f"Rs. {principal_sum:.2f}",
                f"Rs. {interest_sum:.2f}",
                f"Rs. {processing_fee_sum:.2f}",
                f"Rs. {total_payment:.2f}",
                f"Rs. {ending_balance:.2f}",
            ]

            for text in row_data:
                label = MDLabel(text=text, font_size=dp(12), halign="center")
                container.add_widget(label)

            beginning_balance = ending_balance
            loan_amount_beginning_balance = loan_amount_ending_balance

        # Handle the remaining months
        if remaining_months > 0:
            principal_sum = 0
            interest_sum = 0
            processing_fee_sum = 0

            for month in range(remaining_months):
                monthly_interest = loan_amount_beginning_balance * monthly_interest_rate
                principal = monthly_emi - monthly_interest

                principal_sum += principal
                interest_sum += monthly_interest
                processing_fee_sum += total_processing_fee / self.loan_tenure

            total_payment = (monthly_emi * remaining_months) + processing_fee_sum + interest_sum

            ending_balance = max(0, beginning_balance - total_payment)
            loan_amount_ending_balance = max(0, loan_amount_beginning_balance - principal_sum)

            row_data = [
                f"{num_periods + 1}",
                f"Rs. {beginning_balance:.2f}",
                f"Rs. {principal_sum:.2f}",
                f"Rs. {interest_sum:.2f}",
                f"Rs. {processing_fee_sum:.2f}",
                f"Rs. {total_payment:.2f}",
                f"Rs. {ending_balance:.2f}",
            ]

            for text in row_data:
                label = MDLabel(text=text, font_size=dp(12), halign="center")
                container.add_widget(label)

            beginning_balance = ending_balance
            loan_amount_beginning_balance = loan_amount_ending_balance

    def calculate_six_months_payment(self):
        container = self.ids.container
        container.clear_widgets()

        header_texts = [
            "Emi Number", "Beginning Balance", "Principal", "Interest",
            "Processing Fee", "Total Emi Payment", "Ending Balance"
        ]

        # Add header labels
        for text in header_texts:
            label = MDLabel(text=text, font_size=dp(14), halign="center", bold=True)
            container.add_widget(label)

        monthly_interest_rate = (self.interest_rate / 100) / 12
        total_processing_fee = (self.processing_fee / 100) * self.loan_amount

        # Check for valid EMI calculation
        emi_numerator = self.loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** self.loan_tenure)
        emi_denominator = ((1 + monthly_interest_rate) ** self.loan_tenure) - 1

        if emi_denominator == 0:
            return

        monthly_emi = emi_numerator / emi_denominator
        total_interest = (monthly_emi * self.loan_tenure) - self.loan_amount

        beginning_balance = monthly_emi * self.loan_tenure + total_processing_fee + total_interest

        # Calculate the number of six-month periods
        num_periods = int(self.loan_tenure // 6)
        remaining_months = int(self.loan_tenure % 6)
        loan_amount_beginning_balance = self.loan_amount

        # Loop over each six-month period to calculate payments
        for period in range(1, num_periods + 1):
            principal_sum = 0
            interest_sum = 0
            processing_fee_sum = 0

            for month in range(6):
                monthly_interest = loan_amount_beginning_balance * monthly_interest_rate
                principal = monthly_emi - monthly_interest

                principal_sum += principal
                interest_sum += monthly_interest
                processing_fee_sum += total_processing_fee / self.loan_tenure

            total_payment = (monthly_emi * 6) + processing_fee_sum + interest_sum

            # Calculate ending balance for this period
            ending_balance = max(0, beginning_balance - total_payment)
            loan_amount_ending_balance = max(0, loan_amount_beginning_balance - principal_sum)

            # Prepare the row data for this period
            row_data = [
                f"{period}",
                f"Rs. {beginning_balance:.2f}",
                f"Rs. {principal_sum:.2f}",
                f"Rs. {interest_sum:.2f}",
                f"Rs. {processing_fee_sum:.2f}",
                f"Rs. {total_payment:.2f}",
                f"Rs. {ending_balance:.2f}",
            ]

            # Add row data to the container
            for text in row_data:
                label = MDLabel(text=text, font_size=dp(12), halign="center")
                container.add_widget(label)

            beginning_balance = ending_balance
            loan_amount_beginning_balance = loan_amount_ending_balance

        # Handle the remaining months
        if remaining_months > 0:
            principal_sum = 0
            interest_sum = 0
            processing_fee_sum = 0

            for month in range(remaining_months):
                monthly_interest = loan_amount_beginning_balance * monthly_interest_rate
                principal = monthly_emi - monthly_interest

                principal_sum += principal
                interest_sum += monthly_interest
                processing_fee_sum += total_processing_fee / self.loan_tenure

            total_payment = (monthly_emi * remaining_months) + processing_fee_sum + interest_sum

            # Calculate ending balance for the remaining months
            ending_balance = max(0, beginning_balance - total_payment)
            loan_amount_ending_balance = max(0, loan_amount_beginning_balance - principal_sum)

            # Prepare the row data for the remaining months
            row_data = [
                f"{num_periods + 1}",
                f"Rs. {beginning_balance:.2f}",
                f"Rs. {principal_sum:.2f}",
                f"Rs. {interest_sum:.2f}",
                f"Rs. {processing_fee_sum:.2f}",
                f"Rs. {total_payment:.2f}",
                f"Rs. {ending_balance:.2f}",
            ]

            # Add row data for the remaining months to the container
            for text in row_data:
                label = MDLabel(text=text, font_size=dp(12), halign="center")
                container.add_widget(label)

            beginning_balance = ending_balance
            loan_amount_beginning_balance = loan_amount_ending_balance

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'NewloanScreen2'


# Define the PaymentItem class
class PaymentItem(OneLineListItem):
    def __init__(self, payment_str='', loan_amount=0, emi_amount=0, interest_amount=0,
                 processing_fee_amount=0, total_payment=0, balance_amount=0, principal=0, beginning_balance=0,
                 **kwargs):
        super().__init__(**kwargs)
        self.text = payment_str
        self.loan_amount = loan_amount
        self.emi_amount = emi_amount
        self.interest_amount = interest_amount
        self.processing_fee_amount = processing_fee_amount
        self.total_payment = total_payment
        self.balance_amount = balance_amount
        self.principal = principal
        self.beginning_balance = beginning_balance
        self.bind(on_release=self.on_item_click)

    def on_item_click(self, *args):
        app = App.get_running_app()
        screen_manager = app.root

        # Check if the PaymentDetailsScreen already exists in the ScreenManager
        if 'payment_details' in screen_manager.screen_names:
            # If it exists, get the reference to the existing screen
            payment_details_screen = screen_manager.get_screen('payment_details')
        else:
            # If it doesn't exist, create a new PaymentDetailsScreen
            payment_details_screen = PaymentDetailsScreen(name='payment_details')
            # Add the PaymentDetailsScreen to the ScreenManager
            screen_manager.add_widget(payment_details_screen)

        # Update the labels with the corresponding values
        # payment_details_screen.ids.loan_label.text = f" Rs. {self.loan_amount:.2f}"
        payment_details_screen.ids.emi_label.text = f"Rs. {self.emi_amount:.2f}"
        payment_details_screen.ids.interest_label.text = f" Rs. {self.interest_amount:.2f}"
        payment_details_screen.ids.processing_fee_label.text = f" Rs. {self.processing_fee_amount:.2f}"
        payment_details_screen.ids.total_payment_label.text = f" Rs. {self.total_payment:.2f}"
        payment_details_screen.ids.balance_label.text = f" Rs. {self.balance_amount:.2f}"
        payment_details_screen.ids.principal_label.text = f" Rs. {self.principal:.2f}"
        payment_details_screen.ids.beginning_balance_label.text = f" Rs. {self.beginning_balance:.2f}"

        # Switch to the PaymentDetailsScreen
        screen_manager.current = 'payment_details'


class MyScreenManager(ScreenManager):
    pass