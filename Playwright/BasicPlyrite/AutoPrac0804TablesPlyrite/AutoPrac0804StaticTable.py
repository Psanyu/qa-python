import pytest
import time

from playwright.sync_api import Page,expect

def test_St1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    Tbl = page.locator("//table[@name='BookTable']/tbody")
    expect(Tbl).to_be_visible()

# Locator chaining using Table locator
    rws=Tbl.locator("tr")
    rwsN=rws.count()
    print("\n", rwsN)
    expect(rws).to_have_count(rwsN)

# rw0
    trw0=rws.nth(0).locator("th")
    print(trw0.all_inner_texts())

# Locator chaining using rows locator
    cols = rws.locator("th")
    colsN = cols.count()
    print(colsN)
    expect(cols).to_have_count(colsN)

# all other rows
    for iTr in range(rwsN):
       trwn = rws.nth(iTr).locator("td")
       print(trwn.all_inner_texts())

# all other rows using all() option
    Allcells = rws.all()
    for Tcs in Allcells[1:]:
       cells = Tcs.locator("td")
       print("Reprint with all() option:", cells.all_inner_texts())

# all rows for Col Author
    for TcNs in Allcells[1:]:
        authornm = TcNs.locator("td").nth(1).inner_text()
        if (authornm == 'Mukesh'):
            booknm = TcNs.locator("td").nth(0).inner_text()
            print(authornm, "wrote the book", booknm)

# sum of prices
    totalprc=0
    for TcPs in Allcells[1:]:
        prc = TcPs.locator("td").nth(3).inner_text()
        totalprc = totalprc + int(prc)

    print("\n",totalprc)


    page.wait_for_timeout(5000)

    page.close()


