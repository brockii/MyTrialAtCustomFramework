import main


def launch_browser(browser_name="chrome", location_of_launch="https://google.co.in"):
    main.Browser(browser_name, location_of_launch)

def Wait(amount_of_time):
    main.Browser.wait(time_duration=amount_of_time)

def click(elem):
    browser_instance = main.Browser()
    browser_instance.click_on_element(element=elem)