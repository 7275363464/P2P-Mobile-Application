import anvil
from anvil import Label
from anvil.tables import app_tables
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.base import runTouchApp
from kivy.properties import ListProperty, NumericProperty, ColorProperty
from kivy.clock import Clock
from kivy.utils import get_color_from_hex

import numpy as np
from math import sin, cos
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
import matplotlib.pyplot as plt
from kivy.core.image import Image as CoreImage
import matplotlib.pyplot as plt
import io
from kivy.factory import Factory
from kivy.properties import ListProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget

from datetime import datetime

borrower_portfolio = '''
<WindowManager>:
    Lend_Portfolio:
    LenViewPortfolio:

<Lend_Portfolio>:

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

<LenViewPortfolio>:

    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Portfolio"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding:dp(10)
                spacing:dp(15)
                size_hint_y: None
                height: self.minimum_height
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(10)

                    BoxLayout:
                        id: box1
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(530)
                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1
                            Line:
                                width: 0.25
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                        MDBoxLayout:
                            orientation: "vertical"
                            pos_hint: {"top": 1}

                            spacing: dp(-5)
                            padding:dp(10)
                            size_hint_y: None
                            height: dp(100)
                            spacing:
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 0.1
                                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                            text_size: self.width - dp(20), None

                            Image:
                                id: selected_image1
                                source: 'background.jpg'
                                halign: 'center'
                                valign: 'middle'
                                size_hint_x: None
                                allow_stretch: True
                                keep_ratio: True
                                width: dp(20)
                                spacing: dp(30)
                                padding: dp(30)
                                height:dp(20)
                                theme_text_color: 'Custom'
                                text_color: 0.043, 0.145, 0.278, 1
                                size: dp(60), dp(20)
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                                canvas.before:
                                    Color:
                                        rgba: 1, 1, 1, 1

                                canvas:
                                    StencilPush
                                    Ellipse:
                                        size: self.width + 15, self.height + 8
                                        pos: self.x -5, self.y -5
                                    StencilUse
                                    RoundedRectangle:
                                        texture: self.texture
                                        size: self.width + 25, self.height + 15
                                        pos: self.x -5, self.y -5

                                    StencilUnUse
                                    StencilPop

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
                MDBoxLayout:
                    orientation: "vertical"
                    size_hint_x: None
                    spacing:dp(5)
                    size_hint_y: None
                    height: dp(600)
                    width:dp(800)
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                    MDLabel:
                        text: "Ascend Score Summary" 
                        size_hint_y:None
                        font_style: "H6"
                        bold: True
                        height:dp(30)
                        font_size: dp(22)
                        halign: "center" 
                    Gauge:
                        id: gauge

                        size_hint: None, None
                        size: dp(200), dp(200)
                        fill_fraction: 0.4  # Default value
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: dp(15)
                        padding: dp(1)
                        size_hint: None, None
                        height:dp(-120)
                        width:dp(200)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                    MDLabel:
                        id:ascend_percentage
                        text: " "
                        size_hint_y:None
                        bold: True
                        height:dp(0)
                        font_size: dp(25)
                        halign: "center"


                    MDLabel:
                        id:status
                        text: "fwrfwf" 
                        size_hint_y:None
                        height:dp(43)
                        bold: True
                        font_size: dp(20)
                        halign: "center" 
                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: dp(1)
                        padding: dp(1)
                        size_hint: None, None
                        height:dp(20)
                        width:dp(200)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                        MDLabel:
                            text: "0" 
                            size_hint_y:None
                            height:dp(-10)

                            font_size: dp(22)
                            halign: "center"
                        MDLabel:

                            text: "100" 
                            size_hint_y:None
                            height:dp(-10)
                            font_size: dp(22)
                            halign: "center" 
                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: dp(1)
                        padding: dp(1)
                        size_hint: None, None
                        height:dp(40)
                        width:dp(400)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        MDLabel:
                            text: "Borrower Financial Overview" 
                            size_hint_y:None
                            font_style: "H6"
                            bold: True
                            spacing:dp(20)
                            padding:dp(20)
                            height:dp(-50)
                            font_size: dp(22)
                            halign: "center"  
                    PieChartWidget:
                        id: chart_widget
                        size_hint: None, None
                        size: dp(400), dp(370)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    BoxLayout:
                        orientation: 'horizontal'
                        spacing: dp(5)  
                        size_hint_y: None
                        height: dp(-50)
                        size_hint_x: None
                        width: dp(400)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        padding: dp(5)
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(5)  # Space between the widget and label
                            size_hint_y: None
                            height: dp(40)
                            Widget:
                                size_hint_x: None
                                width: dp(13)
                                size_hint_y: None
                                height: dp(13)
                                canvas:
                                    Color:
                                        rgba:  0.914, 0.961, 0.129, 1
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                            MDLabel:
                                text: "Under Process"
                                halign: 'left'
                                valign: 'middle'
                                size_hint_y: None
                                height: dp(13)

                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(5)  # Space between the widget and label
                            size_hint_y: None
                            height: dp(40)
                            Widget:
                                size_hint_x: None
                                width: dp(13)
                                size_hint_y: None
                                height: dp(13)
                                canvas:
                                    Color:
                                        rgba: 0.980, 0.459, 0.200, 1
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                            MDLabel:
                                text: "Disbursed"
                                halign: 'left'
                                valign: 'middle'
                                size_hint_y: None
                                height: dp(13)
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(5)  # Space between the widget and label
                            size_hint_y: None
                            height: dp(40)
                            Widget:
                                size_hint_x: None
                                width: dp(13)
                                size_hint_y: None
                                height: dp(13)
                                canvas:
                                    Color:
                                        rgba: 1, 0, 0, 1  # Green color
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                            MDLabel:
                                text: "Rejected"
                                halign: 'left'
                                valign: 'middle'
                                size_hint_y: None
                                height: dp(13)
                    BoxLayout:
                        orientation: 'horizontal'
                        spacing: dp(5)  # Spacing between the two columns
                        size_hint_y: None
                        height: dp(20)
                        size_hint_x: None
                        width: dp(400)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        padding: dp(5)            
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(5)  # Space between the widget and label
                            size_hint_y: None
                            height: dp(40)
                            Widget:
                                size_hint_x: None
                                width: dp(13)
                                size_hint_y: None
                                height: dp(13)
                                canvas:
                                    Color:
                                        rgba: 0, 0, 1, 1  # Green color
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                            MDLabel:
                                text: "Extension"
                                halign: 'left'
                                valign: 'middle'
                                size_hint_y: None
                                height: dp(13)


                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(5)  # Space between the widget and label
                            size_hint_y: None
                            height: dp(40)
                            Widget:
                                size_hint_x: None
                                width: dp(13)
                                size_hint_y: None
                                height: dp(13)
                                canvas:
                                    Color:
                                        rgba: 0.729, 0.239, 0.976, 1
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                            MDLabel:
                                text: "Foreclosure"
                                halign: 'left'
                                valign: 'middle'
                                size_hint_y: None
                                height: dp(13)
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(5)  # Space between the widget and label
                            size_hint_y: None
                            height: dp(40)
                            Widget:
                                size_hint_x: None
                                width: dp(13)
                                size_hint_y: None
                                height: dp(13)
                                canvas:
                                    Color:
                                        rgba:  0, 1, 0, 1  # Green color
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                            MDLabel:
                                text: "Closed"
                                halign: 'left'
                                valign: 'middle'
                                size_hint_y: None
                                height: dp(13)        

<Gauge>:
    on_size: self.recalculate_lines()
    on_pos: self.recalculate_lines()
    on_fill_fraction: self.recalculate_lines()
    canvas:
        Color:
            rgba: 0.7, 0.7, 0.7, 1
        Line:
            points: self.line_points
            width: self.height * 0.03
        Color:
            rgba: self.color
        Line:
            points: self.filled_in_points
            width: self.height * 0.03


'''
Builder.load_string(borrower_portfolio)
date = datetime.today()
print(date)


