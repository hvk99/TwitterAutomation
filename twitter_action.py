def login(driver, username, password):

    try:
        print_log("Finding and clicking sign in button.")
        driver.find_element(by="xpath", value="//a[@href='/login']").click()

        print_log("Sleeping for 2 seconds")
        time.sleep(2)

        print_log("Finding username input box and entering username.")
        driver.find_element(by="xpath", value="//input[@autocomplete='username']").send_keys(username)

        print_log("Finding next button and clicking it.")
        driver.find_element(by="xpath", value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span").click()

        print_log("Sleeping for 2 seconds")
        time.sleep(2)

        print_log("Finding password input box and entering username.")
        driver.find_element(by="xpath", value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(password)

        print_log("Finding and clicking login button now.")
        driver.find_element(by="xpath", value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div").click()

        print_log("Logged In")

    except Exception as e:
        print_log(f'{type(e).__name__}: {e}')
        print(f'{type(e).__name__}: {e}')


def post_content(driver, content):

    try:
        print_log("Finding and clicking Post button.")
        driver.find_element(by="xpath", value="//a[@href='/compose/post']").click()

        print_log("Filling in the content.")
        action_chains = ActionChains(driver)
        action_chains.send_keys(content).perform()
        action_chains.send_keys(Keys.ENTER).perform()

        print_log("Finding and clicking Post button again.")
        driver.find_element(by="xpath", value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/span/span").click()

        print_log("Posted")
        
    except Exception as e:
        print_log(f'{type(e).__name__}: {e}')
        print(f'{type(e).__name__}: {e}')
