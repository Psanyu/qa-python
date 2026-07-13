import pytest
import time

from playwright.sync_api import Page,expect

def test_ASDT1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")


    dyTab = page.locator("#taskTable")

    rows = dyTab.locator("tbody tr")
    rw_count = rows.count()
    colh = dyTab.locator("thead th").all_inner_texts()
    cpu_index = colh.index("CPU (%)")
    mem_index = colh.index("Memory (MB)")
    netspeed_index = colh.index("Network (Mbps)")
    diskspc_index = colh.index("Disk (MB/s)")


    for i in range(rw_count):
        cells= rows.nth(i).locator("td").all_inner_texts()
        rowh = cells[0]
        if rowh == "Chrome":
           Chrome_CPU_Load = cells[cpu_index]
           displayval = page.locator(".chrome-cpu", has_text="%")
           t1 = displayval.inner_text()
           if t1 == Chrome_CPU_Load:
              assert t1 == Chrome_CPU_Load, (f"CPU mismatch: label={t1}, table={Chrome_CPU_Load}")
              print("\n", "Display value of CPU load:", t1, "matches Table Value of Chrome CPU load", Chrome_CPU_Load)

        if rowh == "Firefox":
            Firefox_mem_Load = cells[mem_index]
            displayval = page.locator(".firefox-memory", has_text="MB")
            t2 = displayval.inner_text()
            if t2 == Firefox_mem_Load:
                assert t2 == Firefox_mem_Load, (f"Memory mismatch: label={t2}, table={Firefox_mem_Load}")
                print("\n","Display value of Memory Size of Firefox:", t2, "matches Table Value of Firefox memory size", Firefox_mem_Load)

        if rowh == "Chrome":
            Chrome_Network_Speed= cells[netspeed_index]
            displayval = page.locator(".chrome-network", has_text="Mbps")
            t3 = displayval.inner_text()
            if t3 == Chrome_Network_Speed:
                assert t3 == Chrome_Network_Speed, (f"Network mismatch: label={t3}, table={Chrome_Network_Speed}")
                print("\n","Display value of Chrome Network speed:", t3,"matches Table Value of Chrome network speed", Chrome_Network_Speed)

        if rowh == "Firefox":
            Firefox_Disk_Space= cells[diskspc_index]
            displayval = page.locator(".firefox-disk", has_text="MB/s")
            t4 = displayval.inner_text()
            if t4 == Firefox_Disk_Space:
               print("\n","Display value of Firefox Disk space:", t4,"matches Table Value of Firefox disk space", Firefox_Disk_Space)

    page.wait_for_timeout(5000)
    page.close()
