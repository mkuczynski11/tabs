import webbrowser

URLS = (
    "http://127.0.0.1:8000/",
    "http://127.0.0.1:8000/admin",
    "http://127.0.0.1:8000/products",
    "http://127.0.0.1:8000/customer",
)

chrome_url = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

b = webbrowser.get(chrome_url)
for u in URLS:
    b.open(u)