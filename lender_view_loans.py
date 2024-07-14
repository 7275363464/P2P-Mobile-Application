import anvil.server
from anvil.tables import app_tables
from kivy.clock import Clock
from kivy.graphics import StencilPush, Ellipse, StencilUse, StencilUnUse, StencilPop
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
from kivy.core.window import Window
import sqlite3
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.uix.stencilview import StencilView
from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatButton, MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.list import *
from kivy.animation import Animation
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IconLeftWidget, IconRightWidget, ImageLeftWidget
from lender_view_loans_request import view_loan_request, ViewLoansProfileScreenLR, ViewLoansProfileScreenRL
from kivy.uix.label import Label
import base64
from kivy.core.image import Image as CoreImage
from io import BytesIO

view_loans = '''
<WindowManager>
    # ViewLoansScreen:
    ALlLoansScreen:
    OpenViewLoanScreen:
    ViewLoansProfileScreens:
    ViewLoansProfileScreens2:
    ViewRejectedLoansScreen:
    ViewUnderProcessLoansScreen:
    ViewClosedLoansScreen:
<ViewLoansScreen>
    MDTopAppBar:
        title: "View Loans"
        elevation: 3
        left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
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
            on_release: root.go_to_under_process_loans()
            size_hint_y: None
            height: dp(60)
            size_hint_x: None
            width: dp(110)

            BoxLayout:
                orientation: 'horizontal'
                spacing:dp(10)
                MDLabel:
                    text: "UnderProcess Loans"
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
            on_release: root.go_to_rejected_loans()
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
            on_release: root.go_to_closed_loans()
            size_hint_y: None
            height: dp(60)
            size_hint_x: None
            width: dp(110)
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


        MDFlatButton:
            size_hint: None, None
            md_bg_color: 0.043, 0.145, 0.278, 1 

            size_hint_y: None
            height: dp(60)
            size_hint_x: None
            width: dp(110)
            on_release: root.all_loanscreen()
            BoxLayout:
                orientation: 'horizontal'
                spacing:dp(10)
                MDLabel:
                    text: "All Loans"
                    font_size:dp(14)
                    bold:True
                    theme_text_color: 'Custom'
                    halign: "center"
                    text_color:1,1,1,1
<OpenViewLoanScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Open Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        MDScrollView:
            MDBoxLayout:
                id: container
                orientation: 'vertical'
                padding: dp(30)
                spacing: dp(10)
                elevation: 3
                size_hint_y: None
                height: self.minimum_height



<ALlLoansScreen> 
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View All Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:
            MDBoxLayout:
                id: container2
                orientation: 'vertical'
                padding: dp(30)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height
                width: self.minimum_width
                adaptive_size: True

                pos_hint: {"center_x": 0, "center_y":  0}


<ViewRejectedLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Rejected Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDBoxLayout:
            padding:30
            orientation: 'vertical'
            md_bg_color: 0.5,0.5,0.5,1
            MDScrollView:
                MDList:
                    id: container1
                    padding:150
                    size_hint_y: None

<ViewClosedLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Closed Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container6

<ViewLoansProfileScreens>
    MDGridLayout:
        cols: 1
        MDTopAppBar:
            title: "Lender View Loan"
            elevation: 2
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            pos_hint: {'top': 1}
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(40)
            padding: dp(20)
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
                    text: 'Amount:'
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
                    bold: True
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1

            MDLabel:
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(20)
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Product Name'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: pro_name
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Borrower Name'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: b_name
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Phone Number'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: phone_num
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Ascend Score'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: ascend
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Interest(%)'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: int_rate
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Duration(M)'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: tenure
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Credit Limit'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: limit
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True


            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Published Date'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: date
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Loan Status'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: status
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
            MDLabel:
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(5)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(30)
            padding: dp(15)
            size_hint_y: None
            height: self.minimum_height
            canvas.before:
                Color:
                    rgba: 249/255, 249/255, 247/255, 1 
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [25, 25, 25, 25]
            MDLabel:
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(5)
            MDGridLayout:
                cols: 3

                MDLabel:
                    text: 'Total'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1 
                    font_size: dp(25)  
                    bold: True
                MDIconButton:
                    icon: 'currency-inr'
                    halign: 'center' 
                    bold: True   

                MDLabel:
                    id: amount_1
                    bold: True
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1

<ViewLoansProfileScreens2>
    MDGridLayout:
        cols: 1

        MDTopAppBar:
            title: "View Loan details"
            elevation: 2
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            pos_hint: {'top': 1}
        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                spacing: dp(40)
                padding: dp(20)
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
                        text: '     Amount:'
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
                        bold: True
                        halign: 'left'
                        theme_text_color: 'Custom'  
                        text_color: 0, 0, 0, 1

                MDLabel:
                    text: ''
                    halign: 'left'
                    size_hint_y: None
                    height: dp(20)
                MDGridLayout:
                    cols: 2
                    MDLabel:
                        text: 'Product Name'
                        halign: 'left'
                        bold: True

                    MDLabel:
                        id: pro_name
                        halign: 'left'
                        theme_text_color: 'Custom'  
                        text_color: 140/255, 140/255, 140/255, 1
                        bold : True

                MDGridLayout:
                    cols: 2
                    MDLabel:
                        text: 'Borrower Name'
                        halign: 'left'
                        bold: True

                    MDLabel:
                        id: b_name
                        halign: 'left'
                        theme_text_color: 'Custom'  
                        text_color: 140/255, 140/255, 140/255, 1
                        bold : True

                MDGridLayout:
                    cols: 2
                    MDLabel:
                        text: 'Phone Number'
                        halign: 'left'
                        bold: True

                    MDLabel:
                        id: phone_num
                        halign: 'left'
                        theme_text_color: 'Custom'  
                        text_color: 140/255, 140/255, 140/255, 1
                        bold : True

                MDGridLayout:
                    cols: 2
                    MDLabel:
                        text: 'EMI start date'
                        halign: 'left'
                        theme_text_color: 'Custom'  
                        bold: True

                    MDLabel:
                        id: first_emi_payment_due_date
                        halign: 'left'
                        theme_text_color: 'Custom'  
                        text_color: 140/255, 140/255, 140/255, 1
                        bold: True
                MDGridLayout:
                    cols: 2
                    MDLabel:
                        text: 'EMI last date'
                        halign: 'left'
                        theme_text_color: 'Custom'  
                        bold: True

                    MDLabel:
                        id: borrower_last_payment_done
                        halign: 'left'
                        theme_text_color: 'Custom'  
                        text_color: 140/255, 140/255, 140/255, 1
                        bold: True

                MDGridLayout:
                    cols: 2
                    MDLabel:
                        text: 'Interest(%)'
                        halign: 'left'
                        bold: True

                    MDLabel:
                        id: int_rate
                        halign: 'left'
                        theme_text_color: 'Custom'  
                        text_color: 140/255, 140/255, 140/255, 1
                        bold : True

                MDGridLayout:
                    cols: 2
                    MDLabel:
                        text: 'Tenure(M)'
                        halign: 'left'
                        bold: True

                    MDLabel:
                        id: tenure
                        halign: 'left' 
                        theme_text_color: 'Custom'  
                        text_color: 140/255, 140/255, 140/255, 1
                        bold : True

                MDGridLayout:
                    cols: 2
                    MDLabel:
                        text: 'Credit Limit'
                        halign: 'left'
                        bold: True

                    MDLabel:
                        id: limit
                        halign: 'left' 
                        theme_text_color: 'Custom'  
                        text_color: 140/255, 140/255, 140/255, 1
                        bold : True


                MDGridLayout:
                    cols: 2
                    MDLabel:
                        text: 'Applied Date'
                        halign: 'left'
                        bold: True

                    MDLabel:
                        id: date
                        halign: 'left'
                        theme_text_color: 'Custom'  
                        text_color: 140/255, 140/255, 140/255, 1
                        bold : True

                MDGridLayout:
                    cols: 2
                    MDLabel:
                        text: 'Loan Status'
                        halign: 'left'
                        bold: True

                    MDLabel:
                        id: status
                        halign: 'left' 
                        theme_text_color: 'Custom'  
                        text_color: 140/255, 140/255, 140/255, 1
                        bold : True

                MDBoxLayout:
                    orientation: 'vertical'
                    padding: dp(15)
                    size_hint_y: None
                    height: self.minimum_height
                    canvas.before:
                        Color:
                            rgba: 249/255, 249/255, 247/255, 1 
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [25, 25, 25, 25]

                    MDGridLayout:
                        cols: 3

                        MDLabel:
                            text: '     Total'
                            halign: 'left'
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1 
                            font_size: dp(25) 
                            bold: True
                        MDIconButton:
                            icon: 'currency-inr'
                            halign: 'center' 
                            bold: True   

                        MDLabel:
                            id: amount_1
                            bold: True
                            halign: 'left'
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                MDLabel:
                    text: ''
                    halign: 'left'
                    size_hint_y: None
                    height: dp(25)
    '''

