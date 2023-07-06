elements = {
    "PageTitle": "getByText('Swag Labs')",
    "UsernamePlaceholder": "[data-test=\"username\"]",
    "PasswordPlaceholder": "[data-test=\"password\"]",
    "LoginButton": "[data-test=\"login-button\"]"
}

class Selectors:
    def __init__(self) -> None:
        self._pageTitle = elements["PageTitle"]
        self._usernamePlaceholder = elements["UsernamePlaceholder"]
        self._passwordPlaceholder = elements["PasswordPlaceholder"]
        self._loginButton = elements["LoginButton"]

    @property
    def pageTitle(self):
        return self._pageTitle

    @property
    def usernamePlaceholder(self):
        return self._usernamePlaceholder

    @property
    def passwordPlaceholder(self):
        return self._passwordPlaceholder

    @property
    def loginButton(self):
        return self._loginButton
