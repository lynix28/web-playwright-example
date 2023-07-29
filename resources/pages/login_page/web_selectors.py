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

    def pageTitle(self):
        return self.pagetitle

    def usernamePlaceholder(self):
        return self.usernameplaceholder

    def passwordPlaceholder(self):
        return self.passwordplaceholder

    def loginButton(self):
        return self.loginbutton
    
    def invalidCredentialInfo(self):
        return self.invalidcredentialinfo