Builder.load_string(view_loans)
conn = sqlite3.connect('fin_user_profile.db')
cursor = conn.cursor()


class ALlLoansScreen(Screen):
    def __init__(self, loan_id=None, instance=None, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_loan_details.search()
        emi = app_tables.fin_emi_table.search()
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        product_name = []
        interest_rate = []
        tenure = []
        monthly_emi = []
        interest_amount = []
        processing_fee = []
        loan_amount = []
        lender_customer_id = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            product_name.append(i['product_name'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])
            tenure.append(i['tenure'])
            interest_amount.append(i['total_interest_amount'])
            processing_fee.append(i['total_processing_fee_amount'])
            monthly_emi.append(i['monthly_emi'])
            lender_customer_id.append(i['lender_customer_id'])
        remaining_tenure = []
        next_payment = []
        emi_loan_id = []
        for i in emi:
            remaining_tenure.append(i['remaining_tenure'])
            next_payment.append(i['next_payment'])
            emi_loan_id.append(i['loan_id'])
        profile_customer_id = []
        profile_mobile_number = []
        ascend_value = []
        profile_email = []
        profile_photo = {}
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            ascend_value.append(i['ascend_value'])
            profile_email.append(i['email_user'])

            # Load profile photo if available
            if i['user_photo']:
                image_data = i['user_photo'].get_bytes()
                if isinstance(image_data, bytes):
                    try:
                        profile_texture_io = BytesIO(image_data)
                        photo_texture = CoreImage(profile_texture_io, ext='png').texture
                        profile_photo[i['customer_id']] = photo_texture
                    except Exception as e:
                        print(f"Error processing image for customer {i['customer_id']}: {e}")
                else:
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        profile_texture_io = BytesIO(image_data_binary)
                        photo_texture = CoreImage(profile_texture_io, ext='png').texture
                        profile_photo[i['customer_id']] = photo_texture
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for customer {i['customer_id']}: {e}")
                    except Exception as e:
                        print(f"Error processing image for customer {i['customer_id']}: {e}")

        lender_data = app_tables.fin_lender.search()
        lender_cus_id = []
        for i in lender_data:
            lender_cus_id.append(i['customer_id'])

        email = anvil.server.call('another_method')

        log_index = 0
        if email in profile_email:
            log_index = profile_email.index(email)
        else:
            print("email not there")

        a = -1
        total_commitment = []
        present_commitment = []
        for i in range(s):
            a += 1
            if lender_customer_id[i] == profile_customer_id[log_index] and loan_status[i] not in ['lost opportunities',
                                                                                                  'rejected']:
                total_commitment.append(loan_amount[i])

            if lender_customer_id[i] == profile_customer_id[log_index] and loan_status[i] not in ['lost opportunities',
                                                                                                  'rejected', 'closed']:
                present_commitment.append(loan_amount[i])

        if len(total_commitment) >= 1:
            if lender_customer_id[log_index] in lender_cus_id:
                lender_index = lender_cus_id.index(lender_customer_id[log_index])
                lender_data[lender_index]['lender_total_commitments'] = sum(total_commitment)
                print(total_commitment, sum(total_commitment))
            else:
                print('customer id not there')

        if len(present_commitment) >= 1:
            if lender_customer_id[log_index] in lender_cus_id:
                lender_index = lender_cus_id.index(lender_customer_id[log_index])
                lender_data[lender_index]['present_commitments'] = sum(present_commitment)
                print(present_commitment, sum(present_commitment))
            else:
                print('customer id not there')

        c = -1
        index_list = []
        for i in range(s):
            c += 1
            index_list.append(c)

        b = 1
        k = -1
        for i in reversed(index_list):
            b += 1
            k += 1
            if customer_id[i] in profile_customer_id:
                number = profile_customer_id.index(customer_id[i])
            else:
                number = 0
            card = MDCard(
                orientation='horizontal',
                size_hint=(None, None),
                size=("340dp", "200dp"),
                padding="8dp",
                spacing="5dp",
                elevation=1,
                radius=[0, 0, 0, 0]
            )

            left_box = MDBoxLayout(orientation='vertical', padding=dp(10), size_hint_x=0.3,
                                   pos_hint={"center_y": 0.53}, )
            if customer_id[i] in profile_photo:
                image = CircularImage(
                    texture=profile_photo[customer_id[i]],  # Get the profile photo texture
                    size_hint_x=None,
                    height="30dp",
                    width="60dp"
                )
            else:
                image = CircularImage(
                    source='img.png',  # Update with the actual path to the image
                    size_hint_x=None,
                    height="70dp",
                    width="80dp"
                )
            left_box.add_widget(image)

            left_box.add_widget(MDLabel(
                text=f"[b]{borrower_name[i]}[/b]",
                markup=True,
                font_size='10sp',
                height="50dp",
                font_style='Caption',  # You can adjust font style as needed
                theme_text_color='Primary',
                halign='center',
            ))
            left_box.add_widget(Widget(size_hint_y=None, height=dp(10)))
            left_box.add_widget(MDLabel(
                text=f"[b]{profile_mobile_number[number]}[/b]",
                markup=True,
                font_size='10sp',
                font_style='Caption',  # You can adjust font style as needed
                theme_text_color='Secondary',
                halign='center',
            ))
            left_box.add_widget(MDLabel(
                text=f" ",
                markup=True,
                font_size='8sp',
                font_style='Subtitle2',  # You can adjust font style as needed
                theme_text_color='Secondary',
                halign='left',
            ))

            card.add_widget(left_box)
            # Define status color
            status_color = (0.545, 0.765, 0.290, 1)  # default color
            if loan_status[i] == "under process":
                status_color = (253 / 255, 218 / 255, 13 / 255, 1)
            elif loan_status[i] == "disbursed":
                status_color = (0.8588, 0.4392, 0.5765, 1.0)
            elif loan_status[i] == "closed":
                status_color = (0.4235, 0.5569, 0.1373, 1.0)
            elif loan_status[i] == "extension":
                status_color = (1.0, 0.6275, 0.4824, 1.0)
            elif loan_status[i] == "foreclosure":
                status_color = (0.0, 0.749, 1.0, 1.0)
            elif loan_status[i] == "rejected":
                status_color = (0.902, 0.141, 0.141, 1)
            elif loan_status[i] == "approved":
                status_color = (0.2353, 0.7019, 0.4431, 1.0)
            elif loan_status[i] == "lost opportunities":
                status_color = (0.902, 0.141, 0.141, 1)

            # Right side: Loan details
            right_box = MDBoxLayout(orientation='vertical', size_hint_x=0.6)

            right_box.add_widget(MDLabel(
                text=f"[color=000000][b]Loan Status:[/color] {loan_status[i]}[/b]",
                markup=True,
                font_size='19sp',
                font_style='Caption',  # You can adjust font style as needed
                theme_text_color='Custom',
                halign='left',
                text_color=status_color
            ))

            right_box.add_widget(MDLabel(
                text=f"[b]Product Name:[/b] {product_name[i]}",
                markup=True,
                font_size='15sp',
                font_style='Caption',  # You can adjust font style as needed
                theme_text_color='Primary',
                halign='left',
            ))

            right_box.add_widget(MDLabel(
                text=f"[b]Loan Amount:[/b] {loan_amount[i]}",
                markup=True,
                font_size='15sp',
                font_style='Caption',  # You can adjust font style as needed
                theme_text_color='Primary',
                halign='left',
            ))
            if loan_status[i] not in ["extension", "foreclosure", "approved", "disbursed"]:
                right_box.add_widget(MDLabel(
                    text=f"[b]Tenure:[/b] {tenure[i]}",
                    markup=True,
                    font_size='15sp',
                    font_style='Caption',  # You can adjust font style as needed
                    theme_text_color='Primary',
                    halign='left',
                ))
            if loan_status[i] not in ["extension", "foreclosure", "approved", "disbursed"]:
                right_box.add_widget(MDLabel(
                    text=f"[b]Processing Fee:[/b] {processing_fee[i]}",
                    markup=True,
                    font_size='15sp',
                    font_style='Caption',  # You can adjust font style as needed
                    theme_text_color='Primary',
                    halign='left',
                ))
            if loan_status[i] not in ["extension", "foreclosure", "approved", "disbursed"]:
                right_box.add_widget(MDLabel(
                    text=f"[b]Interest Amount:[/b] {interest_amount[i]}",
                    markup=True,
                    font_size='15sp',
                    font_style='Caption',  # You can adjust font style as needed
                    theme_text_color='Primary',
                    halign='left',
                ))
            if loan_status[i] not in ["rejected", "closed", "under process"]:
                if loan_id[i] in emi_loan_id:
                    last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(loan_id[i])
                    right_box.add_widget(MDLabel(
                        text=f"[b]emi_remaining:[/b] {remaining_tenure[last_index]}",
                        markup=True,
                        font_size='15sp',
                        font_style='Caption',  # You can adjust font style as needed
                        theme_text_color='Primary',
                        halign='left',
                    ))

            if loan_status[i] not in ["rejected", "closed", "under process"]:
                if loan_id[i] in emi_loan_id:
                    last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(loan_id[i])
                    right_box.add_widget(MDLabel(
                        text=f"[b]EMI Amount:[/b] {monthly_emi[last_index]}",
                        markup=True,
                        font_size='15sp',
                        font_style='Caption',  # You can adjust font style as needed
                        theme_text_color='Primary',
                        halign='left',
                    ))
            if loan_status[i] not in ["rejected", "closed", "under process"]:
                if loan_id[i] in emi_loan_id:
                    last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(loan_id[i])
                    right_box.add_widget(MDLabel(
                        text=f"[b]Next_emi_date: [color=32CD32]{next_payment[last_index]}[/color][/b]",
                        markup=True,
                        font_size='15sp',
                        font_style='Caption',  # You can adjust font style as needed
                        theme_text_color='Primary',
                        halign='left',
                    ))
            if loan_status[i] not in ["under process", "rejected"]:
                button2 = MDFillRoundFlatButton(
                    text="  View Details  ",
                    size_hint=(None, None),
                    height="10dp",
                    width="150dp",
                    pos_hint={"center_x": 0.6},
                    md_bg_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x, i=i: self.icon_button_clicked(x, loan_id[i])
                )
                right_box.add_widget(button2)
            card.add_widget(right_box)

            self.ids.container2.add_widget(card)

    def icon_button_clicked(self, instance, loan_id):
        data = app_tables.fin_loan_details.search()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewLoansProfileScreens2(name='ViewLoansProfileScreens2')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewLoansProfileScreens2'
        self.manager.get_screen('ViewLoansProfileScreens2').initialize_with_value(loan_id, data)

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

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'

    def refresh(self):
        self.ids.container2.clear_widgets()
        self.__init__()


class ViewLoansScreen(Screen):

    def all_loanscreen(self):
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
        Clock.schedule_once(lambda dt: self.performance_all_loanscreen(modal_view), 2)

    def performance_all_loanscreen(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = ALlLoansScreen(name='ALlLoansScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'ALlLoansScreen'

    def go_to_open_loans(self):
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
        Clock.schedule_once(lambda dt: self.performance_go_to_open_loans(modal_view), 2)

    def performance_go_to_open_loans(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        open = OpenViewLoanScreen(name='OpenViewLoanScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(open)

        # Switch to the LoginScreen
        sm.current = 'OpenViewLoanScreen'

    def go_to_rejected_loans(self):
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
        Clock.schedule_once(lambda dt: self.performance_go_to_rejected_loans(modal_view), 2)

    def performance_go_to_rejected_loans(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        rejected = ViewRejectedLoansScreen(name='ViewRejectedLoansScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(rejected)

        # Switch to the LoginScreen
        sm.current = 'ViewRejectedLoansScreen'

    def go_to_under_process_loans(self):
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
        Clock.schedule_once(lambda dt: self.performance_go_to_under_process_loans(modal_view), 2)

    def performance_go_to_under_process_loans(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        from lender_underprocess import ViewUnderProcess
        sm = self.manager

        # Create a new instance of the LoginScreen
        under_process = ViewUnderProcess(name='ViewUnderProcess')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(under_process)

        # Switch to the LoginScreen
        sm.current = 'ViewUnderProcess'

    def go_to_closed_loans(self):
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
        Clock.schedule_once(lambda dt: self.performance_go_to_closed_loans(modal_view), 2)

    def performance_go_to_closed_loans(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        closed = ViewClosedLoansScreen(name='ViewClosedLoansScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(closed)

        # Switch to the LoginScreen
        sm.current = 'ViewClosedLoansScreen'


class OpenViewLoanScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        product_name = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            product_name.append(i['product_name'])

        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[c] == 'disbursed':
                index_list.append(c)

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
                tertiary_text=f"Product Name : {product_name[i]}",
                text_color=(0, 0, 0, 1),  # Black color
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
            self.ids.container1.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
        # Handle the on_release event here

        data = app_tables.fin_loan_details.search()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewLoansProfileScreens(name='ViewLoansProfileScreens')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewLoansProfileScreens'
        self.manager.get_screen('ViewLoansProfileScreens').initialize_with_value(loan_id, data)

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

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager
        profile = ViewLoansScreen(name='ViewLoansScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewLoansScreen'

    def refresh(self):
        self.ids.container1.clear_widgets()
        self.__init__()


class ViewLoansProfileScreens(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_back_button_press(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'

    def initialize_with_value(self, value, data):
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        product_name = []
        borrower_name = []
        tenure = []
        interest_rate = []
        loan_amount = []
        loan_amount1 = []
        credit_limit = []
        date_of_apply = []
        status = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            product_name.append(i['product_name'])
            borrower_name.append(i['borrower_full_name'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])
            loan_amount1.append(i['loan_amount'])
            credit_limit.append(i['credit_limit'])
            date_of_apply.append(i['borrower_loan_created_timestamp'])
            status.append(i['loan_updated_status'])
        profile_customer_id = []
        profile_mobile_number = []
        ascend_score = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            ascend_score.append(i['ascend_value'])

        index = 0

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.pro_name.text = str(product_name[index])
            self.ids.b_name.text = str(borrower_name[index])
            self.ids.int_rate.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.amount_1.text = str(loan_amount1[index])
            self.ids.limit.text = str(credit_limit[index])
            self.ids.date.text = str(date_of_apply[index])
            self.ids.status.text = str(status[index])

        if customer_id[index] in profile_customer_id:
            index2 = profile_customer_id.index(customer_id[index])

            self.ids.phone_num.text = str(profile_mobile_number[index2])
            self.ids.ascend.text = str(ascend_score[index2])

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

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'


class ViewLoansProfileScreens2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_back_button_press(self):
        self.manager.current = 'ALlLoansScreen'

    def initialize_with_value(self, value, data):
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        product_name = []
        borrower_name = []
        tenure = []
        interest_rate = []
        loan_amount = []
        loan_amount1 = []
        credit_limit = []
        date_of_apply = []
        status = []
        first_emi_payment_due_date = []
        borrower_last_payment_done = []

        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            product_name.append(i['product_name'])
            borrower_name.append(i['borrower_full_name'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])
            loan_amount1.append(i['loan_amount'])
            credit_limit.append(i['credit_limit'])
            first_emi_payment_due_date.append(i['first_emi_payment_due_date'])
            borrower_last_payment_done.append(i['borrower_last_payment_done'])
            date_of_apply.append(i['borrower_loan_created_timestamp'])
            status.append(i['loan_updated_status'])
        profile_customer_id = []
        profile_mobile_number = []

        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])

        index = 0

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.pro_name.text = str(product_name[index])
            self.ids.b_name.text = str(borrower_name[index])
            self.ids.int_rate.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.first_emi_payment_due_date.text = str(first_emi_payment_due_date[index])
            self.ids.borrower_last_payment_done.text = str(borrower_last_payment_done[index])
            self.ids.amount_1.text = str(loan_amount1[index])
            self.ids.limit.text = str(credit_limit[index])
            self.ids.date.text = str(date_of_apply[index])
            self.ids.status.text = str(status[index])

        if customer_id[index] in profile_customer_id:
            index2 = profile_customer_id.index(customer_id[index])

            self.ids.phone_num.text = str(profile_mobile_number[index2])

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

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')

        self.manager.current = 'ALlLoansScreen'


class ViewRejectedLoansScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        product_name = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            product_name.append(i['product_name'])

        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[c] == 'rejected':
                index_list.append(c)

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
                tertiary_text=f"Product Name : {product_name[i]}",
                text_color=(0, 0, 0, 1),  # Black color
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
            self.ids.container4.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
        # Handle the on_release event here
        data = app_tables.fin_loan_details.search()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewLoansProfileScreens(name='ViewLoansProfileScreens')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewLoansProfileScreens'
        self.manager.get_screen('ViewLoansProfileScreens').initialize_with_value(loan_id, data)

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

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewLoansScreen'

    def refresh(self):
        self.ids.container4.clear_widgets()
        self.__init__()


class ViewClosedLoansScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        product_name = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            product_name.append(i['product_name'])

        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[c] == 'closed':
                index_list.append(c)

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
                tertiary_text=f"Product Name : {product_name[i]}",
                text_color=(0, 0, 0, 1),  # Black color
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
            self.ids.container6.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
        # Handle the on_release event here
        data = app_tables.fin_loan_details.search()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewLoansProfileScreens(name='ViewLoansProfileScreens')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewLoansProfileScreens'
        self.manager.get_screen('ViewLoansProfileScreens').initialize_with_value(loan_id, data)

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

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewLoansScreen'

    def refresh(self):
        self.ids.container6.clear_widgets()
        self.__init__()


class CircularImage(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = ("80dp", "120dp")  # Initial size of the image
        self.bind(pos=self.update_shape, size=self.update_shape)

    def update_shape(self, *args):
        self.canvas.before.clear()

        # Calculate the diameter of the circle
        diameter = min(self.width, self.height)
        radius = diameter / 2.0

        # Calculate the position of the ellipse to center it on the image
        ellipse_pos = (self.center_x - radius, self.center_y - radius)

        with self.canvas.before:
            StencilPush()
            Ellipse(pos=ellipse_pos, size=(diameter, diameter))
            StencilUse()

        self.canvas.after.clear()
        with self.canvas.after:
            StencilUnUse()
            Ellipse(pos=ellipse_pos, size=(diameter, diameter))
            StencilPop()


class MyScreenManager(ScreenManager):
    pass
