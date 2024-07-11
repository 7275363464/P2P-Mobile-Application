import os
import re
from anvil import media
import anvil.server
import base64
from anvil import media
from io import BytesIO
from kivy.core.image import Image as CoreImage
from anvil.tables import app_tables
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivymd.toast import toast
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
import sqlite3
from kivy import platform
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
import sqlite3
from kivymd.uix.pickers import MDDatePicker
from kivy.utils import platform
from kivy.clock import mainthread
from datetime import datetime, date
from kivy.uix.button import Button
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.snackbar import Snackbar
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from kivy.uix.label import Label
from kivymd.uix.spinner import MDSpinner
import json
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivy.graphics import Color, Line
from kivy.utils import get_color_from_hex
from kivy.core.image import Image as CoreImage
from io import BytesIO
import base64
import json

from kivymd.uix.textfield import MDTextField
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.properties import StringProperty
import anvil
from anvil.tables import app_tables
from io import BytesIO
import base64
from kivy.core.image import Image as CoreImage
from anvil._server import LazyMedia
import tempfile
from kivy.uix.image import AsyncImage

from borrower_dashboard import DashboardScreen

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission
    )
import anvil.server

# anvil.server.connect("server_VRGEXX5AO24374UMBBQ24XN6-ZAWBX57M6ZDN6TBV")
Borrower = '''
<WindowManager>:
    BorrowerScreen:
    BorrowerScreen1:
    BorrowerScreen2:
    BorrowerScreen3:
    # BorrowerScreen_Edu_10th:
    # BorrowerScreen_Edu_Intermediate:
    # BorrowerScreen_Edu_Bachelors:
    # BorrowerScreen_Edu_Masters:
    # BorrowerScreen_Edu_PHD:
    BorrowerScreen4:
    BorrowerScreen5:
    BorrowerScreen6:
    BorrowerScreen7:
    BorrowerScreen8:
    BorrowerScreen9:
    BorrowerScreen10:
    BorrowerScreen11:
    BorrowerScreen12:
    BorrowerScreen13:
    BorrowerScreen14:
    BorrowerScreen15:
    BorrowerScreen16:
    BorrowerScreen17:
    BorrowerScreen18:
    BorrowerScreen19:
    BorrowerScreen20:
    BorrowerScreen21:
    BorrowerScreen22:
    BorrowerScreen23:
    BorrowerScreen24:
    BorrowerScreen25:
    BorrowerScreen26:

<CustomSpinnerOption>:
    background_color: 0, 1, 0, 1  # Example: Green background
    color: 1, 0, 0, 1  # Example: Red text color
<BorrowerScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "P2P LENDING"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.go_to_dashboard()]]
            right_action_items: [['home', lambda x: root.go_to_dashboard()]]
            title_align: 'center'  # Center-align the title
            md_bg_color: 0.043, 0.145, 0.278, 1
        
        MDScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(18)
                padding: dp(30)
                size_hint_y: None  # Ensure the layout fits within the ScrollView
                height: self.minimum_height  # Dynamically adjust the height
                   
        
                MDLabel:
                    text: 'Borrower Registration Form'
                    halign: 'center'
                    font_size: "20dp"
                    font_name: "Roboto-Bold"
                    size_hint_y: None
                    height: dp(50)
    
                MDTextField:
                    id: username
                    hint_text: ' Enter Full Name *'
                    multiline: False
                    helper_text: "Enter Valid Name"
                    helper_text_mode: 'on_focus'
                    height: self.minimum_height
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    radius: [0, 0, 0,0]
                    mode: "rectangle"
        
                Spinner:
                    id: gender_id
                    text: "Select Gender"
                    font_size: "15dp"
                    multiline: False
                    multiline: False
                    size_hint: 1, None
                    halign: "left"
                    height: "48dp"
                    background_color: 0, 0, 0, 0
                    background_normal: ''
                    text_size: self.width - dp(20), None
                    color: 0, 0, 0, 1
                    option_cls: 'CustomSpinnerOption'
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1  # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.8 

                MDBoxLayout:
                    orientation: 'horizontal'
                    spacing: "10dp"
                    size_hint: 1, None
                    halign: "left"
                    font_size: "15dp"
                    height: "48dp"
                    width: dp(200)  
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1   # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.8    
                    MDLabel:
                        id: date_textfield
                        text: " Enter Date Of Birth *"
                        helper_text: 'YYYY-MM-DD'
                        helper_text_mode: "on_error"
                        font_size: "15dp"
                        height: dp(40)
                        width: dp(300)
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        on_touch_down: root.on_date_touch_down()
                        mode: "rectangle"
                        radius: [0, 0, 0,0]
                    MDIconButton:
                        icon: 'calendar'
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        on_release: root.show_date_picker()
    
    
                MDTextField:
                    id: mobile_number
                    hint_text: ' Enter mobile number *'
                    multiline: False
                    input_type: 'number'  
                    on_touch_down: root.on_mobile_number_touch_down()
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    mode: "rectangle"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    radius: [0, 0, 0,0]
    
                MDTextField:
                    id: alternate_email
                    hint_text: ' Enter Alternate Email ID *'
                    multiline: False
                    helper_text: "Enter Valid Alternate Email ID"
                    helper_text_mode: 'on_focus'
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    mode: "rectangle"
                    radius: [0, 0, 0,0]
    
                BoxLayout:
                    orientation: 'horizontal'
                    padding: "10dp"
                    spacing: "10dp"
                    size_hint: 1, None
                    halign: "left"
                    font_size: "15dp"
                    height: "60dp"
                    width: dp(200)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1  # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.8 
    
                    MDIconButton:
                        icon: 'upload'
                        id: upload_icon1
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1  # Black text color
                        size_hint_x: None
                        width: dp(24)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        on_release: app.root.get_screen('BorrowerScreen').check_and_open_file_manager1()
    
                    MDLabel:
                        id: upload_label1
                        text: 'Upload Profile Photo'
                        halign: 'left'
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1  # Black text color
                        size_hint_y: None
                        height: dp(36)
                        valign: 'middle'  # Align the label text vertically in the center
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
                    Image:
                        id: image_label1
                        source: ''
                        allow_stretch: True
                        keep_ratio: True
                        size_hint_y: None
                        size: dp(50), dp(50)
                        height: dp(36)
                        valign: 'middle'  # Align the label text vertically in the center
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        on_touch_down: root.on_image_click(self, args[1])
    
                MDTextField:
                    id: aadhar_number
                    hint_text: ' Enter Government ID1 *'
                    multiline: False
                    size_hint_y: None
                    height: self.minimum_height
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    on_text: root.on_aadhar_number_text(self.text)
                    mode: "rectangle"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    radius: [0, 0, 0,0]
    
                BoxLayout:
                    id: GovID1
                    orientation: 'horizontal'
                    padding: "10dp"
                    spacing: "10dp"
                    size_hint: 1, None
                    halign: "left"
                    font_size: "15dp"
                    height: "48dp"
                    width: dp(200)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1  # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.8  
    
                    MDIconButton:
                        icon: 'upload'
                        id: upload_icon2
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1  # Black text color
                        size_hint_x: None
                        width: dp(24)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        on_release: app.root.get_screen('BorrowerScreen').check_and_open_file_manager2()
                        disabled: True
    
                    MDLabel:
                        id: upload_label2
                        text: 'Upload Govt ID1'
                        halign: 'left'
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1  # Black text color
                        size_hint_y: None
                        height: dp(36)
                        valign: 'middle'  # Align the label text vertically in the center
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
                    Image:
                        id: image_label2
                        source: ''
                        allow_stretch: True
                        keep_ratio: True
                        size_hint_y: None
                        size: dp(50), dp(50)
                        height: dp(36)
                        valign: 'middle'  # Align the label text vertically in the center
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        on_touch_down: root.on_image_click(self, args[1])
    
                MDTextField:
                    id: pan_number
                    hint_text: ' Enter Government ID2 *'
                    multiline: False
                    size_hint_y: None
                    height: self.minimum_height
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    on_text: root.on_pan_number_text(self.text)
                    mode: "rectangle"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    radius: [0, 0, 0,0]
    
    
                BoxLayout:
                    id: GovID2
                    orientation: 'horizontal'
                    padding: "10dp"
                    spacing: "10dp"
                    size_hint: 1, None
                    halign: "left"
                    font_size: "15dp"
                    height: "48dp"
                    width: dp(200)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1  # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.8 
    
                    MDIconButton:
                        id: upload_icon3
                        icon: 'upload'
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1  # Black text color
                        size_hint_x: None
                        width: dp(24)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        on_release: app.root.get_screen('BorrowerScreen').check_and_open_file_manager3()
                        disabled: True
    
                    MDLabel:
                        id: upload_label2
                        text: 'Upload Govt ID2'
                        halign: 'left'
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1  # Black text color
                        size_hint_y: None
                        height: dp(36)
                        valign: 'middle'  # Align the label text vertically in the center
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
                    Image:
                        id: image_label3
                        source: ''
                        allow_stretch: True
                        keep_ratio: True
                        size_hint_y: None
                        size: dp(50), dp(50)
                        height: dp(36)
                        valign: 'middle'  # Align the label text vertically in the center
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        on_touch_down: root.on_image_click(self, args[1])
    
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(username.text, gender_id.text, date_textfield.text, mobile_number.text, alternate_email.text, aadhar_number.text, pan_number.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<CustomSpinnerOption@SpinnerOption>:
    background_color:0, 0, 1, 1  
    color: 1, 1, 1, 1  # Change the text color if needed

<BorrowerScreen3>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "P2P LENDING"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen24')]]
            right_action_items: [['home', lambda x: root.go_to_dashboard()]]
            title_align: 'center'  # Center-align the title
            md_bg_color: 0.043, 0.145, 0.278, 1
        
        MDScrollView:
            MDBoxLayout:
                id: parent_layout_id
                orientation: 'vertical'
                # spacing: dp(5)
                padding: dp(30)
                size_hint_y: None
                height: self.minimum_height

                # dropdown details
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(5)
                    padding: dp(10)
                    size_hint_y: None
                    height: dp(180)
                   
                    MDLabel:
                        text: 'Borrower Registration Form'
                        halign: 'center'
                        font_size: "20dp"
                        font_name: "Roboto-Bold"
        
                    MDLabel:
                        text: 'Education Details'
                        halign: 'center'
                        bold: True
        
                    MDLabel:
                        text: "Select Your Education Type:"
                        halign: 'left'
                        font_size: "15dp"
                        font_name: "Roboto-Bold"
                    
                    Spinner:
                        id: spinner_id
                        text: "Select Education Details"
                        font_size: "15dp"
                        multiline: False
                        size_hint: 1, None
                        height: "40dp"
                        width: dp(180)
                        text_size: self.width - dp(20), None
                        background_color: 0, 0, 0, 0
                        background_normal: ''
                        color: 0, 0, 0, 1  #0.043, 0.145, 0.278, 1
                        option_cls: 'CustomSpinnerOption'
                        on_text: root.update_education_details(spinner_id.text)
                        canvas.before:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
                       
                # 10th details
                MDBoxLayout:
                    id: box_10th
                    orientation: 'vertical'
                    spacing: dp(5)
                    padding: dp(10)
                    size_hint_y: None
                    height: dp(220)
                    
                    MDLabel:
                        text: "Upload 10th class certificate *"
                        halign: 'left'
                        bold: True
                        size_hint_y: None
                        height: dp(50)
        
                    BoxLayout:
                        orientation: 'horizontal'
                        # padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(63)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager1()
        
                        MDLabel:
                            id: upload_label1
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                        Image:
                            id: image_label1
                            source: ''
                            allow_stretch: True
                            on_touch_down: root.on_image_click(self, args[1])
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                    GridLayout:
                        cols: 1
                        spacing:dp(10)
                        padding: [0, "30dp", 0, 0]
                        MDRectangleFlatButton:
                            text: "Next"
                            on_release: root.go_to_borrower_screen_10()
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "50dp"
                            font_name: "Roboto-Bold"

                # intermediate/puc
                MDBoxLayout:
                    id: box_12th
                    orientation: 'vertical'
                    spacing: dp(5)
                    padding: dp(10)
                    size_hint_y: None
                    height: dp(280)
                   
                    MDLabel:
                        text: "Upload 10th class certificate *"
                        halign: 'left'
                        bold: True
                        size_hint_y: None
                        height: dp(50)
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(63)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager2()
            
                        MDLabel:
                            id: upload_label1
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                        Image:
                            id: image_label2
                            source: ''
                            allow_stretch: True
                            on_touch_down: root.on_image_click(self, args[1])
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            
                    MDLabel:
                        text: "Upload Intermediate/PUC *"
                        halign: 'left'
                        bold: True
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "5dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager3()
        
                        MDLabel:
                            id: upload_label2
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                        Image:
                            id: image_label3
                            source: ''
                            allow_stretch: True
                            on_touch_down: root.on_image_click(self, args[1])
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    GridLayout:
                        cols: 1
                        spacing:dp(15)
                        padding: [0, "30dp", 0, 0]
        
                        MDRectangleFlatButton:
                            text: "Next"
                            on_release: root.go_to_borrower_screen_11()
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "20dp"
                            font_name: "Roboto-Bold"    
                            
                #   for bachelors                
                MDBoxLayout:
                    id: box_bachelors
                    orientation: 'vertical'
                    spacing: dp(5)
                    padding: dp(10)
                    size_hint_y: None
                    height: dp(400)
                  
                    MDLabel:
                        text: "Upload 10th class Certificate *"
                        halign: 'left'
                        bold: True
                                            
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
                
                
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager4()
        
                        MDLabel:
                            id: upload_label1
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                        Image:
                            id: image_label4
                            source: ''
                            allow_stretch: True
                            on_touch_down: root.on_image_click(self, args[1])
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                
                    MDLabel:
                        text: "Upload Intermediate/PUC Certificate *"
                        halign: 'left'
                        bold: True
                
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
                
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager5()
                
                        MDLabel:
                            id: upload_label2
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                
                        Image:
                            id: image_label5
                            source: ''
                            allow_stretch: True
                            on_touch_down: root.on_image_click(self, args[1])
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    
                    MDLabel:
                        text: "Upload Bachelors Certificate *"
                        halign: 'left'
                        bold: True
                
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
                
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager6()
                
                        MDLabel:
                            id: upload_label3
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                
                        Image:
                            id: image_label6
                            on_touch_down: root.on_image_click(self, args[1])
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    GridLayout:
                        cols: 1
                        spacing:dp(15)
                        padding: [0, "30dp", 0, 0]
                        MDRectangleFlatButton:
                            text: "Next"
                            on_release: root.go_to_borrower_screen_btech()
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "50dp"
                            font_name: "Roboto-Bold"    
                # master details
                MDBoxLayout:
                    id: box_masters
                    orientation: 'vertical'
                    spacing: dp(5)
                    padding: dp(10)
                    size_hint_y: None
                    height: dp(480)
                    
                    MDLabel:
                        text: "Upload 10th class Certificate *"
                        halign: 'left'
                        bold: True
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager7()
        
                        MDLabel:
                            id: upload_label1
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                        Image:
                            id: image_label7
                            on_touch_down: root.on_image_click(self, args[1])
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                    MDLabel:
                        text: "Upload Intermediate/PUC Certificate *"
                        halign: 'left'
                        bold: True
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager8()
        
                        MDLabel:
                            id: upload_label2
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                        Image:
                            id: image_label8
                            on_touch_down: root.on_image_click(self, args[1])
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            
                    MDLabel:
                        text: "Upload Bachelors Certificate *"
                        halign: 'left'
                        bold: True
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager9()
        
                        MDLabel:
                            id: upload_label3
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                        Image:
                            id: image_label9
                            source: ''
                            allow_stretch: True
                            on_touch_down: root.on_image_click(self, args[1])
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            
                    MDLabel:
                        text: "Upload Masters Certificate *"
                        halign: 'left'
                        bold: True
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager10()
        
                        MDLabel:
                            id: upload_label4
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label10
                            source: ''
                            allow_stretch: True
                            on_touch_down: root.on_image_click(self, args[1])
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            
                    GridLayout:
                        cols: 1
                        spacing:dp(15)
                        padding: [0, "30dp", 0, 0]
        
                        MDRectangleFlatButton:
                            text: "Next"
                            on_release: root.go_to_borrower_screen_mas()
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "50dp"
                            font_name: "Roboto-Bold"               
                # PHD details
                MDBoxLayout:
                    id: box_phd
                    orientation: 'vertical'
                    spacing: dp(5)
                    padding: dp(10)
                    size_hint_y: None
                    height: dp(600)
        
                    MDLabel:
                        text: "Upload 10th Class Certificate *"
                        halign: 'left'
                        bold: True
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager11()
        
                        MDLabel:
                            id: upload_label1
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                        Image:
                            id: image_label11
                            source: ''
                            allow_stretch: True
                            on_touch_down: root.on_image_click(self, args[1])
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    
                    MDLabel:
                        text: "Upload Intermediate/PUC Certificate *"
                        halign: 'left'
                        bold: True
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager12()
        
                        MDLabel:
                            id: upload_label2
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                        Image:
                            id: image_label12
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            on_touch_down: root.on_image_click(self, args[1])
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                    MDLabel:
                        text: "Upload Bachelors Certificate *"
                        halign: 'left'
                        bold: True
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager13()
        
                        MDLabel:
                            id: upload_label3
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                        Image:
                            id: image_label13
                            source: ''
                            allow_stretch: True
                            on_touch_down: root.on_image_click(self, args[1])
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                    MDLabel:
                        text: "Upload Masters Certificate *"
                        halign: 'left'
                        bold: True
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager14()
        
                        MDLabel:
                            id: upload_label4
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                        Image:
                            id: image_label14
                            on_touch_down: root.on_image_click(self, args[1])
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                    MDLabel:
                        text: "Upload PHD Certificate *"
                        halign: 'left'
                        bold: True
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('BorrowerScreen3').check_and_open_file_manager15()
                        MDLabel:
                            id: upload_label5
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label15
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            on_touch_down: root.on_image_click(self, args[1])
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                    GridLayout:
                        cols: 1
                        spacing:dp(15)
                        padding: [0, "30dp", 0, 0]
        
                        MDRectangleFlatButton:
                            text: "Next"
                            on_release: root.go_to_borrower_screen_phd()
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "50dp"
                            font_name: "Roboto-Bold"


<BorrowerScreen5>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen15')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30) # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(50)

            MDLabel:
                text: 'Father Details'
                halign: 'center'
                bold: True

            MDTextField:
                id: father_name
                hint_text: 'Enter Father Name'
                helper_text: 'Enter valid Father Name'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_name: "Roboto-Bold"
                font_size: "15dp"

            MDTextField:
                id: father_dob
                hint_text: "Enter Father D.O.B"
                helper_text: 'YYYY-MM-DD'
                helper_text_mode: "on_error"
                font_name: "Roboto-Bold"
                theme_text_color: 'Custom'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                height:self.minimum_height
                font_size: "15dp"
                input_type:'number'
                on_touch_down: root.on_date_touch_down()

            MDTextField:
                id: father_address
                hint_text: 'Enter Father Address'
                helper_text: 'Enter valid Father Address'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: father_occupation
                hint_text: 'Enter Father Occupation'
                helper_text: 'Enter valid Father Occupation'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: father_ph_no
                hint_text: 'Enter Father Phone NO'
                multiline: False
                font_size: "15dp"
                helper_text: 'Enter valid PH No'
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_name: "Roboto-Bold"
                input_type: 'number'  
                on_touch_down: root.on_father_ph_no_touch_down()


            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(father_name.text, father_address.text, father_occupation.text, father_ph_no.text, father_dob.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<BorrowerScreen6>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen15')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30) # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Mother Details'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)

            MDTextField:
                id: mother_name
                hint_text: 'Enter Mother Name'
                helper_text: 'Enter valid Mother Name'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0,0,0, 1
                font_name: "Roboto-Bold"
                font_size: "15dp"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: mother_dob
                hint_text: "Enter Mother D.O.B"
                helper_text: 'YYYY-MM-DD'
                font_name: "Roboto-Bold"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                input_type:'number'
                font_size: "15dp"
                on_touch_down: root.on_date_touch_down()
            MDTextField:
                id: mother_address
                hint_text: 'Enter Mother Address'
                helper_text: 'Enter valid Mother Address'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: mother_occupation
                hint_text: 'Enter Mother Occupation'
                helper_text: 'Enter valid Mother Occupation'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: mother_ph_no
                hint_text: 'Enter Mother Phone NO'
                multiline: False
                font_size: "15dp"
                helper_text: 'Enter valid PH No'
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_name: "Roboto-Bold"
                input_type: 'number'  
                on_touch_down: root.on_mother_ph_no_touch_down()

            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(mother_name.text, mother_address.text, mother_occupation.text, mother_ph_no.text, mother_dob.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<BorrowerScreen7>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(30)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(50)

            MDLabel:
                text: 'Profession Information'
                halign: 'center'
                bold: True
            MDLabel:
                text:"Select Your Profession Type:"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(20)

            Spinner:
                id: spinner_id
                text: "Select Profession type"
                font_size: "15dp"
                multiline: False
                width: dp(200)
                text_size: self.width - dp(20), None
                size_hint: 1 , None
                height:"40dp"
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: ''
                halign: 'center'
                size_hint_y: None
                height:dp(5)

            GridLayout:
                cols: 1
                spacing:dp(30)
                MDRectangleFlatButton:
                    text: "Next"
                    on_press: root.add_data(spinner_id.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
            MDLabel:
                text: ''
                halign: 'center'
                size_hint_y: None
                height:dp(50)

<BorrowerScreen8>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Student Details'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)

            MDTextField:
                id: collage_name
                hint_text: 'Enter Collage Name '
                multiline: False
                helper_text: 'Enter Valid Collage Name'
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: collage_id
                hint_text: 'Enter Collage ID'
                multiline: True
                helper_text: "Enter valid Collage ID"
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDLabel:
                text:"Upload College ID:"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(15)

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(270), dp(60)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7 # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen8').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
                    halign: 'left'
                    theme_text_color: "Custom"

                Image:
                    id: image_label1
                    source: ''
                    allow_stretch: True
                    keep_ratio: True
                    size_hint_y: None
                    size: dp(50), dp(50)
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDTextField:
                id:  college_address
                hint_text: 'Enter College Address'
                halign: 'left'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: 'Enter valid College Address'
                helper_text_mode: 'on_focus'
                bold: True
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            GridLayout:
                cols: 1
                spacing:dp(30)

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(collage_name.text, college_address.text, collage_id.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen9>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(30)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Business Details'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)

            MDTextField:
                id: business_name
                hint_text: 'Enter Business Name '
                multiline: False
                helper_text: "Enter valid Business Name"
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDLabel:
                text:"Select Your Business Type:"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(20)

            Spinner:
                id: spin
                text: " Select Business Type"
                multiline: False
                font_size: "15dp"
                size_hint: 1 , None
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:
                id:  business_address
                hint_text: 'Enter Business Address'
                multiline: False
                helper_text: "Enter valid Business Address"
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDLabel:
                text:"Select Your No of Employees Working:"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(20)

            Spinner:
                id: no_of_employees_working
                text: "No of Employees Working"
                font_size: "15dp"
                multiline: False
                size_hint: 1 , None
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(business_name.text, spin.text, business_address.text,no_of_employees_working.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen10>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen9')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Business Details'
                halign: 'center'
                bold: True

            MDTextField:
                id: industry_type
                hint_text: 'Enter Industry Type'
                multiline: False
                helper_text: "Enter valid Industry Type"
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: year_of_estd
                hint_text: 'Enter Year of Estd'
                multiline: False
                helper_text: 'YYYY-MM-DD'
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                input_type: 'number'

            MDTextField:
                id: last_six_months_turnover
                hint_text: 'Enter Last Six Months Turnover '
                multiline: False
                helper_text: "Enter Last Six Months Turnover"
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDLabel:
                text: "Upload Last 6 months Bank Statements"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(20)

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    id: upload_icon1
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen10').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Document' 
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                Image:
                    id: image_label1
                    source: ''
                    allow_stretch: True
                    keep_ratio: True
                    size_hint_y: None
                    size: dp(50), dp(50)
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(industry_type.text,last_six_months_turnover.text,year_of_estd.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"

<BorrowerScreen11>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen10')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Business Details'
                halign: 'center'
                bold: True

            MDTextField:
                id: cin
                hint_text: 'Enter CIN'
                multiline: False
                helper_text: "Enter valid CIN"
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: din
                hint_text: 'Enter DIN'
                multiline: False
                helper_text: "Enter valid DIN"
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: reg_office_address
                hint_text: 'Enter Registered Office Address '
                multiline: False
                helper_text: "Enter valid Registration Office Address"
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDLabel:
                text: "Upload Proof Of Verification"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(20)

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(260), dp(60)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    id: upload1
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen11').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                Image:
                    id: image_label1
                    source: ''
                    allow_stretch: True
                    keep_ratio: True
                    size_hint_y: None
                    size: dp(50), dp(50)
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(cin.text,din.text,reg_office_address.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen12>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(30)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Employment Details'
                halign: 'center'
                bold: True   
                size_hint_y: None

            MDTextField:              
                id:company_name
                hint_text: 'Enter company name'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDLabel:
                text:"Select Your Employment Type:"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(20)

            Spinner:
                id: spinner1
                text: " Select Employment Type"
                font_size: "15dp"
                multiline: False
                size_hint: 1 , None
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text:"Select Your Organisation Type:"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(20)
            Spinner:
                id: spinner2
                text: " Select Organisation Type"
                font_size: "15dp"
                multiline: False
                size_hint: 1 , None
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(spinner1.text, company_name.text, spinner2.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen13>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen12')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(35)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: ""
                size_hint_y: None
                height:dp(15)

            MDLabel:
                text: 'Employment Details'
                halign: 'center'
                bold: True   
                size_hint_y: None
                height:dp(30)

            MDTextField:              
                id: annual_salary
                hint_text: 'Enter Annual Salary'
                halign: 'left'
                multiline: False
                helper_text:  "Enter Valid Annual Salary"
                helper_text_mode: 'on_focus'
                input_type: 'number'  
                on_touch_down: root.on_annual_salary_touch_down()
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
            
            MDLabel:
                text:"Select Your Salary Type:"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
            MDLabel:
                text:""
            Spinner:
                id: salary_type_id
                text: " Select Salary type"
                font_size: "15dp"
                multiline: False
                size_hint: 1 , None
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:              
                id: designation
                hint_text: 'Enter Designation'
                halign: 'left'
                multiline: False
                helper_text: "Enter Valid Designation"
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDLabel:
                text: "Upload Employee ID"
                font_size: dp(15)
                halign: 'left'
                size_hint_y: None
                height: dp(20)
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(270), dp(60)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                canvas:
                    Color:
                        rgba: 0, 0, 0, 1 
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen13').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
                    halign: 'left'
                    theme_text_color: "Custom"

                Image:
                    id: image_label1
                    source: ''
                    allow_stretch: True
                    keep_ratio: True
                    size_hint_y: None
                    size: dp(50), dp(50)
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Last 6 months Bank Statements"
                font_size: dp(15)
                halign: 'left'
                size_hint_y: None
                height: dp(20)
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(270), dp(60)  
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen13').check_and_open_file_manager2()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
                    halign: 'left'
                    theme_text_color: "Custom"

                Image:
                    id: image_label2
                    source: ''
                    allow_stretch: True
                    keep_ratio: True
                    size_hint_y: None
                    size: dp(50), dp(50)
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(salary_type_id.text,annual_salary.text, designation.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
            MDLabel:
                text:""
            MDLabel:
                text:""

<BorrowerScreen14>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen13')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Employment Details'
                halign: 'center'
                font_name: "Roboto-Bold"
                size_hint_y: None

            MDTextField:              
                id:company_address
                hint_text: 'Enter company address'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDLabel:
                text:"Select Your Occupation Type:"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(20)
            Spinner:
                id: spinner
                text: " Select Occupation Type"
                font_size: "15dp"
                multiline: False
                width: dp(200)
                text_size: self.width - dp(20), None
                size_hint: 1 , None
                height:"40dp"
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:              
                id:landmark
                hint_text: 'Enter landmark'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:              
                id:business_number
                hint_text: 'Enter Company Phone Number'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                input_type: 'number'  
                on_touch_down: root.on_business_phone_number_touch_down()
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(company_address.text, spinner.text, landmark.text, business_number.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<CustomSpinnerOption@SpinnerOption>:
    background_color:0, 0, 1, 1  
    color: 1, 1, 1, 1
<IconListItem>
    IconLeftWidget:
        icon: root.icon 
<BorrowerScreen15>:
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            id: bar
            title: "P2P LENDING"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
            right_action_items: [["icon8.png", lambda x: root.account()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: dp(30)
                spacing: dp(20)

                MDLabel:
                    text: 'Borrower Registration Form'
                    halign: 'center'
                    font_size: "20dp"
                    font_name: "Roboto-Bold"

                MDLabel:
                    text: ''
                    halign: 'center'
                    size_hint_y: None
                    height: dp(0)

                MDLabel:
                    text: "Select Marital Status Type:"
                    halign: 'left'
                    font_size: "15dp"
                    font_name: "Roboto-Bold"
                    size_hint_y: None
                    height: dp(20)

                Spinner:
                    id: marital_status_id
                    text: "Marital Status"
                    values: ["Married", "Unmarried", "Others"]
                    font_size: "15dp"
                    multiline: False
                    size_hint: 1, None
                    height: "40dp"
                    width: dp(200)
                    text_size: self.width - dp(20), None
                    background_color: 0, 0, 0, 0
                    background_normal: ''
                    color: 0, 0, 0, 1
                    option_cls: 'CustomSpinnerOption'
                    on_text: root.update_details(marital_status_id.text)
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1  
                        Line:
                            width: 0.7
                            rectangle: (self.x, self.y, self.width, self.height)

                MDLabel:
                    text:"Select Your Guaranter:"
                    halign: 'left'
                    font_size: "15dp"
                    font_name: "Roboto-Bold"
                    size_hint_y: None
                    height: dp(20)

                Spinner:
                    id: relation_name
                    text: "How is the person related to you"
                    font_size: "15dp"
                    multiline: False
                    size_hint: 1 , None
                    height: "40dp"
                    width: dp(200)
                    text_size: self.width - dp(20), None
                    background_color: 0, 0, 0, 0
                    background_normal: ''
                    color: 0, 0, 0, 1
                    option_cls: 'CustomSpinnerOption'  
                    on_text: root.update_person_details_visibility(relation_name.text)
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1  
                        Line:
                            width: 0.7
                            rectangle: (self.x, self.y, self.width, self.height)
                            
                MDBoxLayout:
                    id: box
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    opacity: 1
                    spacing: dp(22)


                GridLayout:
                    cols: 1
                    spacing: dp(30)
                    padding: [0, "30dp", 0, 0]

                    MDRaisedButton:
                        text: "Next"
                        on_release: root.add_data(marital_status_id.text)
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        pos_hint: {'right': 1, 'y': 0.5}
                        text_color: 1, 1, 1, 1
                        size_hint: 1, None
                        height: "50dp"
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ''
                    halign: 'center'
                    size_hint_y: None
                    height: dp(50)

<BorrowerScreen16>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen15')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Spouse Details'
                halign: 'center'
                bold:True

            MDTextField:
                id: spouse_name
                hint_text: 'Enter Spouse Name '
                multiline: False
                helper_text: "Enter Valid Spouse Name"
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"


            MDTextField:
                id: spouse_date_textfield
                hint_text: "Enter Marriage Date"
                helper_text: 'YYYY-MM-DD'
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                input_type:'number'
                font_size: "15dp"
                on_touch_down: root.on_date_touch_down()
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: spouse_mobile
                hint_text: 'Enter Spouse Mobile No'
                multiline: False
                helper_text: "Enter valid Spouse Mobile No"
                helper_text_mode: 'on_focus'
                input_type: 'number'  
                font_size: "15dp"
                on_touch_down: root.on_spouse_mobile_touch_down()
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(spouse_name.text, spouse_date_textfield.text, spouse_mobile.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen17>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen16')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(25)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Spouse Details'
                halign: 'center'
                bold:True

            MDLabel:
                text:"Select Spouse Profession Type:"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(20)

            Spinner:
                id: spouse_profession
                text: "Select Spouse Profession"
                font_size: "15dp"
                multiline: False
                size_hint: 1 , None
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:
                id: spouse_company_name
                hint_text: 'Enter Spouse Company Name'
                multiline: False
                helper_text: 'Enter Valid Spouse Company Name (if working)'
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: spouse_annual_salary
                hint_text: 'Enter Annual Salary'
                multiline: False
                helper_text: 'Enter valid Annual Salary (if working)'
                helper_text_mode: 'on_focus'
                input_type: 'number'
                on_touch_down: root.on_spouse_annual_salary_touch_down()
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(spouse_company_name.text, spouse_profession.text, spouse_annual_salary.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen18>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "P2P LENDING"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen20')]]
            right_action_items: [['home', lambda x: root.go_to_dashboard()]]
            title_align: 'center'  # Center-align the title
            md_bg_color: 0.043, 0.145, 0.278, 1
            
        MDScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height        
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(15)
                    padding: dp(10)
                    size_hint_y: None
                    height: dp(600)
        
                    MDLabel:
                        text: 'Applicant Bank Details'
                        halign: 'center'
                        font_size: "15dp"
                        font_name: "Roboto-Bold"
        
                    MDTextField:
                        id: account_holder_name
                        on_text: root.validate_zip_code_text(self)
                        hint_text: 'Enter account holder name '
                        multiline: False
                        size_hint_y:None
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        mode: "rectangle"
                        radius: [0, 0, 0, 0]  # Makes the corners square
        
                    MDBoxLayout:
                        size_hint_y:None
                        height:"50dp"
                        Spinner:
                            id: account_type_id
                            text: "Select Account Type"
                            font_size: "15dp"
                            multiline: False
                            size_hint: 1 , None
                            width: dp(200)
                            text_size: self.width - dp(20), None
                            height: "40dp"
                            background_color: 0,0,0,0
                            option_cls: 'CustomSpinnerOption'
                            background_normal:''
                            color: 0, 0, 0, 1
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1  
                                Line:
                                    rectangle: self.x, self.y, self.width, self.height
                                    width: 0.7
            
        
                    MDTextField:
                        id: account_number
                        hint_text: 'Enter Account number *'
                        on_text: root.validate_zip_code(self)
                        multiline: False
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        input_type: 'number'
                        mode: "rectangle"
                        radius: [0, 0, 0, 0]  # Makes the corners square
        
                    MDTextField:
                        id: bank_name
                        on_text: root.validate_zip_code_text(self)
                        hint_text: 'Enter Bank Name *'
                        multiline: False
                        helper_text_mode: 'on_focus'
                        size_hint_y:None
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        mode: "rectangle"
                        radius: [0, 0, 0, 0]  # Makes the corners square
        
                    MDTextField:
                        id: ifsc_code
                        on_text: root.validate_zip_code_numchar(self)
                        hint_text: 'Enter Ifsc_code *'
                        multiline: False
                        helper_text_mode: 'on_focus'
                        size_hint_y:None
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        mode: "rectangle"
                        radius: [0, 0, 0, 0]  # Makes the corners square
        
                    MDTextField:
                        id: branch_name
                        on_text: root.validate_zip_code_text(self)
                        hint_text: 'Enter Branch Name *'
                        hint_text_mode: 'on_focus'
                        multiline: False
                        halign: 'left'
                        multiline: False
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        mode: "rectangle"
                        radius: [0, 0, 0, 0]  # Makes the corners square
        
                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: "32dp"
                        spacing:dp(10)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        MDCheckbox:
                            id: check
                            size_hint: None, None
                            size: "30dp", "30dp"
                            active: False
                            on_active: root.on_checkbox_active(self, self.active)
        
                        MDLabel:
                            text: "I Agree Terms and Conditions"
                            size: "30dp", "30dp"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            halign: "left"
                            valign: "center"
                            on_touch_down: app.root.get_screen("BorrowerScreen18").show_terms_dialog() if self.collide_point(*args[1].pos) else None
                    MDLabel:
                        id: error_message
                        text: "Pleas fill all details! *"
                        size: "30dp", "30dp"
                        theme_text_color: "Custom"
                        text_color: 150, 0, 0, 1
                        halign: "left"
                    GridLayout:
                        cols: 1
                        spacing:dp(30)        
                        MDRaisedButton:
                            text: "Submit"
                            on_release: root.go_to_borrower_dashboard(ifsc_code.text, branch_name.text, account_holder_name.text, account_type_id.text, account_number.text, bank_name.text)
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "50dp"
                            font_name: "Roboto-Bold"
                            disabled: root.all_fields_filled
<BorrowerScreen20>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen15')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text: "Loan Details"
            size_hint_y: None
            height: dp(40)
            padding: [0, dp(40), 0, 0]  # Padding: [left, top, right, bottom]
            halign: "center"
            bold: True
            font_name: "Roboto-Bold"
        BoxLayout:
            orientation: "vertical"
            spacing: "10dp"
            padding: "10dp"
            MDLabel:
                text: "Do you have any running Home Loan?"
                halign: "center"
                size_hint_y: None
                height: dp(50)

            MDGridLayout:
                cols: 2
                spacing: dp(20)
                halign: "center"
                pos_hint: {'center_x': 0.7, 'center_y': 0.5}  # Fixed the typo here
                MDFillRoundFlatButton:
                    id: yes1
                    text: "Yes"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed1()
                MDFillRoundFlatButton:
                    id: no1
                    text: "No"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_no_button_pressed1()
            MDLabel:
                text: "Do you have any other loan against your name?"
                halign: "center"
                size_hint_y: None
                height: dp(50)

            MDGridLayout:
                cols: 2
                spacing: dp(20)
                halign: "center"
                pos_hint: {'center_x': 0.7, 'center_y': 0.5}  # Fixed the typo here
                MDFillRoundFlatButton:
                    id: yes2
                    text: "Yes"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed2()
                MDFillRoundFlatButton:
                    id: no2
                    text: "No"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_no_button_pressed2()
            MDLabel:
                text: "Do you have any Personal Credit Card Loans?"
                halign: "center"
                size_hint_y: None
                height: dp(50)

            MDGridLayout:
                cols: 2
                spacing: dp(20)
                halign: "center"
                pos_hint: {'center_x': 0.7, 'center_y': 0.5}  # Fixed the typo here
                MDFillRoundFlatButton:
                    id: yes3
                    text: "Yes"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed3()
                MDFillRoundFlatButton:
                    id: no3
                    text: "No"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_no_button_pressed3()
            MDLabel:
                text: "Do you have any Two Wheeler / Four Wheeler Loans?"
                halign: "center"
                size_hint_y: None
                height: dp(50)

            MDGridLayout:
                cols: 2
                spacing: dp(20)
                pos_hint: {'center_x': 0.7, 'center_y': 0.5}  # Fixed the typo here
                MDFillRoundFlatButton:
                    id: yes4
                    text: "Yes"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed4()
                MDFillRoundFlatButton:
                    id: no4
                    text: "No"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_no_button_pressed4()
            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data()
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen21>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen15')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text: "Family Members Details"
            size_hint_y: None
            height: dp(40)
            padding: [0, dp(40), 0, 0]  # Padding: [left, top, right, bottom]
            halign: "center"
            bold: True
            font_name: "Roboto-Bold"
        BoxLayout:
            orientation: "vertical"
            spacing: "7dp"
            padding: "15dp"
            MDLabel:
                text: "Provide Another Person Details"
                halign: "center"
                size_hint_y: None
                height: dp(70)

            MDGridLayout:
                cols: 4
                spacing: dp(10)
                pos_hint: {'center_x': 0.3, 'center_y': 0.5}  # Fixed the typo here
                MDFillRoundFlatButton:
                    id: id1
                    text: "Father"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed1()
                MDFillRoundFlatButton:
                    id: id2
                    text: "Mother"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed2()
                MDFillRoundFlatButton:
                    id: id3
                    text: "Spouse"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed3()
                MDFillRoundFlatButton:
                    id: id4
                    text: "Other"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed4()

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data()
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen22>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen15')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text: "Family Members Details"
            size_hint_y: None
            height: dp(40)
            padding: [0, dp(40), 0, 0]  # Padding: [left, top, right, bottom]
            halign: "center"
            bold: True
            font_name: "Roboto-Bold"
        BoxLayout:
            orientation: "vertical"
            spacing: "10dp"
            padding: "10dp"
            MDLabel:
                text: "Provide Another Person Details"
                halign: "center"
                size_hint_y: None
                height: dp(70)

            MDGridLayout:
                cols: 4
                spacing: dp(10)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Fixed the typo here
                MDFillRoundFlatButton:
                    id: id1
                    text: "Father"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed1()
                MDFillRoundFlatButton:
                    id: id2
                    text: "Mother"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed2()

                MDFillRoundFlatButton:
                    id: id4
                    text: "Other"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed4()

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data()
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
<BorrowerScreen23>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen15')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Person Details'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)


            MDTextField:
                id: relation_name
                hint_text: 'How is the person related to you'
                helper_text: 'Enter Valid Person Relation'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: person_name
                hint_text: 'Enter Person Name'
                helper_text: 'Enter Valid Person Name'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: person_dob
                hint_text: 'Enter Person D.O.B'
                helper_text: 'YYYY-MM-DD'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                input_type:'number'
                on_touch_down: root.on_date_touch_down()
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"


            MDTextField:
                id: person_ph_no
                hint_text: 'Enter Person Phone No'
                helper_text: 'Enter Valid Person Phone No'
                helper_text_mode: 'on_focus'
                halign: 'left'
                input_type: 'number'  
                on_touch_down: root.on_mother_ph_no_touch_down()
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: person_proffission
                hint_text: 'Enter Person Profession'
                helper_text: 'Enter valid Person Profession'
                multiline: False
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(relation_name.text, person_name.text, person_dob.text, person_ph_no.text, person_proffission.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
<BorrowerScreen24>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "P2P LENDING"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen')]]
            right_action_items: [['home', lambda x: root.go_to_dashboard()]]
            title_align: 'center'  # Center-align the title
            md_bg_color: 0.043, 0.145, 0.278, 1
        
        MDScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(18)
                padding: dp(50)
                size_hint_y: None
                height: self.minimum_height
       
                MDLabel:
                    text: 'Borrower Registration Form'
                    halign: 'center'
                    font_size: "20dp"
                    font_name: "Roboto-Bold"
                MDLabel:
                    text: 'Address Information'
                    halign: 'center'
                    bold: True

                MDTextField:
                    id: street_address1
                    hint_text: 'Enter Street Address1'
                    multiline: False
                    helper_text: 'Enter Your address'
                    helper_text_mode: 'on_focus'
                    size_hint_y: None
                    height: self.minimum_height
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    font_size: "15dp"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    mode: "rectangle"
                    radius: [0, 0, 0,0]

                MDTextField:
                    id: street_address2
                    hint_text: 'Enter Street Address2'
                    multiline: False
                    helper_text: 'Enter Your address'
                    helper_text_mode: 'on_focus'
                    size_hint_y: None
                    height: self.minimum_height
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    mode: "rectangle"
                    radius: [0, 0, 0,0]

                Spinner:
                    id: spinner_id2
                    text: "Select Present Address"
                    multiline: False
                    size_hint: 1, None
                    halign: "left"
                    height: "45dp"
                    width: dp(200)
                    text_size: self.width - dp(20), None
                    font_size: "15dp"
                    background_color: 0, 0, 0, 0
                    background_normal: ''
                    color: 0, 0, 0, 1
                    option_cls: 'CustomSpinnerOption'
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1  # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.8 


                Spinner:
                    id: spinner_id
                    text: "Select How long you are staying"
                    helper_text: "How Long You Are Staying At This Address"
                    multiline: False
                    size_hint: 1, None
                    halign: "left"
                    font_size: "15dp"
                    height: "45dp"
                    background_color: 0, 0, 0, 0
                    background_normal: ''
                    width: dp(200)
                    text_size: self.width - dp(20), None
                    color: 0, 0, 0, 1
                    option_cls: 'CustomSpinnerOption'
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1  # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.8 

                MDTextField:
                    id: city
                    hint_text: 'Enter City Name'
                    multiline: False
                    helper_text: 'Enter Your city'
                    helper_text_mode: 'on_focus'
                    size_hint_y: None
                    height: self.minimum_height
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    font_size: "15dp"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    mode: "rectangle"
                    radius: [0, 0, 0,0]
                    

                MDTextField:
                    id: zip_code
                    hint_text: 'Enter postal/zipcode'
                    multiline: False
                    helper_text: 'Enter Your zipcode'
                    helper_text_mode: 'on_focus'
                    size_hint_y: None
                    height: self.minimum_height
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    input_type: 'number'
                    on_touch_down: root.on_mobile_number_touch_down()
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    mode: "rectangle"
                    radius: [0, 0, 0,0]

                MDTextField:
                    id: state
                    hint_text: 'Enter State Name'
                    multiline: False
                    helper_text: 'Enter Your State'
                    helper_text_mode: 'on_focus'
                    size_hint_y: None
                    height: self.minimum_height
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    mode: "rectangle"

                MDTextField:
                    id: country
                    hint_text: 'Enter Country Name'
                    multiline: False
                    helper_text: 'Enter Your Country'
                    helper_text_mode: 'on_focus'
                    size_hint_y: None
                    height: self.minimum_height
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    mode: "rectangle"
                    radius: [0, 0, 0,0]

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(street_address1.text, street_address2.text, spinner_id.text, spinner_id2.text, city.text, zip_code.text, state.text, country.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen25>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(30)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(50)

            MDLabel:
                text: 'Profession Information'
                halign: 'center'
                bold: True
            MDLabel:
                text:"Select Self Employement Type:"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(20)

            Spinner:
                id: spinner_id
                text: "Select Your Self Employement type"
                font_size: "15dp"
                multiline: False
                size_hint: 1 , None
                width: dp(200)
                text_size: self.width - dp(20), None
                height:"40dp"
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: ''
                halign: 'center'
                size_hint_y: None
                height:dp(5)

            GridLayout:
                cols: 1
                spacing:dp(30)
                MDRectangleFlatButton:
                    text: "Next"
                    on_press: root.add_data(spinner_id.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
            MDLabel:
                text: ''
                halign: 'center'
                size_hint_y: None
                height:dp(50)

<BorrowerScreen26>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen25')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Farmer Details'
                halign: 'center'
                bold: True

            MDLabel:
                text:"Select Your Type Of Land:"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(20)

            Spinner:
                id: land
                text: " Select Type Of Land"
                values: ["Select Type Of Land", "Rented", "Owned"]
                font_size: "15dp"
                multiline: False
                size_hint: 1 , None
                width: dp(200)
                text_size: self.width - dp(20), None
                height:"40dp"
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:
                id: acers
                hint_text: 'Enter the number of acres of land'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                input_type: 'number'

            MDTextField:
                id: corp
                hint_text: 'Enter Crop Name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None  
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: income
                hint_text: 'Enter Your Yearly Income'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None  
                input_type: 'number'  
                on_touch_down: root.on_mobile_number_touch_down()
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"


            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(land.text, acers.text, corp.text, income.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

'''

