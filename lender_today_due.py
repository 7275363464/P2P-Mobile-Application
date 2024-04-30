from datetime import datetime, timezone

from anvil.tables import app_tables
from bson import utc
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget
import anvil.server
import anvil.server

lender_today_due = '''

<WindowManager>:
    TodayDuesTD:
    ViewProfileTD:

<TodayDuesTD>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Today's Dues"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container
<ViewProfileTD>:

    BoxLayout:
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        elevation: 2

        spacing: dp(20)
        orientation: 'vertical'

        MDTopAppBar:
            title:"Today's Dues"
            md_bg_color:0.043, 0.145, 0.278, 1
            theme_text_color: 'Custom'
            text_color: 1,1,1,1 # Set color to white
            size_hint:1,None
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            pos_hint: {'center_x': 0.5, 'center_y': 0.96}

        MDLabel:
            text: "" 
            size_hint_y:None
            height:dp(1) 

        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                text: "Borrower Name"
                font_size:dp(16)
                bold:True

            MDLabel:
                id: borrower_name
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1 
                color: 0, 0, 0, 1


        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                text: "Loan Amount"
                font_size:dp(16)
                bold:True

            MDLabel:
                id: loan_amount1
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1  
                color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                text: "Tenure"
                font_size:dp(16)
                bold:True

            MDLabel:
                id: tenure
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1  
                color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                text: "Interest Rate"
                font_size:dp(16)
                bold:True

            MDLabel:
                id: interest_rate
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1 
                color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                text: "Account Number"
                font_size:dp(16)
                bold:True

            MDLabel:
                id:account_number
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1 
                color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                text: "Emi Amount"
                font_size:dp(16)
                bold:True

            MDLabel:
                id:emi_amount
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1 
                color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                id: extra
                text: "Extra Payment"
                font_size:dp(16)
                bold:True

            MDLabel:
                id: extra_amount
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1  
                color: 0, 0, 0, 1           

        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                id: total
                text: "Total Amount"
                font_size:dp(16)
                bold:True

            MDLabel:
                id:total_amount
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1 
                color: 0, 0, 0, 1            
        MDLabel:
            text: " "    
'''
Builder.load_string(lender_today_due)
date = datetime.today().date()
print(date)


