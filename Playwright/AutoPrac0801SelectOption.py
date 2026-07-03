import pytest
import time

from playwright.sync_api import Page,expect

def test_S1Verifi(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # select single option ---1
    print("SingleOptions1:")
    page.locator("#country").select_option(value="United States")

    #select single option ---2
    dropdown_options= page.locator("#country>option")
    expect(dropdown_options).to_have_count(10)
    options_text=[text.strip() for text in dropdown_options.all_text_contents()]
    print("SingleOptions2:")
    for option in options_text:
        print(option)

    # select single multi-option ---1
    colours_options= page.locator("#colors").select_option(label=["Red","Blue","Yellow","Green"])
    print("Multioptions1:")
    for colour in colours_options:
        print(colour)

    # select single multi-option ---2
    colours_options2 = page.locator("#colors").select_option(value=["Red", "Blue", "Yellow", "Green"])
    print("Multioptions2:")
    for colours2 in colours_options2:
        print(colours2)

    # select single multi-option ---3
    colours_options3 = page.locator("#colors").select_option(index=[1,3,5])
    print("Multioptions3:")
    for colours3 in colours_options3:
        print(colours3)

  # select multi option ---4
    dropdown_option1 = page.locator("#colors>option")
    expect(dropdown_option1).to_have_count(7)
    option_text1 = [text.strip() for text in dropdown_option1.all_text_contents()]
    print("Multioptions4:")
    for option1 in option_text1:
        print(option1)

  # select multi option ---5
    dropdown_optionSL = page.locator("#colors>option")
    expect(dropdown_optionSL).to_have_count(7)
    option_textSL = [text.strip() for text in dropdown_optionSL.all_text_contents()]
    sortedList = sorted(option_textSL)
    revList = list (reversed(option_textSL))
    print("Sorted List:", sortedList)
    print("Unsorted List:", option_textSL)
    print(f"Reversed List:{revList}")
    if (sortedList == option_textSL):
        print("Dropdown was originally in a sorted list")
    else:
        print("Dropdown was not originally in a sorted list")

    page.wait_for_timeout(5000)

    page.close()


