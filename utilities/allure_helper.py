import allure

def attach_step_screenshot(page, step_name):
    allure.attach(
        page.screenshot(),
        name=step_name,
        attachment_type=allure.attachment_type.PNG
    )
