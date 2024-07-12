import base64
import json
import os
import random
import smtplib
import sqlite3
from datetime import datetime
from email.message import EmailMessage

import bcrypt
from bson import utc
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from twilio.rest import Client

import anvil.server
from anvil.tables import app_tables

from borrower_dashboard import DashboardScreen
from chatbot import ChatBotScreen
from dashboard import DashScreen

from lender_dashboard import LenderDashboard
from login import OTPScreen, PreLoginScreen
from new_loan_request import NewloanScreen
from signup import SignupScreen, EmailOTPScreen

anvil.server.connect("server_ICVO6RJCL6BCD7JT3ASVXABB-DVKXHXN3FMGIYIJX")


class MyApp(MDApp):
    otp_screen_visible = BooleanProperty(False)
    client = Client("TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN")
    n = random.randint(100000, 999999)
    dialog = None

    def build(self):
        self.sm = ScreenManager(transition=SlideTransition())
        self.load_initial_screen()

        # Add all the screens to the ScreenManager
        main_screen = PreLoginScreen(name='prelogin')
        otp_screen = OTPScreen(name='otp')
        signup_screen = SignupScreen(name='SignupScreen')
        email_otp_screen = EmailOTPScreen(name='email_otp')
        chatbot_screen = ChatBotScreen(name ="ChatBotScreen")
        self.sm.add_widget(main_screen)
        self.sm.add_widget(otp_screen)
        self.sm.add_widget(signup_screen)
        self.sm.add_widget(email_otp_screen)
        self.sm.add_widget(chatbot_screen)

        return self.sm

    def toggle_password_visibility(self, password_field1, password_field2, icon_button):
        password_field1.password = not password_field1.password
        password_field2.password = not password_field2.password
        icon_button.icon = "eye" if password_field1.password else "eye-off"


    def resend_otp(self):
        ##user_input = login_screen.ids.user_input.text
        self.verify_login()

    def verify_email(self):
        signup_screen = self.root.get_screen('SignupScreen')
        user_input = signup_screen.ids.user_input.text.strip()
        if user_input:
            self.send_otp(signup=True)
        else:
            self.show_dialog("Please enter email ID or phone number")

    def verify_login(self):
        login_screen = self.root.get_screen('login')
        user_input = login_screen.ids.user_input.text.strip()
        print(f"User input: {user_input}")  # Debug print
        login_screen = self.root.get_screen('login')
        login_screen.ids.otp_input.opacity = 1
        login_screen.ids.otp_input.disabled = False
        login_screen.ids.disable_otp.opacity = 1
        login_screen.ids.disable_otp.disabled = False
        login_screen.ids.verify_otp.opacity = 1
        login_screen.ids.verify_otp.disabled = False

        login_screen.ids.login_with_otp.disabled = True
        if user_input:
            self.send_otp(signup=False)
        else:
            self.show_dialog("Please enter email ID or phone number")

    def send_otp(self, signup=True):
        if signup:
            signup_screen = self.root.get_screen('SignupScreen')
            user_input = signup_screen.ids.user_input.text.strip()
        else:
            login_screen = self.root.get_screen('login')
            user_input = login_screen.ids.user_input.text.strip()

        print(f"Sending OTP to: {user_input}")  # Debug print

        if user_input:
            self.n = random.randint(100000, 999999)
            if "@" in user_input:
                self.send_email_otp(user_input)
            else:
                self.send_sms_otp(user_input)
            if signup:
                self.show_email_otp_screen(user_input, signup=True)
            else:
                pass
        else:
            self.show_dialog("Please enter a phone number or email ID")

    def send_sms_otp(self, user_input):
        try:
            if not user_input.startswith("+"):
                user_input = "+91" + user_input
            self.client.messages.create(
                to=user_input,
                from_="+15302874473",
                body=f"Your OTP is: {self.n}"
            )
            self.show_dialog("OTP sent via SMS")
        except Exception as e:
            self.show_dialog(f"Failed to send SMS: {e}")

    def send_email_otp(self, email):
        try:
            from_mail = "gtpl.march2023@gmail.com"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_mail, "ohcz etov xtpy zhne")

            msg = EmailMessage()
            msg['Subject'] = "OTP Verification"
            msg['From'] = from_mail
            msg['To'] = email
            msg.set_content(f"Your OTP is: {self.n}")
            server.send_message(msg)
            server.quit()
            self.show_dialog("OTP sent via Email")
        except Exception as e:
            self.show_dialog(f"Failed to send email: {e}")

    def check_otp(self):
        login_screen = self.root.get_screen('login')
        entered_otp = login_screen.ids.otp_input.text
        user_input = login_screen.ids.user_input.text

        if str(self.n) == entered_otp:
            self.show_dialog("OTP verified successfully")
            self.sm.add_widget(OTPScreen(name='otp'))
            self.sm.current = 'otp'
        else:
            self.show_dialog("Invalid OTP. Please try again.")

    def update_password(self):
        login_screen = self.root.get_screen('login')
        user_input = login_screen.ids.user_input.text
        otp_screen = self.root.get_screen('otp')
        password = otp_screen.ids.password.text
        password2 = otp_screen.ids.password2.text

        if password and password2 and password == password2:
            try:
                # Hash the password
                hashed_password_str = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

                # Update the password in Anvil table
                user = app_tables.users.get(email=user_input)
                if user:
                    user['password_hash'] = hashed_password_str

                self.show_dialog("Password updated successfully")
                self.sm.add_widget(PreLoginScreen(name='prelogin'))
                self.sm.current = 'prelogin'
            except Exception as e:
                self.show_dialog(f"Failed to update password in Anvil table: {e}")
        else:
            self.show_dialog("Passwords do not match")

    def show_dialog(self, message):
        if not self.dialog:
            self.dialog = MDDialog(
                text=message,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=lambda x: self.dialog.dismiss()
                    )
                ]
            )
        self.dialog.text = message
        self.dialog.open()

    def send_signup_success_email(self, email):
        try:
            from_mail = "gtpl.march2023@gmail.com"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_mail, "ohcz etov xtpy zhne")

            msg = EmailMessage()
            msg['Subject'] = "Welcome to P2P Lending Platform!"
            msg['From'] = from_mail
            msg['To'] = email
            msg.set_content(f"""
            Hello,

            Welcome to P2P Lending Platform!

            Thank you for joining. We're excited to have you join our community of lenders and borrowers.
            Complete signup and registration process.
            Get started by logging in and exploring the opportunities available to you.

            Best regards,
            The P2P Team
            """)

            server.send_message(msg)
            server.quit()
            print("Signup success email sent.")
        except Exception as e:
            print(f"Failed to send signup success email: {e}")
    def check_otp_email(self, signup=True):
        email_otp_screen = self.root.get_screen('email_otp')
        entered_otp = email_otp_screen.ids.otp_input.text
        if str(self.n) == entered_otp:
            if signup:
                signup_screen = self.root.get_screen('SignupScreen')
                user_input = signup_screen.ids.user_input.text.strip()
                self.update_email_verification_status(user_input)
                self.show_dialog("Email verified successfully")
                signup_screen.ids.verify_button.text = "verified"
                signup_screen.ids.user_input.helper_text = "Email verified successfully. Click signup to continue"
                signup_screen.ids.user_input.helper_text_color = (0, 1, 0, 1)
                Clock.schedule_once(self.go_to_signup_screen, 0)
                self.send_signup_success_email(user_input)
            else:
                self.show_dialog("OTP verified successfully")
                # Handle other case if needed
        else:
            self.show_dialog("Invalid OTP. Please try again.")

    def update_email_verification_status(self, email):
        try:
            # Connect to Anvil server
            anvil.server.connect("server_UZIZ2X7JH2VWL7MZUF3E7H2W-Z4NNV2LPHIX6BAPW")

            # Check if the email already exists in the table
            user = app_tables.users.get(email=email)

            if user is not None:
                # Update the existing row
                user.update(email_verified=True)
            else:
                # Create a new row
                app_tables.users.add_row(email=email, email_verified=True)
        except Exception as e:
            print(f"Error updating email verification status: {e}")

    def go_to_signup_screen(self, dt):
        self.sm.current = 'SignupScreen'

    def perform_database_operations(self, entered_email):
        print(entered_email)
        conn = sqlite3.connect("fin_user.db")
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM fin_users
            WHERE email = ?
        ''', (entered_email,))

        user_data = cursor.fetchone()
        data = app_tables.users.search()
        profile = app_tables.fin_user_profile.search()
        email_list = []
        registration_approve = []
        user_type = []
        email_user = []

        for i in data:
            email_list.append(i['email'])
        for i in profile:
            registration_approve.append(i['registration_approve'])
            user_type.append(i['usertype'])
            email_user.append(i['email_user'])

        if entered_email in email_list:
            i = email_list.index(entered_email)
            if entered_email in email_user:
                index = email_user.index(entered_email)
            else:
                self.show_dialog('No email found')
                return

            if (email_list[i] == entered_email) and (registration_approve[index] is True):
                # Update and save user info to email.json
                self.save_user_info(entered_email, user_type[index])

                if user_type[index] == 'borrower':
                    Clock.schedule_once(lambda dt: self.show_dashboard('DashboardScreen'), 0)
                elif user_type[index] == 'lender':
                    Clock.schedule_once(lambda dt: self.show_dashboard('LenderDashboard'), 0)
                else:
                    Clock.schedule_once(lambda dt: self.show_dashboard('DashScreen'), 0)

                return
            elif registration_approve[index] is None or user_type[index] == "":
                Clock.schedule_once(lambda dt: self.show_dashboard('DashScreen'), 0)
                return
            else:
                Clock.schedule_once(lambda dt: self.show_error_dialog("Unapproved registration or other issue"), 0)
                return
        else:
            self.show_dialog("Email not found")

    def save_user_info(self, email, user_type):
        user_data = {
            'email': email,
            'logged_status': True,
            'user_type': user_type
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

    def show_dashboard(self, screen_name):
        if screen_name == 'DashboardScreen':
            self.sm.add_widget(DashboardScreen(name=screen_name))
        elif screen_name == 'LenderDashboard':
            self.sm.add_widget(LenderDashboard(name=screen_name))
        else:
            self.sm.add_widget(DashScreen(name=screen_name))
        self.sm.current = screen_name



    def show_email_otp_screen(self, user_input, signup=True):
        email_otp_screen = self.root.get_screen('email_otp')
        email_otp_screen.ids.user_contact.text = user_input
        self.sm.current = 'email_otp'

    def email_check_otp(self):  # Define the email_check_otp method
        self.check_otp_email(signup=True)

    def edit_user_input(self):
        self.root.current = 'login'

    def show_dialog(self, message):
        if self.dialog:
            self.dialog.dismiss()

        dialog = MDDialog(
            title="Success",
            text=message,
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

    def get_otp_call(self):
        login_otp_screen = self.root.get_screen('login')
        user_input = login_otp_screen.ids.user_input.text
        if user_input:
            self.n = random.randint(100000, 999999)
            self.send_voice_otp(user_input)
            self.show_otp_screen(user_input)  # Pass user_input to show_otp_screen
        else:
            self.show_dialog("Please enter a phone number or email ID")

    def send_voice_otp(self, user_input):
        try:
            if not user_input.startswith("+"):
                user_input = "+91" + user_input
            call = self.client.calls.create(
                twiml=f'<Response><Say>Your OTP is {self.n}</Say></Response>',
                to=user_input,
                from_="+14175242099"
            )
            self.show_dialog("OTP call initiated")
        except Exception as e:
            self.show_dialog(f"Failed to send OTP call: {e}")

    #### ended otp code ####

    def load_initial_screen(self):
        # Load initial screen based on logged status and user type
        with open("emails.json", "r") as file:
            user_data = json.load(file)
        print("user_data:", user_data)  # Debug print

        for email, data in user_data.items():
            print("email:", email)  # Debug print
            print("data type:", type(data))  # Debug print
            print("data:", data)  # Debug print
            if isinstance(data, dict) and data.get("logged_status", False):
                user_type = data.get("user_type", "")
                if user_type == "borrower":
                    self.sm.add_widget(DashboardScreen(name='DashboardScreen'))
                    self.sm.current = 'DashboardScreen'
                elif user_type == "lender":
                    self.sm.add_widget(LenderDashboard(name='LenderDashboard'))
                    self.sm.current = 'LenderDashboard'
                else:
                    self.sm.add_widget(DashScreen(name='DashScreen'))
                    self.sm.current = 'DashScreen'
                break
        else:
            self.sm.add_widget(PreLoginScreen(name='prelogin'))
            self.sm.current = 'prelogin'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        # Preload data when the app starts
        self.fetch_product_groups()

    def fetch_product_groups(self):
        try:
            # Fetch user email and profession
            email = anvil.server.call('another_method')
            user_row = app_tables.fin_user_profile.search(email_user=email)

            if not user_row:
                raise ValueError("User profile not found")

            user_profession = user_row[0]['profession']
            #print(f"User profession: {user_profession}")  # Debug statement

            # Fetch product details from the server
            product_groups = app_tables.fin_product_details.search()

            # Filter product groups based on user profession
            filtered_product_groups = [
                product for product in product_groups
                if user_profession in [occ.strip() for occ in product['occupation'].split(',')]
            ]

            # Extract unique product groups
            unique_groups = set(product['product_group'] for product in filtered_product_groups)

            # Update the Spinner with unique product groups
            spinner = self.root.get_screen('NewloanScreen').ids.group_id1
            spinner.values = list(unique_groups)
            # Clear other Spinners and labels
            self.clear_spinners_and_labels(['group_id2', 'group_id3'])
            self.clear_label('product_description')

            # Debugging: Print the filtered product groups
            #print(f"Number of product groups fetched: {len(unique_groups)}")
            for group in unique_groups:
                print(f"Filtered product group: {group}")

        except Exception as e:
            print(f"Error fetching product groups: {e}")

    def fetch_product_categories(self):
        # Clear other Spinners and labels
        self.clear_spinners_and_labels(['group_id3'])
        self.clear_label('product_description')

        # Get the selected product group
        selected_group = self.root.get_screen('NewloanScreen').ids.group_id1.text

        # Call the server function using Anvil Uplink to filter categories based on the selected group
        product_categories = app_tables.fin_product_details.search(product_group=selected_group)

        # Extract unique product categories for the selected group
        unique_categories = set(product['product_categories'] for product in product_categories)

        # Update the Spinner with unique product categories
        spinner = self.root.get_screen('NewloanScreen').ids.group_id2
        spinner.values = list(unique_categories)

    def fetch_product_name(self):
        # Clear other Spinners and labels
        self.clear_label('product_description')

        # Get the selected product category
        selected_category = self.root.get_screen('NewloanScreen').ids.group_id2.text

        # Call the server function using Anvil Uplink to filter product names based on the selected category
        product_names = app_tables.fin_product_details.search(product_categories=selected_category)

        # Extract unique product names for the selected category
        unique_names = set(product['product_name'] for product in product_names)

        # Update the Spinner with unique product names
        spinner = self.root.get_screen('NewloanScreen').ids.group_id3
        spinner.values = list(unique_names)

    def fetch_emi_type(self):
        # Get the selected product category
        selected_category = self.root.get_screen('NewloanScreen').ids.group_id3.text
        # Call the server function using Anvil Uplink to filter product names based on the selected category
        emi_type = app_tables.fin_product_details.search(product_name=selected_category)
        # Extract emi_type from the fetched data
        if emi_type:
            emi_type_list = emi_type[0]['emi_payment'].split(',')  # Split the emi_type string by commas
            # Update the Spinner with filtered product names
            spinner = self.root.get_screen('NewloanScreen').ids.group_id4
            spinner.values = emi_type_list
        else:
            # Clear the Spinner if no emi_type is found
            self.root.get_screen('NewloanScreen').ids.group_id4.values = []

    def fetch_product_description(self):
        # Get the selected product name
        selected_product_name = self.root.get_screen('NewloanScreen').ids.group_id3.text

        # Call the server function using Anvil Uplink to fetch the product description based on the selected product name
        product = app_tables.fin_product_details.search(product_name=selected_product_name)

        # Check if product list is not empty before accessing its elements
        if product:
            if len(product) > 0:
                product_description = product[0]['product_description']
                # Check if product_description is not None before updating the label
                if product_description is not None:
                    # Update the product description label with the fetched description
                    self.root.get_screen('NewloanScreen').ids.product_description.text = f" Discription: {product_description}"
                    self.root.get_screen('NewloanScreen').ids.loan_box.opacity = 1
                    self.root.get_screen('NewloanScreen').ids.loan_box.disabled = False
                    #self.root.get_screen('NewloanScreen').ids.loan_box.height = dp(350)
                else:
                    # Set a default message when product_description is None
                    self.root.get_screen('NewloanScreen').ids.product_description.text = "No description available"
            else:
                # Clear the product description label if no product is found
                self.root.get_screen('NewloanScreen').ids.product_description.text = ""
        else:
            # Clear the product description label if no product is found
            self.root.get_screen('NewloanScreen').ids.product_description.text = ""

    def clear_spinners_and_labels(self, spinner_ids):
        for spinner_id in spinner_ids:
            self.root.get_screen('NewloanScreen').ids[spinner_id].text = "Select"
            self.root.get_screen('NewloanScreen').ids[spinner_id].values = []

    def clear_label(self, label_id):
        self.root.get_screen('NewloanScreen').ids[label_id].text = ""

    def extension_on(self):
        extend = app_tables.fin_extends_loan.search()
        approval_date = app_tables.fin_approval_days.search()
        today_date = datetime.now(tz=utc).date()
        foreclose = app_tables.fin_foreclosure.search()
        data = app_tables.fin_loan_details.search()
        emi = app_tables.fin_emi_table.search()
        log_email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search()
        email_user = []
        customer_id = []

        for i in profile:
            email_user.append(i['email_user'])
            customer_id.append(i['customer_id'])
        if log_email in email_user:
            email_index = email_user.index(log_email)

        loan_id = []
        loan_tenure = []
        loan_customer_id = []

        for i in data:
            loan_id.append(i['loan_id'])
            loan_tenure.append(i['tenure'])
            loan_customer_id.append(i['borrower_customer_id'])

        if customer_id in loan_customer_id:
            cos = loan_customer_id.index(customer_id)

        requested_on = []
        extend_status = []
        loan_extend_id = []
        loan_rx_mon_tenure = []
        new_emi1 = []

        s = 0
        for i in extend:
            s += 1
            requested_on.append(i['extension_request_date'])
            extend_status.append(i['status'])
            loan_extend_id.append(i['loan_id'])
            loan_rx_mon_tenure.append(i['total_extension_months'])
            new_emi1.append(i['new_emi'])

        ext_lan = 0
        if loan_id in loan_extend_id:
            ext_lan = loan_extend_id.index(loan_id)

        emi_loan_id1 = []
        emi_remaining_tenure1 = []
        for i in emi:
            emi_loan_id1.append(i['loan_id'])
            emi_remaining_tenure1.append(i['remaining_tenure'])

        last_index = 0
        if loan_id not in emi_loan_id1:
            emi_number = 1
        else:
            last_index = len(emi_loan_id1) - 1 - emi_loan_id1[::-1].index(loan_id)

        #extend_mon = emi_remaining_tenure1[last_index] + loan_rx_mon_tenure[ext_lan]
        #tenure_month = loan_tenure[index1] + loan_rx_mon_tenure[ext_lan]

        for_request_time = []
        foreclose_status = []

        w = 0
        for i in foreclose:
            w += 1
            for_request_time.append(i['requested_on'])
            foreclose_status.append(i['status'])

        status_type = []
        app_date = []
        for i in approval_date:
            status_type.append(i['loans'])
            app_date.append(i['days_for_approval'])

        index = 0
        if "Extension" in status_type:
            index = status_type.index("Extension")
        index1 = 0
        if "Foreclosure" in status_type:
            index = status_type.index("Foreclosure")

        a = -1
        for i in range(s):
            a += 1
            if extend_status[i] == "under process" and requested_on != None :
                if ((today_date - requested_on[i].date()).days) >= app_date[index]:
                    if loan_extend_id[i] in emi_loan_id1:
                        last_index = len(emi_loan_id1) - 1 - emi_loan_id1[::-1].index(loan_extend_id[i])
                        emi[last_index]['remaining_tenure'] += loan_rx_mon_tenure[ext_lan]

                    if loan_extend_id[i] in loan_id:
                        tenure_index = loan_id.index(loan_extend_id[i])
                        data[tenure_index]['tenure'] += loan_rx_mon_tenure[ext_lan]
                        data[tenure_index]['monthly_emi'] = new_emi1[ext_lan]


                    extend[i]["status"] = "approved"

        y = -1
        for i in range(w):
            y += 1
            if foreclose_status[i] == "under process" and for_request_time != None:
                if ((today_date - for_request_time[i].date()).days) >= app_date[index1]:
                    foreclose[i]["status"] = "approved"

    def on_start(self):
        Window.softinput_mode = "below_target"
        self.extension_on()


class MyScreenManager(ScreenManager):
    pass


if __name__ == '__main__':
    MyApp().run()
