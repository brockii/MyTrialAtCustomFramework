*** Settings ***
Library    function.py

*** Test Cases ***
Launch the browser
    launch browser    chrome    https://google.co.in
    click             //*[@id="gb"]/div/div[1]/div/div[1]/a
