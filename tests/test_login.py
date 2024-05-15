# def test_positive_login():
#     assert 1 == 1


# def test_negative_login():
#     assert 1 != 1


def test_negative_login():
    """
    Summary: Test negative login attemp

    Steps:
    1. Navigate to login page
    2. Enter wrong creds
    3. Click login/sign in button

    Expected result
    Error saying BLA appeared
    """

    #1. Navigate to login page
    chromeBrowser.open()
    chromeBrowser.github_login_page.navigate_to()

    #2. Enter wrong creds

    user_name_fld = github_login_page.find_username_fld()
    user_name_fld.enter_txt("abcdef")

    password_fld = github_login_page.find_password_fld()
    password_fld.enter_text("abcdef")

    #3. Click login/signin button
    singin_btn = github_login_page.find_signin_btn()
    singin_btn.click()

    # Expected result
    error_message = github_login_page.find_error_message()
    assert error_message.text() == "SOMETHING"
    
    # CleanUp
    chromeBrowser.close()


def test_negative_login_updated(GitHubUI):
    """
    Summary: Test negative login attemp

    Steps:
    1. Navigate to login page
    2. Enter wrong creds
    3. Click login/sign in button

    Expected result
    Error saying BLA appeared
    """

    #1. Navigate to login page
    GitHubUI.open()
    GitHubUI.login_page.navigate_to()

    #2. Enter wrong creds

    GitHubUI.try_login(username='abcdef', password='abcdef')

    # Expected result
    assert GitHubUI.login_page.check_wrong_creds_message()
    
    # CleanUp
    GitHubUI.close()
