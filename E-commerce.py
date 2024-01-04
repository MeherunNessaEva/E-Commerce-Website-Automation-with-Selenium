import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

custom_option= webdriver.ChromeOptions()
custom_option.add_experimental_option("detach",True)
custom_option.add_argument("--start-maximized")
driver=webdriver.Chrome(options=custom_option)
driver.get('https://tutorialsninja.com/demo/')
driver.maximize_window()

#select phones and PDA's
phones=driver.find_element(By.XPATH,"//a[text()='Phones & PDAs']")
phones.click()

#select iphone
iphone=driver.find_element(By.XPATH,"//a[text()='iPhone']")
iphone.click()
time.sleep(2)

#Show picture of mobile
first_pic=driver.find_element(By.XPATH,"//ul[@class='thumbnails']/li[1]")
first_pic.click()
time.sleep(2)

next_click=driver.find_element(By.XPATH,'//button[@title="Next (Right arrow key)"]')
for i in range (0,5):
    next_click.click()
    time.sleep(2)

#save screenshot
driver.save_screenshot("screenshot.png")

#close
x_button=driver.find_element(By.XPATH,"//button[@title='Close (Esc)']")
x_button.click()
time.sleep(2)

#quantity
quantity=driver.find_element(By.XPATH,'//input[@id="input-quantity"]')
quantity.click()
time.sleep(1)

#clear and add quantity
quantity.clear()
time.sleep(1)
quantity.send_keys('2')
time.sleep(1)


#added to cart(iphone)
add_to_button=driver.find_element(By.XPATH,'//button[@class="btn btn-primary btn-lg btn-block"]')
add_to_button.click()
time.sleep(2)

#select laptops and notebooks
laptop=driver.find_element(By.XPATH,'//a[text()="Laptops & Notebooks"]')
action=ActionChains(driver)
action.move_to_element(laptop).perform()
time.sleep(1)
laptop_2=driver.find_element(By.XPATH,'//a[text()="Show AllLaptops & Notebooks"]')
laptop_2.click()

#select laptop
HP=driver.find_element(By.XPATH,'//img[@title="HP LP3065"]')
HP.click()
time.sleep(2)

#scroll down
add_to_button_2=driver.find_element(By.XPATH,'//button[text()="Add to Cart"]')
add_to_button_2.location_once_scrolled_into_view
time.sleep(2)

#add delivary date
calender=driver.find_element(By.XPATH,'//i[@class="fa fa-calendar"]')
calender.click()
time.sleep(1)

next_click_calender=driver.find_element(By.XPATH,'//th[@class="next"]')
month_year=driver.find_element(By.XPATH,'//th[@class="picker-switch"]')
while month_year.text != "January 2024":
    next_click_calender.click()

date=driver.find_element(By.XPATH,'//td[text()="7"]')
date.click()
time.sleep(2)
add_to_button_2.click()
time.sleep(2)

#add to cart (laptop_HP)
go_to_cart=driver.find_element(By.XPATH,'//span[@id="cart-total"]')
go_to_cart.click()
time.sleep(1)

#checkout products
checkout=driver.find_element(By.XPATH,'//p[@class="text-right"]/a[2]')
checkout.click()
time.sleep(1)

#remove a product from cart
remove=driver.find_element(By.XPATH,'//button[@class="btn btn-danger"]')
remove.click()
time.sleep(2)

#new checkout after removing
new_checkout=driver.find_element(By.XPATH,'//div[@class="pull-right"]')
new_checkout.click()
time.sleep(2)

#place order as a guest
guest=driver.find_element(By.XPATH,'//input[@value="guest"]')
guest.click()

#to continue
continue_1=driver.find_element(By.XPATH,'//input[@id="button-account"]')
continue_1.click()
time.sleep(2)

#scroll the page of payment details
step_2=driver.find_element(By.XPATH,'//a[@class="accordion-toggle"]')
step_2.location_once_scrolled_into_view
time.sleep(2)

#add first name
first_name=driver.find_element(By.XPATH,'//input[@id="input-payment-firstname"]')
first_name.click()
time.sleep(1)
first_name.send_keys("ABC")
time.sleep(1)

#add last name
last_name=driver.find_element(By.XPATH,'//input[@id="input-payment-lastname"]')
last_name.click()
time.sleep(1)
last_name.send_keys("XYZ")
time.sleep(1)

#add email_id
email=driver.find_element(By.XPATH,'//input[@id="input-payment-email"]')
email.click()
time.sleep(1)
email.send_keys("abc@gmail.com")
time.sleep(1)

#add telephone
telephone=driver.find_element(By.XPATH,'//input[@id="input-payment-telephone"]')
telephone.click()
time.sleep(1)
telephone.send_keys("01565799555")
time.sleep(1)

#add address
address_1=driver.find_element(By.XPATH,'//input[@id="input-payment-address-1"]')
address_1.click()
time.sleep(1)
address_1.send_keys("PQR")
time.sleep(1)

#add city
city=driver.find_element(By.XPATH,'//input[@id="input-payment-city"]')
city.click()
time.sleep(1)
city.send_keys("Dhaka")
time.sleep(1)

#add postcode
postcode=driver.find_element(By.XPATH,'//input[@id="input-payment-postcode"]')
postcode.click()
time.sleep(1)
postcode.send_keys("123")
time.sleep(1)

#select country
country=driver.find_element(By.XPATH,'//select[@id="input-payment-country"]')
dropdown=Select(country)
dropdown.select_by_visible_text("Bangladesh")
time.sleep(1)

#select region
region=driver.find_element(By.XPATH,'//select[@id="input-payment-zone"]')
dropdown_2=Select(region)
dropdown_2.select_by_visible_text("Dhaka")
time.sleep(1)

#to continue
continue_2=driver.find_element(By.XPATH,'//input[@id="button-guest"]')
continue_2.click()
time.sleep(2)

#to continue
continue_3=driver.find_element(By.XPATH,'//input[@id="button-shipping-method"]')
continue_3.click()
time.sleep(2)

#agree to Terms and Conditions
terms_condition=driver.find_element(By.XPATH,'//input[@name="agree"]')
terms_condition.click()
time.sleep(2)

#to continue
continue_4=driver.find_element(By.XPATH,'//input[@id="button-payment-method"]')
continue_4.click()
time.sleep(2)

#print final price in console
final_price=driver.find_element(By.XPATH,'//table[@class="table table-bordered table-hover"]//tfoot//tr[3]//td[2]')
print("The final price of the product is: " ,final_price.text )
time.sleep(2)

#to confirm
confirm=driver.find_element(By.XPATH,'//input[@id="button-confirm"]')
confirm.click()
time.sleep(2)

#confirmation message
message=driver.find_element(By.XPATH,'//div[@class="col-sm-12"]//h1')
print(message.text)
time.sleep(2)

driver.close()
