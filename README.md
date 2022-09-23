# Pytest
Here I am planning to upload all my pytest tests for a lot of different websites.
Each website is made for sole purpose of being tested automatically. 

### Install

1. `pip3 install -r requirements.txt`

### Run tests(CMD and terminal)

pytest (for all tests)\
pytest test_******(specific test name in case you want to specific thing)

### Description

test_ACME.py is a testing website http://a.testaddressbook.com/, which is basically an address book website, which requires using a lot of different approaches to fill
long form, including color picking, date picking and uploading some file. 

test_swag_labs.py is testing website https://www.saucedemo.com, which is an online shop with different logins, one of them is supposed not to work, another one is a 
standard user that I tested too. Problem_user isn't working properly (surprisingly), but I'm planning to test it as a negative test in the future. Performance-glitch user
just looks bad, but it works exactly the same as standard_user so I didn't make it as it makes no difference.

test_ultimate_qa.py is testing website https://ultimateqa.com/simple-html-elements-for-automation which is more about different approaches for finding elements. On top
of that it verifies if tester can handle radio buttons, checkboxes, menu dropdowns and tabs. The last test is login site, but sometimes it forces a captcha.

test_demoqa.py is the most complex testing site. The site https://demoqa.com is basically a place where I found every UI test I ever could. It's very complex site that 
checked a lot of little and longer test cases. Sometimes tester have to click some button somewhere or radio button and then you can find form that has a lot of different
types. It makes you to use elements, forms, alerts, frames, windows and a lot of different types of widgets. On top of that there is a section about interactions with
elements. 
