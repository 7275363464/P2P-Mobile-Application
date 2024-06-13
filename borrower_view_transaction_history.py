import anvil
from anvil.tables import app_tables
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import platform
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
import anvil.server
from kivy.lang import Builder
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)


view_transaction_history = '''
<WindowManager>:
    TransactionBH:
    ViewProfileScreenBTH:

<TransactionBH>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Transaction History"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back_screen()]]
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


<ViewProfileScreenBTH>:

    MDGridLayout:
        cols:1
        MDTopAppBar:
            title: "Borrower Transaction Details"
            elevation: 2
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            halign: 'left'
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
                    text: 'Amount:'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1
            MDGridLayout:
                cols: 2
                MDIconButton:
                    icon: 'currency-inr'
                    halign: 'left'
                    size_hint_y: None
                    height: dp(1)

                MDLabel:
                    id: amount
                    halign: 'left'
                    text_color: 140/255, 140/255, 140/255, 1

            MDLabel:
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(20)
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Transaction ID'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: transaction_id
                    halign: 'left'
                    text_color: 140/255, 140/255, 140/255, 1

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'User Email'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: user_email
                    halign: 'left'
                    text_color: 140/255, 140/255, 140/255, 1

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Receiver Email'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: receiver_email
                    halign: 'left'
                    text_color: 140/255, 140/255, 140/255, 1

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: "Transaction Type" 
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True
                MDLabel:
                    id: transaction_type
                    halign: "left"
                    text_color: 140/255, 140/255, 140/255, 1


            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Published Date'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: date_time
                    halign: 'left'
                    text_color: 140/255, 140/255, 140/255, 1
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Status'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: status
                    halign: 'left' 
                    text_color: 140/255, 140/255, 140/255, 1

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
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
                    bold: True
                MDIconButton:
                    icon: 'currency-inr'
                    halign: 'center' 
                    bold: True   

                MDLabel:
                    id: amount_1
                    halign: 'left'
                    text_color: 140/255, 140/255, 140/255, 1
                    bold: True



'''

Builder.load_string(view_transaction_history)


