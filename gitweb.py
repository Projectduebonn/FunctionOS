import webbrowser
import os

count_file = "count.txt"
github_url = "https://github.com/Projectduebonn"

def open_github():
    webbrowser.open(github_url)

def get_count():
    if os.path.exists(count_file):
        with open(count_file, "r") as f:
            return int(f.read())
    else:
        return 0

def save_count(count):
    with open(count_file, "w") as f:
        f.write(str(count))

count = get_count()
if count >= 50:
    os.remove(count_file)
    os.system("""osascript -e 'tell app "System Events" to display dialog "已经打开50次" buttons "OK"'""")
else:
    open_github()
    os.system("""osascript -e 'tell app "System Events" to display dialog "text" buttons "OK"'""")
    save_count(count + 1)
