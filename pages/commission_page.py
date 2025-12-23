from playwright.sync_api import Page, expect


class CreateCommissionPage:
    def __init__(self, page: Page):
        self.page = page
        self.button_create_commission = page.locator("//span[text()='Создать комиссию']")
        self.input_amount_commission_usdt = page.locator("//input[@id='amount']")
        self.button_create_commission_end = page.locator("//span[text()='Создать']")

    '''общие методы commissions'''
    def click_create_commission(self):
        self.button_create_commission.click()

    def click_dropdown_menu_network_tax(self):
        dropdown = self.page.locator("input#network").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")
        dropdown_link = self.page.locator("div.ant-select-dropdown:visible div", has_text="BSC").last
        dropdown_link.click()

    def enter_amount_commission(self, commission):
        self.input_amount_commission_usdt.fill(commission)


    async def click_create_commission_end(self, custom_page=None):
        await self.button_create_commission_end.click()

        locator = custom_page.locator('div.ant-notification-notice-message', has_text='Успех')
        await expect(locator).to_be_visible(timeout=3000)

    '''методы commissions-transaction'''
    def click_dropdown_menu_type(self):
        dropdown = self.page.locator("input#type").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")

        print("Подсвечиваем элементы для отладки...")
        self.page.locator("div.ant-select-dropdown").highlight()
        self.page.locator("div.ant-select-dropdown:visible div:text('Транзакция')").highlight()

        dropdown_link = self.page.locator("div.ant-select-dropdown:visible div", has_text="Транзакция").last
        dropdown_link.click()

    def click_dropdown_menu_transaction(self):
        dropdown = self.page.locator("input#transaction").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")
        self.page.locator("div.ant-select-dropdown").highlight()
        self.page.locator("div.ant-select-dropdown:visible div.ant-select-item-option").highlight()

        first_item = self.page.locator("div.ant-select-dropdown:visible div.ant-select-item-option").first
        first_item.click()

    '''методы commissions-user'''
    def click_dropdown_menu_type_user(self):
        dropdown = self.page.locator("input#type").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")

        dropdown_link = self.page.locator("div.ant-select-dropdown:visible div", has_text="Пользователь").last
        dropdown_link.click()

    def click_dropdown_menu_commission_user(self):
        dropdown = self.page.locator("input#user").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")
        self.page.locator("div.ant-select-dropdown").highlight()
        self.page.locator("div.ant-select-dropdown:visible div.ant-select-item-option").highlight()

        first_item = self.page.locator("div.ant-select-dropdown:visible div.ant-select-item-option").first
        first_item.click()

    '''методы commissions-address'''
    def click_dropdown_menu_type_address(self):
        dropdown = self.page.locator("input#type").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")

        dropdown_link = self.page.locator("div.ant-select-dropdown:visible div", has_text="Адрес").last
        dropdown_link.click()

    def click_dropdown_menu_address_commission(self):
        dropdown = self.page.locator("input#addresses").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")
        self.page.locator("div.ant-select-dropdown").highlight()
        self.page.locator("div.ant-select-dropdown:visible div.ant-select-item-option").highlight()

        first_item = self.page.locator("div.ant-select-dropdown:visible div.ant-select-item-option").first
        first_item.click()



