from selenium.webdriver.common.by import By


class RegistrationLocators:
    # Поле «Имя»
    NAME_FIELD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')

    # Поле «Email»
    EMAIL_FIELD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')

    # Поле «Пароль»
    PASSWORD_FIELD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')

    # Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')

    # Сообщение об ошибке при некорректном пароле
    PASSWORD_ERROR = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')

     # Кнопка «Войти» в форме регистрации
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')


class MainPageLocators:
    # Кнопка «Войти в аккаунт»
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')

    # Кнопка «Личный кабинет»
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p')


class ForgotPasswordLocators:
    # Кнопка «Войти» в форме восстановления пароля
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')

class LoginLocators:
    # Поле «Email»
    EMAIL_FIELD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')

    # Поле «Пароль»
    PASSWORD_FIELD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')

    # Кнопка «Войти»
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')

    # Кнопка «Восстановить пароль»
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a')

class PersonalAccountLocators:
    # Кнопка «Выйти» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')   

    # Кнопка «Конструктор»
    CONSTRUCTOR_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p')

    # Логотип Stellar Burgers
    LOGO = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a')  

class ConstructorLocators:
    # Раздел «Булки»
    BUNS_TAB = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')

    # Раздел «Соусы»
    SAUCES_TAB = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span')

    # Раздел «Начинки»
    FILLINGS_TAB = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span')  

    # Первый элемент раздела «Булки»
    BUN_ITEM = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[2]/img')

    # Элемент раздела «Соусы»
    SAUCE_ITEM = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[3]/img')

    # Первый элемент раздела «Начинки»
    FILLING_ITEM = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[1]/img')