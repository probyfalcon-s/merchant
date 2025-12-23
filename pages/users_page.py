from playwright.sync_api import Page, expect



class CreateUserPage:
    def __init__(self, page: Page):
        self.page = page
        self.button_create = page.locator("//span[text()='Создать пользователя']")
        self.input_name = page.locator("//input[@id='name']")
        self.input_description = page.locator("//textarea[@id='description']")
        self.input_email_user = page.locator("//input[@id='email']")
        self.input_ipv4 = page.locator("//input[@id='ip4_access']")
        self.input_balance_commissions = page.locator("//input[@id='commission_balance']")
        self.button_next = page.locator("//span[text()='Далее']")
        self.button_create_user_end = page.locator("//span[text()='Создать']")


    def click_create_user(self):
        self.button_create.click()

    def enter_name_input(self, name):
        self.input_name.fill(name)

    def enter_description_input(self, description):
        self.input_description.fill(description)

    def enter_create_email_user_input(self, email_user):
        self.input_email_user.fill(email_user)

    def enter_ip4_input(self, ipv4):
        self.input_ipv4.fill(ipv4)

    def enter_balance_commissions_input(self, balance_commissions):
        self.input_balance_commissions.fill(balance_commissions)

    def click_next_button_user(self):
        self.button_next.click()


    async def click_create_button_user_end(self, custom_page=None):
        await self.button_create_user_end.click()

        locator = custom_page.locator('div.ant-notification-notice-message', has_text='Успех')
        await expect(locator).to_be_visible(timeout=3000)

