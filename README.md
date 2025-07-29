
https://github.com/user-attachments/assets/6f88bff7-1031-4189-8dfc-4e58e6b17648

# GHDBMiner 🕵️‍♂️

**GHDBMiner** is a Google Dorking tool built for cybersecurity researchers and tech enthusiasts to mine the latest Google Dorks from the [Exploit-DB](https://www.exploit-db.com/google-hacking-database). It helps explore the hidden corners of the web with precision and automation.

---

## 🚀 Features

- **🔍 Live Dork Extraction:**  
  Automatically scrapes and displays the latest Google Dorks from the official GHDB site.

- **🔑 Keyword-Based Dork Filtering:**  
  Enter a specific keyword or dork operator (e.g., `inurl:admin`) to filter results in real time.

- **🗂️ Category-Based Dork Selection:**  
  Choose from predefined GHDB categories such as login portals, sensitive files, vulnerable servers, and more.

- **💾 Optional Output Saving:**  
  Save the extracted dorks to a file of your choice for future use or offline analysis.

  
## 💻 Platform Compatibility

- ✅ **Tested and built on:** Windows 11 (Python 3.10+)
- ✅ **Tested with Chrome Version 138.0.7204.169** (Official Build) (64-bit)
- ⚠️ **Not yet tested on:** Linux or macOS  
  > Contributions for compatibility testing are welcome!


 **Clone the Repository:**
   ```bash
   git clone https://github.com/incoggeek/GHDBMiner.git
   cd GHDBMiner
   ```
Or you may download and extract code

<img width="1378" height="118" alt="image" src="https://github.com/user-attachments/assets/33a871d6-374c-4037-bcd8-01171e3f1586" /> <br>

 **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
📌 Ensure chromedriver is installed and accessible via PATH.
[Download](https://googlechromelabs.github.io/chrome-for-testing/)

**Run the Script:**
   ```bash
   python3 ghdbminer.py
   python ghdbminer.py
   ```

## How To Contribute 🤝

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push to the branch
6. Create a new Pull Request

Please ensure that your pull request adheres to the following guidelines:

- Follow the existing coding style.
- Include tests for any new features or bug fixes.
- Document any changes to the README.md

## Self Troubleshooting 😵‍💫
- [Selenium Web Driver](https://www.selenium.dev/documentation/webdriver/troubleshooting/)
- [HTTP Codes Documention](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Disclaimer 🔒
*Use responsibly, respecting privacy, and adhering to ethical guidelines.* 
</br>Happy Dorking! 🌐🔍 #GoogleDorking #CyberSecTool
