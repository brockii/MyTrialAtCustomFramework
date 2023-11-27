import main


browser_instance = None

def launch_browser(browser_name="chrome", location_of_launch="https://google.co.in"):
    global browser_instance

    browser_instance = main.Browser(browser_name, location_of_launch)

def Wait(amount_of_time):
    browser_instance.wait(time_duration=int(amount_of_time))

def click(elem):
    browser_instance.click_on_element(elem)