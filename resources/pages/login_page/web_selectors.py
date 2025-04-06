elements = {
    "PageTitle": "text=\"Swag Labs\"",
    "UsernamePlaceholder": "[data-test=\"username\"]",
    "PasswordPlaceholder": "[data-test=\"password\"]",
    "LoginButton": "[data-test=\"login-button\"]",
    "InvalidCredentialInfo": "//*[@id=\"login_button_container\"]/div/form/div[3]/h3",
}

class Selectors:
    def __init__(self) -> None:
        self.pagetitle = elements["PageTitle"]
        self.usernameplaceholder = elements["UsernamePlaceholder"]
        self.passwordplaceholder = elements["PasswordPlaceholder"]
        self.loginbutton = elements["LoginButton"]
        self.invalidcredentialinfo = elements["InvalidCredentialInfo"]

    def page_title(self):
        return self.pagetitle

    def username_placeholder(self):
        return self.usernameplaceholder

    def password_placeholder(self):
        return self.passwordplaceholder

    def login_button(self):
        return self.loginbutton
    
    def invalid_credential_info(self):
        return self.invalidcredentialinfo