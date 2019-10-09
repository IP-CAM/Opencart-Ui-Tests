class Catalog:

    class filter_product:
        accept_filter = {'xpath': "//button[@id='button-filter']"}
        input_product_name = {'css': "#input-name"}


    class productList:
        product_list = {'css': '#form-product'}
        product_table = {'css': product_list['css'] + ' > div > table > tbody'}
        first_line = {'css': product_table['css'] + ' > tr:nth-child(1)'}
        edit_product = {'css': product_table['css'] + " > td:nth-child(8) > aech"}
        product_check_box = {'css': "input[name='selected[]']"}
    #
    #
    # product_check_box = {'xpath': "//input[@name='selected[]']"}
    # products = {'link_text': "Products"}
    # product_nav_tabs = "ul.nav.nav-tabs > li"
    # product_name_field = "product_description[1][name]"
    # product_description = {'xpath': "//div[@contenteditable='true']"}
    # meta_tag_title = "product_description[1][meta_title]"
    # data_tab = "//a[@href='#tab-data']"
    # model_field = "model"

    class navigation:
        main_menu = {'css': "#column-left"}
        catalog_outs = {'id': "menu-catalog"}
        catalog_list = {'css': 'ul#collapse1'}


    class edit_products:
        catalog_list = {'css': 'ul#collapse1'}
        products = {'css': catalog_list['css'] + ' > li:nth-child(2)'}
        page_header = {'css': "div.page-header"}
        product_buttons_menu = {'css': 'div.pull-right '}
        add_new_product = {'css': product_buttons_menu['css'] + " > [data-original-title='Add New']"}
        delete_product = {'css': product_buttons_menu['css'] + " > [data-original-title='Delete']"}
