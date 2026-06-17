from selenium.webdriver.common.by import By

# Step 1:
account_field = (By.XPATH, '//div[@class="_10iL_95W"]//div[@class=\
                           "_2CSyqUbD"]')
email_field = (By.CSS_SELECTOR, "div.left-1kKiY div.inputGroupWrap-2MjaI")
continue_botton = (By.CSS_SELECTOR, "#submit-button")
password_field = (By.CSS_SELECTOR, "#pwdInputInLoginDialog")
login_botton = (By.CSS_SELECTOR, "#submit-button")

# Extra step if you do not allow marketing email:
exit_botton = (By.CSS_SELECTOR, "div[role='dialog'] svg._2IxJmTj7")

# Step 2:
search_field = (By.ID, 'searchInput')
search_botton = (By.CSS_SELECTOR, 'input#searchInput div[role="button"]')
item_to_buy = (By.CSS_SELECTOR, 'div.wx5xL7Ky div._1KPRonPK')

# Step 3:
select_color = (By.XPATH, "//div[@class='_1thUmrmy']//div[@aria-label='[Negro]']")
add_to_shopping_cart = (By.XPATH, "//div[@class='_100Uy0HO']//span[@class='_3cgghkPI']")
go_to_the_cart = (By.CSS_SELECTOR, "div._2oPZebLl div.vd-NrRvD")

# Extra step if it is your first time:
next_botton = (By.CLASS_NAME, '_2mdvMidB')

# Step 4:
buy_botton = (By.CSS_SELECTOR, "span._3cgghkPI div.f1y5eRaa")
oxxo_botton = (By.CSS_SELECTOR, "div[role='combobox'] span[role='radio']")
complete_purchase = (By.CSS_SELECTOR, "div._1UBLGSqv div._3XAninB_")
