from anvil import Label
from anvil.tables import app_tables
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import *
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
import matplotlib.pyplot as plt
import numpy as np
from matplot_figure import MatplotFigure
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.progressbar import MDProgressBar

from datetime import datetime

borrower_portfolio = '''
<WindowManager>:
    LenderDetails:
    ViewPortfolio:

<LenderDetails>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Lender Details"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:
            MDList:
                id: container

<ViewPortfolio>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Portfolio"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                padding: dp(20)
                spacing: dp(20)
                size_hint_y: None
                height: self.minimum_height

                MDBoxLayout:
                    orientation: 'vertical'
                    padding: dp(10)
                    spacing: dp(10)
                    size_hint_y: None
                    height: dp(550)
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            width: 0.25
                            rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                    
                    MDGridLayout:
                        cols: 2
                        spacing: dp(10)
                        padding: dp(10)
                        MDLabel:
                            text: "Full Name" 
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: full_name      
                            text: "" 
                            size_hint_y:None
                            height:dp(50)
                            halign: "left"                    
                    MDGridLayout:
                        cols: 2
                        spacing: dp(10)
                        padding: dp(10)
                        MDLabel:
                            text: "Mobile Number" 
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: mobile_number      
                            text: "" 
                            size_hint_y:None
                            height:dp(50)
                            halign: "left"
                    MDGridLayout:
                        cols: 2
                        spacing: dp(10)
                        padding: dp(10)
                        MDLabel:
                            text: "Date of Birth" 
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: date_of_birth      
                            text: "" 
                            size_hint_y:None
                            height:dp(50)
                            halign: "left"
                    MDGridLayout:
                        cols: 2
                        spacing: dp(10)
                        padding: dp(10)
                        MDLabel:
                            text: "Gender" 
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
                            text: "Marital Status" 
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: marital_status      
                            text: "" 
                            size_hint_y:None
                            height:dp(50)
                            halign: "left"
                    MDGridLayout:
                        cols: 2
                        spacing: dp(10)
                        padding: dp(10)
                        MDLabel:
                            text: "Type of Address" 
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: type_of_address      
                            text: "" 
                            size_hint_y:None
                            height:dp(50)
                            halign: "left"

                    MDGridLayout:
                        cols: 2
                        spacing: dp(10)
                        padding: dp(10)
                        MDLabel:
                            text: "Qualification" 
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: qualification      
                            text: "" 
                            size_hint_y:None
                            height:dp(50)
                            halign: "left"
                    MDGridLayout:
                        cols: 2
                        spacing: dp(10)
                        padding: dp(10)
                        MDLabel:
                            text: "Profession" 
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: profession      
                            text: "" 
                            size_hint_y:None
                            height:dp(50)
                            halign: "left"

                    MDGridLayout:
                        cols: 2
                        spacing: dp(10)
                        padding: dp(10)
                        MDLabel:
                            text: "Annual Salary" 
                            size_hint_y:None
                            height:dp(50)
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: annual_salary      
                            text: "" 
                            size_hint_y:None
                            height:dp(50)
                            halign: "left"   
                
                AnchorLayout:
                    size_hint_y: None
                    height: dp(500)
                    padding: dp(10)
                    BoxLayout:
                        id: chart_container
                        orientation: "horizontal"
                        padding: dp(10)
                        spacing: dp(40)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing: dp(10)
                    size_hint_y: None
                    height: dp(40)
                    padding: dp(10)

                    MDLabel:
                        text: "Investment"
                        halign: 'left'
                        padding: [0, 0, dp(10), 0]  # Adjusted padding

                    Widget:
                        size_hint_x: None
                        width: dp(13)
                        size_hint_y: None
                        height: dp(13)
                        canvas:
                            Color:
                                rgba: 0, 1, 0, 1  # Green color
                            Rectangle:
                                pos: self.pos
                                size: self.size

                    MDLabel:
                        text: "Returns"
                        halign: 'left'
                    Widget:
                        size_hint_x: None
                        width: dp(13)
                        size_hint_y: None
                        height: dp(13)
                        canvas:
                            Color:
                                rgba: 1, 0, 0, 1  # Red color
                            Rectangle:
                                pos: self.pos
                                size: self.size 

'''
Builder.load_string(borrower_portfolio)
date = datetime.today()
print(date)


