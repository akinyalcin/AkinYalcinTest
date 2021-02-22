
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urljoin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from TestData import TestData


class WebDriverTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Setup of WebDriver test cases.
        """
        cls.driver = webdriver.Chrome(executable_path=r'E:\Softtech\hepsiburada\driver\chromedriver.exe')
        #cls.driver = webdriver.Firefox(executable_path=r'E:\Softtech\hepsiburada\driver\geckodriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(TestData.base_url)
        cls.driver.implicitly_wait(10)

    def test_01_homepage(self):

        """
        Homepage test steps:
        1. Check title is correct.
        2. Check header is displayed.
        3. Check different pages on homepage.
        4. Check footer is displayed.
        """
        driver = self.driver
        #Check the homepage title is correct
        self.assertEqual(TestData.homePageTitle, driver.title, "Wrong title!")
        print("Title is correct!")

        #Check the header is displayed on the page
        driver.find_element_by_class_name("sf-OldHeader-5sPZX").is_displayed()
        print("Header is displayed!")

        #Check the hero image is displayed and clickable on the page
        driver.find_element_by_class_name("sf-HerouselBaseTemplate-140fN").is_displayed()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "sf-HerouselBaseTemplate-140fN"))
        )
        print("Image is displayed and clickable!")

        #Check different pages on the page

        driver.find_element_by_class_name("sf-DealOfTheDay-3mP0O").is_displayed()
        driver.find_element_by_class_name("sf-MarketingBillboard-1UkbC").is_displayed()
        driver.find_element_by_class_name("sf-FeatureList-3R48W").is_displayed()
        driver.find_element_by_class_name("sf-Recommendation-aOWMV").is_displayed()
        driver.find_element_by_class_name("sf-Explore-1pWGu").is_displayed()
        print("Other pages are displayed!")


        #Check the footer end is displayed
        driver.find_element_by_tag_name("body").send_keys(Keys.END)
        time.sleep(5)
        driver.find_element_by_class_name("footer-end").is_displayed()
        print("Footer is displayed!")

        print("Homepage is loaded successfully!")

    def test_02_createAccount(self):

        """
        Create an account test steps:
        1. Open create account url.
        2. Enter account informations.
        3. Create an account.
        4. Check the account title is correct.
        """
        print("Create an Account")
        driver = self.driver
        self.signup_url = TestData.signup_url
        if self.signup_url != self.driver.current_url:
            self.driver.get(self.signup_url)
        time.sleep(10)

        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]").click()
        self.driver.find_element_by_id("txtName").clear()
        self.driver.find_element_by_id("txtName").send_keys(TestData.username)
        self.driver.find_element_by_id("txtSurname").clear()
        self.driver.find_element_by_id("txtSurname").send_keys(TestData.userSurname)
        self.driver.find_element_by_id("txtEmail").clear()
        self.driver.find_element_by_id("txtEmail").send_keys(TestData.email)
        self.driver.find_element_by_id("txtNewPassEmail").clear()
        self.driver.find_element_by_id("txtNewPassEmail").send_keys(TestData.password)
        self.driver.find_element_by_id("btnSignUpSubmit").click()
        time.sleep(10)
        self.driver.refresh()
        title = self.driver.find_element_by_id("myAccount").text
        print(title)
        self.assertEqual(TestData.myAccountTitle, title, "Titles did not match!")
        print("The account has been successfully created!")


    def test_03_loginAccount(self):

        """
        Login account test steps:
        1. Open login url.
        2. Enter wrong login informations.
        3. Check the error message is displayed.
        4. Enter correct login informations.
        5. Check the account title is correct.
        6. Add a new shipping address.
        7. Add a new billing address.
        """

        print("Login Account")
        driver = self.driver
        self.login_url = TestData.login_url
        if self.login_url != self.driver.current_url:
            self.driver.get(self.login_url)
        self.driver.implicitly_wait(10)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div[4]/div").click()

        self.driver.find_element_by_id("txtUserName").clear()
        self.driver.find_element_by_id("txtUserName").send_keys(TestData.email)
        self.driver.find_element_by_id("txtPassword").clear()
        self.driver.find_element_by_id("txtPassword").send_keys(TestData.wrong_password)
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/"
                                               "div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]").is_displayed()
        print("Wrong username or password. Login failed!")
        self.driver.find_element_by_id("txtUserName").clear()
        self.driver.find_element_by_id("txtUserName").send_keys(TestData.email)
        self.driver.find_element_by_id("txtPassword").clear()
        self.driver.find_element_by_id("txtPassword").send_keys(TestData.password)
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(10)
        self.driver.refresh()
        title = self.driver.find_element_by_id("myAccount").text
        print(title)
        self.assertEqual(TestData.myAccountTitle, title, "Titles did not match!")
        print("The account has been logged in successfully!")

        #Add shipping address
        self.driver.get(TestData.account_url)
        time.sleep(5)
        self.driver.refresh()
        driver.find_element_by_xpath("//*[@id='AccountMenu']/div/div/div[2]/div/div[7]/a/div[2]").click()
        driver.find_element_by_xpath("//*[@id='customer-addresses']/div/div/div/ul/li/a").click()
        driver.find_element_by_name("firstName").send_keys(TestData.username)
        driver.find_element_by_name("lastName").send_keys(TestData.userSurname)
        driver.find_element_by_xpath("//*[@id='form-address']/div/div/section[2]/div[3]/div/div/button/span[2]").click()
        driver.find_element_by_xpath(
            "//*[@id='form-address']/div/div/section[2]/div[3]/div/div/div/ul/li[4]/a/span").click()
        driver.find_element_by_xpath("//*[@id='form-address']/div/div/section[2]/div[4]/div/div/button/span[2]").click()
        driver.find_element_by_xpath(
            "//*[@id='form-address']/div/div/section[2]/div[4]/div/div/div/ul/li[5]/a/span").click()
        driver.find_element_by_name("address").send_keys(TestData.addresLine)
        driver.find_element_by_name("addressName").send_keys("Ev")
        driver.find_element_by_name("phone").send_keys(TestData.phone)
        driver.find_element_by_xpath("//*[@id='form-address']/div/div/div[2]/div/button").click()
        time.sleep(5)
        print("Shipping address is created!")

        #Add billing address
        driver.find_element_by_xpath("//*[@id='customer-addresses']/div/ul/li[2]/a").click()
        driver.find_element_by_xpath("//*[@id='customer-addresses']/div/div/div/ul/li/a").click()
        driver.find_element_by_name("firstName").send_keys(TestData.username)
        driver.find_element_by_name("lastName").send_keys(TestData.userSurname)
        driver.find_element_by_xpath("//*[@id='form-address']/div/div/section[2]/div[3]/div/div/button/span[2]").click()
        driver.find_element_by_xpath(
            "//*[@id='form-address']/div/div/section[2]/div[3]/div/div/div/ul/li[4]/a/span").click()
        driver.find_element_by_xpath("//*[@id='form-address']/div/div/section[2]/div[4]/div/div/button/span[2]").click()
        driver.find_element_by_xpath(
            "//*[@id='form-address']/div/div/section[2]/div[4]/div/div/div/ul/li[5]/a/span").click()
        driver.find_element_by_name("address").send_keys(TestData.addresLine)
        driver.find_element_by_name("addressName").send_keys("Ev")
        driver.find_element_by_name("phone").send_keys(TestData.phone)
        driver.find_element_by_xpath("//*[@id='form-address']/div/div/div[4]/div/button").click()
        time.sleep(5)
        print("Billing address is created!")

    def test_04_search(self):

        """
        Search test steps:
        1. Open homepage.
        2. Search according to the product.
        3. Check how many products are displayed on the page.
        4. Check the results are releated to the search product.
        5. Navigate to the second page.
        6. Check how many products are displayed on the page.
        7. Check the results are releated to the search product.
        8. Check search according to the category.
        9. Check the first element of the category list.
        10. Check how many products are displayed on the page.
        11. Navigate to the second page.
        12. Check how many products are displayed on the page.
        13. Check search according to the brand.
        14. Check how many products are displayed on the page.
        15. Navigate to the second page.
        16. Check how many products are displayed on the page.
        """

        driver = self.driver
        driver.get(TestData.base_url)
        time.sleep(5)

        ### Check search field according to product ###

        print("Check search field according to product:")
        driver.find_element_by_class_name("desktopOldAutosuggestTheme-input").send_keys(TestData.searchProduct)
        driver.find_element_by_class_name("SearchBoxOld-buttonContainer").click()
        time.sleep(5)
        driver.find_element_by_class_name("category-suggestion-title")
        keyword = driver.find_element_by_xpath("//*[@id='categorySuggestionList']/div[1]/h1").text
        self.assertEqual(keyword, TestData.searchProduct, "Keywords are not matched!")

        # Check how many products are shown on the first page
        results = driver.find_elements_by_class_name("product-detail")
        print(len(results), "products are shown on the first page!")

        # Check the results are related to the search text
        for i in range(len(results)):
            self.assertIn(TestData.searchProduct, results[i].text, "Product info does not contain the search text!")
        print("All products are related to the search!")

        # Navigate to the second page
        driver.find_element_by_class_name("page-2").click()
        time.sleep(5)

        # Check how many products are shown on the second page
        results = driver.find_elements_by_class_name("product-detail")
        print(len(results), "products are shown on the second page!")

        # Check the results are related to the search text
        for i in range(len(results)):
            self.assertIn(TestData.searchProduct, results[i].text, "Product info does not contain the search text!")
        print("All products are related to the search!")
        driver.find_element_by_class_name("desktopOldAutosuggestTheme-input").clear()

        ### Check search field according to category ###

        print("Check search field according to category:")
        driver.find_element_by_class_name("desktopOldAutosuggestTheme-input").send_keys(TestData.searchCategory)
        driver.find_element_by_class_name("SearchBoxOld-buttonContainer").click()
        time.sleep(5)
        driver.find_element_by_class_name("category-suggestion-title")
        keyword = driver.find_element_by_xpath("//*[@id='categorySuggestionList']/div[1]/h1").text
        self.assertEqual(keyword, TestData.searchCategory, "Keywords are not matched!")

        # Check the first element of the category list
        categoryList = driver.find_elements_by_id("categoryList")
        self.assertIn(TestData.searchCategory, categoryList[0].text, "Category item does contain the search text!")

        # Check how many products are shown on the first page
        results = driver.find_elements_by_class_name("product-detail")
        print(len(results), "products are shown on the first page!")

        # Navigate to the second page
        driver.find_element_by_class_name("page-2").click()
        time.sleep(5)

        # Check how many products are shown on the second page
        results = driver.find_elements_by_class_name("product-detail")
        print(len(results), "products are shown on the second page!")
        driver.find_element_by_class_name("desktopOldAutosuggestTheme-input").clear()

        ### Check search field according to brand ###

        print("Check search field according to brand:")
        driver.find_element_by_class_name("desktopOldAutosuggestTheme-input").send_keys(TestData.searchBrand)
        driver.find_element_by_class_name("SearchBoxOld-buttonContainer").click()
        time.sleep(5)
        driver.find_element_by_class_name("category-suggestion-title")
        keyword = driver.find_element_by_xpath("//*[@id='categorySuggestionList']/div[1]/h1").text
        self.assertEqual(keyword, TestData.searchBrand, "Keywords are not matched!")

        # Check how many products are shown on the first page
        results = driver.find_elements_by_class_name("product-detail")
        print(len(results), "products are shown on the first page!")

        # Navigate to the second page
        driver.find_element_by_class_name("page-2").click()
        time.sleep(5)

        # Check how many products are shown on the second page
        results = driver.find_elements_by_class_name("product-detail")
        print(len(results), "products are shown on the second page!")
        driver.find_element_by_class_name("desktopOldAutosuggestTheme-input").clear()


    def test_05_productDetails(self):

        """
        Product Details test steps:
        1. Search brand.
        2. Select the first product from the results.
        3. Get the product details
        """

        driver = self.driver

        ### Check product details ###
        print("Check search field according to brand:")
        driver.find_element_by_class_name("desktopOldAutosuggestTheme-input")\
            .send_keys(TestData.productname)
        driver.find_element_by_class_name("SearchBoxOld-buttonContainer").click()
        time.sleep(5)

        results = driver.find_elements_by_class_name("product-detail")
        print(len(results), "products are shown on the first page!")
        results[0].click()
        time.sleep(5)
        productName = driver.find_element_by_id("product-name").text
        print("Product Name: ", productName)
        productPrice = driver.find_element_by_id("offering-price").text
        print("Product Price: ", productPrice)
        productDiscount = driver.find_element_by_xpath(".//span[@class ='discount-amount']")
        print("Product Discount: ", productDiscount)
        productSeller = driver.find_element_by_class_name("seller-container").text
        print("Product Seller and Rating: ", productSeller)
        shipment = driver.find_element_by_xpath("/html/body/div[2]/main/div[3]/section[1]/"
                                                "div[5]/div/div[4]/div[1]/div[5]/div/div[2]/div/ul/li[1]").text
        print("Shipment: ", shipment)
        rating = driver.find_element_by_class_name("rating-information").text
        print("Rating: ", rating)

    def test_06_shoppingCart(self):

        """
        Shopping Cart test steps:
        1. Search brand.
        2. Sorting from expensive to cheap.
        3. Select the first product from the results.
        4. Add the product to the cart.
        5. Check the product quantity and price.
        6. Delete the product from the cart.
        7. Add prudoct again to the cart.
        8. Check the prices again.
        9. Navigate to payment page.
        10. Select the shipping address.
        11. Select credit card as a payment type.
        12. Enter wrong credit card informations.
        13. Check the error message.
        """

        driver = self.driver

        ### Check product details ###
        print("Check search field according to brand:")
        driver.find_element_by_class_name("desktopOldAutosuggestTheme-input")\
            .send_keys(TestData.searchProduct)
        driver.find_element_by_class_name("SearchBoxOld-buttonContainer").click()
        time.sleep(5)

        driver.find_element_by_xpath("//*[text()='Fiyat Azalan']").click()

        results = driver.find_elements_by_class_name("product-detail")
        print(len(results), "products are shown on the first page!")

        results[0].click()
        time.sleep(5)

        quantity = driver.find_element_by_id("quantity").get_attribute("value")
        print("Quantity: ", quantity)

        productPrice = driver.find_element_by_id("offering-price").text
        productPriceLast = productPrice[:-3]
        print("Product Price: ", productPriceLast)
        driver.find_element_by_id("addToCart").click()
        time.sleep(5)
        self.driver.refresh()
        cartQuantity = driver.find_element_by_id("cartItemCount").text
        self.assertEqual(quantity,cartQuantity,"Quantity Error!")
        print("Product is added to the cart!")
        driver.find_element_by_id("shoppingCart").click()
        time.sleep(5)

        totalPrice = driver.find_element_by_class_name("total_price_3V-CM").text
        totalPriceLast = totalPrice[:-3]
        print("Total Price: ", totalPriceLast)
        self.assertEqual(productPriceLast, totalPriceLast, "Product and Total Price are not equal!")

        driver.find_element_by_class_name("product_delete_1zR-0").click()
        deleteText = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div[2]"
                                                  "/div[1]/div[1]/div/div[2]/span").text
        self.assertEqual(TestData.productDeletedText, deleteText, "Delete Error!")
        print("Product is deleted successfully!")
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div[2]/div[1]"
                                     "/div[1]/div/div[2]/div[1]/a[1]").click()
        totalPrice = driver.find_element_by_class_name("total_price_3V-CM").text
        totalPriceLast = totalPrice[:-3]
        print("Total Price: ", totalPriceLast)
        self.assertEqual(productPriceLast, totalPriceLast, "Product and Total Price are not equal!")
        time.sleep(5)
        driver.find_element_by_id("continue_step_btn").click()
        time.sleep(5)

        driver.find_element_by_xpath("//*[@id='shipping']/div/div[1]/div[1]/div[1]/label/input").click()
        driver.find_element_by_id("continue_step_btn").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='payment-methods']/div/div[1]/div[1]/div[1]/label/input").click()
        driver.find_element_by_name("cardNumber").send_keys(TestData.cardNumber)
        driver.find_element_by_name("holderName").send_keys(TestData.holderName)
        driver.find_element_by_name("expireDate").send_keys(TestData.expireDate)
        driver.find_element_by_name("cvv").send_keys(TestData.cvv)

        invalidCardText = driver.find_element_by_xpath("//*[@id='payment-methods']/div[1]/div/div[2]/div/div[1]" \
                                                              "/form/div[1]/div[1]/div/div/span").text
        self.assertEqual(invalidCardText, TestData.invalidCard, "Invalid Card Message Error!")
        print("Payment error because of invalid card data!")
        print("Test completed successfully!")


    @classmethod
    def tearDownClass(cls):
        """
        Terminates the WebDriver test case session.
        """
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
