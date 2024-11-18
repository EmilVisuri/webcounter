*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}    localhost:5001
${DELAY}     0.5 seconds
${HOME_URL}  http://${SERVER}
${BROWSER}   chrome
${HEADLESS}  true

*** Test Cases ***
Set Counter Value
    Open Browser  ${HOME_URL}  ${BROWSER}  headless=${HEADLESS}
    Input Text  value  10
    Click Button  Set Counter
    Page Should Contain  10
    Close Browser