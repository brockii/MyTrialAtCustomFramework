*** Settings ***
Library    function.py

*** Test Cases ***
Launch the browser
    launch browser    edge    https://google.co.in
    Wait              5
    click             //*[@id="gb"]/div/div[1]/div/div[1]/a