conn = sqlite3.connect("fin_user.db")
cursor = conn.cursor()


class BorrowerScreen(Screen):
    Builder.load_string(Borrower)
    MAX_IMAGE_SIZE_MB = 2

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
            self.ids.gender_id.values = self.unique_gender
        else:
            self.ids.gender_id.values = ['Select a Gender']

        data = app_tables.fin_user_profile.search()

        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            self.ids.username.text = data[index]['full_name']
            self.ids.mobile_number.text = data[index]['mobile']

        else:
            print('email not found')

    def validate_image_loaded(self, image_label):
        if not image_label.source or 'error.png' in image_label.source:  # Adjust 'error.png' as per your placeholder image
            return False
        return True


        # if self.ids.aadhar_number.text:
        #     self.on_aadhar_number_text(self.ids.aadhar_number.text)
        # else:
        #     self.show_validation_error('Please enter valid ID1')

    def on_aadhar_number_text(self, text):
        upload_icon = self.ids.upload_icon2
        upload_icon.disabled = not bool(text)

    def on_pan_number_text(self, text):
        upload_icon = self.ids.upload_icon3
        upload_icon.disabled = not bool(text)
    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.date_textfield.input_type = 'number'

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

    def calculate_age(self, date_of_birth):
        today = datetime.today()
        dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def add_data(self, name, gender, date_of_birth, mobile_number, alternate_email, aadhar_number, pan_number):
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
        anim = Animation(y=modal_view.height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        validation_errors = []  # Define validation_errors here
        Clock.schedule_once(lambda dt: self.process_data(name, gender, date_of_birth, mobile_number, alternate_email,aadhar_number, pan_number, modal_view, validation_errors), 2)

    def process_data(self, name, gender, date_of_birth, mobile_number, alternate_email, aadhar_number, pan_number, modal_view, validation_errors):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view
        modal_view.dismiss()

        validation_errors = []

        if not self.validate_image_loaded(self.ids.image_label1):
            validation_errors.append((self.ids.image_label1, "Image not loaded."))
            self.show_validation_error("Please Upload Profile Pic.")
        elif not self.validate_image_loaded(self.ids.image_label2):
            validation_errors.append((self.ids.image_label1, "Image not loaded."))
            self.show_validation_error("Please Upload Gov ID1.")
        elif not self.validate_image_loaded(self.ids.image_label3):
            validation_errors.append((self.ids.image_label1, "Image not loaded."))
            self.show_validation_error("Please Upload Gov ID2.")
        elif not self.validate_image_loaded(self.ids.image_label3) and self.validate_image_loaded(self.ids.image_label2) and self.validate_image_loaded(self.ids.image_label3):
            validation_errors.append((self.ids.image_label1, "Image not loaded."))
            self.show_validation_error("Please Upload all Images.")
        else:
            pass

        # Check for mandatory fields
        if not name:
            validation_errors.append((self.ids.username, "Please fill the * mandatory details."))
        if not date_of_birth:
            validation_errors.append(
                (self.ids.date_textfield, "Please fill the * mandatory details."))  # Corrected to date_textfield

        if not mobile_number:
            validation_errors.append((self.ids.mobile_number, "Please fill the * mandatory details."))

        if not aadhar_number:
            validation_errors.append((self.ids.aadhar_number, "Please fill the * mandatory details."))
        if not pan_number:
            validation_errors.append((self.ids.pan_number, "Please fill the * mandatory details."))

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return  # Prevent further execution if there are missing fields

        # Validate mobile number
        if not re.match(r'^\d{10}$|^\d{12}$', mobile_number):
            validation_errors.append(
                (self.ids.mobile_number, "Please enter a valid 10-digit or 12-digit mobile number."))

        # Validate email
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', alternate_email):
            validation_errors.append((self.ids.alternate_email, "Please enter a valid email address."))

        # Validate date of birth
        try:
            dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 18:
                validation_errors.append((self.ids.date_textfield, "You must be at least 18 years old to register."))
        except ValueError:
            validation_errors.append((self.ids.date_textfield, "Invalid date format. Please use YYYY-MM-DD."))

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []

        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET name = ?, gender = ?,  date_of_birth = ?,mobile_number = ?, alternate_email = ?, aadhar_number = ?, pan_number = ?  WHERE customer_id = ?",
                (name, gender, date_of_birth, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()

        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['full_name'] = name
            data[index]['gender'] = gender
            data[index]['date_of_birth'] = date_of_birth
            age = self.calculate_age(date_of_birth)
            data[index]['user_age'] = age
            data[index]['mobile'] = mobile_number
            data[index]['another_email'] = alternate_email
            data[index]['aadhaar_no'] = aadhar_number
            data[index]['pan_number'] = pan_number


        else:
            print("email not there")

        sm = self.manager
        borrower_screen = BorrowerScreen24(name='BorrowerScreen24')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen24'

    def show_validation_errors(self, validation_errors):
        for widget, error_message in validation_errors:
            widget.error = True
            widget.helper_text_color = (1, 0, 0, 1)
            widget.helper_text = error_message
            widget.helper_text_mode = "on_error"
            if isinstance(widget, MDTextField):
                widget.line_color_normal = (1, 0, 0, 1)  # Red color for the line when not focused
                widget.line_color_focus = (1, 0, 0, 1)
            if isinstance(widget, MDCheckbox):
                widget.theme_text_color = 'Error'
    def upload_image(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return

            user_photo_media = media.from_file(file_path, mime_type='image/png')
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['user_photo'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_file1(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return

            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['aadhaar_photo'] = user_photo_media

            print("File uploaded successfully.")
            if file_extension in ['.png', '.jpg', '.jpeg']:
                self.ids.image_label2.source = file_path
                print(f"Set image source to: {file_path}")

        except Exception as e:
            print(f"Error uploading file: {e}")

    def upload_file2(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return

            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['pan_photo'] = user_photo_media

            print("File uploaded successfully.")
            if file_extension in ['.png', '.jpg', '.jpeg']:
                self.ids.image_label3.source = file_path
                print(f"Set image source to: {file_path}")

        except Exception as e:
            print(f"Error uploading file: {e}")
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

    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mobile_number.input_type = 'number'

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1", self.upload_image)
    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2", self.upload_file1)

    def check_and_open_file_manager3(self):
        self.check_and_open_file_manager("upload_icon3", "upload_label3", "selected_file_label3", "selected_image3",
                                         "image_label3", self.upload_file2)

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id, upload_function),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        upload_function(path)  # Upload the selected image
        self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
        self.file_manager.close()
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()
    def on_image_click(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.show_image_popup(instance.source)

    def show_image_popup(self, image_source):
        layout = BoxLayout(orientation='vertical')

        popup_img = Image(source=image_source)
        layout.add_widget(popup_img)

        close_button = Button(text='Close', size_hint=(1, 0.1))
        close_button.bind(on_press=self.close_popup)
        layout.add_widget(close_button)

        self.popup = Popup(title='Image Preview',
                           content=layout,
                           size_hint=(0.8, 0.8))
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()
    def get_email(self):
        return anvil.server.call('another_method')

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants):
            # All grants are truthy, permission granted, open the file manager
            self.file_manager_open()
        else:
            # At least one grant is falsy, permission denied, show a modal view
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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET profile_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label1.text = 'Upload Successfully'

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET aadhar_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label1.text = 'Upload Successfully'

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET aadhar_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label2.text = 'Upload Successfully'

    def on_save(self, instance, value, date_range):
        # print(instance, value, date_range)
        self.ids.date_textfield.text = str(value)

    # Cancel
    def on_cancel(self, instance, time):
        self.ids.date_textfield.text = "You Clicked Cancel!"

    def show_date_picker(self):
        date_dialog = MDDatePicker(year=2000, month=2, day=14)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

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


class BorrowerScreen3(Screen):
    MAX_IMAGE_SIZE_MB = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_borrower_qualification.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['borrower_qualification'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.spinner_id.values = self.unique_list
        else:
            self.ids.spinner_id.values = ['Select Education Details']

        self.ids.box_10th.opacity = 0
        self.ids.box_12th.opacity = 0
        self.ids.box_bachelors.opacity = 0
        self.ids.box_masters.opacity = 0
        self.ids.box_phd.opacity = 0

    def validate_image_loaded(self, image_label):
        if not image_label.source or 'error.png' in image_label.source:  # Adjust 'error.png' as per your placeholder image
            return False
        return True

    def on_image_click(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.show_image_popup(instance.source)

    def show_image_popup(self, image_source):
        layout = BoxLayout(orientation='vertical')

        popup_img = Image(source=image_source)
        layout.add_widget(popup_img)

        close_button = Button(text='Close', size_hint=(1, 0.1))
        close_button.bind(on_press=self.close_popup)
        layout.add_widget(close_button)

        self.popup = Popup(title='Image Preview',
                           content=layout,
                           size_hint=(0.8, 0.8))
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()

    def update_education_details(self, id):
        # modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # modal_view.dismiss()
        spinner_id = self.ids.spinner_id.text
        print(spinner_id)
        if spinner_id not in self.unique_list:
            self.show_validation_error('Select a Valid Education Type')
            return

        # List of all box layouts
        all_boxes = ['box_10th', 'box_12th', 'box_bachelors', 'box_masters', 'box_phd']

        # Map spinner_id to the corresponding box id
        spinner_to_box = {
            '10th class': 'box_10th',
            '10th standard': 'box_10th',
            'Intermediate': 'box_12th',
            '12th standard': 'box_12th',
            'Bachelors': 'box_bachelors',
            "Bachelor's degree": 'box_bachelors',
            'Masters': 'box_masters',
            "Master's degree": 'box_masters',
            'PHD': 'box_phd',
            'PhD': 'box_phd'
        }

        selected_box_id = spinner_to_box.get(spinner_id)

        # Get the parent layout of the boxes
        parent_layout = self.ids.parent_layout_id  # Replace with the actual id of the parent layout

        # Hide all boxes
        for box_id in all_boxes:
            box = self.ids[box_id]
            box.opacity = 0

        # Show the selected box
        if selected_box_id:
            selected_box = self.ids[selected_box_id]
            selected_box.opacity = 1

        # Remove all boxes from the parent layout
        for box_id in all_boxes:
            box = self.ids[box_id]
            if box.parent:
                parent_layout.remove_widget(box)

        # Re-add boxes to the parent layout in order, with the visible box on top
        if selected_box_id:
            parent_layout.add_widget(self.ids[selected_box_id])
        for box_id in all_boxes:
            if box_id != selected_box_id:
                parent_layout.add_widget(self.ids[box_id])

        self.adjust_screen_height()

        print(id)
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET highest_qualification = ? WHERE customer_id = ?",
                           (id, row_id_list[log_index]))
            conn.commit()
        else:
            print('User is not logged in.')
        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['qualification'] = id
        else:
            print('email not found')

    def adjust_screen_height(self):
        height = 0
        for box_id in ['box_10th', 'box_12th', 'box_bachelors', 'box_masters', 'box_phd']:
            box = self.ids[box_id]
            if box.opacity == 1:
                height += box.height
        self.height = height

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

    # def go_to_borrower_screen(self):
    #     modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])
    #
    #     # Create MDLabel with white text color, increased font size, and bold text
    #     loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
    #                             theme_text_color="Custom", text_color=[1, 1, 1, 1],
    #                             font_size="50sp", bold=True)
    #
    #     # Set initial y-position off-screen
    #     loading_label.y = -loading_label.height
    #
    #     modal_view.add_widget(loading_label)
    #     modal_view.open()
    #
    #     # Perform the animation
    #     self.animate_loading_text(loading_label, modal_view.height)
    #
    #     # Perform the actual action (e.g., fetching loan requests)
    #     # You can replace the sleep with your actual logic
    #     Clock.schedule_once(lambda dt: self.perform_loan_request_action10th(modal_view), 2)
    #
    # def perform_loan_request_action10th(self, modal_view):
    #     # Close the modal view after performing the action
    #     modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
    #     modal_view.dismiss()
    #     # Get the existing ScreenManager
    #     sm = self.manager
    #
    #     # Create a new instance of the LoginScreen
    #     borrower_screen = BorrowerScreen7(name='BorrowerScreen7')
    #
    #     # Add the LoginScreen to the existing ScreenManager
    #     sm.add_widget(borrower_screen)
    #
    #     # Switch to the LoginScreen
    #     sm.current = 'BorrowerScreen7'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen2'

    #     # ================================================================================================================================
    #     # 10th class
    #
    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1", self.upload_image)

    # def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     if platform == 'android':
    #         if check_permission(Permission.READ_MEDIA_IMAGES):
    #             self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #         else:
    #             self.request_media_images_permission()
    #     else:
    #         # For non-Android platforms, directly open the file manager
    #         self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #
    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
    #                                                    image_label_id, upload_function),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         # For other platforms, show the file manager from the root directory
    #         self.file_manager.show('/')

    def get_email(self):
        return anvil.server.call('another_method')

    def upload_image(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return
            # if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
            #     self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
            #     return
            #
            # file_extension = os.path.splitext(file_path)[1].lower()
            # if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
            #     self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
            #     return
            #
            # if file_extension in ['.png', '.jpg', '.jpeg']:
            #     mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            # elif file_extension == '.pdf':
            #     mime_type = 'application/pdf'

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['tenth_class'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    # def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     upload_function(path)  # Upload the selected image
    #     self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
    #     file_name = os.path.basename(path)  # Extract file name from the path
    #     self.manager.get_screen('BorrowerScreen_Edu_10th').ids[image_label_id].text = file_name  # Update the label text
    #     self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants):
            # All grants are truthy, permission granted, open the file manager
            self.file_manager_open()
        else:
            # At least one grant is falsy, permission denied, show a modal view
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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        else:
            print('User is not logged in.')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen3'

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

    def go_to_borrower_screen_10(self):
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
        Clock.schedule_once(lambda dt: self.perform_loan_request_action10th(modal_view), 2)

    def perform_loan_request_action10th(self, modal_view):
        # Close the modal view after performing the action
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        validation_errors = []

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return
        #
        # if not self.validate_image_loaded(self.ids.image_label1):
        #     validation_errors.append((self.ids.image_label1, "Image not loaded."))
        #     self.show_validation_error("Please Upload 10th Certificate.")
        # else:

        if not self.validate_image_loaded(self.ids.image_label1):
            validation_errors.append((self.ids.image_label1, "Image not loaded."))
            self.show_validation_error("Please Upload 10th Certificate.")
        else:
            borrower_screen = BorrowerScreen7(name='BorrowerScreen7')
            sm.add_widget(borrower_screen)
            sm.current = 'BorrowerScreen7'

    #
    #     #     ==================================================================================
    # #     PUC, intermediate
    #
    def upload_image1(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['tenth_class'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def get_email(self):
        return anvil.server.call('another_method')

    def upload_image2(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['intermediate'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label2", self.upload_image1)

    def check_and_open_file_manager3(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label3", self.upload_image2)

    # def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     if platform == 'android':
    #         if check_permission(Permission.READ_MEDIA_IMAGES):
    #             self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #         else:
    #             self.request_media_images_permission()
    #     else:
    #         # For non-Android platforms, directly open the file manager
    #         self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #
    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
    #                                                    image_label_id, upload_function),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         # For other platforms, show the file manager from the root directory
    #         self.file_manager.show('/')
    #
    # def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     upload_function(path)  # Upload the selected image
    #     self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
    #     file_name = os.path.basename(path)  # Extract file name from the path
    #     self.manager.get_screen('BorrowerScreen_Edu_Intermediate').ids[
    #         image_label_id].text = file_name  # Update the label text
    #     self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants):
            # All grants are truthy, permission granted, open the file manager
            self.file_manager_open()
        else:
            # At least one grant is falsy, permission denied, show a modal view
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

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    # def go_to_dashboard(self):
    #     self.manager.current = 'DashScreen'
    #
    # def on_pre_enter(self):
    #     Window.bind(on_keyboard=self.on_back_button)
    #
    # def on_pre_leave(self):
    #     Window.unbind(on_keyboard=self.on_back_button)
    #
    # def on_back_button(self, instance, key, scancode, codepoint, modifier):
    #     if key == 27:
    #         self.go_back()
    #         return True
    #     return False
    #
    # def go_back(self):
    #     self.manager.transition = SlideTransition(direction='right')
    #     self.manager.current = 'BorrowerScreen3'

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

    def go_to_borrower_screen_11(self):
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
        Clock.schedule_once(lambda dt: self.perform_loan_request_action11th(modal_view), 2)

    def perform_loan_request_action11th(self, modal_view):
        # Close the modal view after performing the action
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        validation_errors = []

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return

        if not self.validate_image_loaded(self.ids.image_label2):
            validation_errors.append((self.ids.image_label2, "Image not loaded."))
            self.show_validation_error("Please Upload 10th Certificates.")
        # Create a new instance of the LoginScreen
        elif not self.validate_image_loaded(self.ids.image_label3):
            validation_errors.append((self.ids.image_label3, "Image not loaded."))
            self.show_validation_error("Please Upload 12th Certificates.")
        else:
            borrower_screen = BorrowerScreen7(name='BorrowerScreen7')
            sm.add_widget(borrower_screen)
            sm.current = 'BorrowerScreen7'

    # # ======================================================================================================================
    # #     bachelors degree
    def upload_image3(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['tenth_class'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def get_email(self):
        return anvil.server.call('another_method')

    def upload_image4(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['intermediate'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image5(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['btech'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

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

    def check_and_open_file_manager4(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label4", self.upload_image3)

    def check_and_open_file_manager5(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label5", self.upload_image4)

    def check_and_open_file_manager6(self):
        self.check_and_open_file_manager("upload_icon3", "upload_label3", "selected_file_label3", "selected_image3",
                                         "image_label6", self.upload_image5)

    # def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     if platform == 'android':
    #         if check_permission(Permission.READ_MEDIA_IMAGES):
    #             self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #         else:
    #             self.request_media_images_permission()
    #     else:
    #         # For non-Android platforms, directly open the file manager
    #         self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #
    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
    #                                                    image_label_id, upload_function),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         # For other platforms, show the file manager from the root directory
    #         self.file_manager.show('/')
    #
    # def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
    #     upload_function(path)  # Upload the selected image
    #     self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
    #     file_name = os.path.basename(path)  # Extract file name from the path
    #     self.manager.get_screen('BorrowerScreen_Edu_Bachelors').ids[
    #         image_label_id].text = file_name  # Update the label text
    #     self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants):
            # All grants are truthy, permission granted, open the file manager
            self.file_manager_open()
        else:
            # At least one grant is falsy, permission denied, show a modal view
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

    def update_data_with_file_4(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_5(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_6(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label3.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    # def go_to_dashboard(self):
    #     self.manager.current = 'DashScreen'
    #
    # def on_pre_enter(self):
    #     Window.bind(on_keyboard=self.on_back_button)
    #
    # def on_pre_leave(self):
    #     Window.unbind(on_keyboard=self.on_back_button)
    #
    # def on_back_button(self, instance, key, scancode, codepoint, modifier):
    #     if key == 27:
    #         self.go_back()
    #         return True
    #     return False
    #
    # def go_back(self):
    #     self.manager.transition = SlideTransition(direction='right')
    #     self.manager.current = 'BorrowerScreen3'

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

    def go_to_borrower_screen_btech(self):
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
        Clock.schedule_once(lambda dt: self.perform_loan_request_action_bachelors(modal_view), 2)

    def perform_loan_request_action_bachelors(self, modal_view):
        # Close the modal view after performing the action
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        validation_errors = []

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return

        # Create a new instance of the LoginScreen
        if not self.validate_image_loaded(self.ids.image_label4):
            validation_errors.append((self.ids.image_label4, "Image not loaded."))
            self.show_validation_error("Please Upload 10th Certificates.")
        elif not self.validate_image_loaded(self.ids.image_label5):
            validation_errors.append((self.ids.image_label5, "Image not loaded."))
            self.show_validation_error("Please Upload 12th Certificates.")
        elif not self.validate_image_loaded(self.ids.image_label6):
            validation_errors.append((self.ids.image_label6, "Image not loaded."))
            self.show_validation_error("Please Upload Bachelor's degree Certificates.")
        else:
            borrower_screen = BorrowerScreen7(name='BorrowerScreen7')
            sm.add_widget(borrower_screen)
            sm.current = 'BorrowerScreen7'

    #
    # # ======================================================================
    # #     masters degree
    def upload_image6(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['tenth_class'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def get_email(self):
        return anvil.server.call('another_method')

    def upload_image7(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['intermediate'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image8(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['btech'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image9(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['mtech'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

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

    def check_and_open_file_manager7(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label7", self.upload_image8)

    def check_and_open_file_manager8(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label8", self.upload_image9)

    def check_and_open_file_manager9(self):
        self.check_and_open_file_manager("upload_icon3", "upload_label3", "selected_file_label3", "selected_image3",
                                         "image_label9", self.upload_image10)

    def check_and_open_file_manager10(self):
        self.check_and_open_file_manager("upload_icon4", "upload_label4", "selected_file_label4", "selected_image4",
                                         "image_label10", self.upload_image10)

    # def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     if platform == 'android':
    #         if check_permission(Permission.READ_MEDIA_IMAGES):
    #             self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #         else:
    #             self.request_media_images_permission()
    #     else:
    #         # For non-Android platforms, directly open the file manager
    #         self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #
    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
    #                                                    image_label_id, upload_function),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         # For other platforms, show the file manager from the root directory
    #         self.file_manager.show('/')
    #
    # def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
    #     upload_function(path)  # Upload the selected image
    #     self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
    #     file_name = os.path.basename(path)  # Extract file name from the path
    #     self.manager.get_screen('BorrowerScreen_Edu_Masters').ids[
    #         image_label_id].text = file_name  # Update the label text
    #     self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants):
            # All grants are truthy, permission granted, open the file manager
            self.file_manager_open()
        else:
            # At least one grant is falsy, permission denied, show a modal view
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

    def update_data_with_file_7(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_8(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_9(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label3.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_10(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET masters_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label4.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    # def go_to_dashboard(self):
    #     self.manager.current = 'DashScreen'
    #
    # def on_pre_enter(self):
    #     Window.bind(on_keyboard=self.on_back_button)
    #
    # def on_pre_leave(self):
    #     Window.unbind(on_keyboard=self.on_back_button)
    #
    # def on_back_button(self, instance, key, scancode, codepoint, modifier):
    #     if key == 27:
    #         self.go_back()
    #         return True
    #     return False
    #
    # def go_back(self):
    #     self.manager.transition = SlideTransition(direction='right')
    #     self.manager.current = 'BorrowerScreen3'

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

    def go_to_borrower_screen_mas(self):
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
        Clock.schedule_once(lambda dt: self.perform_masters_action_mas(modal_view), 2)

    def perform_masters_action_mas(self, modal_view):
        # Close the modal view after performing the action
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        validation_errors = []

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return

        # Create a new instance of the LoginScreen
        if not self.validate_image_loaded(self.ids.image_label7):
            validation_errors.append((self.ids.image_label7, "Image not loaded."))
            self.show_validation_error("Please Upload 10th Certificate.")
        elif not self.validate_image_loaded(self.ids.image_label8):
            validation_errors.append((self.ids.image_label8, "Image not loaded."))
            self.show_validation_error("Please Upload 12th Certificate.")
        elif not self.validate_image_loaded(self.ids.image_label9):
            validation_errors.append((self.ids.image_label9, "Image not loaded."))
            self.show_validation_error("Please Upload Bachelor's degree Certificates.")
        elif not self.validate_image_loaded(self.ids.image_label10):
            validation_errors.append((self.ids.image_label10, "Image not loaded."))
            self.show_validation_error("Please Upload Master's Certificate.")
        else:
            borrower_screen = BorrowerScreen7(name='BorrowerScreen7')
            sm.add_widget(borrower_screen)
            sm.current = 'BorrowerScreen7'

    # =====================================================================
    #     PHDegree
    def check_and_open_file_manager11(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label11", self.upload_image10)

    def check_and_open_file_manager12(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label12", self.upload_image11)

    def check_and_open_file_manager13(self):
        self.check_and_open_file_manager("upload_icon3", "upload_label3", "selected_file_label3", "selected_image3",
                                         "image_label13", self.upload_image12)

    def check_and_open_file_manager14(self):
        self.check_and_open_file_manager("upload_icon4", "upload_label4", "selected_file_label4", "selected_image4",
                                         "image_label14", self.upload_image13)

    def check_and_open_file_manager15(self):
        self.check_and_open_file_manager("upload_icon5", "upload_label5", "selected_file_label5", "selected_image5",
                                         "image_label15", self.upload_image14)

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id, upload_function),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        upload_function(path)  # Upload the selected image
        self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen3').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def upload_image10(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['tenth_class'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image11(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['intermediate'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image12(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['btech'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image13(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['mtech'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image14(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['phd'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

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

    def get_email(self):
        return anvil.server.call('another_method')

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants):
            # All grants are truthy, permission granted, open the file manager
            self.file_manager_open()
        else:
            # At least one grant is falsy, permission denied, show a modal view
            self.show_permission_denied()

    def show_validation_errors(self, validation_errors):
        for widget, error_message in validation_errors:
            widget.error = True
            widget.helper_text_color = (1, 0, 0, 1)
            widget.helper_text = error_message
            widget.helper_text_mode = "on_error"
            widget.line_color_normal = (1, 0, 0, 1)  # Red color for the line when not focused
            if isinstance(widget, MDCheckbox):
                widget.theme_text_color = 'Error'

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

    def update_data_with_file_11(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_12(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_13(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label3.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_14(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET masters_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label4.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_15(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET phd_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label5.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')
            # Handle the case where the user is not logged in, possibly by displaying an error message to the user.

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

    def go_to_borrower_screen_phd(self):
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
        Clock.schedule_once(lambda dt: self.perform_phd_action_phd(modal_view), 2)

    def perform_phd_action_phd(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        validation_errors = []

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return

        if not self.validate_image_loaded(self.ids.image_label11):
            validation_errors.append((self.ids.image_label11, "Image not loaded."))
            self.show_validation_error("Please Upload 10th Certificate.")
        elif not self.validate_image_loaded(self.ids.image_label12):
            validation_errors.append((self.ids.image_label12, "Image not loaded."))
            self.show_validation_error("Please Upload 12th Certificate.")
        elif not self.validate_image_loaded(self.ids.image_label13):
            validation_errors.append((self.ids.image_label13, "Image not loaded."))
            self.show_validation_error("Please Upload Bachelor's degree Certificates.")
        elif not self.validate_image_loaded(self.ids.image_label14):
            validation_errors.append((self.ids.image_label14, "Image not loaded."))
            self.show_validation_error("Please Upload Master's Certificate.")
        elif not self.validate_image_loaded(self.ids.image_label15):
            validation_errors.append((self.ids.image_label15, "Image not loaded."))
            self.show_validation_error("Please Upload PHD Certificate.")
        else:
            borrower_screen = BorrowerScreen7(name='BorrowerScreen7')
            sm.add_widget(borrower_screen)
            sm.current = 'BorrowerScreen7'


class BorrowerScreen5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.father_dob.input_type = 'number'

    def on_father_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.father_ph_no.input_type = 'number'

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

    def add_data(self, father_name, father_address, father_occupation, father_ph_no, father_dob):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(father_name, father_address, father_occupation, father_ph_no,
                                                         father_dob,
                                                         modal_view), 2)

    def perform_data_addition_action(self, father_name, father_address, father_occupation, father_ph_no, father_dob,
                                     modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Check for missing fields
        if not all([father_name, father_address, father_occupation, father_ph_no, father_dob]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing

        if not father_ph_no.isdigit() or len(father_ph_no) not in (10, 12):
            self.show_validation_error("Please Enter Valid Father Number.")
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', father_name):
            self.show_validation_error("Please Enter Valid Father Name.")
            return
        if len(father_occupation) < 3:
            self.show_validation_error("Please Enter Valid Father Occupation.")
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', father_address):
            self.show_validation_error("Please enter valid father Age.")
            return
        try:
            dob = datetime.strptime(father_dob, "%Y-%m-%d")
            today = datetime.now()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 18:
                self.show_validation_error("Enter a Valid Date of Birth Age must be Greater Than 18")
                return

        except ValueError:
            self.show_validation_error("Please enter a valid date of birth in the format YYYY-MM-DD")
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET father_name = ?, father_address = ?, father_occupation = ?, father_ph_no = ? WHERE customer_id = ?",
                (father_name, father_address, father_occupation, father_ph_no, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_name'] = father_name
                data2[index2]['guarantor_address'] = father_address
                data2[index2]['guarantor_mobile_no'] = int(father_ph_no)
                data2[index2]['guarantor_profession'] = father_occupation
                data2[index2]['guarantor_date_of_births'] = father_dob
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = BorrowerScreen20(name='BorrowerScreen20')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen20'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen6(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mother_dob.input_type = 'number'

    def on_mother_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mother_ph_no.input_type = 'number'

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

    def add_data(self, mother_name, mother_address, mother_occupation, mother_ph_no, mother_dob):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(mother_name, mother_address, mother_occupation, mother_ph_no,
                                                         mother_dob,
                                                         modal_view), 2)

    def perform_data_addition_action(self, mother_name, mother_address, mother_occupation, mother_ph_no, mother_dob,
                                     modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Check for missing fields
        if not all([mother_name, mother_address, mother_occupation, mother_ph_no, mother_dob]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing

        if not mother_ph_no.isdigit() and len(mother_ph_no) not in (10, 12):
            self.show_validation_error("Please Enter Valid Mother Number.")
            return

        if not re.match(r'^[a-zA-Z\s]{3,}$', mother_name):
            self.show_validation_error("Please Enter Valid Mother Name.")
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', mother_occupation):
            self.show_validation_error("Please Enter Valid Mother Occupation.")
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', mother_address):
            self.show_validation_error("Please Enter Valid Mother Address.")
            return
        try:
            dob = datetime.strptime(mother_dob, "%Y-%m-%d")
            today = datetime.now()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 18:
                self.show_validation_error("Enter a Valid Date of Birth Age must be Greater Than 18")
                return

        except ValueError:
            self.show_validation_error("Please enter a valid date of birth in the format YYYY-MM-DD")
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET mother_name = ?, mother_address = ?, mother_occupation = ?, mother_ph_no = ? WHERE customer_id = ?",
                (mother_name, mother_address, mother_occupation, mother_ph_no, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_name'] = mother_name
                data2[index2]['guarantor_address'] = mother_address
                data2[index2]['guarantor_mobile_no'] = int(mother_ph_no)
                data2[index2]['guarantor_profession'] = mother_occupation
                data2[index2]['guarantor_date_of_births'] = mother_dob
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = BorrowerScreen20(name='BorrowerScreen20')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen20'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen7(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_borrower_profession.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['borrower_profession'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.spinner_id.values = ['Select Profession type'] + self.unique_list
        else:
            self.ids.spinner_id.values = ['Select Profession type']

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

    def add_data(self, spinner_id):
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
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(spinner_id, modal_view), 2)

    def perform_data_addition_action(self, spinner_id, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        if not all([spinner_id]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if spinner_id not in self.unique_list:
            self.show_validation_error('Select valid Profession type')
            return

        if spinner_id == 'Student':
            sm = self.manager
            borrower_screen = BorrowerScreen8(name='BorrowerScreen8')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen8'

        elif spinner_id == 'Business' or spinner_id == 'Self employment':
            sm = self.manager
            borrower_screen = BorrowerScreen25(name='BorrowerScreen25')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen25'

        elif spinner_id == 'Employee':
            sm = self.manager
            borrower_screen = BorrowerScreen12(name='BorrowerScreen12')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen12'
        else:
            sm = self.manager
            borrower_screen = BorrowerScreen15(name='BorrowerScreen15')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen15'
        print(spinner_id)
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []

        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET proficient_type = ? WHERE customer_id = ?",
                (spinner_id, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['profession'] = spinner_id
        else:
            print('no email found')

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen4'


class BorrowerScreen8(Screen):
    MAX_IMAGE_SIZE_MB = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1", self.upload_image)

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id, upload_function),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        upload_function(path)  # Upload the selected image
        self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen8').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def get_email(self):
        return anvil.server.call('another_method')

    def upload_image(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['college_proof'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")
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
    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants):
            # All grants are truthy, permission granted, open the file manager
            self.file_manager_open()
        else:
            # At least one grant is falsy, permission denied, show a modal view
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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

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

    def add_data(self, collage_name, college_address, collage_id):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(collage_name, college_address, collage_id, modal_view), 2)

    def perform_data_addition_action(self, collage_name, college_address, collage_id, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        if not all([collage_name, college_address, collage_id]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if len(collage_name) < 3:
            self.show_validation_error('Enter a valid college Name')
            return
        if len(collage_id) < 3:
            self.show_validation_error('Enter a valid college ID')
            return
        if len(college_address) < 3:
            self.show_validation_error('Enter a valid college Address')
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            # Check if any user is logged in
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET collage_name = ?, college_address = ?, college_id = ? WHERE customer_id = ?",
                (collage_name, college_address, collage_id, row_id_list[log_index]))
            conn.commit()

        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")
            print("Moving to BorrowerScreen15...")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['college_name'] = collage_name
            data[index]['college_address'] = college_address
            data[index]['college_id'] = collage_id
        else:
            print('email not found')
        sm = self.manager
        borrower_screen = BorrowerScreen15(name='BorrowerScreen15')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'
        sm.current = 'BorrowerScreen15'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen7'


class BorrowerScreen9(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_borrower_business_type.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['borrower_business_type'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.spin.values = ['Select Business Type'] + self.unique_list
        else:
            self.ids.spin.values = ['Select Business Type']

        spinner_data1 = app_tables.fin_borrower_no_of_employees.search()
        data_list1 = []
        for i in spinner_data1:
            data_list1.append(i['borrower_no_of_employees'])
        self.unique_list1 = []
        for i in data_list1:
            if i not in self.unique_list1:
                self.unique_list1.append(i)
        print(self.unique_list1)
        if len(self.unique_list1) >= 1:
            self.ids.no_of_employees_working.values = ['No of Employees Working'] + self.unique_list1
        else:
            self.ids.no_of_employees_working.values = ['No of Employees Working']

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

    def add_data(self, business_name, business_location, business_address, no_of_emp):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(business_name, business_location, business_address, no_of_emp,
                                                         modal_view), 2)

    def perform_data_addition_action(self, business_name, business_location, business_address, no_of_emp, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        if not all([business_name, business_location, business_address, no_of_emp]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if len(business_name) < 3:
            self.show_validation_error('Enter a valid business Name')
            return
        if business_location not in self.unique_list:
            self.show_validation_error('Select valid business type')
            return
        if len(business_address) < 3:
            self.show_validation_error('Enter a valid business address')
            return
        if no_of_emp not in self.unique_list1:
            self.show_validation_error('Select a valid no of employees type')
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET business_name = ?, business_type = ?, business_address = ?, no_of_employees_working=? WHERE customer_id = ?",
                (business_name, business_location, business_address, no_of_emp, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['business_name'] = business_name
            data[index]['business_add'] = business_address
            data[index]['business_type'] = business_location
            data[index]['employees_working'] = no_of_emp
        else:
            print('no email found')

        sm = self.manager
        borrower_screen = BorrowerScreen10(name='BorrowerScreen10')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'
        sm.current = 'BorrowerScreen10'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen7'


class BorrowerScreen10(Screen):
    MAX_IMAGE_SIZE_MB = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_last_six_months_turnover_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.last_six_months_turnover.input_type = 'number'

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1", self.upload_image)

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id, upload_function),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def get_email(self):
        return anvil.server.call('another_method')

    def upload_image(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['last_six_month_bank_proof'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")
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
    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        upload_function(path)  # Upload the selected image
        self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen10').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants):
            # All grants are truthy, permission granted, open the file manager
            self.file_manager_open()
        else:
            # At least one grant is falsy, permission denied, show a modal view
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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET last_six_months_turnover_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

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

    def add_data(self, industry_type, last_six_months_turnover, year_of_estd):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(industry_type, last_six_months_turnover,
                                                         year_of_estd, modal_view), 2)

    def calculate_age(self, year_of_estd):
        today = datetime.today()
        dob = datetime.strptime(year_of_estd, '%Y-%m-%d')
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def perform_data_addition_action(self, industry_type, last_six_months_turnover,
                                     year_of_estd, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        # Check for missing fields
        if not all([industry_type, last_six_months_turnover, year_of_estd]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if len(industry_type) < 3:
            self.show_validation_error('Enter a valid industry type')
            return

        if len(last_six_months_turnover) < 3:
            self.show_validation_error('Enter a valid last six months turnover')
            return
        try:
            dob = datetime.strptime(year_of_estd, "%Y-%m-%d")

        except ValueError:
            self.show_validation_error("Please enter a valid Year of Establishment in the format YYYY-MM-DD")
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET industry_type = ?, last_six_months_turnover = ?, year_of_estd = ? WHERE customer_id = ?",
                (industry_type, last_six_months_turnover, year_of_estd,
                 row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['industry_type'] = industry_type
            data[index]['six_month_turnover'] = last_six_months_turnover
            data[index]['year_of_estd'] = year_of_estd
            age = self.calculate_age(year_of_estd)
            data[index]['business_age'] = age
        else:
            print('no email found')
        sm = self.manager
        borrower_screen = BorrowerScreen11(name='BorrowerScreen11')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'
        sm.current = 'BorrowerScreen11'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen9'


class BorrowerScreen11(Screen):
    MAX_IMAGE_SIZE_MB = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_last_six_months_turnover_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.last_six_months_turnover.input_type = 'number'

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1", self.upload_image)

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id, upload_function),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def get_email(self):
        return anvil.server.call('another_method')

    def upload_image(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['proof_verification'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")
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
    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        upload_function(path)  # Upload the selected image
        self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen11').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants):
            # All grants are truthy, permission granted, open the file manager
            self.file_manager_open()
        else:
            # At least one grant is falsy, permission denied, show a modal view
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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET last_six_months_turnover_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

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

    def add_data(self, cin, din, reg_addres):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(cin, din, reg_addres, modal_view), 2)

    def perform_data_addition_action(self, cin, din, reg_addres, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([cin, din, reg_addres]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if len(cin) < 3:
            self.show_validation_error("Enter a valid CIN.")
            return
        if len(din) < 3:
            self.show_validation_error("Enter a valid DIN")
            return
        if len(reg_addres) < 3:
            self.show_validation_error("Enter a valid Registration Address")
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET CIN = ?, DIN = ?, registered_office_address = ? WHERE customer_id = ?",
                (cin, din, reg_addres, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['cin'] = cin
            data[index]['din'] = din
            data[index]['registered_off_add'] = reg_addres
        else:
            print('email not found')

        sm = self.manager
        borrower_screen = BorrowerScreen15(name='BorrowerScreen15')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'
        sm.current = 'BorrowerScreen15'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen7'


class BorrowerScreen12(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_borrower_employee_type.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['borrower_employee_type'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.spinner1.values = ['Select Employment Type'] + self.unique_list
        else:
            self.ids.spinner1.values = ['Select Employment Type']

        spinner_data1 = app_tables.fin_borrower_organization_type.search()
        data_list1 = []
        for i in spinner_data1:
            data_list1.append(i['borrower_organization_type'])
        self.unique_list1 = []
        for i in data_list1:
            if i not in self.unique_list1:
                self.unique_list1.append(i)
        print(self.unique_list1)
        if len(self.unique_list1) >= 1:
            self.ids.spinner2.values = ['Select Organisation Type'] + self.unique_list1
        else:
            self.ids.spinner2.values = ['Select Organisation Type']

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

    def add_data(self, employment_type, company_name, organization):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(employment_type, company_name, organization, modal_view), 2)

    def perform_data_addition_action(self, employment_type, company_name, organization, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Check for missing fields
        if not all([employment_type, company_name, organization]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if employment_type not in self.unique_list:
            self.show_validation_error('Select a valid employment type')
            return
        if len(company_name) < 3:
            self.show_validation_error('Enter a valid company name')
            return
        if organization not in self.unique_list1:
            self.show_validation_error('Select a valid organisation type')
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET employment_type = ?, company_name = ?, organization_type = ? WHERE customer_id = ?",
                (employment_type, company_name, organization, row_id_list[log_index]))
            conn.commit()

        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['employment_type'] = employment_type
            data[index]['company_name'] = company_name
            data[index]['organization_type'] = organization
        else:
            print('email not found')

        sm = self.manager
        borrower_screen = BorrowerScreen13(name='BorrowerScreen13')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'
        sm.current = 'BorrowerScreen13'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen7'


class BorrowerScreen14(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_occupation_type.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['occupation_type'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.spinner.values = ['Select Occupation Type'] + self.unique_list
        else:
            self.ids.spinner.values = ['Select Occupation Type']

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

    def add_data(self, company_address, occupation_type, landmark, business_number):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(company_address, occupation_type, landmark,
                                                         business_number, modal_view), 2)

    def perform_data_addition_action(self, company_address, occupation_type, landmark, business_number,
                                     modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([company_address, occupation_type, landmark, business_number]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if len(company_address) < 3:
            self.show_validation_error("Please Enter Valid Company Address.")
            return
        if occupation_type not in self.unique_list:
            self.show_validation_error("Please Select Valid Occupation Type")
            return
        if len(landmark) < 3:
            self.show_validation_error("Please Enter Valid Landmark.")
            return
        if not business_number.isdigit() or len(business_number) != 10:
            self.show_validation_error("Please Enter Valid Business Number.")
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET company_address = ?, landmark = ?, business_number = ? WHERE customer_id = ?",
                (company_address, landmark, business_number, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['company_address'] = company_address
            data[index]['company_landmark'] = landmark
            data[index]['business_no'] = business_number
            data[index]['occupation_type'] = occupation_type
        else:
            print('email not found')

        sm = self.manager
        borrower_screen = BorrowerScreen15(name='BorrowerScreen15')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'
        sm.current = 'BorrowerScreen15'

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

    def on_company_pincode_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.company_pincode.input_type = 'number'

    def on_business_phone_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.business_number.input_type = 'number'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen13'


class BorrowerScreen13(Screen):
    MAX_IMAGE_SIZE_MB = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        gender_data = app_tables.fin_borrower_salary_type.search()
        gender_list = []
        for i in gender_data:
            gender_list.append(i['borrower_salary_type'])
        self.unique_gender = []
        for i in gender_list:
            if i not in self.unique_gender:
                self.unique_gender.append(i)
        print(self.unique_gender)
        if len(self.unique_gender) >= 1:
            self.ids.salary_type_id.values = ['Select Salary type'] + self.unique_gender
        else:
            self.ids.salary_type_id.values = ['Select Salary type']

    def get_email(self):
        return anvil.server.call('another_method')

    def upload_image(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['emp_id_proof'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image1(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['last_six_month_bank_proof'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def on_annual_salary_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.annual_salary.input_type = 'number'

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1", self.upload_image)

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2", self.upload_image1)

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id, upload_function),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        upload_function(path)  # Upload the selected image
        self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen13').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants):
            # All grants are truthy, permission granted, open the file manager
            self.file_manager_open()
        else:
            # At least one grant is falsy, permission denied, show a modal view
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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET employee_id_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET six_months_bank_statement_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

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

    def add_data(self, annual_salary, designation,salary_type_id):
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
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(annual_salary, salary_type_id,designation, modal_view), 2)

    def perform_data_addition_action(self,salary_type_id, annual_salary, designation, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([annual_salary, designation]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if len(annual_salary) < 3 and not annual_salary.isdigit():
            self.show_validation_error("Please Enter Valid Company Number.")
            return
        if len(designation) < 3:
            self.show_validation_error("Please Enter Valid Designation.")
            return

        if not all([salary_type_id]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if salary_type_id not in self.unique_gender:
            self.show_validation_error('Select a valid salary type')
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET annual_salary = ?, designation = ? WHERE customer_id = ?",
                (annual_salary, designation, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['annual_salary'] = annual_salary
            data[index]['designation'] = designation
            data[index]['salary_type'] = salary_type_id
        else:
            print('email not found')

        sm = self.manager
        borrower_screen = BorrowerScreen14(name='BorrowerScreen14')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'
        sm.current = 'BorrowerScreen14'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen12'

class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class BorrowerScreen15(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.profession_type = None
        spinner_data = app_tables.fin_borrower_marrital_status.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['borrower_marrital_status'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.marital_status_id.values = ['Select Marital Status'] + self.unique_list
        else:
            self.ids.marital_status_id.values = ['Select Marital Status']

        self.update_top_bar_image()
        Clock.schedule_once(self.setup_menu, 0.5)  # Schedule menu setup after a delay

    def update_top_bar_image(self):
        # Replace with your Anvil server call to fetch email
        log_email = "mamidalasai3469@gmail.com"

        # Replace with your Anvil table search method to fetch profile data
        profile = app_tables.fin_user_profile.search()

        # Initialize lists to store profile data
        email_user = []
        name_list = []
        investment = []
        user_age = []
        p_customer_id = []
        ascend_score = []
        emp_type = []
        profile_list = []

        # Extract data from the profile list
        for i in profile:
            email_user.append(i['email_user'])
            name_list.append(i['full_name'])
            investment.append(i['investment'])
            user_age.append(i['user_age'])
            p_customer_id.append(i['customer_id'])
            ascend_score.append(i['ascend_value'])
            emp_type.append(i['profession'])
            profile_list.append(i['user_photo'])  # Assuming 'user_photo' is the key for the photo

        # Find the index of log_email in email_user list
        log_index = email_user.index(log_email) if log_email in email_user else 0

        top_bar = self.ids.bar

        if profile_list[log_index] is not None:
            image_data = profile_list[log_index]
            try:
                # Load image data into CoreImage texture
                print(isinstance(image_data, bytes), isinstance(image_data, str), image_data)
                if isinstance(image_data, bytes):
                    profile_texture_io = BytesIO(image_data)
                elif isinstance(image_data, str):
                    image_data_binary = base64.b64decode(image_data)
                    profile_texture_io = BytesIO(image_data_binary)
                elif isinstance(image_data, LazyMedia):
                    image_data_bytes = image_data.get_bytes()
                    profile_texture_io = BytesIO(image_data_bytes)
                else:
                    raise ValueError("Unsupported image data type")

                # Create CoreImage texture
                photo_texture = CoreImage(profile_texture_io, ext='png').texture

                # Save the texture to a temporary file
                with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
                    temp_file.write(profile_texture_io.getvalue())
                    temp_file_path = temp_file.name

                # Update right_action_items with the temp file path
                top_bar.right_action_items = [
                    [temp_file_path, lambda x: self.account()]
                ]

            except Exception as e:
                print(f"Error loading photo texture: {e}")

        else:
            # No profile picture available, set a default image or action
            top_bar.right_action_items = [
                ['icon8.png', lambda x: self.account()]
            ]

    def setup_menu(self, *args):
        menu_items = [
            {
                "text": "Profile",
                "viewclass": "IconListItem",
                "icon": "account-circle",
                "on_release": lambda x="Profile": self.menu_callback(x),
            },
            {
                "viewclass": "IconListItem",
                "text": "Logout",
                "icon": "logout",
                "on_release": lambda x="Logout": self.menu_callback(x),
            },
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.bar.ids.right_actions,
            items=menu_items,
            position="bottom",
            width_mult=3,
        )

    def menu_callback(self, item):
        print(f"Menu item clicked: {item}")

    def account(self):
        self.menu.open()

    def update_details(self, marital_status_id):
        if marital_status_id == "Married":
            self.ids.relation_name.values = ["Father", "Mother", "Spouse", "Others"]
        else:
            self.ids.relation_name.values = ["Father", "Mother", "Others"]

    def update_rect(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(0, 0, 0, 1)  # Set the color to black with full opacity
            Line(width=0.7, rectangle=(instance.x, instance.y, instance.width, instance.height))

    def logout(self):
        # Implement logout functionality here
        print("Logout clicked")
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
        self.manager.current = 'prelogin'
        self.menu.dismiss()

    def update_person_details_visibility(self, relation):
        # Remove any existing spouse details box
        self.ids.box.clear_widgets()

        if relation == "Spouse":
            spouse_details = self.ids.box

            self.spouse_name = MDTextField(id='spouse_name', hint_text='Enter Spouse Name *', multiline=False,
                                           helper_text_mode='on_focus', font_size=15, mode="rectangle",
                                           radius=[0, 0, 0, 0])
            self.spouse_name.bind(text=self.spouse_name_validation)
            spouse_details.add_widget(self.spouse_name)

            self.spouse_date_textfield = MDTextField(id='spouse_date_textfield', hint_text='Enter Marriage Date *',
                                                     helper_text_mode='on_focus',
                                                     input_type='number',
                                                     font_size=15, mode="rectangle")
            self.spouse_date_textfield.bind(text=self.spouse_date_validation)
            spouse_details.add_widget(self.spouse_date_textfield)

            self.spouse_mobile = MDTextField(id='spouse_mobile', hint_text='Enter Spouse Mobile No *', multiline=False,
                                             helper_text_mode='on_focus',
                                             input_type='number', font_size=15, mode="rectangle")
            self.spouse_mobile.bind(text=self.spouse_mobile_validation)
            spouse_details.add_widget(self.spouse_mobile)

            spouse_profession_label = MDLabel(text='Spouse Profession Type:', halign='left', font_size=15,
                                              font_name='Roboto-Bold', size_hint_y=None, height=dp(20))
            spouse_details.add_widget(spouse_profession_label)

            self.spouse_profession = Spinner(
                text="Select Spouse Profession",
                font_size="15dp",
                multiline=False,
                size_hint=(1, None),
                height=dp(40),
                width=dp(200),  # Adjust color as needed
                background_normal='',
                color=(0, 0, 0, 1),
                values=['Nothing'],
                option_cls='CustomSpinnerOption'

            )
            self.spouse_profession.bind(size=self.update_rect, pos=self.update_rect)

            # Configure canvas for border
            self.spouse_profession.text_size = (self.spouse_profession.width - dp(20), None)

            with self.spouse_profession.canvas.before:
                Color(0, 0, 0, 1)  # Set the color to black with full opacity
                Line(width=0.7, rectangle=(
                self.spouse_profession.x, self.spouse_profession.y, self.spouse_profession.width,
                self.spouse_profession.height))

            spouse_details.add_widget(self.spouse_profession)

            self.spouse_company_name = MDTextField(id='spouse_company_name', hint_text='Enter Spouse Company Name *',
                                                   multiline=False,
                                                   helper_text_mode='on_focus', font_size=15, mode="rectangle")
            self.spouse_company_name.bind(text=self.spouse_company_name_validation)
            spouse_details.add_widget(self.spouse_company_name)

            self.spouse_annual_salary = MDTextField(id='spouse_annual_salary', hint_text='Enter Annual Salary *',
                                                    multiline=False,
                                                    helper_text_mode='on_focus', input_type='number', font_size=15,
                                                    mode="rectangle")
            self.spouse_annual_salary.bind(text=self.spouse_annual_salary_validation)
            spouse_details.add_widget(self.spouse_annual_salary)

            self.error_msg = MDLabel(text='', halign='left', font_size=15,
                                     font_name='Roboto-Bold', size_hint_y=None, height=dp(20),
                                     theme_text_color="Custom", text_color='red')
            spouse_details.add_widget(self.error_msg)

        # Add other person details widgets based on selected relation
        elif relation == "Father" or relation == "Mother":
            # Add details for father
            person_details_box1 = self.ids.box

            self.person_name = MDTextField(id='person_name', hint_text='Enter Full Name *', multiline=False,
                                           helper_text_mode='on_focus',
                                           halign='left', font_size=15, mode='rectangle')
            self.person_name.bind(text=self.person_name_validtion)
            person_details_box1.add_widget(self.person_name)

            self.person_dob = MDTextField(id='person_dob', hint_text='Enter Date Of Birth *',
                                          multiline=False, helper_text_mode='on_focus', halign='left',
                                          input_type='number',
                                          font_size=15, mode='rectangle')
            self.person_dob.bind(text=self.person_dob_validtion)
            person_details_box1.add_widget(self.person_dob)

            self.person_ph_no = MDTextField(id='person_ph_no', hint_text='Enter Phone No *',
                                            helper_text_mode='on_focus', halign='left', input_type='number',
                                            font_size=15, mode='rectangle')
            self.person_ph_no.bind(text=self.person_ph_no_validtion)
            person_details_box1.add_widget(self.person_ph_no)

            self.person_profession = MDTextField(id='person_profession', hint_text='Enter Profession *',
                                                 multiline=False,
                                                 helper_text_mode='on_focus', font_size=15, mode='rectangle')
            self.person_profession.bind(text=self.person_profession_validtion)
            person_details_box1.add_widget(self.person_profession)
            self.error_msg = MDLabel(text='', halign='left', font_size=15,
                                     font_name='Roboto-Bold', size_hint_y=None, height=dp(20),
                                     theme_text_color="Custom", text_color='red')
            person_details_box1.add_widget(self.error_msg)

        elif relation == "Others":
            # Add details for other relations
            person_details_box1 = self.ids.box

            self.relation_name1 = MDTextField(id='relation_name1', hint_text='How is the person related to you',
                                              multiline=False,
                                              helper_text_mode='on_focus', halign='left', font_size=15,
                                              mode='rectangle')
            self.relation_name1.bind(text=self.relation_name1_validation)
            person_details_box1.add_widget(self.relation_name1)

            self.person_name = MDTextField(id='person_name', hint_text='Enter Full Name *', multiline=False,
                                           helper_text_mode='on_focus',
                                           halign='left', font_size=15, mode='rectangle')
            self.person_name.bind(text=self.person_name_validtion)
            person_details_box1.add_widget(self.person_name)

            self.person_dob = MDTextField(id='person_dob', hint_text='Enter Date Of Birth *',
                                          multiline=False, helper_text_mode='on_focus', halign='left',
                                          input_type='number',
                                          font_size=15, mode='rectangle')
            self.person_dob.bind(text=self.person_dob_validtion)
            person_details_box1.add_widget(self.person_dob)

            self.person_ph_no = MDTextField(id='person_ph_no', hint_text='Enter Phone No *',
                                            helper_text_mode='on_focus', halign='left', input_type='number',
                                            font_size=15, mode='rectangle')
            self.person_ph_no.bind(text=self.person_ph_no_validtion)
            person_details_box1.add_widget(self.person_ph_no)

            self.person_profession = MDTextField(id='person_profession', hint_text='Enter Profession *',
                                                 multiline=False,
                                                 helper_text_mode='on_focus', font_size=15, mode='rectangle')
            self.person_profession.bind(text=self.person_profession_validtion)
            person_details_box1.add_widget(self.person_profession)
            self.error_msg = MDLabel(text='', halign='left', font_size=15,
                                     font_name='Roboto-Bold', size_hint_y=None, height=dp(20),
                                     theme_text_color="Custom", text_color='red')
            person_details_box1.add_widget(self.error_msg)

        # Add widgets for other relations as needed
    def update_rect(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(0, 0, 0, 1)  # Set the color to black with full opacity
            Line(width=0.7, rectangle=(instance.x, instance.y, instance.width, instance.height))

    def spouse_name_validation(self, instance, value):
        if value.isdigit() or len(value) < 3:
            instance.error = True
            self.spouse_name.helper_text = 'Enter Correct Name'
            self.spouse_name._helper_text_color = 'red'
            return
        else:
            instance.error = False
            self.spouse_name.helper_text = ''

    def spouse_mobile_validation(self, instance, value):
        if not value.isdigit() or len(value) != 10:
            instance.error = True
            self.spouse_mobile.helper_text = 'Enter Correct Number like 10 Digits'
            self.spouse_mobile._helper_text_color = 'red'
            return
        else:
            instance.error = False
            self.spouse_mobile.helper_text = ''

    def spouse_date_validation(self, instance, value):

        try:
            dob = datetime.strptime(value, "%Y-%m-%d").date()  # Convert to date object
            today = datetime.now().date()
            if dob > today:
                instance.error = True
                self.spouse_date_textfield.helper_text = ' Enter Correct Date Must be greater than today'
                self.spouse_date_textfield._helper_text_color = 'red'
                return
            else:
                instance.error = False
                self.spouse_date_textfield.helper_text = ''
        except ValueError:
            instance.error = True
            self.spouse_date_textfield.helper_text = 'Enter Correct Date like YYYY-MM_DD'
            self.spouse_date_textfield._helper_text_color = 'red'
            return

    def spouse_company_name_validation(self, instance, value):
        if value.isdigit() or len(value) < 3:
            instance.error = True
            self.spouse_company_name.helper_text = 'Enter Correct Name'
            self.spouse_company_name._helper_text_color = 'red'
            return
        else:
            instance.error = False
            self.spouse_company_name.helper_text = ''

    def spouse_annual_salary_validation(self, instance, value):
        if not value.isdigit() or len(value) < 3:
            instance.error = True
            self.spouse_annual_salary.helper_text = 'Enter Correct Annual Salary'
            self.spouse_annual_salary._helper_text_color = 'red'
            return
        else:
            instance.error = False
            self.spouse_company_name.helper_text = ''

    def person_name_validtion(self, instance, value):
        if value.isdigit() or len(value) < 3:
            instance.error = True
            self.person_name.helper_text = 'Enter Correct Name'
            self.person_name._helper_text_color = 'red'
            return
        else:
            self.person_name.helper_text = ''
            instance.error = False

    def person_ph_no_validtion(self, instance, value):
        if not value.isdigit() or len(value) != 10:
            instance.error = True
            self.person_ph_no.helper_text = 'Enter Correct Phone Number'
            self.person_dob._helper_text_color = 'red'
            return
        else:
            self.person_ph_no.helper_text = ''
            instance.error = False
    def person_dob_validtion(self, instance, value):
        try:
            dob = datetime.strptime(value, "%Y-%m-%d")
            today = datetime.now()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 18:
                instance.error = True
                self.person_dob.helper_text = 'Enter Correct Date Must Greater than 18'
                self.person_dob._helper_text_color = 'red'
                return
            else:
                self.person_dob.helper_text = ''
                instance.error = False

        except ValueError:
            instance.error = True
            self.person_dob.helper_text = 'Enter Correct Date like YYYY-MM-DD'
            self.person_dob._helper_text_color = 'red'
            return

    def person_profession_validtion(self, instance, value):
        if value.isdigit() or len(value) < 3:
            instance.error = True
            self.person_profession.helper_text = 'Enter Correct Profession'
            self.person_profession._helper_text_color = 'red'
            return
        else:
            self.person_profession.helper_text = ''
            instance.error = False

    def relation_name1_validation(self, instance, value):
        if value.isdigit() or len(value) < 3:
            instance.error = True
            self.relation_name1.helper_text = 'Enter Correct Relation Name'
            self.relation_name1._helper_text_color = 'red'
            return
        else:
            self.relation_name1.helper_text = ''
            instance.error = False

    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.person_dob.input_type = 'number'

    def on_mother_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.person_ph_no.input_type = 'number'
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

    def add_data(self, marital_status_id):
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
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(marital_status_id, modal_view), 2)

    def perform_data_addition_action(self, marital_status_id, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([marital_status_id]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if marital_status_id not in self.unique_list:
            self.show_validation_error('Select a valid Marital status')
            return

        relation_name = self.ids.relation_name.text
        if relation_name not in self.ids.relation_name.values:
            self.show_validation_error('Select a valid Relation Name')
            return

        if relation_name == 'Father' or relation_name == 'Mother':
            person_name = self.person_name.text
            person_dob = self.person_dob.text
            person_ph_no = self.person_ph_no.text
            person_proffession = self.person_profession.text
            if not all([ person_name, person_dob, person_ph_no, person_proffession]):
                self.error_msg.text = 'Please Fill All Mandatory * Values'
                self.person_name.error = True
                self.person_dob.error = True
                self.person_ph_no.error = True
                self.person_profession.error = True
            else:
                self.error_msg.text = ''
            if len(self.person_name.text) < 3:
                self.person_name.helper_text = ''
                self.person_name._helper_text_color = 'red'
                self.person_name.error = True

            try:
                dob = datetime.strptime(person_dob, "%Y-%m-%d")
                today = datetime.now()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                if age < 18:
                    self.person_dob.helper_text = ''
                    self.person_dob._helper_text_color = 'red'
                    self.person_dob.error = True
                    return
                else:
                    self.person_dob.helper_text = ''

            except ValueError:
                self.person_dob.helper_text = ''
                self.person_dob._helper_text_color = 'red'
                self.person_dob.error = True
                return

            if len(self.person_ph_no.text) != 10 and not self.person_dob.text.isdigit():
                self.person_ph_no.helper_text = ''
                self.person_ph_no._helper_text_color = 'red'
                self.person_ph_no.error = True
                return

            if len(self.person_profession.text) < 3:
                self.person_profession.helper_text = ''
                self.person_profession._helper_text_color = 'red'
                self.person_profession.error = True
                return

        elif relation_name == 'Others':
            person_name = self.person_name.text
            person_dob = self.person_dob.text
            person_ph_no = self.person_ph_no.text
            person_proffession = self.person_profession.text
            relation_name1 = self.relation_name1.text
            if not all([relation_name1, person_name, person_dob, person_ph_no, person_proffession]):
                self.error_msg.text = 'Please Fill All Mandatory * Values'
                self.person_name.error = True
                self.person_dob.error = True
                self.person_ph_no.error = True
                self.person_profession.error = True
                self.relation_name1.error = True
            else:
                self.error_msg.text = ''
            if len(self.person_name.text) < 3:
                self.person_name.helper_text = ''
                self.person_name._helper_text_color = 'red'
                self.person_name.error = True

            try:
                dob = datetime.strptime(person_dob, "%Y-%m-%d")
                today = datetime.now()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                if age < 18:
                    self.person_dob.helper_text = ''
                    self.person_dob._helper_text_color = 'red'
                    self.person_dob.error = True
                    return
                else:
                    self.person_dob.helper_text = ''

            except ValueError:
                self.person_dob.helper_text = ''
                self.person_dob._helper_text_color = 'red'
                self.person_dob.error = True
                return

            if len(self.person_ph_no.text) != 10 and not self.person_dob.text.isdigit():
                self.person_ph_no.helper_text = ''
                self.person_ph_no._helper_text_color = 'red'
                self.person_ph_no.error = True
                return

            if len(self.person_profession.text) < 3:
                self.person_profession.helper_text = ''
                self.person_profession._helper_text_color = 'red'
                self.person_profession.error = True
                return


        elif relation_name == 'Spouse':
            spouse_name = self.spouse_name.text
            spouse_date_textfield = self.spouse_date_textfield.text
            spouse_mobile = self.spouse_mobile.text
            spouse_company_name = self.spouse_company_name.text
            spouse_company_address = self.spouse_profession.text
            spouse_annual_salary = self.spouse_annual_salary.text
            if not all([spouse_name, spouse_date_textfield, spouse_mobile, spouse_company_name, spouse_company_address, spouse_annual_salary]):
                self.error_msg.text = 'Please Fill All Mandatory * Values'
                self.spouse_name.error = True
                self.spouse_date_textfield.error = True
                self.spouse_mobile.error = True
                self.spouse_company_name.error = True
                self.spouse_annual_salary.error = True
            else:
                self.error_msg.text = ''

            if len(self.spouse_name.text) < 3:
                self.spouse_name.helper_text = ''
                self.spouse_name._helper_text_color = 'red'
                self.spouse_name.error = True
                return
            if len(self.spouse_mobile.text) != 10 and not self.spouse_mobile.text.isdigit():
                self.spouse_mobile.helper_text = ''
                self.spouse_mobile._helper_text_color = 'red'
                self.spouse_mobile.error = True
                return
            try:
                dob = datetime.strptime(self.spouse_date_textfield.text, "%Y-%m-%d").date()  # Convert to date object
                today = datetime.now().date()
                if dob > today:
                    self.spouse_date_textfield.helper_text = ''
                    self.spouse_date_textfield._helper_text_color = 'red'
                    self.spouse_date_textfield.error = True
                    return
                else:
                    self.spouse_date_textfield.helper_text = ''
            except ValueError:
                self.spouse_date_textfield.helper_text = ''
                self.spouse_date_textfield._helper_text_color = 'red'
                self.spouse_date_textfield.error = True
                return
            if len(self.spouse_company_name.text) < 3:
                self.spouse_company_name.helper_text = ''
                self.spouse_company_name._helper_text_color = 'red'
                self.spouse_company_name.error = True
                return
            if len(self.spouse_annual_salary.text) != 10 and not self.spouse_annual_salary.text.isdigit():
                self.spouse_annual_salary.helper_text = ''
                self.spouse_annual_salary._helper_text_color = 'red'
                self.spouse_annual_salary.error = True
                return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET marital_status = ? WHERE customer_id = ?",
                (marital_status_id, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['marital_status'] = marital_status_id
        else:
            print('email not found')

        if self.ids.marital_status_id.text == "Married" and self.ids.relation_name.text == "Spouse":
            spouse_name = self.spouse_name.text
            spouse_date_textfield = self.spouse_date_textfield.text
            spouse_mobile = self.spouse_mobile.text
            spouse_company_name = self.spouse_company_name.text
            spouse_company_address = self.spouse_profession.text
            spouse_annual_salary = self.spouse_annual_salary.text

            cursor.execute('select * from fin_users')
            rows = cursor.fetchall()
            row_id_list = []
            status = []
            for row in rows:
                row_id_list.append(row[0])
                status.append(row[-1])

            if 'logged' in status:
                log_index = status.index('logged')
                cursor.execute(
                    "UPDATE fin_registration_table SET spouse_name = ?,spouse_date_textfield = ?, spouse_mobile = ? WHERE customer_id = ?",
                    (spouse_name, spouse_date_textfield, spouse_mobile, row_id_list[log_index]))
                conn.commit()
            else:
                # Handle the case where the user is not logged in
                print("User is not logged in.")

            data = app_tables.fin_user_profile.search()
            data2 = app_tables.fin_guarantor_details.search()
            cus_id_list2 = [i['customer_id'] for i in data2]
            id_list = [i['email_user'] for i in data]
            cus_id_list = [i['customer_id'] for i in data]
            user_email = anvil.server.call('another_method')
            if user_email in id_list:
                index = id_list.index(user_email)
                if cus_id_list[index] in cus_id_list2:
                    index2 = cus_id_list2.index(cus_id_list[index])
                    data2[index2]['guarantor_name'] = spouse_name
                    data2[index2]['guarantor_mobile_no'] = int(spouse_mobile)
                    data2[index2]['guarantor_marriage_dates'] = str(spouse_date_textfield)
                    data2[index2]['guarantor_company_name'] = spouse_company_name
                    data2[index2]['guarantor_annual_earning'] = spouse_annual_salary
                    data2[index2]['guarantor_profession'] = spouse_company_address
                else:
                    print('customer_id is not valid')

            else:
                print('email not valid')
        elif self.ids.relation_name.text == "Mother" or self.ids.relation_name.text == "Father":
            relation_name = self.ids.relation_name.text
            person_name = self.person_name.text
            person_dob = self.person_dob.text
            person_ph_no = self.person_ph_no.text
            person_proffession = self.person_profession.text

            data = app_tables.fin_user_profile.search()
            data2 = app_tables.fin_guarantor_details.search()
            cus_id_list2 = [i['customer_id'] for i in data2]
            id_list = [i['email_user'] for i in data]
            cus_id_list = [i['customer_id'] for i in data]
            user_email = anvil.server.call('another_method')
            if user_email in id_list:
                index = id_list.index(user_email)
                if cus_id_list[index] in cus_id_list2:
                    index2 = cus_id_list2.index(cus_id_list[index])
                    data2[index2]['guarantor_name'] = person_name
                    data2[index2]['guarantor_person_relation'] = relation_name
                    data2[index2]['guarantor_mobile_no'] = int(person_ph_no)
                    data2[index2]['guarantor_profession'] = person_proffession
                    data2[index2]['guarantor_date_of_births'] = person_dob

                else:
                    print('customer_id is not valid')

            else:
                print('email not valid')
        elif self.ids.relation_name.text == "Others":

            relation_name = self.ids.relation_name.text
            person_name = self.person_name.text
            person_dob = self.person_dob.text
            person_ph_no = self.person_ph_no.text
            person_proffession = self.person_profession.text

            data = app_tables.fin_user_profile.search()
            data2 = app_tables.fin_guarantor_details.search()
            cus_id_list2 = [i['customer_id'] for i in data2]
            id_list = [i['email_user'] for i in data]
            cus_id_list = [i['customer_id'] for i in data]
            user_email = anvil.server.call('another_method')
            if user_email in id_list:
                index = id_list.index(user_email)
                if cus_id_list[index] in cus_id_list2:
                    index2 = cus_id_list2.index(cus_id_list[index])
                    data2[index2]['guarantor_name'] = person_name
                    data2[index2]['guarantor_person_relation'] = relation_name
                    data2[index2]['guarantor_mobile_no'] = int(person_ph_no)
                    data2[index2]['guarantor_profession'] = person_proffession
                    data2[index2]['guarantor_date_of_births'] = person_dob

                else:
                    print('customer_id is not valid')

            else:
                print('email not valid')

        if marital_status_id == 'Un-Married' or marital_status_id == 'Not Married':
            sm = self.manager
            borrower_screen = BorrowerScreen20(name='BorrowerScreen20')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen20'

        elif marital_status_id == 'Married':
            sm = self.manager
            borrower_screen = BorrowerScreen20(name='BorrowerScreen20')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen20'

        elif marital_status_id == 'Divorced':
            sm = self.manager
            borrower_screen = BorrowerScreen20(name='BorrowerScreen20')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen20'
        elif marital_status_id == 'Other':
            sm = self.manager
            borrower_screen = BorrowerScreen20(name='BorrowerScreen20')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen20'
        else:
            sm = self.manager
            borrower_screen = BorrowerScreen20(name='BorrowerScreen20')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen20'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen6'


class BorrowerScreen16(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_date_textfield.input_type = 'number'

    def on_spouse_mobile_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_mobile.input_type = 'number'

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

    def add_data(self, spouse_name, spouse_date_textfield, spouse_mobile):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(spouse_name, spouse_date_textfield, spouse_mobile
                                                         , modal_view), 2)

    def perform_data_addition_action(self, spouse_name, spouse_date_textfield, spouse_mobile,
                                     modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([spouse_name, spouse_date_textfield, spouse_mobile]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if len(spouse_name) < 3:
            self.show_validation_error("Please Enter Spouse Valid Name.")
            return
        try:
            dob = datetime.strptime(spouse_date_textfield, "%Y-%m-%d").date()  # Convert to date object
            today = datetime.now().date()
            if dob > today:
                self.show_validation_error("Spouse's marriage date must be less than today's date.")
                return
        except ValueError:
            self.show_validation_error("Please enter a valid Marriage Date in format YYYY-MM-DD")
            return

        if len(spouse_mobile) != 10 or not spouse_mobile.isdigit():
            self.show_validation_error("Please Enter Spouse Valid Mobile Number.")
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET spouse_name = ?,spouse_date_textfield = ?, spouse_mobile = ? WHERE customer_id = ?",
                (spouse_name, spouse_date_textfield, spouse_mobile, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_name'] = spouse_name
                data2[index2]['guarantor_mobile_no'] = int(spouse_mobile)
                data2[index2]['guarantor_marriage_dates'] = str(spouse_date_textfield)
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = BorrowerScreen17(name='BorrowerScreen17')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen17'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen17(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_spouse_profession.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['spouse_profession'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.spouse_profession.values = ['Select Spouse Profession Type'] + self.unique_list
        else:
            self.ids.spouse_profession.values = ['Select Spouse Profession Type']

    def on_spouse_annual_salary_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_annual_salary.input_type = 'number'

    def on_spouse_office_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_office_no.input_type = 'number'

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

    def add_data(self, spouse_company_name, spouse_company_address, spouse_annual_salary):
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
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(spouse_company_name, spouse_company_address,
                                                                         spouse_annual_salary,
                                                                         modal_view), 2)

    def perform_data_addition_action(self, spouse_company_name, spouse_company_address, spouse_annual_salary
                                     , modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([spouse_company_address]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET spouse_company_name = ?,spouse_company_address = ?, spouse_annual_salary = ? WHERE customer_id = ?",
                (spouse_company_name, spouse_company_address, spouse_annual_salary,
                 row_id_list[log_index]))
            conn.commit()
        else:
            print('User is not logged in.')

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_company_name'] = spouse_company_name
                data2[index2]['guarantor_annual_earning'] = spouse_annual_salary
                data2[index2]['guarantor_profession'] = spouse_company_address
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = BorrowerScreen20(name='BorrowerScreen20')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen20'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen16'


class BorrowerScreen18(Screen):
    all_fields_filled = BooleanProperty(True)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_borrower_account_type.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['borrower_account_type'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.account_type_id.values = self.unique_list
        else:
            self.ids.account_type_id.values = ['Select Account Type']

        self.check = None

    def validate_zip_code(self, zip_code):
        zip_code_text = zip_code.text

        # Check if the input contains only numeric characters
        if not zip_code_text.isdigit():
            zip_code.helper_text = "Should contain only numbers"
            zip_code.error = True
        else:
            zip_code.helper_text = ""
            zip_code.error = False

    def validate_zip_code_text(self, zip_code):
        zip_code_text = zip_code.text

        # Check if the input contains only alphabetic characters
        if not zip_code_text.isalpha():
            zip_code.helper_text = "Should contain only alphabetic characters"
            zip_code.error = True
        else:
            zip_code.helper_text = ""
            zip_code.error = False

    def validate_zip_code_numchar(self, zip_code):
        zip_code_text = zip_code.text

        # Check if the input contains both alphabetic characters and numeric digits
        has_alpha = any(char.isalpha() for char in zip_code_text)
        has_digit = any(char.isdigit() for char in zip_code_text)

        if has_alpha and has_digit:
            zip_code.helper_text = ""
            zip_code.error = False
        else:
            zip_code.helper_text = "Should Contain characters and numbers."
            zip_code.error = True

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen20'

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.check = True
            self.all_fields_filled = not all([
                self.ids.ifsc_code.text,
                self.ids.branch_name.text,
                self.ids.account_holder_name.text,
                self.ids.account_type_id.text,
                self.ids.account_number.text,
                self.ids.bank_name.text
            ])
        else:
            self.check = False

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

    def go_to_borrower_dashboard(self, bank_id, branch_name,account_holder_name, account_type, account_number, bank_name):
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
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(bank_id, branch_name,account_holder_name, account_type, account_number, bank_name, modal_view), 2)

    def perform_data_addition_action(self, bank_id, branch_name,account_holder_name, account_type, account_number, bank_name, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([bank_id, branch_name, account_holder_name, account_type, account_number, bank_name]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if not re.match(r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{3,}$', bank_id):
            self.show_validation_error(
                "Bank ID should contain at least 3 characters, including both numbers and letters.")
            return
        if not branch_name.isalpha() or len(branch_name) < 3:
            self.show_validation_error('Enter a valid branch name')
            return
        if not re.match(r'^[a-zA-Z]{3,}$', account_holder_name) or not account_holder_name[0].isupper():
            self.show_validation_error('Enter a valid account name and first letter should be capital')
            return
        if account_type not in account_type == 'Select Account Type':
            self.show_validation_error('Enter a valid account type')
            return
        if len(account_number) < 3 or not account_number.isdigit():
            self.show_validation_error('Enter a valid account number')
            return
        if not re.match(r'^[a-zA-Z]{3,}$', bank_name):
            self.show_validation_error('Enter a valid bank name')
            return
        if self.check != True:
            self.show_validation_error('Select The Terms and Conditions')
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        b = 'borrower'
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET bank_id = ?, branch_name = ?, user_type = ?  WHERE customer_id = ?",
                (bank_id, branch_name, b, row_id_list[log_index]))
            conn.commit()
        else:
            print('User is not logged in.')

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        user_id_list = [i['customer_id'] for i in data]

        manage_credit_limit = app_tables.fin_manage_credit_limit.search()
        credit_limit = [i['credit_limit'] for i in manage_credit_limit]

        users = app_tables.users.search()
        users_email_list = [i['email'] for i in users]

        wallet = app_tables.fin_wallet.search()
        wallet_cus_id = [i['customer_id'] for i in wallet]

        user_index = 0
        if user_email in users_email_list:
            user_index = users_email_list.index(user_email)
        else:
            print("email id not found")

        print(len(credit_limit) >= 1)

        if len(credit_limit) >= 1:
            limit = credit_limit[0]
        else:
            limit = 0
        print(credit_limit)

        index = 0
        ascend = 0
        wallet_index = 0
        if user_email in id_list:
            index = id_list.index(user_email)
            if user_id_list[index] in wallet_cus_id:
                wallet_index = wallet_cus_id.index(user_id_list[index])
            else:
                print("wallet id not found")
            try:
                ascend = anvil.server.call('final_points_update_bessem_table', user_id_list[index])
            except Exception as e:
                print(f"An error occurred: {e}")
            data[index]['bank_id'] = bank_id
            data[index]['account_bank_branch'] = branch_name
            data[index]['account_name'] = account_holder_name
            data[index]['account_type'] = account_type
            data[index]['account_number'] = account_number
            data[index]['bank_name'] = bank_name
            data[index]['usertype'] = b
            data[index]['registration_approve'] = True
            data[index]['last_confirm'] = True
            data[index]['profile_status'] = True
            data[index]['mobile_check'] = True
            data[index]['ascend_value'] = float(ascend)

            existing_record = app_tables.fin_borrower.get(email_id=user_email)

            # If the record does not exist, add a new row
            if not existing_record:
                app_tables.fin_borrower.add_row(
                    email_id=user_email,
                    user_name=data[index]['full_name'],
                    ascend_score=float(ascend),
                    customer_id=user_id_list[index],
                    bank_acc_details=data[index]['account_number'],
                    credit_limit=limit,
                    borrower_since=users[user_index]['signed_up'].date(),
                    wallet_id=wallet[wallet_index]['wallet_id']
                )
            else:
                # Optionally, update the existing record if needed
                # existing_record.update(user_name=data[index]['full_name'], ...)
                print(f"Record for {user_email} already exists. Skipping insertion.")
        else:
            print('email not valid')
        print(user_id_list[index])
        print(ascend)
        self.save_user_info(user_email, b)

        sm = self.manager
        borrower_screen = DashboardScreen(name='DashboardScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'DashboardScreen'

    def save_user_info(self, email, b):
        user_data = {
            'email': email,
            'logged_status': True,
            'user_type': b
        }

        # Check if the emails.json file exists and load data, or initialize as an empty dict
        if os.path.exists("emails.json"):
            with open("emails.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}

        data[email] = user_data

        # Write back the updated data to emails.json
        with open("emails.json", "w") as file:
            json.dump(data, file, indent=4)

    def show_terms_dialog(self):
        dialog = MDDialog(
            title="Terms and Conditions",
            text="Agreements, Privacy Policy and Applicant should accept following:Please note that any information concealed (as what we ask for), would be construed as illegitimate action on your part and an intentional attempt to hide material information which if found in future, would attract necessary action (s) at your sole cost. Hence, request to be truthful to your best knowledge while sharing your details)",
            size_hint=(0.8, 0.5),
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda *args: dialog.dismiss()
                )
            ]
        )
        dialog.open()

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


class BorrowerScreen20(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.first = None
        self.second = None
        self.third = None
        self.fourth = None

    def on_yes_button_pressed1(self):
        self.ids.no1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.no1.text_color = (1, 1, 1, 1)
        self.ids.yes1.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.yes1.text_color = (1, 1, 1, 1)
        self.first = "Yes"

    def on_no_button_pressed1(self):
        self.ids.no1.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.no1.text_color = (1, 1, 1, 1)
        self.ids.yes1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.yes1.text_color = (1, 1, 1, 1)
        self.first = "No"

    def on_yes_button_pressed2(self):
        self.ids.no2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.no2.text_color = (1, 1, 1, 1)
        self.ids.yes2.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.yes2.text_color = (1, 1, 1, 1)
        self.second = "Yes"

    def on_no_button_pressed2(self):
        self.ids.no2.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.no2.text_color = (1, 1, 1, 1)
        self.ids.yes2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.yes2.text_color = (1, 1, 1, 1)
        self.second = "No"

    def on_yes_button_pressed3(self):
        self.ids.no3.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.no3.text_color = (1, 1, 1, 1)
        self.ids.yes3.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.yes3.text_color = (1, 1, 1, 1)
        self.third = "Yes"

    def on_no_button_pressed3(self):
        self.ids.no3.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.no3.text_color = (1, 1, 1, 1)
        self.ids.yes3.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.yes3.text_color = (1, 1, 1, 1)
        self.third = "No"

    def on_yes_button_pressed4(self):
        self.ids.no4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.no4.text_color = (1, 1, 1, 1)
        self.ids.yes4.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.yes4.text_color = (1, 1, 1, 1)
        self.fourth = "Yes"

    def on_no_button_pressed4(self):
        self.ids.no4.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.no4.text_color = (1, 1, 1, 1)
        self.ids.yes4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.yes4.text_color = (1, 1, 1, 1)
        self.fourth = "No"

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

    def add_data(self):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(modal_view), 2)

    def perform_data_addition_action(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if self.first == None or self.second == None or self.third == None or self.fourth == None:
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['home_loan'] = self.first
            data[index]['other_loan'] = self.second
            data[index]['credit_card_loans'] = self.third
            data[index]['vehicle_loan'] = self.fourth
        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = BorrowerScreen18(name='BorrowerScreen18')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen18'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen21(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = None

    def on_yes_button_pressed1(self):
        self.ids.id1.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id3.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id3.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Father"

    def on_yes_button_pressed2(self):
        self.ids.id2.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id3.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id3.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Mother"

    def on_yes_button_pressed3(self):
        self.ids.id3.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id3.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Spouse"

    def on_yes_button_pressed4(self):
        self.ids.id4.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id3.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id3.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.type = "Other"

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

    def add_data(self):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(modal_view), 2)

    def perform_data_addition_action(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if self.type == None:
            # Display a validation error dialog
            self.show_validation_error("Please Select Valid Type.")
            return  # Prevent further execution if any field is missing

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['another_person'] = self.type
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        if self.type == 'Father':
            sm = self.manager
            borrower_screen = BorrowerScreen5(name='BorrowerScreen5')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'BorrowerScreen5'
        elif self.type == 'Mother':
            sm = self.manager
            borrower_screen = BorrowerScreen6(name='BorrowerScreen6')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'BorrowerScreen6'
        elif self.type == "Spouse":
            sm = self.manager
            borrower_screen = BorrowerScreen16(name='BorrowerScreen16')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'BorrowerScreen16'
        elif self.type == 'Other':
            sm = self.manager
            borrower_screen = BorrowerScreen23(name='BorrowerScreen23')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'BorrowerScreen23'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen22(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = None

    def on_yes_button_pressed1(self):
        self.ids.id1.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Father"

    def on_yes_button_pressed2(self):
        self.ids.id2.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Mother"

    def on_yes_button_pressed4(self):
        self.ids.id4.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.type = "Other"

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

    def add_data(self):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(modal_view), 2)

    def perform_data_addition_action(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if self.type == None:
            # Display a validation error dialog
            self.show_validation_error("Please Select Valid Type.")
            return  # Prevent further execution if any field is missing

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['another_person'] = self.type
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        if self.type == 'Father':
            sm = self.manager
            borrower_screen = BorrowerScreen5(name='BorrowerScreen5')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'BorrowerScreen5'
        elif self.type == 'Mother':
            sm = self.manager
            borrower_screen = BorrowerScreen6(name='BorrowerScreen6')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'BorrowerScreen6'
        elif self.type == 'Other':
            sm = self.manager
            borrower_screen = BorrowerScreen23(name='BorrowerScreen23')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'BorrowerScreen23'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen23(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.person_dob.input_type = 'number'

    def on_mother_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.person_ph_no.input_type = 'number'

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

    def add_data(self, relation_name, person_name, person_dob, person_ph_no, person_proffession):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(relation_name, person_name, person_dob, person_ph_no,
                                                         person_proffession,
                                                         modal_view), 2)

    def perform_data_addition_action(self, relation_name, person_name, person_dob, person_ph_no, person_proffession,
                                     modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Check for missing fields
        if not all([relation_name, person_name, person_dob, person_ph_no, person_proffession]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing

        if len(relation_name) < 3:
            self.show_validation_error('Enter a valid relation name')
            return
        if len(person_name) < 3:
            self.show_validation_error('Enter a valid person name')
            return
        try:
            dob = datetime.strptime(person_dob, "%Y-%m-%d")
            today = datetime.now()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 18:
                self.show_validation_error("Enter a Valid Date of Birth Age must be Greater Than 18")
                return

        except ValueError:
            self.show_validation_error("Please enter a valid date of birth in the format YYYY-MM-DD")
            return
        if not person_ph_no.isdigit() or len(person_ph_no) != 10:
            self.show_validation_error("Please Enter Valid Person Number.")
            return
        if len(person_name) < 3:
            self.show_validation_error('Enter a valid person profession')
            return

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_name'] = person_name
                data2[index2]['guarantor_person_relation'] = relation_name
                data2[index2]['guarantor_mobile_no'] = int(person_ph_no)
                data2[index2]['guarantor_profession'] = person_proffession
                data2[index2]['guarantor_date_of_births'] = person_dob
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = BorrowerScreen20(name='BorrowerScreen20')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen20'

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen24(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_duration_at_address.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['duration_at_address'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.spinner_id.values = ['Select How long you are staying'] + self.unique_list
        else:
            self.ids.spinner_id.values = ['Select How long you are staying']

        spinner_data1 = app_tables.fin_present_address.search()
        data_list1 = []
        for i in spinner_data1:
            data_list1.append(i['present_address'])
        self.unique_list1 = []
        for i in data_list1:
            if i not in self.unique_list1:
                self.unique_list1.append(i)
        print(self.unique_list1)
        if len(self.unique_list1) >= 1:
            self.ids.spinner_id2.values = ['Select Present Address'] + self.unique_list1
        else:
            self.ids.spinner_id2.values = ['Select Present Address']

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

    def add_data(self, street, spinner_id, spinner_id2, street_address2,city, zip_code, state, country):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action1(street, spinner_id, spinner_id2, street_address2,city, zip_code, state, country,
                                                          modal_view),
            2)

    def perform_data_addition_action1(self, street, spinner_id, spinner_id2, street_address2, city, zip_code, state, country,modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        validation_errors = []
        # Check for missing fields
        if not street:
            validation_errors.append((self.ids.street_address1, "Please fill the * mandatory details."))
        if not street_address2:
            validation_errors.append((self.ids.street_address2, "Please fill the * mandatory details."))
        if not spinner_id:
            validation_errors.append((self.ids.spinner_id, "Please fill the * mandatory details."))
        if not spinner_id2:
            validation_errors.append((self.ids.spinner_id2, "Please fill the * mandatory details."))
        if not city:
            validation_errors.append((self.ids.city, "Please fill the * mandatory details."))
        if not zip_code:
            validation_errors.append((self.ids.zip_code, "Please fill the * mandatory details."))
        if not state:
            validation_errors.append((self.ids.state, "Please fill the * mandatory details."))
        if not country:
            validation_errors.append((self.ids.country, "Please fill the * mandatory details."))
        if validation_errors:
            self.show_validation_error(validation_errors)
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET street_name = ?,city_name = ?, zip_code = ?, state_name = ?, country_name = ? WHERE customer_id = ?",
                (street, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['street_adress_1'] = street
            data[index]['street_address_2']=street_address2
            data[index]['duration_at_address'] = spinner_id
            data[index]['present_address'] = spinner_id2
            data[index]['city'] = city
            data[index]['pincode'] = zip_code
            data[index]['state'] = state
            data[index]['country'] = country
        else:
            print('no email found')
        # self.manager.current = 'BorrowerScreen2'
        sm = self.manager
        borrower_screen = BorrowerScreen3(name='BorrowerScreen3')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen3'

    def on_mobile_number_touch_down(self):
    ## Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.zip_code.input_type = 'number'

    def show_validation_errors(self, validation_errors):
        for widget, error_message in validation_errors:
            widget.error = True
            widget.helper_text_color = (1, 0, 0, 1)
            widget.helper_text = error_message
            widget.helper_text_mode = "on_error"
            if isinstance(widget, MDTextField):
                widget.line_color_normal = (1, 0, 0, 1)  # Red color for the line when not focused
                widget.line_color_focus = (1, 0, 0, 1)
            if isinstance(widget, MDCheckbox):
                widget.theme_text_color = 'Error'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen'


class BorrowerScreen25(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_self_employment.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['self_employment'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.spinner_id.values = ['Select Self Employment type'] + self.unique_list
        else:
            self.ids.spinner_id.values = ['Select Self Employment type']

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

    def add_data(self, spinner_id):
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
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(spinner_id, modal_view), 2)

    def perform_data_addition_action(self, spinner_id, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        if not all([spinner_id]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if spinner_id not in self.unique_list:
            self.show_validation_error('Select valid Self Employment type')
            return

        if spinner_id == 'Farmer':
            sm = self.manager
            borrower_screen = BorrowerScreen26(name='BorrowerScreen26')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen26'

        elif spinner_id == 'Business' or spinner_id == 'Self employment':
            sm = self.manager
            borrower_screen = BorrowerScreen9(name='BorrowerScreen9')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen9'

        else:
            sm = self.manager
            borrower_screen = BorrowerScreen15(name='BorrowerScreen15')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen15'
        print(spinner_id)
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []

        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET proficient_type = ? WHERE customer_id = ?",
                (spinner_id, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['self_employment'] = spinner_id
        else:
            print('no email found')

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

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen7'


class BorrowerScreen26(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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

    def add_data(self, land, acers, corp, income):
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
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(land, acers, corp, income, modal_view), 2)

    def perform_data_addition_action4(self, land, acers, corp, income, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        if not all([land, acers, corp, income]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing

        if not acers.isdigit():
            self.show_validation_error('Enter a valid No Of Acers')
            return
        if len(corp) < 3:
            self.show_validation_error('Enter a valid Corp Name')
            return
        if len(income) < 3 or not income.isdigit():
            self.show_validation_error('Enter a valid Yearly Income')
            return

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['land_type'] = land
            data[index]['crop_name'] = corp
            data[index]['total_acres'] = int(acers)
            data[index]['farmer_earnings'] = income
        else:
            print('no email found')

        sm = self.manager
        borrower_screen = BorrowerScreen15(name='BorrowerScreen15')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen15'

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

    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.income.input_type = 'number'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen25'


class MyScreenManager(ScreenManager):
    pass

from kivy.uix.spinner import SpinnerOption

class CustomSpinnerOption(SpinnerOption):
    pass