class Gauge(Widget):
    line_points = ListProperty([])
    filled_in_points = ListProperty([])
    fill_fraction = NumericProperty(0.4)
    color = ColorProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super(Gauge, self).__init__(**kwargs)
        self.bind(fill_fraction=self.update_color)
        Clock.schedule_once(self.recalculate_lines, 0)

    def recalculate_lines(self, *args):
        centre_x, centre_y = self.center
        radius = self.height * 0.4
        start_angle = np.radians(220)
        end_angle = np.radians(-40)
        angles = np.linspace(start_angle, end_angle, 1000)

        line_points = []
        for angle in angles:
            line_points.append((cos(angle) * radius, sin(angle) * radius))

        self.line_points = [(x + centre_x, y + centre_y) for x, y in line_points]
        self.filled_in_points = self.line_points[:int(self.fill_fraction * len(self.line_points))]

    def update_color(self, *args):
        score = self.fill_fraction * 100
        if score > 65:
            self.color = [0, 1, 0, 1]  # Green
        elif 50 < score <= 65:
            self.color = [1, 0.5, 0, 1]  # Orange
        elif 25 < score <= 50:
            self.color = [1, 0.5, 0, 1]  # Orange
        else:
            self.color = [1, 0, 0, 1]  # Red


class WindowManager(ScreenManager):
    pass


