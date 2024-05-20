import anvil
from anvil.tables import app_tables
from kivy import properties
from pytz import utc
from kivy.core.window import Window
from kivy.properties import ListProperty, Clock
from kivy.uix.modalview import ModalView
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget, TwoLineAvatarIconListItem
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
import sqlite3
from math import pow
from kivymd.uix.dialog import MDDialog, dialog
import anvil.server
from kivy.uix.spinner import Spinner
from datetime import datetime, timezone, timedelta, date

from kivymd.uix.spinner import MDSpinner
import anvil.tables.query as q
from borrower_wallet import WalletScreen
from datetime import datetime

user_helpers2 = """
<WindowManager>:
    BorrowerDuesScreen:
    DuesScreen:
    LastScreenWallet:
    PartPayment:
<DuesScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title:"Today's Dues"
            elevation: 2
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container 


<BorrowerDuesScreen>:
    GridLayout:
        cols: 1

        MDTopAppBar:
            title:"Today's Dues"
            md_bg_color:0.043, 0.145, 0.278, 1
            theme_text_color: 'Custom'
            text_color: 1,1,1,1 
            size_hint:1,None
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['wallet']]
            pos_hint: {'top': 1} 

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

                MDLabel:
                    id: loan_amount1
                    halign: 'left'
                    bold: True
                    text_color: 140/255, 140/255, 140/255, 1
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
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: name
                    halign: 'left'
                    text_color: 140/255, 140/255, 140/255, 1    
                
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Tenure'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: tenure
                    halign: 'left'
                    text_color: 140/255, 140/255, 140/255, 1
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Interest Rate'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: interest_rate
                    halign: 'left'
                    text_color: 140/255, 140/255, 140/255, 1
                    
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Account Number'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: account_number
                    halign: 'left'
                    text_color: 140/255, 140/255, 140/255, 1
                    
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Emi Amount'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: emi_amount
                    halign: 'left'
                    text_color: 140/255, 140/255, 140/255, 1
                    
            MDGridLayout:
                cols: 2
                MDLabel:
                    id: extra
                    text: 'Extra Payment'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: extra_amount
                    halign: 'left'
                    text_color: 140/255, 140/255, 140/255, 1
            
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Total Amount'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: total_amount
                    halign: 'left'
                    text_color: 140/255, 140/255, 140/255, 1
        
        MDLabel:
            text: ''
            halign: 'left'
            size_hint_y: None
            height: dp(55)
            
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
                text: "Part Payment"
                md_bg_color:0.043, 0.145, 0.278, 1
                on_release: root.go_to_part_payment()
                pos_hint: {'center_x': 0.5, 'center_y': 2}
                size_hint: 0.4, None 
                font_name:"Roboto-Bold"
                font_size:dp(15) 
                     
            MDRaisedButton:
                text: "Pay Now"
                md_bg_color:0.043, 0.145, 0.278, 1
                on_release: root.go_to_paynow()
                pos_hint: {'center_x': 0.5, 'center_y': 2}
                size_hint: 0.4, None 
                font_name:"Roboto-Bold"
                font_size:dp(15) 
<PartPayment>          
    GridLayout:
        cols: 1
        MDTopAppBar:
            title: "Part Payment"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1 
            title_align: 'left'

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
                            source: "E:\photo10.jpg"
                    MDGridLayout:
                        cols: 2
        
                        MDLabel:
                            text: 'Loan Amount:'
                            halign: 'left'
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                    MDGridLayout:
                        cols: 2
                        MDIconButton:
                            icon: 'currency-inr'
                            halign: 'left'
                            size_hint_y: None
                            height: dp(1)
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
        
                        MDLabel:
                            id: amount
                            halign: 'left'
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    
                    MDLabel:
                        text: ''
                        halign: 'left'
                        size_hint_y: None
                        height: dp(5)

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Borrower Name"
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: name
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout: 
                        cols: 2    
                        MDLabel:
                            text: "Tenure" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: tenure
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout: 
                        cols: 2       
                        MDLabel:
                            text: "Interest Amount" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: interest
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout: 
                        cols: 2 
                        MDLabel:
                            text: "Account number" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: account_number
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout: 
                        cols: 2 
                        MDLabel:
                            text: "Emi Amount" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: emi_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    
                    MDGridLayout: 
                        cols: 2 
                        MDLabel:
                            text: "Remaining Amount" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: remain_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout: 
                        cols: 2 
                        MDLabel:
                            text: "Total Amount" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: total_amount1
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            
                    MDGridLayout: 
                        cols: 2 
                        MDLabel:
                            text: "Amount" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: amount1
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                MDLabel:
                    text: ''
                    halign: 'left'
                    size_hint_y: None
                    height: dp(55)
                    
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
                        text: "Back"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        on_release: root.reject_request()
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1, 1
                        size_hint: 1, 1

                    MDRaisedButton:
                        text: "Pay Now"
                        theme_text_color: 'Custom'
                        on_release: root.accept_request() 
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        size_hint: 1, 1

<LastScreenWallet>:
    MDTopAppBar:
        title: "Today Due Request Submitted"
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
            text: "The payment has been successfully completed. Your transaction has been processed"
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

"""
Builder.load_string(user_helpers2)


class BorrowerDuesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize_with_value(self, value, shechule_date):
        print(value)
        self.loan_id = value
        today_date = datetime.now(tz=utc).date()
        emi_data = app_tables.fin_emi_table.search()
        emi_loan_id = []
        emi_num = []
        next_payment = []
        for i in emi_data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])

        product = app_tables.fin_product_details.search()
        product_id = []
        lapsed_fee = []
        default_fee_percentage = []
        default_fee_amount = []
        npa_percentage = []
        npa_fee_amount = []
        default_type = []
        npa_type = []

        for i in product:
            product_id.append(i['product_id'])
            lapsed_fee.append(i['lapsed_fee'])
            default_fee_percentage.append(i['default_fee'])
            default_fee_amount.append(i['default_fee_amount'])
            default_type.append(i['default_select_percentage_amount'])
            npa_percentage.append(i['npa'])
            npa_fee_amount.append(i['npa_amount'])
            npa_type.append(i['npa_select_percentage_amount'])
        data1 = app_tables.fin_loan_details.search()
        user_profile = app_tables.fin_user_profile.search()

        loan_id = []
        borrower_name = []
        cos_id1 = []
        loan_amount = []
        loan_amount_1 = []
        loan_status = []
        tenure = []
        interest = []
        monthly_emi = []
        emi_pay_type = []
        total_int_amount = []
        total_pro_fee_amount = []
        total_repay = []
        shedule_payment = []
        loan_product = []
        for i in data1:
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            cos_id1.append(i['borrower_customer_id'])
            loan_amount.append(i['loan_amount'])
            loan_amount_1.append(i['loan_amount'])
            loan_status.append(i['loan_updated_status'])
            tenure.append(i['tenure'])
            interest.append(i['interest_rate'])
            monthly_emi.append(i['monthly_emi'])
            emi_pay_type.append(i['emi_payment_type'])
            total_int_amount.append(i['total_interest_amount'])
            total_pro_fee_amount.append(i['total_processing_fee_amount'])
            total_repay.append(i['total_repayment_amount'])
            shedule_payment.append(i['first_emi_payment_due_date'])
            loan_product.append(i['product_id'])
        index = 0

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.name.text = str(borrower_name[index])
            self.ids.loan_amount1.text = str(loan_amount[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.interest_rate.text = str(interest[index])
            self.ids.emi_amount.text = str(monthly_emi[index])

        cos_id = []
        account_num = []
        for i in user_profile:
            cos_id.append(i['customer_id'])
            account_num.append(i['account_number'])

        if cos_id1[index] in cos_id:
            index1 = cos_id1.index(cos_id1[index])
            self.ids.account_number.text = str(account_num[index1])

        extend_row = None
        extend_amount = 0
        foreclose_amount1 = 0
        emi_amount1 = 0
        new_emi_amount = 0

        if loan_status[index] == "disbursed":
            extra_amount = 0
            print(loan_status[index])
            print(extra_amount)
            if (today_date - shechule_date[value]).days >= 6 and (today_date - shechule_date[value]).days < 16:
                days_left = (today_date - shechule_date[value]).days
                if days_left > 6:
                    days_left = (today_date - shechule_date[value]).days - 7
                else:
                    days_left = 0
                product_index = product_id.index(loan_product[index])
                lapsed_percentage = lapsed_fee[product_index] + days_left
                lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                print(lapsed_amount)
                print(lapsed_percentage)
                print(days_left)
                total_amount = monthly_emi[index] + extra_amount
                self.ids.extra.text = "Extra Payment (Late payment Fee)"
                self.ids.extra_amount.text = str(round(extra_amount + lapsed_amount, 2))
                self.ids.total_amount.text = str(round(total_amount + lapsed_amount, 2))
                data1[index]['loan_state_status'] = "lapsed"


            elif (today_date - shechule_date[value]).days >= 16 and (today_date - shechule_date[value]).days < 106:
                default_amount = 0
                days_left = (today_date - shechule_date[value]).days - 17
                product_index = product_id.index(loan_product[index])
                default_percentage = default_fee_percentage[product_index] + days_left
                print(days_left)
                print(default_percentage)
                if default_type[product_index] == 'Default fee (%)':
                    default_amount = (monthly_emi[index] * default_percentage) / 100
                elif default_type[product_index] == 'Default fee (₹)':
                    default_amount = default_fee_amount[product_index] * days_left

                total_amount = monthly_emi[index] + extra_amount
                self.ids.extra.text = "Extra Payment(Default)"
                self.ids.extra_amount.text = str(round(extra_amount + default_amount, 2))
                self.ids.total_amount.text = str(round(total_amount + default_amount, 2))
                data1[index]['loan_state_status'] = 'default'
                print(default_amount)
                print(default_type[product_index] == 'Non Performing Asset (%)')
                print(default_type[product_index] == 'Non Performing Asset (₹)')
                print(default_type[product_index])

            elif (today_date - shechule_date[value]).days >= 106:
                npa_amount = 0
                days_left = (today_date - shechule_date[value]).days - 107
                product_index = product_id.index(loan_product[index])
                npa_percentage = npa_percentage[product_index] + days_left
                print(npa_percentage)
                print(days_left)
                if npa_type[product_index] == 'Non Performing Asset (%)':
                    npa_amount = (monthly_emi[index] * npa_percentage) / 100
                elif npa_type[product_index] == 'Non Performing Asset (₹)':
                    npa_amount = default_fee_amount[product_index]
                total_amount = monthly_emi[index] + extra_amount
                self.ids.extra.text = "Extra Payment(NPA)"
                self.ids.extra_amount.text = str(round(extra_amount + npa_amount, 2))
                self.ids.total_amount.text = str(round(total_amount + npa_amount, 2))
                data1[index]['loan_state_status'] = 'npa'

            else:
                total_amount = monthly_emi[index] + extra_amount
                self.ids.extra_amount.text = str(round(extra_amount, 2))
                self.ids.total_amount.text = str(round(total_amount))
                self.ids.extra.text = "Extra Payment "


        elif loan_status[index] == "extension":
            emi_num = 0
            emi_data = app_tables.fin_emi_table.search(loan_id=str(value))
            if emi_data:
                emi = emi_data[0]
                emi_number = emi['emi_number']
            print(loan_status[index])
            extend_row = app_tables.fin_extends_loan.get(
                loan_id=str(value),
                emi_number=emi_number
            )
            if extend_row is not None and extend_row['status'] == "approved":
                extend_amount += extend_row['extension_amount']
                new_emi_amount += extend_row['new_emi']
                total_amount = new_emi_amount + extend_amount
                print(new_emi_amount, extend_amount)
                print(extend_amount)
                next_emi_num = emi_number + 1
                next_emi = app_tables.fin_emi_table.get(loan_id=str(value), emi_number=next_emi_num)

                if next_emi is not None:
                    next_payment_amount = next_emi['amount_paid']
                    extend_amount += next_payment_amount
                if (today_date - shechule_date[value]).days >= 6 and (today_date - shechule_date[value]).days < 16:
                    days_left = (today_date - shechule_date[value]).days
                    if days_left > 6:
                        days_left = (today_date - shechule_date[value]).days - 7
                    else:
                        days_left = 0
                    product_index = product_id.index(loan_product[index])
                    lapsed_percentage = lapsed_fee[product_index] + days_left
                    lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                    self.ids.extra_amount.text = str(round(extend_amount + lapsed_amount, 2))
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(round(total_amount + lapsed_amount, 2))
                    self.ids.extra.text = "Extra Payment (Late payment Fee)"
                    data1[index]['loan_state_status'] = "lapsed"
                elif (today_date - shechule_date[value]).days >= 16 and (today_date - shechule_date[value]).days < 98:
                    default_amount = 0
                    days_left = (today_date - shechule_date[value]).days - 17
                    product_index = product_id.index(loan_product[index])
                    default_percentage = default_fee_percentage[product_index] + days_left
                    print(default_percentage)
                    print(days_left)
                    if default_type[product_index] == 'Default fee (%)':
                        default_amount = (monthly_emi[index] * default_percentage) / 100
                    elif default_type[product_index] == 'Default fee (₹)':
                        default_amount = default_fee_amount[product_index]
                    self.ids.extra_amount.text = str(round(extend_amount + default_amount, 2))
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(round(total_amount + default_amount, 2))
                    self.ids.extra.text = "Extra Payment (Default)"
                    data1[index]['loan_state_status'] = "default"
                    print(default_amount)

                elif (today_date - shechule_date[value]).days >= 106:
                    npa_amount = 0
                    days_left = (today_date - shechule_date[value]).days - 107
                    product_index = product_id.index(loan_product[index])
                    npa_percentage = npa_percentage[product_index] + days_left
                    print(npa_percentage)
                    print(days_left)
                    if npa_type[product_index] == 'Non Performing Asset (%)':
                        npa_amount = (monthly_emi[index] * npa_percentage) / 100
                    elif npa_type[product_index] == 'Non Performing Asset (₹)':
                        npa_amount = default_fee_amount[product_index]
                    self.ids.extra_amount.text = str(round(extend_amount + npa_amount, 2))
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(round(total_amount + npa_amount, 2))
                    self.ids.extra.text = "Extra Payment (Default)"
                    data1[index]['loan_state_status'] = 'npa'
                else:
                    self.ids.extra_amount.text = str(round(extend_amount))
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(round(total_amount))
                    self.ids.extra.text = "Extra Payment"
                print(extend_amount, new_emi_amount, total_amount)

        elif loan_status[index] == "foreclosure":
            print(loan_status[index])
            foreclosure_row = app_tables.fin_foreclosure.get(
                loan_id=str(value)
            )
            if foreclosure_row is not None and foreclosure_row['status'] == 'approved':
                foreclose_amount1 += foreclosure_row['foreclose_amount']
                emi_amount1 += foreclosure_row['total_due_amount']
                total_amount = foreclose_amount1 + emi_amount1
                print(foreclose_amount1, emi_amount1)
                print(emi_amount1)
                print(foreclose_amount1)
                if (today_date - shechule_date[value]).days >= 6 and (today_date - shechule_date[value]).days < 16:
                    days_left = (today_date - shechule_date[value]).days
                    if days_left > 6:
                        days_left = (today_date - shechule_date[value]).days - 7
                    else:
                        days_left = 0
                    product_index = product_id.index(loan_product[index])
                    lapsed_percentage = lapsed_fee[product_index] + days_left
                    lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                    self.ids.extra_amount.text = str(round(foreclose_amount1 + lapsed_amount, 2))
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(round(total_amount + lapsed_amount, 2))
                    self.ids.total.text = "Total Amount (Late payment Fee)"
                    data1[index]['loan_state_status'] = "lapsed"
                    data1[index]['loan_updated_status'] = "closed"
                    emi_data[index]['next_payment'] = None

                elif (today_date - shechule_date[value]).days >= 16 and (today_date - shechule_date[value]).days < 106:
                    default_amount = 0
                    days_left = (today_date - shechule_date[value]).days - 17
                    product_index = product_id.index(loan_product[index])
                    default_percentage = default_fee_percentage[product_index] + days_left
                    print(default_percentage)
                    print(days_left)
                    if default_type[product_index] == 'Default fee (%)':
                        default_amount = (monthly_emi[index] * default_percentage) / 100
                    elif default_type[product_index] == 'Default fee (₹)':
                        default_amount = default_fee_amount[product_index]
                    self.ids.extra_amount.text = str(round(foreclose_amount1 + default_amount, 2))
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(round(total_amount + default_amount, 2))
                    self.ids.total.text = "Total Amount (Default)"
                    data1[index]['loan_state_status'] = "default"
                    data1[index]['loan_updated_status'] = "closed"

                elif (today_date - shechule_date[value]).days >= 106:
                    npa_amount = 0
                    days_left = (today_date - shechule_date[value]).days - 107
                    product_index = product_id.index(loan_product[index])
                    npa_percentage = npa_percentage[product_index] + days_left
                    print(npa_percentage)
                    print(days_left)
                    if npa_type[product_index] == 'Non Performing Asset (%)':
                        npa_amount = (monthly_emi[index] * npa_percentage) / 100
                    elif npa_type[product_index] == 'Non Performing Asset (₹)':
                        npa_amount = default_fee_amount[product_index]
                    self.ids.extra_amount.text = str(round(foreclose_amount1 + npa_amount, 2))
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(round(total_amount + npa_amount, 2))
                    self.ids.extra.text = "Extra Payment (Default)"
                    data1[index]['loan_state_status'] = "default"
                    data1[index]['loan_updated_status'] = "closed"

                else:
                    self.ids.extra.text = "Extra Payment"
                    self.ids.extra_amount.text = str(round(foreclose_amount1))
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(round(total_amount))
                    data1[index]['loan_updated_status'] = "closed"

    def go_to_paynow(self):
        emi_data = app_tables.fin_emi_table.search()
        emi_loan_id = []
        emi_num = []
        next_payment = []
        paid_amount = []
        for i in emi_data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])
            paid_amount.append(i['amount_paid'])

        value = self.loan_id
        data1 = app_tables.fin_loan_details.search()
        wallet = app_tables.fin_wallet.search()
        total = self.ids.total_amount.text
        extra_amount = self.ids.extra_amount.text
        user_profile = app_tables.fin_user_profile.search()
        tenure = self.ids.tenure.text

        emi_number = 0

        if value not in emi_loan_id:
            emi_number = 1
        else:
            last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(value)
            emi_number = emi_num[last_index] + 1

        schedule_date = []
        loan_id = []
        cos_id1 = []
        emi_type_pay = []
        lender_customer_id = []
        borrower_email = []
        lender_email = []
        total_repay_amount = []
        for i in data1:
            loan_id.append(i['loan_id'])
            cos_id1.append(i['borrower_customer_id'])
            schedule_date.append(i['first_emi_payment_due_date'])
            emi_type_pay.append(i['emi_payment_type'])
            lender_customer_id.append(i['lender_customer_id'])
            borrower_email.append(i['borrower_email_id'])
            lender_email.append(i['lender_email_id'])
            total_repay_amount.append(i['total_repayment_amount'])

        cos_id = []
        account_num = []

        for i in user_profile:
            cos_id.append(i['customer_id'])
            account_num.append(i['account_number'])
        index = 0
        if cos_id1[index] in cos_id:
            index2 = cos_id1.index(cos_id1[index])
            self.ids.account_number.text = str(account_num[index2])

        wallet_customer_id = []
        wallet_amount = []
        for i in wallet:
            wallet_customer_id.append(i['customer_id'])
            wallet_amount.append(i['wallet_amount'])

        lender_customer_id = []
        loan_id_list = []
        for i in data1:
            loan_id_list.append(i['loan_id'])
            lender_customer_id.append(i['lender_customer_id'])

        index = 0
        if value in loan_id:
            index = loan_id.index(value)

        next_payment_date = None
        b_index = 0
        l_index = 0

        index1 = 0
        print(lender_customer_id[index] in wallet_customer_id and int(cos_id1[index]) in wallet_customer_id)
        if lender_customer_id[index] in wallet_customer_id and int(cos_id1[index]) in wallet_customer_id:
            b_index = wallet_customer_id.index(int(cos_id1[index]))
            l_index = wallet_customer_id.index(lender_customer_id[index])
        print(b_index, l_index)
        print(value)
        print(wallet_amount[b_index], float(total))
        print(wallet_amount[b_index] >= float(total))
        print(wallet[b_index]['wallet_amount'])
        if wallet[b_index]['wallet_amount'] >= float(total):
            wallet[b_index]['wallet_amount'] -= float(total)
            wallet[l_index]['wallet_amount'] += float(total)

            if emi_type_pay[index].strip() == 'Monthly':
                next_payment_date = schedule_date[index] + timedelta(days=30)
                print(schedule_date[index])
            elif emi_type_pay[index].strip() == 'Three Months':
                next_payment_date = schedule_date[index] + timedelta(days=90)
            elif emi_type_pay[index].strip() == 'Six Months':
                next_payment_date = schedule_date[index] + timedelta(days=180)
            elif emi_type_pay[index].strip() == 'One Time':
                if tenure:
                    next_payment_date = schedule_date[index] + timedelta(days=30 * int(tenure))

            paid_amount1 = 0
            for i in emi_loan_id:
                if i == value:
                    index3 = emi_loan_id.index(value)
                    paid_amount1 += paid_amount[index3] * emi_number
                else:
                    paid_amount1 = 0

            print(paid_amount1)
            remain_amount = total_repay_amount[index] - paid_amount1
            print(remain_amount)
            app_tables.fin_emi_table.add_row(
                loan_id=str(value),
                extra_fee=float(extra_amount),
                amount_paid=float(total),
                scheduled_payment_made=datetime.today(),
                scheduled_payment=schedule_date[index],
                next_payment=next_payment_date,
                account_number=account_num[index1],
                emi_number=emi_number,
                borrower_email=borrower_email[index],
                borrower_customer_id=cos_id1[index],
                lender_customer_id=lender_customer_id[index],
                lender_email=lender_email[index]

            )
            data1[index]['total_amount_paid'] = float(paid_amount1)
            data1[index]['remaining_amount'] = float(remain_amount)
            anvil.server.call('loan_text', None)
            sm = self.manager
            wallet_screen = LastScreenWallet(name='LastScreenWallet')
            sm.add_widget(wallet_screen)
            sm.current = 'LastScreenWallet'

        elif wallet_amount[b_index] < float(total):
            self.show_success_dialog2(f"Insufficient Balance Please Deposit {float(total)}")
            anvil.server.call('loan_text', total)

            sm = self.manager
            # Create a new instance of the LenderWalletScreen
            wallet_screen = WalletScreen(name='WalletScreen', loan_amount_text=float(total))
            # Add the LenderWalletScreen to the existing ScreenManager
            sm.add_widget(wallet_screen)
            # Switch to the LenderWalletScreen
            sm.current = 'WalletScreen'
    def go_to_part_payment(self):
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = PartPayment(name='PartPayment')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'PartPayment'

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

    def show_success_dialog2(self, text):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.open_dashboard_screen2(dialog),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ]
        )
        dialog.open()

    def open_dashboard_screen(self, dialog):

        dialog.dismiss()
        self.manager.current = 'DashboardScreen'

    def open_dashboard_screen2(self, dialog):

        dialog.dismiss()
        self.manager.current = 'WalletScreen'

    def on_pre_enter(self, *args):
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
        self.manager.current = 'DuesScreen'

    def current(self):
        self.manager.current = 'DuesScreen'