class TransactionBH(Screen):
    def __init__(self, instance=None, **kwargs):
        super().__init__(**kwargs)
        email = self.get_table()
        profile = app_tables.fin_user_profile.search()
        transaction = app_tables.fin_wallet_transactions.search()
        s = 0
        transaction_id = []
        wallet_customer_id = []
        status = []
        transaction_type = []
        amount = []
        transaction_time_stamp = []
        for i in transaction:
            transaction_id.append(i['transaction_id'])
            wallet_customer_id.append(i['customer_id'])
            transaction_type.append(i['transaction_type'])
            transaction_time_stamp.append(i['transaction_time_stamp'])
            status.append(i['status'])
            amount.append(i['amount'])
        print(transaction_id)

        pro_customer_id = []
        pro_mobile_number = []
        pro_email_id = []
        borrower_name = []

        for i in profile:
            pro_customer_id.append(i['customer_id'])
            pro_mobile_number.append(i['mobile'])
            pro_email_id.append(i['email_user'])
            borrower_name.append(i['full_name'])

        index = -1
        if email in pro_email_id:
            index = pro_email_id.index(email)
        print(pro_customer_id[index])

        index_list = []

        for idx, val in enumerate(wallet_customer_id):
            if val == pro_customer_id[index]:
                index_list.append(idx)
        print(index_list)
        print(wallet_customer_id)

        b = 1
        k = -1
        for i in reversed(index_list):
            b += 1
            k += 1
            if wallet_customer_id[i] in pro_customer_id:
                number = pro_customer_id.index(wallet_customer_id[i])
            else:
                number = 0
            card = MDCard(
                orientation='vertical',
                size_hint=(None, None),
                size=("320dp", "240dp"),
                padding="8dp",
                spacing="5dp",
                elevation=3
            )
            horizontal_layout = BoxLayout(orientation='horizontal')
            image = Image(
                source='img.png',  # Update with the actual path to the image
                size_hint_x=None,
                height="60dp",
                width="70dp"
            )
            horizontal_layout.add_widget(image)

            horizontal_layout.add_widget(Widget(size_hint_x=None, width='10dp'))
            text_layout = BoxLayout(orientation='vertical')
            text_layout.add_widget(MDLabel(
                text=f"[b]{borrower_name[number]}[/b],\n[b]{pro_mobile_number[number]}[/b]",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Transaction id[/b] : {transaction_id[i]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Transaction Type[/b] : {transaction_type[i]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))

            text_layout.add_widget(MDLabel(
                text=f"[b]Amount[/b] : {amount[i]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Transaction time[/b] : {transaction_time_stamp[i].date()}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            horizontal_layout.add_widget(text_layout)
            card.add_widget(horizontal_layout)
            # item = ThreeLineAvatarIconListItem(
            #
            #     IconLeftWidget(
            #         icon="card-account-details-outline"
            #     ),
            #     text=f"Borrower Name : {borrower_name[number]}",
            #     secondary_text=f"Borrower Mobile Number : {pro_mobile_number[number]}",
            #     tertiary_text=f"Transaction Name : {transaction_id[i]}",
            #     text_color=(0, 0, 0, 1),  # Black color
            #     theme_text_color='Custom',
            #     secondary_text_color=(0, 0, 0, 1),
            #     secondary_theme_text_color='Custom',
            #     tertiary_text_color=(0, 0, 0, 1),
            #     tertiary_theme_text_color='Custom'
            # )
            # item.bind(
            #     on_release=lambda instance, transactions_id=transaction_id[i]: self.icon_button_clicked(instance,
            #                                                                                             transactions_id))
            # self.ids.container1.add_widget(item)
            # else:
            #     print("Index out of range!")
            card.add_widget(Widget(size_hint_y=None, height='10dp'))
            button_layout = BoxLayout(
                size_hint_y=None,
                height="40dp",
                padding="10dp",
                spacing="35dp"
            )
            status_color = (0.545, 0.765, 0.290, 1)  # default color
            if status[i] in ["success"]:
                status_color = (0.2353, 0.7019, 0.4431, 1.0)  # light green
            elif status[i] in ["fail"]:
                status_color = (0.902, 0.141, 0.141, 1)  # light green
            status_text = {
                "success": "   successful    ",
                "fail": "      failed      ",
            }
            button1 = MDFillRoundFlatButton(
                text=status_text.get(status[i], "Unknown status"),
                size_hint=(None, None),
                height="40dp",
                width="250dp",
                pos_hint={"center_x": 0},
                md_bg_color=status_color,
                # on_release=lambda x, i=i: self.close_loan(i)
            )
            button2 = MDFillRoundFlatButton(
                text="  View Details  ",
                size_hint=(None, None),
                height="40dp",
                width="250dp",
                pos_hint={"center_x": 1},
                md_bg_color=(0.043, 0.145, 0.278, 1),
                on_release=lambda instance, transactions_id=transaction_id[i]: self.icon_button_clicked(instance,
                                                                                                        transactions_id)
            )
            button_layout.add_widget(button1)
            button_layout.add_widget(button2)
            card.add_widget(button_layout)

            # card.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
            self.ids.container2.add_widget(card)
        #     item = ThreeLineAvatarIconListItem(
        #
        #         IconLeftWidget(
        #             icon="card-account-details-outline"
        #         ),
        #         text=f"Borrower Name : {borrower_name[number]}",
        #         secondary_text=f"Borrower Mobile Number : {pro_mobile_number[number]}",
        #         tertiary_text=f"Transaction Name : {transaction_id[i]}",
        #         text_color=(0, 0, 0, 1),  # Black color
        #         theme_text_color='Custom',
        #         secondary_text_color=(0, 0, 0, 1),
        #         secondary_theme_text_color='Custom',
        #         tertiary_text_color=(0, 0, 0, 1),
        #         tertiary_theme_text_color='Custom'
        #     )
        #     item.bind(
        #         on_release=lambda instance, transactions_id=transaction_id[i]: self.icon_button_clicked(instance,
        #                                                                                                 transactions_id))
        #     self.ids.container1.add_widget(item)
        # else:
        #     print("Index out of range!")

    def icon_button_clicked(self, instance, transactions_id):
        value = instance.text.split(':')
        value = value[-1][1:]
        data = app_tables.fin_foreclosure.search()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewProfileScreenBTH(name='ViewProfileScreenBTH')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewProfileScreenBTH'
        self.manager.get_screen('ViewProfileScreenBTH').initialize_with_value(transactions_id, data)

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back_screen()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back_screen(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def refresh(self):
        self.ids.container2.clear_widgets()
        self.__init__()

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreenLF'


class ViewProfileScreenBTH(Screen):
    def initialize_with_value(self, value, data):
        data = app_tables.fin_wallet_transactions.search()
        transaction_id = []
        user_email = []
        receiver_email = []
        wallet_id = []
        transaction_type = []
        amount = []
        amount1 = []
        date_time = []
        status = []
        for i in data:
            transaction_id.append(i['transaction_id'])
            user_email.append(i['user_email'])
            receiver_email.append(i['receiver_email'])
            wallet_id.append(i['wallet_id'])
            transaction_type.append(i['transaction_type'])
            amount.append(i['amount'])
            amount1.append(i['amount'])
            date_time.append(i['transaction_time_stamp'])
            status.append(i['status'])

        if value in transaction_id:
            index = transaction_id.index(value)
            self.ids.transaction_id.text = str(transaction_id[index])
            self.ids.user_email.text = str(user_email[index])
            self.ids.receiver_email.text = str(receiver_email[index])
            self.ids.transaction_type.text = str(transaction_type[index])
            self.ids.amount.text = str(amount[index])
            self.ids.amount_1.text = str(amount1[index])
            self.ids.date_time.text = str(date_time[index].date())
            self.ids.status.text = str(status[index])

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

    def on_back_button_press(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'TransactionBH'


class MyScreenManager(ScreenManager):
    pass