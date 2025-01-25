# Playwright

* 用 Playwright 做簡單的自動化。
* Python 版的入門文件 https://playwright.dev/python/docs/intro
  * 如果不是用 Python，上方選單可以選想用的語言。
* 給自己的錄影記錄 https://youtu.be/D2taW0Qmw5M?si=5SRy3ZcqmuObFygM

## 安裝

裝 library

```
pip install pytest-playwright
```

裝 Browser

```
playwright install
```

預設是全都下載回來

```
$ playwright install
Downloading Chromium 131.0.6778.33 (playwright build v1148) from https://playwright.azureedge.net/builds/chromium/1148/chromium-mac-arm64.zip
121.6 MiB [====================] 100% 0.0s
Chromium 131.0.6778.33 (playwright build v1148) downloaded to /Users/qrtt1/Library/Caches/ms-playwright/chromium-1148
Downloading Chromium Headless Shell 131.0.6778.33 (playwright build v1148) from https://playwright.azureedge.net/builds/chromium/1148/chromium-headless-shell-mac-arm64.zip
77.5 MiB [====================] 100% 0.0s
Chromium Headless Shell 131.0.6778.33 (playwright build v1148) downloaded to /Users/qrtt1/Library/Caches/ms-playwright/chromium_headless_shell-1148
Downloading Firefox 132.0 (playwright build v1466) from https://playwright.azureedge.net/builds/firefox/1466/firefox-mac-arm64.zip
81.6 MiB [====================] 100% 0.0s
Firefox 132.0 (playwright build v1466) downloaded to /Users/qrtt1/Library/Caches/ms-playwright/firefox-1466
Downloading Webkit 18.2 (playwright build v2104) from https://playwright.azureedge.net/builds/webkit/2104/webkit-mac-13-arm64.zip
69.5 MiB [====================] 100% 0.0s
Webkit 18.2 (playwright build v2104) downloaded to /Users/qrtt1/Library/Caches/ms-playwright/webkit-2104
```

## 官網上的第 1 個範例

test_example.py

```
import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
```

```
$ python -m pytest
============================= test session starts ==============================
platform darwin -- Python 3.10.6, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/qrtt1/temp/cookbook/recipes/playwright
plugins: playwright-0.6.2, base-url-2.1.0
collected 2 items

test_example.py ..                                                       [100%]

============================== 2 passed in 3.78s ===============================
```