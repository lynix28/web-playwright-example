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

    def header_title(self):
        return self.headertitle

    def header_side_menu_button(self):
        return self.headersidemenubutton

    def header_shopping_cart_button(self):
        return self.headershoppingcartbutton

    def header_sort_button(self):
        return self.headersortbutton

    def header_content_title(self):
        return self.contenttitle

    def body_content_container(self, index=1):
        locator = self.bodycontentcontainer
        return f"{locator}:nth-child({index})"