class TodayDuesTD(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = app_tables.fin_emi_table.search()
        data1 = app_tables.fin_loan_details.search()
        today_date = datetime.now(timezone.utc).date()
        loan_id = []
        loan_status = []
        borrower_name = []
        schedule_date = []
        s = 0

        for i in data1:
            s += 1
            loan_id.append(i['loan_id'])
            loan_status.append(i['loan_updated_status'])
            borrower_name.append(i['borrower_full_name'])
            schedule_date.append(i['first_emi_payment_due_date'])

        emi_loan_id = []
        emi_num = []
        next_payment = []
        for i in data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])
        index_list = []
        a = -1
        shedule_date = {}
        for i in range(s):
            a += 1
            if loan_status[i] == "disbursed" or loan_status[i] == "extension" or loan_status[i] == "foreclosure":
                if loan_id[i] not in emi_loan_id and schedule_date[i] != None and today_date >= schedule_date[i]:
                    index_list.append(i)
                    shedule_date[loan_id[i]] = schedule_date[i]
                elif loan_id[i] in emi_loan_id:
                    last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(loan_id[i])
                    if today_date >= next_payment[last_index]:
                        index_list.append(i)
                        shedule_date[loan_id[i]] = next_payment[last_index]

        print(index_list)
        print(shedule_date)
        today_date = datetime.now(timezone.utc).date()


        for i in index_list:
            item = ThreeLineAvatarIconListItem(

                IconLeftWidget(
                    icon="card-account-details-outline"
                ),
                text=f"Borrower Name: {borrower_name[i]}",
                secondary_text=f"Scheduled Date  : {shedule_date[loan_id[i]]}",
                tertiary_text=f"Day Passed Due Date : {(today_date - shedule_date[loan_id[i]]).days}",
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
        lender_today_due = ViewProfileTD(name='ViewProfileTD')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(lender_today_due)

        # Switch to the LoginScreen
        sm.current = 'ViewProfileTD'
        self.manager.get_screen('ViewProfileTD').initialize_with_value(loan_id, shedule_date)

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
        self.manager.current = 'LenderDashboard'


class ViewProfileTD(Screen):
    def initialize_with_value(self, value, shechule_date):
        print(value)
        self.loan_id = value
        today_date = datetime.now(timezone.utc).date()
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
            self.ids.borrower_name.text = str(borrower_name[index])
            self.ids.loan_amount1.text = str(loan_amount[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.interest_rate.text = str(interest[index])
            self.ids.emi_amount.text = str(monthly_emi[index])

        pro_fee = total_pro_fee_amount[index] / tenure[index]
        monthly_interest = interest[index] / 12 / 100
        total_pay = tenure[index] * 12

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
                self.ids.extra.text = "Extra Payment (Late Payment Fee)"
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
                if default_type[product_index] == 'Non Performing Asset (%)':
                    default_amount = (monthly_emi[index] * default_percentage) / 100
                elif default_type[product_index] == 'Non Performing Asset (₹)':
                    default_amount = default_fee_amount[product_index] * days_left

                total_amount = monthly_emi[index] + extra_amount
                self.ids.extra.text = "Extra Payment(Default)"
                self.ids.extra_amount.text = str(extra_amount + default_amount)
                self.ids.total_amount.text = str(total_amount + default_amount)
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
                self.ids.extra_amount.text = str(extra_amount + npa_amount)
                self.ids.total_amount.text = str(total_amount + npa_amount)
                data1[index]['loan_state_status'] = 'npa'

            else:
                total_amount = monthly_emi[index] + extra_amount
                self.ids.extra_amount.text = str(extra_amount)
                self.ids.total_amount.text = str(total_amount)
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
                    next_payment_amount = next_emi['payment_amount']
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
                    self.ids.extra_amount.text = str(extend_amount + lapsed_amount)
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(total_amount + lapsed_amount)
                    self.ids.extra.text = "Extra Payment (Late Payment Fee)"
                    data1[index]['loan_state_status'] = "lapsed"
                elif (today_date - shechule_date[value]).days >= 10 and (today_date - shechule_date[value]).days < 98:
                    default_amount = 0
                    days_left = (today_date - shechule_date[value]).days - 17
                    product_index = product_id.index(loan_product[index])
                    default_percentage = default_fee_percentage[product_index] + days_left
                    print(default_percentage)
                    print(days_left)
                    if default_type[product_index] == 'Non Performing Asset (%)':
                        default_amount = (monthly_emi[index] * default_percentage) / 100
                    elif default_type[product_index] == 'Non Performing Asset (₹)':
                        default_amount = default_fee_amount[product_index]
                    self.ids.extra_amount.text = str(extend_amount + default_amount)
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(total_amount + default_amount)
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
                    self.ids.extra_amount.text = str(extend_amount + npa_amount)
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(total_amount + npa_amount)
                    self.ids.extra.text = "Extra Payment (Default)"
                    data1[index]['loan_state_status'] = 'npa'
                else:
                    self.ids.extra_amount.text = str(extend_amount)
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(total_amount)
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
                    self.ids.extra_amount.text = str(foreclose_amount1 + lapsed_amount)
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(total_amount + lapsed_amount)
                    self.ids.total.text = "Total Amount (Late Payment Fee)"
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
                    if default_type[product_index] == 'Non Performing Asset (%)':
                        default_amount = (monthly_emi[index] * default_percentage) / 100
                    elif default_type[product_index] == 'Non Performing Asset (₹)':
                        default_amount = default_fee_amount[product_index]
                    self.ids.extra_amount.text = str(foreclose_amount1 + default_amount)
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(total_amount)
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
                    self.ids.extra_amount.text = str(foreclose_amount1 + npa_amount)
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(total_amount + npa_amount)
                    self.ids.extra.text = "Extra Payment (Default)"
                    data1[index]['loan_state_status'] = "default"
                    data1[index]['loan_updated_status'] = "closed"

                else:
                    self.ids.extra.text = "Extra Payment"
                    self.ids.extra_amount.text = str(foreclose_amount1)
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(total_amount)
                    data1[index]['loan_updated_status'] = "closed"

    date = datetime.today()

    def get_table_data(self):

        return anvil.server.call('get_today_data')

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

    def profile(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('profile')

    def menu(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_extension_data')

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

    def on_back_button_press(self):
        self.manager.current = 'TodayDuesTD'


class MyScreenManager(ScreenManager):
    pass
