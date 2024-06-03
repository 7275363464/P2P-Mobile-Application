import configparser
import json
import sqlite3
from datetime import datetime

import anvil
from anvil.tables import app_tables
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.material_resources import dp
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.spinner import MDSpinner
from borrower_notification import NotificationScreen
from borrower_extend_loan import ExtensionLoansRequest
from borrower_view_transaction_history import TransactionBH
from borrower_application_tracker import ALLLoansAPT
from borrower_dues import BorrowerDuesScreen
from new_loan_request import NewloanScreen
from borrower_viewloan import DashboardScreenVLB, ClosedLoanVLB, UnderProcessLoanVLB, OpenLoanVLB, RejectedLoanVLB
from borrower_foreclosure import LoansDetailsB
from kivy.uix.modalview import ModalView
from kivymd.uix.spinner import MDSpinner
from kivy.clock import Clock
from kivy.animation import Animation
from kivymd.uix.label import MDLabel
from kivy.factory import Factory
from kivymd.uix.button import MDFillRoundFlatButton

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)

user_helpers = '''
<WindowManager>:
    DashboardScreen:
    ProfileScreen:
    EditScreen:
<DashboardScreen>:

    MDBottomNavigation:
        panel_color: '#F5F5F5'
        selected_color_background: "#666666"
        text_color_active: "#007BFF"
        elevation: 10
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
                                    elevation: 2
                                    pos_hint: {'top': 1}
                                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                                    title_align: 'center'
                                    md_bg_color: 0.043, 0.145, 0.278, 1
        
        
        
                                    BoxLayout:
                                        size_hint_x: None
                                        width: dp(20)
                                        pos_hint: {"center_x": 0.9, "center_y": 1.5}
                                        spacing: dp(-16)
        
                                        MDIconButton:
                                            icon: "bell"
                                            on_touch_down: root.notification() if self.collide_point(*args[1].pos) else None    
                                            pos_hint: {"center_y": 1.3}
                                            theme_text_color: 'Custom'
                                            text_color: 1, 1, 1, 1 
        
        
                                        MDLabel:
                                            id: notification_label
                                            text: root.false_count_text
                                            size_hint_x: None
                                            width: self.texture_size[0]
                                            halign: "center"
                                            size_hint_x: None
                                            width: dp(20)
                                            valign: "center"
                                            theme_text_color: 'Custom'
                                            text_color: 1, 0, 0, 1 
                                            font_name: "Roboto-Bold"
                                            pos_hint: {"center_y": 1.5}

                                ScrollView:
                                    MDBoxLayout:
                                        orientation: 'vertical'
                                        padding: "10dp", "5dp", "10dp", "0dp"
                                        size_hint_y: None
                                        height: dp(750)
                                        spacing: dp(20)
                                        ThreeLineAvatarListItem:
                                            id: details
                                            text: "Welcome Sai Mamidala"
                                            secondary_text: "Joined Date: 22-03-12"
                                            tertiary_text: "Credit Limit: 10000000"
                                            bg_color: '#F5F5F5'
                                            theme_text_color: 'Custom'
                                            secondary_theme_text_color: 'Custom'
                                            tertiary_theme_text_color: 'Custom'
                                            text_color: '#007BFF'
                                            secondary_text_color: '#666666'
                                            tertiary_text_color: '#666666'
                                            on_release: root.go_to_profile()
                                            ImageLeftWidget:
                                        GridLayout:
                                            cols: 2
                                            padding: dp(10)
                                            spacing: dp(10)
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: self.minimum_height
                                                md_bg_color: "#AEDFF7"
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 0.1
                                                        rectangle: (self.x, self.y, self.width, self.height)
                                                MDLabel:
                                                    id: total_amount1
                                                    text: "Rs. 50,000"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    theme_text_color: "Custom"
                                                    text_color: "#333333"
                                                    font_name: "Roboto-Bold"
                                                    font_size: dp(20)

                                                MDLabel:
                                                    text: "Opening Balance"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    font_name: "Roboto-Bold"
                                                    theme_text_color: "Custom"
                                                    text_color: "#333333"
                                                MDFlatButton:
                                                    text: "View All"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    pos_hint: {'center_x': 0.5}
                                                    theme_text_color: "Custom"
                                                    text_color: "#007BFF"
                                                    on_release: root.go_to_wallet()
                                        MDLabel:
                                            text: ""
                                            size_hint_y: None
                                            height: dp(50)
                                        Widget:
                                            size_hint_y: None
                                            height: 5
                                            canvas:
                                                Color:
                                                    rgba: 0, 0, 0, 1  # Change color if needed
                                                Line:
                                                    points: self.x, self.y, self.x + self.width, self.y
                                        MDBoxLayout:
                                            orientation: 'vertical'
                                            spacing: dp(10)
                                            BoxLayout:  
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: self.minimum_height
                                                MDLabel:
                                                    text: 'My Loans'
                                                    bold: True
                                                    size_hint_y: None
                                                    height: dp(20)
                                        GridLayout:
                                            cols: 3  
                                            spacing: dp(10)
                                            size_hint_y: None
                                            height: dp(20)
                                            
                                            MDLabel:
                                                id: product_name
                                                text: "Product Name:"
                                                font_family: "Arial"
                                                bold: True
                                                halign: "left"

                                            MDLabel:
                                                id: product_name
                                                text: "TVS"
                                                font_family: "Arial"
                                                halign: "left"
                                            MDLabel:
                                                text: ""
                                                font_family: "Arial"
                                                bold: True
                                                halign: "left"
                                        
                                        
                                                
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
                                                        source: "icon1.png"
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
                                                    spacing: dp(10)
                                                    padding: dp(5)

                                                    Image:
                                                        source: "icon5.png"
                                                        size_hint: None, None
                                                        size: "60dp", "60dp"
                                                    MDBoxLayout:
                                                        orientation: 'vertical'
                                                        MDLabel:
                                                            text: "Loan Status"
                                                            font_size: dp(12)
                                                        MDLabel:
                                                            id:status
                                                            text: "under process"
                                                            font_size:dp(15)
                                        MDLabel:
                                            text: ""
                                        
                                        GridLayout:
                                            cols: 1
                                            spacing: dp(20)
                                            padding: dp(20)
                                            pos_hint: {'center_x': 0.80}
                                            MDFillRoundFlatIconButton:
                                                text: "View More"
                                                icon: "clipboard-text-outline"
                                                font_name: "Roboto-Bold"
                                                text_color: "white"
                                                md_bg_color: 0.043, 0.145, 0.278, 1
                                                on_release: root.go_to_view_loan_screen()
                                        MDLabel:
                                            text: ''
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
                                        
                                        MDLabel:
                                            text: ""
                                        MDLabel:
                                            text: ''
                                            size_hint_y: None
                                            height: dp(30)

                                            
            
                    
                MDNavigationDrawer:
                    id: nav_drawer
                    radius: (0, 16, 16, 0)

                    MDNavigationDrawerMenu:

                        MDNavigationDrawerHeader:
                            id: my_name
                            title: "Welcome Back"
                            title_color: "#4a4939"
                            text: "Sai Mamidala"
                            spacing: "4dp"
                            padding: "12dp", 0, 0, "56dp"

                        MDNavigationDrawerItem
                            icon: "newspaper"
                            text: "New Loan Requests"
                            icon_color: "#23639e"
                            on_release: root.go_to_newloan_screen()
                        MDNavigationDrawerDivider:

                        MDNavigationDrawerItem
                            icon: "bank"
                            text: "View Loans"
                            icon_color: "#23639e"
                            on_release: root.go_to_view_loan_screen()
                        MDNavigationDrawerDivider:

                        MDNavigationDrawerItem
                            icon: "calendar-check-outline"
                            text: "Today's Dues"
                            icon_color: "#23639e"
                            on_release: root.go_to_dues_screen()
                        MDNavigationDrawerDivider:

                        MDNavigationDrawerItem
                            icon: "progress-check"
                            text: "Application Tracker"
                            icon_color: "#23639e"
                            on_release: root.go_to_app_tracker()
                        MDNavigationDrawerDivider:

                        MDNavigationDrawerItem
                            icon: "home-minus"
                            text: "Loan Foreclose"
                            icon_color: "#23639e"
                            on_release: root.go_to_fore_closer_details()
                        MDNavigationDrawerDivider:

                        MDNavigationDrawerItem
                            icon: "plus-circle"
                            text: "Extended Loan Request"
                            icon_color: "#23639e"
                            on_release: root.go_to_extend()
                        MDNavigationDrawerDivider:

                        MDNavigationDrawerItem
                            icon: "history"
                            text: "View Transaction History"
                            icon_color: "#23639e"
                            on_release: root.go_to_transaction_history()
                        MDNavigationDrawerDivider:
                        MDNavigationDrawerItem
                            icon: "logout"
                            text: "Logout"
                            icon_color: "#23639e"
                            on_release: root.logout()
                        MDNavigationDrawerDivider:
                    
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Wallet'
            icon: 'wallet'
            on_tab_press: root.wallet()
            MDTopAppBar:
                title: "GP2P-Wallet"
                elevation: 2
                pos_hint: {'top': 1}
                right_action_items: [['refresh', lambda x: root.refresh1()]]
                title_align: 'center'
                md_bg_color: 0.043, 0.145, 0.278, 1

            MDBoxLayout:
                id: box1
                orientation: 'vertical'
                spacing: dp(30)
                padding: dp(30)
                MDLabel:
                    text: 'Available Balance'
                    halign: 'center'
                    size_hint_y: None
                    height: dp(30)

                GridLayout:
                    cols: 2
                    spacing: dp(20)
                    pos_hint: {'center_x': 0.7, 'center_y':0.3}
                    size_hint_y: None
                    height: dp(30)
                    MDIcon:
                        icon: 'currency-inr'
                        halign: 'center'
                    MDLabel:
                        id: total_amount
                        halign: 'left'
                        font_size: dp(25)
                        bold: True

                GridLayout:
                    cols: 2
                    spacing: dp(20)
                    size_hint_y: None
                    height: dp(50)
                    pos_hint: {'center_x': 0.6}
                    MDRectangleFlatIconButton:
                        text: "Deposit"
                        id: deposit_button_grid
                        line_color: 0, 0, 0, 0
                        icon: "cash"
                        text_color: 0, 0, 0, 1
                        md_bg_color:1,1,1,1
                        font_name:"Roboto-Bold"
                        on_release: root.highlight_button('deposit')
                    MDRectangleFlatIconButton:
                        id: withdraw_button_grid
                        text: "Withdraw"
                        icon: "cash"
                        line_color: 0, 0, 0, 0
                        text_color: 0, 0, 0, 1
                        md_bg_color: 1,1,1,1
                        font_name:"Roboto-Bold"
                        on_release: root.highlight_button('withdraw')
                MDLabel:
                    text: 'Enter Amount'
                    bold: True
                    size_hint_y: None
                    height: dp(5)
                MDTextField:
                    id: enter_amount
                    multiline: False
                    helper_text: 'Enter valid Amount'
                    helper_text_mode: 'on_focus'
                    size_hint_y:None
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    on_touch_down: root.on_amount_touch_down()

                MDFlatButton:
                    text: "View Transaction History >"
                    theme_text_color: "Custom"
                    text_color: "black"
                    pos_hint: {'center_x': 0.5}
                    padding: dp(10)
                    md_bg_color: 140/255, 140/255, 140/255, 1
                    on_release: root.view_transaction_history()
                GridLayout:
                    id: box
                    cols: 1
                    spacing: dp(20)
                    size_hint_y: None
                    height: dp(50)
                    pos_hint: {'center_x': 0.65}


                MDRoundFlatButton:
                    text: "Submit"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    theme_text_color: 'Custom'
                    font_name: "Roboto-Bold" 
                    text_color: 1, 1, 1, 1
                    size_hint: 0.7, None
                    height: "40dp"
                    pos_hint: {'center_x': 0.5}
                    on_release: root.submit()
                MDLabel:
                    text:''
                    size_hint_y:None
                    height:dp(20)
        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'My Loans'
            icon: 'cash'
            text_color_normal: '#4c594f'
            text_color_active: 1, 0, 0, 1
            MDFloatLayout:
                md_bg_color:1,1,1,1
                size_hint: 1, 1 
        
                MDTopAppBar:
                    title: "Borrower View Loan"
                    elevation: 3
                    right_action_items: [['refresh', lambda x: root.refresh()]]
                    pos_hint: {'top': 1}
                    md_bg_color: 0.043, 0.145, 0.278, 1
        
                MDGridLayout:
                    cols: 2
                    spacing: dp(15)
                    size_hint_y: None
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    height: self.minimum_height
                    width: self.minimum_width
                    size_hint_x: None
        
                    MDFlatButton:
                        size_hint: None, None
        
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        md_bg_color: 0.043, 0.145, 0.278, 1
        
                        size_hint_y: None
                        height: dp(60)
                        size_hint_x: None
                        width: dp(110)
                        on_release: root.go_to_open_loans()
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing:dp(10)
                            MDLabel:
                                text: "Open Loans"
                                font_size:dp(14)
                                bold:True
                                theme_text_color: 'Custom'
                                halign: "center"
                                text_color:1,1,1,1
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                    MDFlatButton:
                        size_hint: None, None
        
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        md_bg_color: 0.043, 0.145, 0.278, 1 
                        on_release: root.go_to_under_loans()
                        size_hint_y: None
                        height: dp(60)
                        size_hint_x: None
                        width: dp(110)
        
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing:dp(10)
                            MDLabel:
                                text: "Under process Loans"
                                font_size:dp(14)
                                bold:True
                                theme_text_color: 'Custom'
                                halign: "center"
                                text_color:1,1,1,1
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                    MDFlatButton:
                        size_hint: None, None
        
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        md_bg_color: 0.043, 0.145, 0.278, 1 
                        on_release: root.go_to_reject_loans()
                        size_hint_y: None
                        height: dp(60)
                        size_hint_x: None
                        width: dp(110)
        
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing:dp(10)
                            MDLabel:
                                text: "Rejected Loans"
                                font_size:dp(14)
                                bold:True
                                theme_text_color: 'Custom'
                                halign: "center"
                                text_color:1,1,1,1
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                    MDFlatButton:
                        size_hint: None, None
        
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        md_bg_color: 0.043, 0.145, 0.278, 1 
        
                        size_hint_y: None
                        height: dp(60)
                        size_hint_x: None
                        width: dp(110)
                        on_release: root.closed_loans()
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing:dp(10)
                            MDLabel:
                                text: "Closed Loans"
                                font_size:dp(14)
                                bold:True
                                theme_text_color: 'Custom'
                                halign: "center"
                                text_color:1,1,1,1
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Account'
            icon: 'account'
            icon_color: '#4c594f'
            font_name: "Roboto-Bold"
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Account Info"
                    elevation: 2
                    pos_hint: {'top': 1}
                    left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
                    right_action_items: [['refresh', lambda x: root.refresh()]]
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
                        padding:dp(10)
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1
                            Line:
                                width: 0.25
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
        
        
                        text_size: self.width - dp(20), None
        
                        Image:
                            source: 'icon8.png'
                            halign: 'center'
                            valign: 'middle'
                            size_hint_x: None
                            width: dp(34)
                            spacing: dp(30)
                            padding: dp(30)
                            theme_text_color: 'Custom'
                            text_color: 0.043, 0.145, 0.278, 1
                            size: dp(90), dp(90)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_touch_down:  root.go_to_profile() if self.collide_point(*args[1].pos) else None
                            canvas.before:
                                Color:
                                    rgba: 1, 1, 1, 1
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
                                        on_release: root.go_to_profile()
        
                                        Image:
                                            source: "icon7.png"
                                            size_hint: (0.4, 1)
                                            pos_hint:{"center_x":0.5,"center_y":0.2}
                                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                                        MDLabel:
                                            text: "Profile Info"
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
        
                                        Image:
                                            source: "icon6.png"
                                            size_hint: (0.4, 1)
                                            pos_hint:{"center_x":0.5,"center_y":0.2}
                                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
        
                                        MDLabel:
                                            text: "Personal Info"
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
        
                                        Image:
                                            source: "icon8.png"
                                            size_hint: (0.4, 1)
                                            pos_hint:{"center_x":0.5,"center_y":0.2}
                                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
        
                                        MDLabel:
                                            text: "Professional Info"
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
        
                                        Image:
                                            source: "icon9.png"
                                            size_hint: (0.4, 1)
                                            pos_hint:{"center_x":0.5,"center_y":0.2}
                                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
        
                                        MDLabel:
                                            text: "Business Info"
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
                                        Image:
                                            source: "icon10.png"
                                            size_hint: (0.4, 1)
                                            pos_hint:{"center_x":0.5,"center_y":0.2}
                                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
        
                                        MDLabel:
                                            text: "Bank Details"
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
        
                                        Image:
                                            source: "icon11.png"
                                            size_hint: (0.4, 1)
                                            pos_hint:{"center_x":0.5,"center_y":0.2}
                                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
        
                                        MDLabel:
                                            text: "Change Password"
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
'''


