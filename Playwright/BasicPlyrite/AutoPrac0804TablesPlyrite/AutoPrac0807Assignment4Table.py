from playwright.sync_api import Page, expect

def test_DD1(page: Page):
    page.goto("https://blazedemo.com/")

    DepCity = page.locator("//select[@name='fromPort']")
    OptionDep = DepCity.select_option(label="Boston")
    print("\n",OptionDep)
    expect(DepCity).to_have_value("Boston")

    DestCity = page.locator("//select[@name='toPort']")
    OptionDest = DestCity.select_option(label="London")
    print("\n",OptionDest)
    expect(DestCity).to_have_value("London")

    FlightFind=page.locator("//input[@value='Find Flights']")
    expect(FlightFind).to_be_visible()
    FlightFind.click()

    table = page.locator("table")
    expect(table).to_be_visible()
    tablerw = table.locator("tbody tr")
    tablerw_count = tablerw.count()
    tableHdr = table.locator("thead th").all_inner_texts()
    print(tableHdr)

    priceCol_index = tableHdr.index("Price")
    print("Price column index:", priceCol_index)

    flightno_index = tableHdr.index("Flight #")
    print("Flight # index:", flightno_index)

    FlightPriceArray = []
    for i in range(tablerw_count):
        cells = tablerw.nth(i).locator("td").all_inner_texts()
        FlightPriceArray.append({
            "FlightNo":cells[flightno_index],
            "FlightPrice":float(cells[priceCol_index].replace("$", ""))
        })

    FlightPriceArray.sort(key=lambda x: x["FlightPrice"])

    for item in FlightPriceArray:
        print(item)

    cells_count = len(cells[flightno_index])
    print("\n","Total Flight count is", cells_count)

    page.wait_for_timeout(5000)
    page.close()



