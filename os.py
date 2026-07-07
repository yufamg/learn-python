# import time
# from pathlib import Path
import glob
import os
import shutil
from string import Template

s = Template("Hello, $name! ${greeting}")
print(s.substitute(name="World", greeting="Good morning"))
# p = Path("write.txt")
# if not p.exists():
#     p.write_text("Hello, World!", "utf-8")
#     print(p.read_text("utf-8"))
#     time.sleep(5)
#     p.unlink(missing_ok=True)
# # 当前目录下一层
# for child in Path("/usr").iterdir():
#     print(child)
# Path("./mk").mkdir(parents=True, exist_ok=True)
# time.sleep(2)
# Path("./mk").rmdir()
from urllib.request import urlopen

print(os.getcwd())
shutil.copyfile("./mock.json", "./copy.json")
print(glob.glob("*.json"))


with urlopen("https://oa.caocaokeji.cn/") as response:
    for line in response:
        line = line.decode()  # Convert bytes to a str
        # if "updated" in line:
        #     print(line.rstrip())  # Remove trailing newline
        # print(line.strip())

# import smtplib

# server = smtplib.SMTP("localhost")
# server.sendmail(
#     "soothsayer@example.org",
#     "jcaesar@example.org",
#     """To: jcaesar@example.org
# From: soothsayer@example.org

# Beware the Ides of March.
# """,
# )
# server.quit()
