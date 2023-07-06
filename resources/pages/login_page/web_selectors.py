elements = {
    "PageTitle": "text=\"Swag Labs\"",
    "UsernamePlaceholder": "[data-test=\"username\"]",
    "PasswordPlaceholder": "[data-test=\"password\"]",
    "LoginButton": "[data-test=\"login-button\"]"
}

class Selectors:
    def __init__(self) -> None:
        self.pagetitle = elements["PageTitle"]
        self.usernameplaceholder = elements["UsernamePlaceholder"]
        self.passwordplaceholder = elements["PasswordPlaceholder"]
        self.loginbutton = elements["LoginButton"]

    def pageTitle(self):
        return self.pagetitle

    def usernamePlaceholder(self):
        return self.usernameplaceholder

    def passwordPlaceholder(self):
        return self.passwordplaceholder

    def loginButton(self):
        return self.loginbutton