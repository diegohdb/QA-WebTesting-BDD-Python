from selenium import webdriver
import os
import shutil
import time
import logging


def before_all(context):
    pass


def before_feature(context, feature):
    context.logger = logging.getLogger('seleniumframework_tests')
    hdlr = logging.FileHandler('./seleniumframework_tests.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    context.logger.addHandler(hdlr)
    context.logger.setLevel(logging.DEBUG)


def before_scenario(context, scenario):
    # behave -D BROWSER=chrome
    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is None:
            BROWSER = 'chrome'
        else:
            BROWSER = context.config.userdata['BROWSER']
    else:
        BROWSER = 'chrome'
    # For some reason, python doesn't have switch case -
    # http://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
    if BROWSER == 'chrome':
        context.browser = webdriver.Chrome()
    elif BROWSER == 'firefox':
        context.browser = webdriver.Firefox()
    elif BROWSER == 'safari':
        context.browser = webdriver.Safari()
    elif BROWSER == 'ie':
        context.browser = webdriver.Ie()
    elif BROWSER == 'opera':
        context.browser = webdriver.Opera()
    elif BROWSER == 'phantomjs':
        context.browser = webdriver.PhantomJS()
    else:
        print("Browser you entered:", BROWSER, "is invalid value")

    context.browser.maximize_window()


def after_scenario(context, scenario):
    print(f'scenario status {scenario.status}')
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")
    context.browser.quit()


def after_feature(context, feature):
    print("\nAfter Feature")


def after_all(context):
    # behave -D ARCHIVE=Yes
    if 'ARCHIVE' in context.config.userdata.keys():
        if os.path.exists("failed_scenarios_screenshots"):
            os.rmdir("failed_scenarios_screenshots")
            os.makedirs("failed_scenarios_screenshots")
        if context.config.userdata['ARCHIVE'] == "Yes":
            shutil.make_archive(
                time.strftime("%d_%m_%Y"),
                'zip',
                "failed_scenarios_screenshots")
            # os.rmdir("failed_scenarios_screenshots")
            print("Executing after all")
