from anvil import Label
from anvil.tables import app_tables
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import *
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.filemanager import MDFileManager
from datetime import datetime

from kivymd.uix.snackbar import Snackbar

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)

import anvil.server


loan_forecloseB = '''
<WindowManager>:
    LoansDetailsB:
    ViewProfileScreenFB:
    ForecloseDetails:

<LoansDetailsB>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Open Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container

<ViewProfileScreenFB>
    GridLayout:
        cols: 1
        MDTopAppBar:
            title: "View Profile"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1 
            title_align: 'left'

        ScrollView:
            GridLayout:
                cols: 1
                
                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(50)
                    padding: dp(30)
                    size_hint_y: None
                    height: self.minimum_height
                    canvas.before:
                        Color:
                            rgba: 230/255, 245/255, 255/255, 1 
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [1, 1, 1, 1]
                            source: "background.jpg"
    
                    MDGridLayout:
                        cols: 2
        
                        MDLabel:
                            text: 'Loan Amount:'
                            halign: 'left'
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                            bold: True
                    MDGridLayout:
                        cols: 2
                        MDIconButton:
                            icon: 'currency-inr'
                            halign: 'left'
                            size_hint_y: None
                            height: dp(1)
                            bold: True
        
                        MDLabel:
                            id: amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 0,0,0,1
                            bold: True
                    MDLabel:
                        text: ''
                        halign: 'left'
                        size_hint_y: None
                        height: dp(5)
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: 'Borrower Name'
                            halign: 'left' 
                            bold: True
        
                        MDLabel:
                            id: name
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1   
                        
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: 'Tenure(Months)'
                            halign: 'left'  
                            bold: True
        
                        MDLabel:
                            id: tenure
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: 'Interest Rate'
                            halign: 'left'
                            theme_text_color: 'Custom'  
                            bold: True
        
                        MDLabel:
                            id: interest
                            halign: 'left'
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Credit limit:" 
                            halign: 'left' 
                            bold: True
                        MDLabel:
                            id: limit
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Total Payment Made:" 
                            halign: 'left' 
                            bold: True
                        MDLabel:
                            id: total_payment
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Foreclosure Type:" 
                            halign: 'left'
                            bold: True
                        MDLabel:
                            id: closer_type
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                MDLabel:
                    text: ''
                    halign: 'left'
                    size_hint_y: None
                    height: dp(25)
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: "48dp"
                    spacing:dp(15)
                    padding: dp(10)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    CheckBox:
                        id: check_box
                        size_hint: None, None
                        size: "30dp", "30dp"
                        bold: True
                        active: False
                        on_active: root.checkbox_callback1(self, self.active)
                        color: 0.043, 0.145, 0.278, 1 

                    MDLabel:
                        text: "I Agree Terms and Conditions"
                        multiline: False  
                        size: "30dp", "30dp"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
                        halign: "left"
                        valign: "center" 
                MDLabel:
                    text: ''
                    halign: 'left'
                    size_hint_y: None
                    height: dp(45)            
                MDBoxLayout:
                    orientation: 'horizontal'
                    spacing: dp(30)
                    padding: dp(30)
                    size_hint_y: None
                    height: self.minimum_height
                    canvas.before:
                        Color:
                            rgba: 249/255, 249/255, 247/255, 1 
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [25, 25, 25, 25]   
                    MDRaisedButton:
                        text: "BACK"
                        md_bg_color: 0.043, 0.145, 0.278, 1 
                        on_release: root.on_back()
                        text_color: 1, 1, 1, 1
                        size_hint: 1, None


                    MDRaisedButton:
                        id: foreclose_button
                        text: "FORECLOSE"
                        md_bg_color: 0.043, 0.145, 0.278, 1 
                        on_release: root.on_foreclose_press()
                        size_hint: 1, None


<ForecloseDetails>
    GridLayout:
        cols: 1 
        ScrollView:
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height 

                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(50)
                    padding: dp(30)
                    size_hint_y: None
                    height: self.minimum_height
                    canvas.before:
                        Color:
                            rgba: 230/255, 245/255, 255/255, 1 
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [1, 1, 1, 1]
                            source: "background.jpg"

                    MDLabel:
                        text: "Foreclosure  Details"
                        bold: True

                    Widget:
                        size_hint_y: None
                        height: dp(2)  
                        canvas:
                            Color:
                                rgba: 0, 0, 0, 1 
                            Line:
                                points: self.x, self.y, self.x + self.width, self.y
                    MDLabel:
                        text: "Amount paid"
                        bold: True

                    GridLayout:
                        cols: 2
                        size_hint_y: None
                        padding: dp(10)
                        spacing: dp(43)  

                        MDLabel:
                            text: "Total amount Paid "
                            halign: 'left' 
                            bold: True

                        MDLabel:
                            id: totalamount
                            halign: 'left'
                            theme_text_color: 'Custom' 
                            text_color: 140/255, 140/255, 140/255, 1

                        MDLabel:
                            text: "Monthly installment"
                            halign: "left"

                        MDLabel:
                            id: monthly_installment
                            halign: 'left'
                            theme_text_color: 'Custom' 
                            text_color: 140/255, 140/255, 140/255, 1

                        MDLabel:
                            text: "Interest Amount"
                            halign: "left"

                        MDLabel:
                            id: interest_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1

                        MDLabel:
                            text: "Monthly EMI"
                            halign: "left"

                        MDLabel:
                            id: monthly_emi1
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDLabel:
                        text: ""
                        size_hint_y: None
                        height: dp(2)

                    Widget:
                        size_hint_y: None
                        canvas:
                            Color:
                                rgba: 0, 0, 0, 1 
                            Line:
                                points: self.x, self.y, self.x + self.width, self.y

                    MDLabel:
                        text: "Loan Closure Amount"
                        bold: True
                    GridLayout:
                        cols: 2
                        size_hint_y: None
                        padding: dp(6)
                        spacing: dp(53)
                        height:dp(70)

                        MDLabel:
                            text: "Over all Outstanding Amount"
                            halign: "left"
                            bold: True

                        MDLabel:
                            id: overall_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                        MDLabel:
                            text: "Over all Monthly installment"
                            halign: "left"

                        MDLabel:
                            id: over_month
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                        MDLabel:
                            text: "Overall Interest Amount "
                            halign: "left"

                        MDLabel:
                            id: overall_interest_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1

                        MDLabel:
                            text: "Total Amount"
                            halign: "left"

                        MDLabel:
                            id: total_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDLabel:
                        text: ""
                        size_hint_y: None
                        height: dp(6)

                    Widget:
                        size_hint_y: None
                        canvas:
                            Color:
                                rgba: 0, 0, 0, 1 
                            Line:
                                points: self.x, self.y, self.x + self.width, self.y

                    MDLabel:
                        text: "Amount Due"
                        halign: "left"
                        bold: True

                    GridLayout:
                        cols: 2
                        size_hint_y: None
                        padding: dp(6)
                        spacing: dp(43)
                        height:dp(70)

                        MDLabel:
                            text: "Outstanding Amount"
                            halign: "left"
                            
                        MDLabel:
                            id: outstanding_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1

                        MDLabel:
                            text: "Foreclosure Fee "
                            halign: "left"

                        MDLabel:
                            id: foreclosure_fee
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1

                        MDLabel:
                            text: "Foreclosure Amount"
                            halign: "left"

                        MDLabel:
                            id: foreclosure_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1

                        MDLabel:
                            text: "Total Due Amount"
                            halign: "left"
                            bold: True

                        MDLabel:
                            id: total_due_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDLabel:
                        text: ""
                        size_hint_y: None
                        height: dp(2)
                Widget:
                    size_hint_y: None
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 0 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: "75dp"
                    spacing:dp(15)
                    padding: dp(10)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                    MDLabel:
                        text: 'Reason for Foreclosure '
                        valign: 'top'
                        bold: True

                    MDTextField:
                        id: reason
                        hint_text: 'Enter text here'

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: "48dp"
                    spacing:dp(15)
                    padding: dp(10)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                    CheckBox:
                        id: check
                        size_hint: None, None
                        size: "30dp", "30dp"
                        bold: True
                        active: False 
                        color: (195/255, 110/255, 108/255, 1)
                        on_active: root.checkbox_callback(self, self.active)

                    MDLabel:
                        text: "I Agree Terms and Conditions"
                        multiline: False  
                        size: "30dp", "30dp"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
                        halign: "left"
                        valign: "center"  

                MDLabel:
                    text: ""

                MDBoxLayout:
                    orientation: 'horizontal'
                    spacing: dp(30)
                    padding: dp(30)
                    size_hint_y: None
                    height: self.minimum_height
                    canvas.before:
                        Color:
                            rgba: 249/255, 249/255, 247/255, 1 
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [25, 25, 25, 25]

                    MDRaisedButton:
                        text: "CANCEL"
                        md_bg_color: 0.043, 0.145, 0.278, 1 
                        theme_text_color: 'Custom'
                        on_release: app.root.current = 'ViewProfileScreenFB'
                        text_color: 1, 1, 1, 1
                        size_hint: 1, None

                    MDRaisedButton:
                        text: "SUBMIT"
                        id : submit
                        md_bg_color: 0.043, 0.145, 0.278, 1 
                        on_release: root.add_data(outstanding_amount.text, foreclosure_fee.text, foreclosure_amount.text, reason.text , total_due_amount.text, totalamount.text , monthly_emi1.text)
                        size_hint: 1, None




'''
Builder.load_string(loan_forecloseB)
date = datetime.today()
print(date)