class DashboardScreen(Screen):
    Builder.load_string(user_helpers)
    false_count_text = StringProperty("")

    dashboard = None  # Initialize this variable properly

    def dash(self, type):
        if type is not None:
            self.dashboard = type
            return self.dashboard
    def type(self):
        if self.dashboard is not None:
            return self.dashboard
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_false_count()
        # Schedule the refresh every 5 seconds
        Clock.schedule_interval(self.refresh_false_count, 5)

    def load_false_count(self):
        try:
            with open("false_count.json", "r") as json_file:
                data = json.load(json_file)
                false_count = data.get("false_count", 0)
                self.false_count_text = str(false_count)
        except FileNotFoundError:
            self.false_count_text = "0"

    def refresh_false_count(self, dt):
        print("mani")
        self.load_false_count()

    def notification(self):
        # Create a modal view for the loading animation
        modal_view = ModalView(size_hint=(None, None), size=(300, 150), background_color=[0, 0, 0, 0])

        # Create a BoxLayout to hold the loading text
        box_layout = BoxLayout(orientation='vertical')

        # Create a label for the loading text
        loading_label = MDLabel(
            text="Loading...",
            halign="center",
            valign="center",
            theme_text_color="Custom",
            text_color=[1, 1, 1, 1],
            font_size="20sp",
            bold=True
        )

        # Add the label to the box layout
        box_layout.add_widget(loading_label)

        # Add the box layout to the modal view
        modal_view.add_widget(box_layout)

        # Open the modal view
        modal_view.open()

        # Perform the actual action (e.g., checking account details and navigating)
        Clock.schedule_once(lambda dt: self.show_transfer_screen(modal_view), 1)

    def show_transfer_screen(self, modal_view):
        # Dismiss the loading animation modal view
        modal_view.dismiss()
        self.manager.add_widget(Factory.NotificationScreen(name='NotificationScreen'))
        self.manager.current = 'NotificationScreen'



    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=5)
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label,
                                                                      modal_height))  # Bind to the completion event to repeat the animation
        anim.start(loading_label)

    def go_to_open_loans(self):
        self.dash('dashboard')
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
        Clock.schedule_once(lambda dt: self.performance_go_to_open_loans(modal_view), 2)

    def performance_go_to_open_loans(self, modal_view):
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = OpenLoanVLB(name='OpenLoanVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'OpenLoanVLB'

    def go_to_under_loans(self):
        self.dash('dashboard')
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.performance_go_to_under_loans(modal_view), 2)

    def performance_go_to_under_loans(self, modal_view):
        # Perform the actual action here (e.g., fetching loan requests)
        # For demonstration purposes, let's simulate a delay of 2 seconds
        # Replace this with your actual logic

        # Dismiss the modal view once the action is complete
        modal_view.dismiss()

        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = UnderProcessLoanVLB(name='UnderProcessLoanVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'UnderProcessLoanVLB'

    def go_to_reject_loans(self):
        self.dash('dashboard')
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.performance_go_to_reject_loans(modal_view), 2)

    def performance_go_to_reject_loans(self, modal_view):
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = RejectedLoanVLB(name='RejectedLoanVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'RejectedLoanVLB'

    def closed_loans(self):
        self.dash('dashboard')
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.performance_go_to_app_tracker(modal_view), 2)

    def performance_go_to_app_tracker(self, modal_view):
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = ClosedLoanVLB(name='ClosedLoanVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'ClosedLoanVLB'
    def refresh_profile_data(self):
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
    def on_back_button_press(self):
        self.manager.current = 'DashboardScreen'
    def wallet(self):
        self.type = None
        data = app_tables.fin_wallet.search()
        email = self.email()
        w_email = []
        w_id = []
        w_amount = []
        for i in data:
            w_email.append(i['user_email'])
            w_id.append(i['wallet_id'])
            w_amount.append(i['wallet_amount'])

        index = 0
        if email in w_email:
            index = w_email.index(email)
            self.ids.total_amount.text = str(round(w_amount[index], 2))
        else:
            print("no email found")

    def on_amount_touch_down(self):
        self.ids.enter_amount.input_type = 'number'

    def view_transaction_history(self):
        sm = self.manager
        # Create a new instance of the LenderWalletScreen
        wallet_screen = TransactionBH(name='TransactionBH')
        # Add the LenderWalletScreen to the existing ScreenManager
        sm.add_widget(wallet_screen)
        # Switch to the LenderWalletScreen
        sm.current = 'TransactionBH'

    def disbrsed_loan(self, instance):
        print("amount paid")
        view_loan_text = anvil.server.call("view_loan_text")
        if view_loan_text == "view_loan_text":
            self.manager.get_screen('ViewUnderScreenLR').paynow()
        else:
            self.manager.get_screen('ViewLoansProfileScreenLR').paynow()

    def highlight_button(self, button_type):
        if button_type == 'deposit':
            self.ids.deposit_button_grid.md_bg_color = 0, 0, 0, 1
            self.ids.withdraw_button_grid.md_bg_color = 1, 1, 1, 1
            self.ids.deposit_button_grid.text_color = 1, 1, 1, 1
            self.ids.withdraw_button_grid.text_color = 0, 0, 0, 1
            self.type = 'deposit'
        elif button_type == 'withdraw':
            self.ids.deposit_button_grid.md_bg_color = 1, 1, 1, 1
            self.ids.withdraw_button_grid.md_bg_color = 0, 0, 0, 1
            self.ids.withdraw_button_grid.text_color = 1, 1, 1, 1
            self.ids.deposit_button_grid.text_color = 0, 0, 0, 1
            self.type = 'withdraw'

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
        self.manager.current = 'LenderWalletScreen'

    def submit(self):
        enter_amount = self.ids.enter_amount.text
        if self.type == None:
            self.show_validation_error3('Please Select Transaction Type')
        elif self.ids.enter_amount.text == '' and not self.ids.enter_amount.text.isdigit():
            self.show_validation_error3('Enter Valid Amount')
        elif self.type == 'deposit':
            data = app_tables.fin_wallet.search()
            transaction = app_tables.fin_wallet_transactions.search()
            email = self.email()
            w_email = []
            w_id = []
            w_amount = []
            w_customer_id = []
            for i in data:
                w_email.append(i['user_email'])
                w_id.append(i['wallet_id'])
                w_amount.append(i['wallet_amount'])
                w_customer_id.append(i['customer_id'])

            t_id = []
            for i in transaction:
                t_id.append(i['transaction_id'])

            if len(t_id) >= 1:
                transaction_id = 'TA' + str(int(t_id[-1][2:]) + 1).zfill(4)
            else:
                transaction_id = 'TA0001'

            transaction_date_time = datetime.today()
            if email in w_email:
                index = w_email.index(email)
                data[index]['wallet_amount'] = int(enter_amount) + w_amount[index]
                self.show_validation_error(f'Amount {enter_amount} Deposited Successfully')
                self.ids.enter_amount.text = ''
                app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                           customer_id=w_customer_id[index], user_email=email,
                                                           transaction_type=self.type, amount=int(enter_amount),
                                                           status='success', wallet_id=w_id[index],
                                                           transaction_time_stamp=transaction_date_time)
            else:
                print("no email found")
            self.refresh1()

        elif self.type == 'withdraw':
            data = app_tables.fin_wallet.search()
            transaction = app_tables.fin_wallet_transactions.search()
            email = self.email()
            w_email = []
            w_id = []
            w_amount = []
            w_customer_id = []
            for i in data:
                w_email.append(i['user_email'])
                w_id.append(i['wallet_id'])
                w_amount.append(i['wallet_amount'])
                w_customer_id.append(i['customer_id'])

            t_id = []
            for i in transaction:
                t_id.append(i['transaction_id'])

            if len(t_id) >= 1:
                transaction_id = 'TA' + str(int(t_id[-1][2:]) + 1).zfill(4)
            else:
                transaction_id = 'TA0001'

            transaction_date_time = datetime.today()

            if email in w_email:
                index = w_email.index(email)
                if w_amount[index] >= int(self.ids.enter_amount.text):
                    data[index]['wallet_amount'] = w_amount[index] - int(self.ids.enter_amount.text)
                    self.show_validation_error(
                        f'Amount {self.ids.enter_amount.text} Withdraw Successfully')
                    self.ids.enter_amount.text = ''
                    app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                               customer_id=w_customer_id[index], user_email=email,
                                                               transaction_type=self.type, amount=int(enter_amount),
                                                               status='success', wallet_id=w_id[index],
                                                               transaction_time_stamp=transaction_date_time)
                else:
                    self.show_validation_error2(
                        f'Insufficient Amount {self.ids.enter_amount.text} Please Deposit Required Money')
                    app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                               customer_id=w_customer_id[index], user_email=email,
                                                               transaction_type=self.type, amount=int(enter_amount),
                                                               status='fail', wallet_id=w_id[index],
                                                               transaction_time_stamp=transaction_date_time)
                    self.ids.enter_amount.text = ''
            else:
                print("no email found")
        self.refresh1()

    def refresh1(self):
        self.wallet()

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Transaction Success",
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

    def show_validation_error2(self, error_message):
        dialog = MDDialog(
            title="Transaction Failure",
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

    def show_validation_error3(self, error_message):
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

    def email(self):
        return anvil.server.call('another_method')

    def refresh2(self):
        self.refresh_profile_data()

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
            ascend_score.append(i['ascend_value'])
            emp_type.append(i['profession'])

        # Check if 'logged' is in the status list
        log_index = 0
        if log_email in email_user:
            log_index = email_user.index(log_email)
            self.ids.details.text = "Welcome " + name_list[log_index]
            self.ids.details.font_style = 'H6'
            self.ids.my_name.text = name_list[log_index]
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
            if customer_id[i] == p_customer_id[log_index]:
                index_list.append(c)
                print(c)
        print(index_list)
        if len(index_list) < 1:
            self.ids.product_name = ''
            self.ids.amount.text = ''
            self.ids.interest.text = ''
            self.ids.tenure.text = ''
            self.ids.status.text = ''

        else:
            a = index_list[-1]
            print(a)
            self.ids.product_name.text = str(product_name[a])
            self.ids.amount.text = "Rs. " + str(round(loan_amount[a], 2))
            self.ids.interest.text = str(interest_rate[a]) + "%"
            self.ids.tenure.text = str(int(tenure[a])) + ' Months'
            self.ids.status.text = str(loan_status[a])

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
            self.ids.total_amount1.text = "Rs. " + str(round(w_amount[index], 2))
        else:
            print("no email found")

        borrower_data = app_tables.fin_borrower.search()
        borrower_cus_id = []
        credit_limit = []
        create_date = []
        for i in borrower_data:
            borrower_cus_id.append(i['customer_id'])
            credit_limit.append(i['credit_limit'])
            create_date.append(i['borrower_since'])

        if p_customer_id[log_index] in borrower_cus_id:
            index1 = borrower_cus_id.index(p_customer_id[log_index])
            self.ids.details.tertiary_text = "Credit Limit: " + str(credit_limit[index1])
            self.ids.details.secondary_text = "Joined Date: " + str(create_date[index1])
        else:
            self.ids.details.tertiary_text = "Credit Limit: "
            self.ids.details.secondary_text = "Joined Date: "

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

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
        sm = self.manager
        wallet_screen = ProfileScreen(name='ProfileScreen')
        sm.add_widget(wallet_screen)
        sm.current = 'ProfileScreen'


class MyScreenManager(ScreenManager):
    pass
