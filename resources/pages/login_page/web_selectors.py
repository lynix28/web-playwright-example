elements = {
    "PageTitle": "text=\"Swag Labs\"",
    "UsernamePlaceholder": "[data-test=\"username\"]",
    "PasswordPlaceholder": "[data-test=\"password\"]",
    "LoginButton": "[data-test=\"login-button\"]",
    "InvalidCredentialInfo": "text='Epic sadface: Username and password do not match any user in this service'"
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