class WindowManager(ScreenManager):
    pass


class LenderDetails(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.populate_lender_list()

    def populate_lender_list(self):
        data = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()

        lender_details = {}

        for loan in data:
            if loan['loan_updated_status'] in ['disbursed', 'foreclosure', 'extension']:
                lender_id = loan['lender_customer_id']
                if lender_id not in lender_details:
                    lender_details[lender_id] = {
                        'full_name': loan['lender_full_name'],
                        'mobile_number': '',
                        'product_name': loan['product_name']
                    }

        for prof in profile:
            if prof['customer_id'] in lender_details:
                lender_details[prof['customer_id']]['mobile_number'] = prof['mobile']

        for lender_id, details in lender_details.items():
            item = ThreeLineAvatarIconListItem(
                IconLeftWidget(icon="account"),
                text=f"Lender Name: {details['full_name']}",
                secondary_text=f"Lender Mobile Number: {details['mobile_number']}",
                tertiary_text=f"Product Name: {details['product_name']}",
                text_color=(0, 0, 0, 1),
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.bind(on_release=lambda instance, lender_id=lender_id: self.icon_button_clicked(instance, lender_id))
            self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance, lender_id):
        sm = self.manager
        approved = ViewPortfolio(name='ViewPortfolio')
        sm.add_widget(approved)
        sm.current = 'ViewPortfolio'
        self.manager.get_screen('ViewPortfolio').initialize_with_value(lender_id)

    def go_back(self):
        self.manager.current = 'DashboardScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()


class BarWidget(Widget):
    def __init__(self, value, color, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.color = color
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(0.98, 0.98, 0.98, 1)  # Grey background
            Rectangle(pos=self.pos, size=self.size)
            Color(*self.color)
            Rectangle(pos=self.pos, size=(self.width, self.height * self.value / 100))


class ViewPortfolio(Screen):
    def initialize_with_value(self, lender_id):
        profile = app_tables.fin_user_profile.get(customer_id=lender_id)

        if profile:
            self.ids.full_name.text = f"{profile['full_name']}"
            self.ids.mobile_number.text = f"{profile['mobile']}"
            self.ids.date_of_birth.text = f"{profile['date_of_birth']}"
            self.ids.gender.text = f"{profile['gender']}"
            self.ids.marital_status.text = f"{profile['marital_status']}"
            self.ids.type_of_address.text = f"{profile['present_address']}"
            self.ids.qualification.text = f"{profile['qualification']}"
            self.ids.profession.text = f"{profile['profession']}"
            self.ids.annual_salary.text = f"{profile['annual_salary']}"

            # Sample data for investment and returns
            investment_data = [60]  # Percentage of total (adjust values accordingly)
            my_returns_data = [20]  # Percentage of total (adjust values accordingly)

            # Create a layout for the progress bars and labels
            chart_layout = BoxLayout(orientation='horizontal', padding=dp(10), spacing=dp(10))

            # Create and add progress bars with labels to the layout
            for investment_percentage, return_percentage in zip(investment_data, my_returns_data):
                # Create BarWidgets for investment and returns
                investment_bar = BarWidget(value=investment_percentage, color=(0, 1, 0, 1), size_hint=(None, 1),
                                           width=dp(60))
                return_bar = BarWidget(value=return_percentage, color=(1, 0, 0, 1), size_hint=(None, 1), width=dp(60))

                # Add the progress bars to the chart layout
                chart_layout.add_widget(investment_bar)
                chart_layout.add_widget(return_bar)

            # Clear previous widgets and add the new layout to the chart container
            self.ids.chart_container.clear_widgets()
            self.ids.chart_container.add_widget(chart_layout)


