from selenium.webdriver.common.by import By


class RegistrationLocators:
    # Поле «Имя»
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

    # Поле «Email»
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    # Поле «Пароль»
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")

    # Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Сообщение об ошибке при некорректном пароле
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")

     # Кнопка «Войти» в форме регистрации
    LOGIN_BUTTON = (By.XPATH, "//a[@href='/login']")


class MainPageLocators:
    # Кнопка «Войти в аккаунт»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка «Личный кабинет»
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")


class ForgotPasswordLocators:
    # Кнопка «Войти» в форме восстановления пароля
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")

class LoginLocators:
    # Поле «Email»
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    # Поле «Пароль»
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

    # Кнопка «Войти»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Кнопка «Восстановить пароль»
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[@href='/forgot-password']")

class PersonalAccountLocators:
    # Кнопка «Выйти» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")   

    # Кнопка «Конструктор»
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[text()='Конструктор']]")

    # Логотип Stellar Burgers
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  

class ConstructorLocators:
    # Раздел «Булки»
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab')][.//span[text()='Булки']]")

    # Раздел «Соусы»
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab')][.//span[text()='Соусы']]")

    # Раздел «Начинки»
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab')][.//span[text()='Начинки']]")  
