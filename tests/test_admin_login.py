from page_object import AdminLogin

def test_login(browser, url):
    open_login_page = AdminLogin(browser)
    open_login_page.open(url)
    open_login_page.input_username("admin")
    open_login_page.input_password("25191")
    open_login_page.submit_login()