class LastScreenWallet(Screen):

    def go_back_home(self):
        self.manager.current = 'DashboardScreen'

class PartPayment(Screen):
    pass
class DuesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        today_date = datetime.now(tz=utc).date()
        data = app_tables.fin_loan_details.search()
        emi_data = app_tables.fin_emi_table.search()
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        loan_status = []
        borrower_id = []
        borrower_name = []
        schedule_date = []
        s = 0

        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            customer_id.append(i['borrower_customer_id'])
            loan_status.append(i['loan_updated_status'])
            borrower_id.append(i['borrower_customer_id'])
            borrower_name.append(i['borrower_full_name'])
            schedule_date.append(i['first_emi_payment_due_date'])

        emi_loan_id = []
        emi_num = []
        next_payment = []
        for i in emi_data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])
        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
        index_list = []
        a = -1
        shedule_date = {}
        for i in range(s):
            a += 1

            if loan_status[i] == "disbursed" or loan_status[i] == "extension" or loan_status[i] == "foreclosure":
                if loan_id[i] not in emi_loan_id and schedule_date[i] is not None and today_date >= schedule_date[i]:
                    index_list.append(i)
                    shedule_date[loan_id[i]] = schedule_date[i]
                elif loan_id[i] in emi_loan_id:
                    last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(loan_id[i])
                    if next_payment[last_index] is not None and today_date >= next_payment[last_index]:
                        index_list.append(i)
                        shedule_date[loan_id[i]] = next_payment[last_index]

        print(index_list)
        print(shedule_date)
        today_date = datetime.now(tz=utc).date()
        b = 1
        k = -1
        for i in reversed(index_list):
            b += 1
            k += 1
            if customer_id[i] in profile_customer_id:
                number = profile_customer_id.index(customer_id[i])
            else:
                number = 0
            item = ThreeLineAvatarIconListItem(
                IconLeftWidget(
                    icon="card-account-details-outline"
                ),
                text=f"Borrower Name : {borrower_name[i]}",
                secondary_text=f"Borrower Mobile Number : {profile_mobile_number[number]}",
                tertiary_text=f"Scheduled Date : {shedule_date[loan_id[i]]}",
                text_color=(0, 0, 0, 1),  # Black color
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.bind(on_release=lambda instance, loan_id=loan_id[i],: self.icon_button_clicked(instance, loan_id,
                                                                                                shedule_date))
            self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance, loan_id, shedule_date):
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = BorrowerDuesScreen(name='BorrowerDuesScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'BorrowerDuesScreen'
        self.manager.get_screen('BorrowerDuesScreen').initialize_with_value(loan_id, shedule_date)

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()

    def go_back(self):
        self.manager.current = 'DashboardScreen'


class MyScreenManager(ScreenManager):
    pass