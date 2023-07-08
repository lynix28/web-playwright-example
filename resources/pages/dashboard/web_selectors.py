elements = {
    "header": {
        "Title": "text='Swag Labs'",
        "SideMenuButton": "xpath=//*[@id='react-burger-menu-btn']",
        "ShoppingCartButton": "#shopping_cart_container a",
        "SortButton": "[data-test='product_sort_container']",
        "ContentTitle": "text='Products'"
    },
    "body": {
        "ContentContainer": "#inventory_container"
    }
}

class Selectors:
    def __init__(self) -> None:
        self.headertitle = elements["header"]["Title"] 
        self.headersidemenubutton = elements["header"]["SideMenuButton"]
        self.headershoppingcartbutton = elements["header"]["ShoppingCartButton"]
        self.headersortbutton = elements["header"]["SortButton"]
        self.contenttitle = elements["header"]["ContentTitle"]
        self.bodycontentcontainer = elements["body"]["ContentContainer"]

    def headerTitle(self):
        return self.headertitle

    def headerSideMenuButton(self):
        return self.headersidemenubutton

    def headerShoppingCartButton(self):
        return self.headershoppingcartbutton

    def headerSortButton(self):
        return self.headersortbutton

    def headerContentTitle(self):
        return self.contenttitle

    def bodyContentContainer(self, index=1):
        locator = self.bodycontentcontainer
        return f"{locator}:nth-child({index})"