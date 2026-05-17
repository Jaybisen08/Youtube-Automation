# 🤖 YouTube Shorts Automation Bot

<div align="center">

✨ *Automating YouTube Shorts browsing using Selenium & Python* ✨

</div>

---

# 📌 Description

The **YouTube Shorts Automation Bot** is a Python automation project built using **Selenium WebDriver**.  

This bot automatically:

✅ Opens YouTube  
✅ Searches for a keyword  
✅ Opens the first Shorts video  
✅ Automatically scrolls through Shorts continuously  

The project demonstrates browser automation and web interaction using Selenium.

---

# 🚀 Features

✨ Automated YouTube search  
🎥 Automatically opens Shorts  
⏭️ Auto-scroll to next Shorts video  
⌨️ Simulated keyboard typing effect  
🌐 Browser automation using Selenium  
💻 Beginner-friendly automation project  

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Programming Language |
| 🌐 Selenium | Browser Automation |
| 🚗 ChromeDriver | Web Driver |
| ▶️ YouTube | Automation Platform |

---

# 📂 Project Structure

```bash
📦 YouTube-Shorts-Bot
 ┣ 📜 shorts_bot.py
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Create a `requirements.txt` file and add:

```txt
selenium
```

---

# 🌐 Install ChromeDriver

Download ChromeDriver compatible with your Chrome browser version:

🔗 https://chromedriver.chromium.org/downloads

After downloading:

✅ Extract the file  
✅ Add ChromeDriver to system PATH  

---

# ▶️ Run the Project

```bash
python shorts_bot.py
```

---

# 💻 Source Code

```python
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

sleep(3)

browser.get("https://youtube.com")

sleep(3)

search_box = browser.find_element("name", "search_query")

for char in "indian veg food":
    search_box.send_keys(char)
    sleep(0.2)

sleep(6)

search_box.send_keys(Keys.ENTER)

sleep(3)

first_short = browser.find_element(
    "xpath",
    '//*[@id="contents"]/grid-shelf-view-model[1]/div[1]/div[1]'
)

first_short.click()

while True:

    sleep(10)

    next_button = browser.find_element(
        "xpath",
        '//*[@id="navigation-button-down"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div[2]'
    )

    next_button.click()
```

---

# ⚡ How It Works

1️⃣ Launches Chrome browser  
2️⃣ Opens YouTube  
3️⃣ Searches for "indian veg food"  
4️⃣ Opens the first Shorts video  
5️⃣ Automatically navigates to next Shorts every 10 seconds  

---

# 🌟 Future Improvements

🔹 Voice command support  
🔹 Random video selection  
🔹 Auto like & subscribe  
🔹 AI-based recommendation system  
🔹 GUI interface  
🔹 Multi-platform automation  

---

# ⚠️ Important Note

YouTube may update its webpage structure anytime, which can break XPath selectors.  
If the bot stops working, update the XPath values accordingly.

---

# 👨‍💻 Author

## Jay Bisen

💡 Passionate about Automation, AI & Web Development

---

# 📄 License

📝 This project is open-source and available under the **MIT License**.

---

<div align="center">

⭐ If you like this project, don't forget to star the repository ⭐

</div>
