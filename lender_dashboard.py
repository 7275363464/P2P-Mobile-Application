import json

from anvil.tables import app_tables
from kivy.factory import Factory
from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
import sqlite3
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from lender_lost_opportunities import LostOpportunitiesScreen
from lender_view_transaction_history import TransactionLH
from lender_view_loans import ViewLoansScreen
from lender_view_loans_request import ViewLoansRequest
from lender_view_extension_request import NewExtension
from lender_foreclosure_request import DashboardScreenLF
from lender_today_due import TodayDuesTD
from kivy.uix.modalview import ModalView
from kivymd.uix.spinner import MDSpinner
from kivy.clock import Clock
from lender_view_loans_request import ViewLoansProfileScreen
from kivy.animation import Animation
from kivymd.uix.label import MDLabel

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)

# anvil.server.connect("server_VRGEXX5AO24374UMBBQ24XN6-ZAWBX57M6ZDN6TBV")

user_helpers1 = """
<WindowManager>:
    LenderDashboard:
    ViewProfileScreen:
    ViewEditScreen:

<LenderDashboard>
    MDBottomNavigation:
        panel_color: 0.043, 0.145, 0.278, 1
        selected_color_background: "white"
        text_color_active: "white"
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Home'
            icon: 'home'
            md_bg_color: "white"
            MDScreen:

                MDNavigationLayout:

                    MDScreenManager:

                        MDScreen:
                            MDBoxLayout:
                                orientation: 'vertical'

                                MDTopAppBar:
                                    title: "Lender Dashboard"
                                    elevation: 0
                                    pos_hint: {"top": 1}
                                    md_bg_color: 0.043, 0.145, 0.278, 1
                                    specific_text_color: "#ffffff"
                                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]


                                ScrollView:
                                    MDBoxLayout:
                                        orientation: 'vertical'
                                        padding: "10dp", "5dp", "10dp", "0dp"
                                        size_hint_y: None
                                        height: dp(950)
                                        spacing: dp(20)
                                        ThreeLineAvatarListItem:
                                            id: details
                                            text: "Welcome Sai Mamidala"
                                            secondary_text: "Joined Date: 22-03-12"
                                            tertiary_text: "Membership_type: Elite"
                                            on_release: root.profile()
                                            ImageLeftWidget:
                                                source: "icon1.jpg"
                                        GridLayout:
                                            cols: 2
                                            padding: dp(10)
                                            spacing: dp(10)
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: self.minimum_height
                                                md_bg_color: "#ABBAE3"
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 0.1
                                                        rectangle: (self.x, self.y, self.width, self.height)
                                                MDLabel:
                                                    id: commitment
                                                    text: "Rs. 12903838"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    theme_text_color: "Custom"
                                                    text_color: "white"
                                                    font_name: "Roboto-Bold"
                                                    font_size: dp(20)

                                                MDLabel:
                                                    text: "My Commitments"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    font_name: "Roboto-Bold"
                                                MDFlatButton:
                                                    text: "view all"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    pos_hint: {'center_x': 0.5}
                                                    theme_text_color: "Custom"
                                                    text_color: "white"
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: self.minimum_height
                                                md_bg_color: "#ABBAE3"
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 0.1
                                                        rectangle: (self.x, self.y, self.width, self.height)
                                                MDLabel:
                                                    id: total_amount
                                                    text: "Rs. 50,000"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    theme_text_color: "Custom"
                                                    text_color: "white"
                                                    font_name: "Roboto-Bold"
                                                    font_size: dp(20)

                                                MDLabel:
                                                    text: "Opening Balance"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    font_name: "Roboto-Bold"
                                                MDFlatButton:
                                                    text: "view all"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    pos_hint: {'center_x': 0.5}
                                                    theme_text_color: "Custom"
                                                    text_color: "white"
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: self.minimum_height
                                                md_bg_color: "#ABBAE3"
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 0.1
                                                        rectangle: (self.x, self.y, self.width, self.height)
                                                MDLabel:
                                                    text: "Rs. 20,000"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    theme_text_color: "Custom"
                                                    text_color: "white"
                                                    font_name: "Roboto-Bold"
                                                    font_size: dp(20)

                                                MDLabel:
                                                    text: "My Returns/ Commission"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    font_name: "Roboto-Bold"
                                                MDFlatButton:
                                                    text: "view all"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    pos_hint: {'center_x': 0.5}
                                                    theme_text_color: "Custom"
                                                    text_color: "white" 
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: self.minimum_height
                                                md_bg_color: "#ABBAE3"
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 0.1
                                                        rectangle: (self.x, self.y, self.width, self.height)
                                                MDLabel:
                                                    id: loan
                                                    text: "3"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    theme_text_color: "Custom"
                                                    text_color: "white"
                                                    font_name: "Roboto-Bold"
                                                    font_size: dp(20)

                                                MDLabel:
                                                    text: "New Loan Requests"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    font_name: "Roboto-Bold"
                                                MDFlatButton:
                                                    text: "view all"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    pos_hint: {'center_x': 0.5}
                                                    theme_text_color: "Custom"
                                                    text_color: "white"

                                        MDLabel:
                                            text: ""
                                        MDLabel:
                                            text: ""
                                        MDLabel:
                                            text: ""
                                            size_hint_y: None
                                            height: dp(30)
                                        Widget:
                                            size_hint_y: None
                                            height: 5
                                            canvas:
                                                Color:
                                                    rgba: 0, 0, 0, 1  # Change color if needed
                                                Line:
                                                    points: self.x, self.y, self.x + self.width, self.y
                                        GridLayout:
                                            cols: 3
                                            spacing: dp(10)
                                            size_hint_y: None
                                            height: dp(50)
                                            Image:
                                                source: "icon1.jpg"
                                                size_hint: None, None
                                                size: "60dp", "60dp"
                                            
                                            MDLabel:
                                                id: borrower_name
                                                text: "Mamidala sai"
                                                font_family: "Arial"
                                                halign: "center"
                                            MDLabel:
                                                id: age
                                                text: "23years"
                                                font_family: "Arial"
                                                font_size: dp(10)
                                            
                                        GridLayout:
                                            cols: 3
                                            spacing: dp(10)
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                height: self.minimum_height
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 1
                                                        rectangle: (self.x, self.y, self.width, self.height)

                                                MDIcon:
                                                    icon: "speedometer"
                                                    pos_hint: {'center_x': 0.5}
                                                MDBoxLayout:
                                                    orientation: 'vertical'
                                                    spacing: dp(30)
                                                    padding: dp(20)
                                                    MDLabel:
                                                        text: "Ascend Score"
                                                        font_size: dp(12)
                                                        halign: 'center'
                                                    MDLabel:
                                                        id: score
                                                        text: "170"
                                                        font_size:dp(16)
                                                        halign: 'center'
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                height: self.minimum_height
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 1
                                                        rectangle: (self.x, self.y, self.width, self.height)

                                                MDIcon:
                                                    icon: "account-tie"
                                                    pos_hint: {'center_x': 0.5}
                                                MDBoxLayout:
                                                    orientation: 'vertical'
                                                    spacing: dp(30)
                                                    padding:dp(20)
                                                    MDLabel:
                                                        text: "Employment Type"
                                                        font_size: dp(12)
                                                        halign: 'center'
                                                    MDLabel:
                                                        id: employment
                                                        text: "Full Time"
                                                        font_size:dp(16)
                                                        halign: 'center'
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: dp(100)
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 1
                                                        rectangle: (self.x, self.y, self.width, self.height)
                                                MDIcon:
                                                    icon: "package-variant-plus"
                                                    pos_hint: {'center_x': 0.5}
                                                MDBoxLayout:
                                                    orientation: 'vertical'
                                                    spacing: dp(30)
                                                    padding:dp(20)
                                                    MDLabel:
                                                        text: "Product Name"
                                                        font_size: dp(12)
                                                        halign: 'center'
                                                    MDLabel:
                                                        id: product_name
                                                        text: "TVS"
                                                        font_size:dp(16)
                                                        halign: 'center'
                                                        
                                        MDLabel:
                                            text: ''
                                            size_hint_y: None
                                            height: dp(30)

                                        GridLayout:
                                            cols: 2
                                            padding: dp(10)
                                            spacing: dp(10)
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: dp(70)
                                                
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 2
                                                        rectangle: (self.x, self.y, self.width, self.height)

                                                GridLayout:
                                                    cols: 2
                                                    spacing: dp(10)
                                                    padding: dp(5)

                                                    Image:
                                                        source: "icon1.jpg"
                                                        size_hint: None, None
                                                        size: "60dp", "60dp"
                                                    MDBoxLayout:
                                                        orientation: 'vertical'
                                                        MDLabel:
                                                            text: "Loan Amount"
                                                            font_size: dp(12)
                                                        MDLabel:
                                                            id: amount
                                                            text: "Rs. 1,50,000"
                                                            font_size:dp(15)

                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: dp(70)
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 2
                                                        rectangle: (self.x, self.y, self.width, self.height)

                                                GridLayout:
                                                    cols: 2
                                                    spacing: dp(10)
                                                    padding: dp(5)

                                                    Image:
                                                        source: "icon2.jpg"
                                                        size_hint: None, None
                                                        size: "60dp", "60dp"
                                                    MDBoxLayout:
                                                        orientation: 'vertical'
                                                        MDLabel:
                                                            text: "Left Amount"
                                                            font_size: dp(12)
                                                        MDLabel:
                                                            id:left
                                                            text: "Rs. 1,50,000"
                                                            font_size:dp(15)
                                                            
                                        MDLabel:
                                            text: ""
                                            size_hint_y: None
                                            height: dp(2)

                                        GridLayout:
                                            cols: 2
                                            padding: dp(10)
                                            spacing: dp(10)
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: dp(70)
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 2
                                                        rectangle: (self.x, self.y, self.width, self.height)

                                                GridLayout:
                                                    cols: 2
                                                    spacing: dp(10)
                                                    padding: dp(5)

                                                    Image:
                                                        source: "icon3.png"
                                                        size_hint: None, None
                                                        size: "50dp", "50dp"
                                                    MDBoxLayout:
                                                        orientation: 'vertical'
                                                        MDLabel:
                                                            text: "Interest Rate"
                                                            font_size: dp(12)
                                                        MDLabel:
                                                            id: interest
                                                            text: "22%"
                                                            font_size:dp(15)

                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: dp(70)
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 2
                                                        rectangle: (self.x, self.y, self.width, self.height)

                                                GridLayout:
                                                    cols: 2
                                                    spacing: dp(20)
                                                    padding: dp(5)

                                                    Image:
                                                        source: "icon4.png"
                                                        size_hint: None, None
                                                        size: "30dp", "60dp"
                                                    MDBoxLayout:
                                                        orientation: 'vertical'
                                                        MDLabel:
                                                            text: "Tenure"
                                                            font_size: dp(12)
                                                        MDLabel:
                                                            id: tenure
                                                            text: "24 Months"
                                                            font_size:dp(15)
                                        MDLabel:
                                            text: ""
                                            size_hint_y: None
                                            height: dp(10)
                                        GridLayout:
                                            cols: 2
                                            spacing: dp(20)
                                            padding: dp(20)
                                            pos_hint: {'center_x': 0.55}
                                            MDFillRoundFlatIconButton:
                                                text: "Invest Now"
                                                icon: "currency-rupee"
                                                text_color: "white"
                                                font_name: "Roboto-Bold"
                                                md_bg_color: 0, 0, 0, 1
                                                on_release: root.invest()
                                            MDFillRoundFlatIconButton:
                                                text: "View More"
                                                icon: "clipboard-text-outline"
                                                font_name: "Roboto-Bold"
                                                text_color: "white"
                                                md_bg_color: 0, 0, 0, 1
                                                on_release: root.view_loan_request()
                                            
                                        Widget:
                                            size_hint_y: None
                                            height: 5
                                            canvas:
                                                Color:
                                                    rgba: 0, 0, 0, 1  # Change color if needed
                                                Line:
                                                    points: self.x, self.y, self.x + self.width, self.y
                                        
                                        
                                        MDLabel:
                                            text: ""
                                        MDLabel:
                                            text: ""
                    MDNavigationDrawer:
                        id: nav_drawer
                        radius: (0, 16, 16, 0)

                        MDNavigationDrawerMenu:

                            MDNavigationDrawerHeader:
                                id: name
                                title: "Welcome Back"
                                title_color: "#4a4939"
                                text: "Sai Mamidala"
                                spacing: "4dp"
                                padding: "12dp", 0, 0, "56dp"

                            MDNavigationDrawerItem
                                icon: "calendar-check-outline"
                                text: "Today's Dues"
                                on_release: root.lender_today_due()
                            MDNavigationDrawerDivider:

                            MDNavigationDrawerItem
                                icon: "bank"
                                text: "View Loan"
                                on_release: root.view_loanscreen()
                            MDNavigationDrawerDivider:

                            MDNavigationDrawerItem
                                icon: "file-document"
                                text: "View Loan Requests"
                                on_release: root.view_loan_request()
                            MDNavigationDrawerDivider:

                            MDNavigationDrawerItem
                                icon: "plus-circle"
                                text: "View Loans Extensions"
                                on_release: root.newloan_extension()
                            MDNavigationDrawerDivider:

                            MDNavigationDrawerItem
                                icon: "home-minus"
                                text: "View Loans Foreclosure"
                                on_release: root.view_loan_foreclose()
                            MDNavigationDrawerDivider:

                            MDNavigationDrawerItem
                                icon: "eye-outline"
                                text: "View Lost Opportunities"
                                on_release: root.view_lost_opportunities()
                            MDNavigationDrawerDivider:

                            MDNavigationDrawerItem
                                icon: "history"
                                text: "View Transactions History"
                                on_release: root.view_transaction_history()
                            MDNavigationDrawerDivider:
                            MDNavigationDrawerItem
                                icon: "logout"
                                text: "Logout"
                                on_release: root.go_to_main_screen()
                            MDNavigationDrawerDivider:

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Wallet'
            icon: 'wallet'

            MDLabel:
                text: 'Wallet'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Loans'
            icon: 'cash'

            MDLabel:
                text: 'Loans'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Account'
            icon: 'account'

            MDLabel:
                text: 'Account'
                halign: 'center'       
<ViewProfileScreen>
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
<ViewEditScreen>                            
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
                                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                                    Line:
                                        width: 0.7  # Border width
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

conn = sqlite3.connect('fin_user.db')
cursor = conn.cursor()


class LenderDashboard(Screen):
    Builder.load_string(user_helpers1)

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)


        log_email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search()
        print(log_email)

        email_user = []
        name_list = []
        investment = []
        user_age = []
        p_customer_id = []
        ascend_score = []
        emp_type = []

        for i in profile:
            email_user.append(i['email_user'])
            name_list.append(i['full_name'])
            investment.append(i['investment'])
            user_age.append(i['user_age'])
            p_customer_id.append(i['customer_id'])
            ascend_score.append(i['bessem_value'])
            emp_type.append(i['employment_type'])

        # Check if 'logged' is in the status list
        log_index = 0
        if log_email in email_user:
            log_index = email_user.index(log_email)
            self.ids.details.text = "Welcome " + name_list[log_index]
            self.ids.name.text = name_list[log_index]
        else:
            # Handle the case when 'logged' is not in the status list
            self.ids.details.text = "User welcome to P2P"

        data = app_tables.fin_loan_details.search()

        loan_id = []
        loan_status = []
        borrower_name = []
        product_name = []
        customer_id = []
        loan_amount = []
        left_amount = []
        interest_rate = []
        tenure = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            loan_status.append(i['loan_updated_status'])
            borrower_name.append(i['borrower_full_name'])
            product_name.append(i['product_name'])
            customer_id.append(i['borrower_customer_id'])
            loan_amount.append(i['loan_amount'])
            left_amount.append(i['remaining_amount'])
            interest_rate.append(i['interest_rate'])
            tenure.append(i['tenure'])

        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[c] == 'under process' or loan_status[c] == 'approved':
                index_list.append(c)

        self.ids.loan.text = str(len(index_list))


        if len(loan_id) < 1:
            self.ids.borrower_name.text = ""
            self.ids.age.text = ''
            self.ids.product_name = ''
            self.ids.amount.text = ''
            self.ids.interest.text = ''
            self.ids.tenure.text = ''
            self.ids.age.text = ''
            self.ids.employment.text = ''
            self.ids.score.text = ''
            self.ids.left.text = ''

        else:
            a = 0
            b = -1
            for i in loan_status:
                b += 1
                if i == 'under process':
                    a = b
            print(a)
            self.ids.borrower_name.text = str(borrower_name[a])
            self.ids.product_name.text = str(product_name[a])
            self.ids.amount.text = "Rs. " + str(loan_amount[a])
            self.ids.interest.text = str(interest_rate[a]) + "%"
            self.ids.tenure.text = str(int(tenure[a])) + ' Months'
            self.ids.left.text = "Rs. " + str(left_amount[a])
            if customer_id[a] in p_customer_id:
                index1 = p_customer_id.index(customer_id[a])
                self.ids.age.text = str(user_age[index1]) + " Years"
                self.ids.employment.text = str(emp_type[index1])
                self.ids.score.text = str(ascend_score[index1])
            else:
                print("customer_id is not there")

        data = app_tables.fin_wallet.search()
        w_email = []
        w_id = []
        w_amount = []
        for i in data:
            w_email.append(i['user_email'])
            w_id.append(i['wallet_id'])
            w_amount.append(i['wallet_amount'])

        index = 0
        if log_email in w_email:
            index = w_email.index(log_email)
            self.ids.total_amount.text = "Rs. " + str(round(w_amount[index], 2))
        else:
            print("no email found")

        users = app_tables.users.search()

        user_email = []
        create_date = []
        for i in users:
            user_email.append(i['email'])
            create_date.append(i['signed_up'])

        if log_email in user_email:
            user_index = user_email.index(log_email)
            self.ids.details.secondary_text = "Joined Date: " + str(create_date[user_index].date())
        else:
            print("no email found")

        member = app_tables.fin_membership.search()

        a = 0
        membership_type = []
        max_amount = []
        min_amount = []
        for i in member:
            a += 1
            membership_type.append(i['membership_type'])
            min_amount.append(i['min_amount'])
            max_amount.append(i['max_amount'])
        print(log_index)
        print(investment)

        if investment[log_index] != None:
            self.ids.commitment.text = "Rs. " + str(investment[log_index])
            for i in range(a):
                if float(investment[log_index]) >= min_amount[i] and float(investment[log_index]) < max_amount[i]:
                    self.ids.details.tertiary_text = f"Membership_type: {membership_type[i]}"
                    break
        else:
            self.ids.details.tertiary_text = f"Membership_type: None"
            print("Investment Amount Not There")

    def invest(self):
        data = app_tables.fin_loan_details.search()

        loan_id = []
        loan_status = []
        borrower_name = []
        product_name = []
        customer_id = []
        loan_amount = []
        left_amount = []
        interest_rate = []
        tenure = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            loan_status.append(i['loan_updated_status'])
            borrower_name.append(i['borrower_full_name'])
            product_name.append(i['product_name'])
            customer_id.append(i['borrower_customer_id'])
            loan_amount.append(i['loan_amount'])
            left_amount.append(i['remaining_amount'])
            interest_rate.append(i['interest_rate'])
            tenure.append(i['tenure'])
        if len(loan_id) < 1:
            pass
        else:
            a = 0
            b = -1
            for i in loan_status:
                b += 1
                if i == 'under process':
                    a = b
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            under_process = ViewLoansProfileScreen(name='ViewLoansProfileScreen')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(under_process)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansProfileScreen'
            self.manager.get_screen('ViewLoansProfileScreen').initialize_with_value(loan_id[a], data)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderLanding'

        # Replace with the actual name of your previous screen

    def homepage(self):
        self.manager.current = 'MainScreen'

    def go_to_main_screen(self):
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

    def profile(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.permformance_profile(modal_view), 2)

    def permformance_profile(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        self.manager.add_widget(Factory.ViewProfileScreen(name='ViewProfileScreen'))
        self.manager.current = 'ViewProfileScreen'

    def lender_today_due(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.performance_lender_today_due(modal_view), 2)

    def view_lost_opportunities(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.perform_view_lost_opportunities(modal_view), 2)

    def perform_view_lost_opportunities(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        self.manager.add_widget(Factory.LostOpportunitiesScreen(name='LostOpportunitiesScreen'))
        self.manager.current = 'LostOpportunitiesScreen'

    def performance_lender_today_due(self, modal_view):
        modal_view.dismiss()
        self.manager.add_widget(Factory.TodayDuesTD(name='TodayDuesTD'))
        self.manager.current = 'TodayDuesTD'

    def view_loan_request(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

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

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label,
                                                                      modal_height))  # Bind to the completion event to repeat the animation
        anim.start(loading_label)

    def perform_loan_request_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        self.manager.add_widget(Factory.ViewLoansRequest(name='ViewLoansRequest'))
        self.manager.current = 'ViewLoansRequest'

    def view_loanscreen(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.perform_view_loanscreen(modal_view), 2)

    def perform_view_loanscreen(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        self.manager.add_widget(Factory.ViewLoansScreen(name='ViewLoansScreen'))
        self.manager.current = 'ViewLoansScreen'

    def newloan_extension(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.perform_newloan_extension(modal_view), 2)

    def perform_newloan_extension(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()

        self.manager.add_widget(Factory.NewExtension(name='NewExtension'))
        self.manager.current = 'NewExtension'

    def view_transaction_history(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.performance_view_transaction_history(modal_view), 2)

    def performance_view_transaction_history(self, modal_view):
        modal_view.dismiss()

        self.manager.add_widget(Factory.TransactionLH(name='TransactionLH'))
        self.manager.current = 'TransactionLH'

    def view_loan_foreclose(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.performance_view_loan_foreclose(modal_view), 2)

    def performance_view_loan_foreclose(self, modal_view):
        modal_view.dismiss()
        self.manager.add_widget(Factory.DashboardScreenLF(name='DashboardScreenLF'))
        self.manager.current = 'DashboardScreenLF'

    def go_to_wallet(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

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
        from lender_wallet import LenderWalletScreen

        modal_view.dismiss()
        self.manager.add_widget(Factory.LenderWalletScreen(name='LenderWalletScreen'))
        self.manager.current = 'LenderWalletScreen'
        # Get the existing ScreenManager

    def help_module(self):
        from help_module import HelpScreen
        self.manager.add_widget(Factory.HelpScreen(name='HelpScreen'))
        self.manager.current = 'HelpScreen'


class ViewProfileScreen(Screen):
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

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('profile')

    def refresh(self):
        pass

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

    def on_edit(self):
        self.manager.add_widget(Factory.EditScreen(name='ViewEditScreen'))
        self.manager.current = 'ViewEditScreen'

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
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.on_back_button_press()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'  # Replace with the actual name of your previous screen

    def on_back_button_press(self):
        self.manager.current = 'LenderDashboard'


class ViewEditScreen(Screen):
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
            self.manager.add_widget(Factory.LenderDashboard(name='LenderDashboard'))
            self.manager.current = 'LenderDashboard'

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
        self.manager.current = 'ViewProfileScreen'

    def on_back_button_press(self):
        self.manager.current = 'ViewProfileScreen'


class MyScreenManager(ScreenManager):
    pass