class LoansDetailsB(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_loan_details.search()
        email = self.get_table()
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        product_name = []
        loan_id = []
        email1 = []
        borrower_name = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            product_name.append(i['product_name'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            email1.append(i['borrower_email_id'])

        profile_customer_id = []
        profile_mobile_number = []
        profile_email_id = []

        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            profile_email_id.append('email_user')

        cos_id = None
        index = -1
        if email in profile_email_id:
            index = profile_email_id.index(email)

        if email in email1:
            index = email1.index(email)
            cos_id = customer_id[index]

        if cos_id is not None:
            print(cos_id, type(cos_id))
            print(customer_id[-1], type(customer_id[-1]))
            c = -1
            index_list = []
            for i in range(s):
                c += 1
                if customer_id[c] == cos_id and loan_status[c] == 'disbursed':
                    index_list.append(c)

            b = 1
            k = -1
            for i in reversed(index_list):
                b += 1
                k += 1
                number = profile_customer_id.index(customer_id[i])
                item = ThreeLineAvatarIconListItem(
                    IconLeftWidget(
                        icon="card-account-details-outline"
                    ),
                    text=f"Borrower Name : {borrower_name[i]}",
                    secondary_text=f"Borrower Mobile Number : {profile_mobile_number[number]}",
                    tertiary_text=f"Product Name : {product_name[i]}",
                    text_color=(0, 0, 0, 1),  # Black color
                    theme_text_color='Custom',
                    secondary_text_color=(0, 0, 0, 1),
                    secondary_theme_text_color='Custom',
                    tertiary_text_color=(0, 0, 0, 1),
                    tertiary_theme_text_color='Custom'
                )
                # Create a lambda function with loan_id as an argument
                item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
                self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
            # Handle the on_release event here
            value = instance.text.split(':')[-1].strip()
            data = app_tables.fin_loan_details.search()

            sm = self.manager

            # Create a new instance of the LoginScreen
            approved = ViewProfileScreenFB(name='ViewProfileScreenFB')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(approved)

            # Switch to the LoginScreen
            sm.current = 'ViewProfileScreenFB'
            self.manager.get_screen('ViewProfileScreenFB').initialize_with_value(loan_id, data)

    def go_back(self):
        self.manager.current = 'DashboardScreen'

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

class ViewProfileScreenFB(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check_box = None

    def checkbox_callback1(self, checkbox, value):
        if value:
            self.check_box = True
        else:
            self.check_box = False
    def initialize_with_value(self, value, data):
        self.loan_id = value
        emi1 = app_tables.fin_emi_table.search()
        pro_details = app_tables.fin_product_details.search()
        loan_id = []
        loan_amount = []
        email1 = []
        name = []
        tenure = []
        interest = []
        credit = []
        min_months = []

        for i in data:
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            email1.append(i['borrower_email_id'])
            name.append(i['borrower_full_name'])
            tenure.append(i['tenure'])
            interest.append(i['interest_rate'])
            credit.append(i['credit_limit'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.amount.text = str(loan_amount[index])
            self.ids.name.text = str(name[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.interest.text = str(interest[index])
            self.ids.limit.text = str(credit[index])

            emi_loan = [i['emi_number'] for i in emi1 if i['loan_id'] == value]
            print(emi_loan)
            if emi_loan:
                highest_number = max(emi_loan)
                total_payment = highest_number
            else:
                total_payment = 0

            self.ids.total_payment.text = str(total_payment)

            foreclose_type = [i['foreclose_type'] for i in pro_details if
                              i['product_id'] == data[index]['product_id']]
            print(foreclose_type)
            if foreclose_type:
                foreclose_value = foreclose_type[0]
                self.ids.closer_type.text = str(foreclose_value)

                if foreclose_value == 'Eligible':
                    self.ids.foreclose_button.disabled = False
                else:
                    self.ids.foreclose_button.disabled = True
                    self.show_success_dialog(f"This Foreclose Value need to be Eligible")

            minimum_months = [i['min_months'] for i in pro_details if i['product_id'] == data[index]['product_id']]
            print(minimum_months)
            print(emi_loan)
            if total_payment >= minimum_months[0]:
                self.ids.foreclose_button.disabled = False
            else:
                self.ids.foreclose_button.disabled = True

            print(minimum_months[0], total_payment)

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

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.on_back_button_press()
            return True
        return False

    def on_back_button_press(self):
        self.manager.current = 'LoansDetailsB'

    def on_back(self):
        self.manager.current = 'LoansDetailsB'

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"

    def on_foreclose_press(self):
        if self.check_box == True:
            sm = self.manager

            # Create a new instance of the LoginScreen
            approved = ForecloseDetails(name='ForecloseDetails')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(approved)

            # Switch to the LoginScreen
            sm.current = 'ForecloseDetails'
            self.manager.get_screen('ForecloseDetails').initialize_with_value(self.loan_id)
        else:
            self.show_validation_error(f"You have to click on check box to proceed")

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

class ForecloseDetails(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check = None

    def checkbox_callback(self, checkbox, value):
        if value:
            self.check = True
        else:
            self.check = False

    def initialize_with_value(self, value):
        self.loan_id = value
        data1 = app_tables.fin_foreclosure.search()
        data = app_tables.fin_loan_details.search()
        pro = app_tables.fin_product_details.search()
        emi1 = app_tables.fin_emi_table.search()
        profile = app_tables.fin_user_profile.search()
        loan_id = []
        request_on = []

        index2 = -1
        for i in data1:
            loan_id.append(i['loan_id'])
            request_on.append(i['requested_on'])

        month_emi = []
        loan_id1 = []
        loan_amount = []
        tenure = []
        for i in data:
            month_emi.append(i['monthly_emi'])
            loan_id1.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            tenure.append(i['tenure'])

        emi_num = []
        loan_id2 = []
        for i in emi1:
            emi_num.append(i['emi_number'])
            loan_id2.append(i['loan_id'])

        if value in loan_id1:
            index = loan_id1.index(value)

        if value in loan_id1:
            index2 = loan_id1.index(value)
            self.ids.monthly_emi1.text = str(month_emi[index2])

        for i in emi1:
            if i['loan_id'] == value:
                emi_num = i['emi_number']
                break

        total_payment = 0
        emi_loan = [i['emi_number'] for i in emi1 if i['loan_id'] == value]
        print(emi_loan)
        if emi_loan:
            number = max(emi_loan)
            total_payment = number
            total_amount = month_emi[index2] * total_payment
            print(month_emi[index2], total_payment)
            self.ids.totalamount.text = str(total_amount)

        if value in loan_id1:
            index3 = loan_id1.index(value)
            monthly_installment = loan_amount[index3] / tenure[index3]
            print(loan_amount[index3], tenure[index3])
            monthly_installment = round(monthly_installment, 2)
            self.ids.monthly_installment.text = str(monthly_installment)

        if value in loan_id1:
            index4 = loan_id1.index(value)
            interest_amount = month_emi[index4] - monthly_installment
            print(month_emi[index4], monthly_installment)
            interest_amount = round(interest_amount, 2)
            self.ids.interest_amount.text = str(interest_amount)

        if value in loan_id1:
            index5 = loan_id1.index(value)
            overall_outstanding_amount = loan_amount[index5] - (monthly_installment * total_payment)
            print(loan_amount[index5], monthly_installment, total_payment)
            overall_outstanding_amount = round(overall_outstanding_amount, 2)
            self.ids.overall_amount.text = str(overall_outstanding_amount)

        if value in loan_id1:
            index6 = loan_id1.index(value)
            outstanding_months = tenure[index6] - total_payment
            overall_monthly_installment = monthly_installment * outstanding_months
            print(monthly_installment, outstanding_months)
            overall_monthly_installment = round(overall_monthly_installment, 2)
            self.ids.over_month.text = str(overall_monthly_installment)

        if value in loan_id1:
            index7 = loan_id1.index(value)
            interest_amount_per_month = month_emi[index7] - monthly_installment
            overall_interest_amount = interest_amount_per_month * outstanding_months
            print(interest_amount_per_month, outstanding_months)
            overall_interest_amount = round(overall_interest_amount, 2)
            self.ids.overall_interest_amount.text = str(overall_interest_amount)

        if value in loan_id1:
            total_amount1 = overall_outstanding_amount + overall_interest_amount
            rounded_total_amount = round(total_amount1, 2)
            self.ids.total_amount.text = str(rounded_total_amount)
            outstanding_amount1 = overall_outstanding_amount
            self.ids.outstanding_amount.text = str(outstanding_amount1)

        product_id1 = []
        for product in data:
            product_id1.append(product['product_id'])
            print(product_id1)
        product_id2 = []
        foreclose_fee = []
        for product in pro:
            product_id2.append(product['product_id'])
            foreclose_fee.append(product['foreclosure_fee'])

        if value in loan_id:
            index10 = loan_id.index(value)
            print(product_id1[index10])

        index10 = -1

        if product_id1[index10] in product_id2:
            index11 = product_id1.index(product_id1[index10])
            self.ids.foreclosure_fee.text = str(foreclose_fee[index11])
            print(foreclose_fee[index11])
            foreclose_amount = overall_outstanding_amount * (foreclose_fee[index11] / 100)
            foreclose_amount = round(foreclose_amount, 2)
            print(overall_outstanding_amount, foreclose_fee[index11])
            self.ids.foreclosure_amount.text = str(foreclose_amount)
            total_due_amount = overall_outstanding_amount + foreclose_amount
            total_due_amount = round(total_due_amount, 2)
            self.ids.total_due_amount.text = str(total_due_amount)

    date = datetime.today()

    def add_data(self, outstanding_amount, foreclose_fee, foreclose_amount, reason, total_due_amount, totalamount, monthly_emi1):
        loan_id = self.loan_id
        index = 0
        if len(self.ids.reason.text) < 3:
            self.show_validation_error('You Must need to enter a reason for foreclosure')
            return
        if self.check != True:
            self.show_validation_error('You need to select Terms and Conditions')
            return
        data = app_tables.fin_loan_details.search()
        data1 = app_tables.fin_emi_table.search()
        loan_id3 = []
        interest_rate = []
        borrower_name1 = []
        loan_amount = []

        for i in data:
            loan_id3.append(i['loan_id'])
            interest_rate.append(i['interest_rate'])
            borrower_name1.append(i['borrower_full_name'])
            loan_amount.append(i['loan_amount'])
        if loan_id in loan_id3:
            index = loan_id3.index(loan_id)

        emi_number = []
        loan_id4 = []

        for i in data1:
            emi_number.append(i['emi_number'])
            loan_id4.append(i['loan_id'])
        if loan_id in loan_id4:
            index = loan_id4.index(loan_id)
            highest_number = max(emi_number) if emi_number else 0
            total_payment = highest_number

            print(loan_id, outstanding_amount, foreclose_amount, foreclose_fee, interest_rate[index], reason,
                  total_due_amount, borrower_name1[index], loan_amount[index], totalamount, monthly_emi1, date,total_payment )
            app_tables.fin_foreclosure.add_row(loan_id=loan_id, outstanding_amount=float(outstanding_amount),
                                               foreclose_fee=float(foreclose_fee),
                                               foreclose_amount=float(foreclose_amount),
                                               reason=reason, status='under process',
                                               total_due_amount=float(total_due_amount),
                                               paid_amount= float(totalamount),
                                               emi_amount=float(monthly_emi1),
                                               requested_on=date,
                                               foreclosure_emi_num=total_payment,
                                               interest_rate=interest_rate[index],
                                               borrower_name=borrower_name1[index],
                                               loan_amount=loan_amount[index])
        data[index]['loan_updated_status'] = 'foreclosure'
        self.show_success_dialog(f"Your foreclosure request has been successfully submitted. You will receive a notification once it is approved.")

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
    def open_dashboard_screen(self, dialog):

        dialog.dismiss()
        self.manager.current = 'DashboardScreen'
class MyScreenManager(ScreenManager):
    pass