class Lend_Portfolio(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.populate_lender_list()

    def populate_lender_list(self):
        data = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()

        borrower_details = {}

        for loan in data:
            if loan['loan_updated_status'] in ['disbursed', 'foreclosure', 'extension']:
                borrower_id = loan['borrower_customer_id']
                if borrower_id not in borrower_details:
                    borrower_details[borrower_id] = {
                        'full_name': loan['borrower_full_name'],
                        'mobile_number': '',
                        'product_name': loan['product_name'],
                        'open_loans': 0,  # Initialize open loans count
                        'closed_loans': 0  # Initialize closed loans count
                    }
                # Count open and closed loans
                if loan['loan_updated_status'] == 'disbursed':
                    borrower_details[borrower_id]['open_loans'] += 1
                else:
                    borrower_details[borrower_id]['closed_loans'] += 1

        for prof in profile:
            if prof['customer_id'] in borrower_details:
                borrower_details[prof['customer_id']]['mobile_number'] = prof['mobile']

        for borrower_id, details in borrower_details.items():
            item = ThreeLineAvatarIconListItem(
                IconLeftWidget(icon="account"),
                text=f"Borrower Name: {details['full_name']}",
                secondary_text=f"Borrower Mobile Number: {details['mobile_number']}",
                tertiary_text=f"Product Name: {details['product_name']}",
                text_color=(0, 0, 0, 1),
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.bind(
                on_release=lambda instance, borrower_id=borrower_id: self.icon_button_clicked(instance, borrower_id))
            self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance, borrower_id):
        sm = self.manager
        approved = LenViewPortfolio(name='LenViewPortfolio')
        sm.add_widget(approved)
        sm.current = 'LenViewPortfolio'
        self.manager.get_screen('LenViewPortfolio').initialize_with_value(borrower_id)

    def go_back(self):
        self.manager.current = 'LenderDashboard'

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
        self.populate_lender_list()


class PieChartWidget(AnchorLayout):
    borrower_id = NumericProperty()

    def __init__(self, **kwargs):
        super(PieChartWidget, self).__init__(**kwargs)
        self.chart_image = Image(allow_stretch=True)
        self.add_widget(self.chart_image)
        self.borrower_id = kwargs.get('borrower_id', 0)  # Get borrower_id from kwargs
        self.plot_pie_chart()

    def plot_pie_chart(self):
        if not self.borrower_id:
            return

        # Fetching data from the database dynamically
        loan_data = app_tables.fin_loan_details.search(borrower_customer_id=self.borrower_id)
        loan_status_count = {
            'disbursed': 0,
            'rejected': 0,
            'extension': 0,
            'foreclosure': 0,
            'under_process': 0,
            'closed': 0
        }

        for loan in loan_data:
            loan_status = loan['loan_updated_status']
            if loan_status == 'under process':
                loan_status_count['under_process'] += 1
            elif loan_status in loan_status_count:
                loan_status_count[loan_status] += 1

        # Remove items with 0 count
        loan_status_count = {status: count for status, count in loan_status_count.items() if count != 0}

        # Define the colors for each status
        status_colors = {
            'disbursed': '#FA7533',
            'rejected': '#F81B1E',
            'extension': '#3D65F9',
            'foreclosure': '#BA3DF9',
            'under_process': '#E9F621',
            'closed': '#30C624'
        }

        # Plot pie chart only if there are non-zero values
        if any(loan_status_count.values()):
            values = list(loan_status_count.values())
            colors = [status_colors[label] for label in loan_status_count.keys()]

            plt.axis("equal")
            patches, _, autotexts = plt.pie(
                values, labels=None, autopct='%1.0f%%', colors=colors,
                textprops={'fontsize': 14}  # Remove fontweight here
            )
            # Display count labels below the percentage
            for i, (count, color) in enumerate(zip(values, colors)):
                percentage = '{:.0f}%'.format(count / sum(values) * 100)
                autotexts[i].set_color('white')  # Set text color to white
                autotexts[i].set_fontsize(14)  # Set font size for percentage
                autotexts[i].set_text(percentage + f'\n{count} loan' + ('s' if count > 1 else ''))

                # Set font weight only for percentage
                if '%' in autotexts[i].get_text():
                    autotexts[i].set_fontweight('bold')

            # Convert matplotlib plot to texture
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            im = CoreImage(buf, ext='png').texture
            plt.close()

            # Display the plot
            self.chart_image.texture = im

            # Set the size of the chart image (adjust as needed)
            self.chart_image.size = (400, 400)

            # Center the chart in the layout
            self.chart_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            self.size_hint = (None, None)
            self.size = self.chart_image.size


class LenViewPortfolio(Screen):
    def go_back(self):
        self.manager.current = 'Lend_Portfolio'

    def initialize_with_value(self, borrower_id):
        self.ids.chart_widget.clear_widgets()

        profile = app_tables.fin_user_profile.get(customer_id=borrower_id)

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
            ascend_value = profile['ascend_value']
            self.ids.ascend_percentage.text = f"{profile['ascend_value']}%"
            gauge_widget = self.ids.gauge
            gauge_widget.fill_fraction = ascend_value / 100  # Assuming ascend_value is a percentage

            if ascend_value > 65:
                self.ids.status.text = "Very Good"
                self.ids.status.color = get_color_from_hex('#00FF00')  # Green
            elif 50 < ascend_value <= 65:
                self.ids.status.text = "Good"
                self.ids.status.color = get_color_from_hex('#FFFF00')  # Orange
            elif 25 < ascend_value <= 50:
                self.ids.status.text = "Average"
                self.ids.status.color = get_color_from_hex('#FFA500')  # Orange
            else:
                self.ids.status.text = "Bad"
                self.ids.status.color = get_color_from_hex('#FF0000')  # Red

            pie_chart_widget = PieChartWidget(borrower_id=borrower_id)
            self.ids.chart_widget.add_widget(pie_chart_widget)