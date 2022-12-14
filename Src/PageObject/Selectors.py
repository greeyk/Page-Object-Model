# The intent is to test login functionality on Booking
# The user has already registered
# Step 1 - Open http
# Step 2 - Locate the Login Button and Sign-In using Credentials
class Locator(object):
    # locators for booking homepage
    # book_decline_cookies = '//*[@id="onetrust-accept-btn-handler"]'
    home_login = '//a[@href="https://phptravels.net/login"]'
    home_signup = '//a[@href="https://phptravels.net/signup"]'

    # locators for login page
    login_user_name = '//*[@id="layoutAuthentication_content"]/main/div/div/div/div[1]/div/form/div[1]/label/input'
    login_password = '//*[@id="layoutAuthentication_content"]/main/div/div/div/div[1]/div/form/div[2]/label/input'
    login_button = '//*[@id="layoutAuthentication_content"]/main/div/div/div/div[1]/div/form/div[4]/button'

    login_captcha = '//*[@id="recaptcha-anchor"]/div[1]'
    login_captcha_iframe = '//*[@id="#divDynamicRecaptcha1"]/div/div/iframe'

    # manage hotels
    add_hotel = 'add_button'
    hotel_name = '//*[@id="general"]/div[2]/div/input'
    hotel_address = '//*[@id="mapaddress"]'
    hotel_status = '//*[@id="layoutDrawer_content"]/main/div/form/div[2]/div/div/strong/div/div[1]/div/select/option[1]'
    hotel_type = '//*[@id="layoutDrawer_content"]/main/div/form/div[2]/div/div/strong/div/div[3]/div/select/option[2]'
    hotel_location = '//*[@id="s2id_searching"]'
    add_button = '//*[@id="add"]/i'
    description_iframe = '//*[@id="cke_1_contents"]/iframe'


