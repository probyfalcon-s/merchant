from playwright.sync_api import Page

class PersonalAccountPage:
    def __init__(self, page: Page):
        self.page = page
        self.input_email = page.locator("//input[@id='auth_email']")
        self.input_password = page.locator("//input[@id='auth_password']")
        self.button_submit = page.locator("//button[@type='submit']")
        self.button_link_users = page.locator("//span[text()='Пользователи']")
        self.button_link_information = page.locator("//span[text()='Информация']")
        self.button_link_wallet = page.locator("//span[text()='Кошельки']")
        self.button_link_transaction = page.locator("//span[text()='Транзакции']")
        self.button_link_commissions = page.locator("//span[text()='Комиссии']")
        self.button_link_down = page.locator("//span[@aria-label='down']")
        self.button_link_russian = page.locator("//span[text()='Русский']")
        self.button_link_language = page.locator("//span[text()='Language']")


    def enter_email(self, email):
        self.input_email.fill(email)

    def enter_password(self, password):
        self.input_password.fill(password)

    def click_submit(self):
        self.button_submit.click()

    '''страницы переходов'''
    def click_link_users(self):
        self.button_link_users.click()

    def click_link_wallet(self):
        self.button_link_wallet.click()

    def click_link_information(self):
        self.button_link_information.click()

    def click_link_transaction(self):
        self.button_link_transaction.click()

    def click_link_commissions(self):
        self.button_link_commissions.click()

    def click_button_down(self):
        self.button_link_down.click()

    def click_link_language(self):
        self.button_link_language.click()

    def click_link_language_russian(self):
        self.button_link_russian.click()



