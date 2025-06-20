# 🛠️ Atlassian Admin Toolkit

Welcome to the **Atlassian Admin Toolkit** – your all-in-one Swiss Army knife for wrangling Jira, Confluence, Okta, Looker, and Slack like a true admin wizard! 🧙‍♂️✨

## What is this?
This repo is a collection of scripts and logic to automate, analyze, and manage your Atlassian (and friends!) environments. Whether you want to:
- Audit users 👀
- Manage groups and permissions 🧑‍🤝‍🧑
- Automate ticketing and reporting 🎟️
- Sync with Okta, Looker, or Slack 🔄
- Or just make your admin life easier...

**...you're in the right place!**

---

## 🏗️ Project Structure

- `calls/` – API wrappers for Jira, Confluence, Okta, Looker, Slack, and more.
- `logic/` – Business logic for handling users, groups, tickets, dashboards, etc.
- `process/` – Automation scripts and workflows (the magic happens here!)
- `file_manip/` – Utilities for working with CSV and JSON files.
- `dataformating/` – Helpers for formatting dates, JSON, and responses.
- `tests/` – Unit tests for the toolkit (because we like things that work!)

---

## 🚀 Getting Started

### 1. Clone this repo
```bash
git clone https://github.com/YOUR_USERNAME/atlassian-admin-toolkit.git
cd atlassian-admin-toolkit
```

### 2. Install dependencies
You'll need Python 3.7+ and pip. Then:
```bash
pip install -r requirements.txt
```

### 3. Set up your secrets 🔑
Some scripts require API tokens or config files (like `auth.py` and `config.py`). These are **not** included for security reasons. Check the scripts in `calls/` and `process/` for what you need, and create these files in the root directory.

- `auth.py` – Store your API tokens here (see code for variable names).
- `config.py` – Store your instance URLs and other config.

**Pro tip:** Never commit your secrets! `.gitignore` already helps with that.

### 4. Run a script!
Most scripts are in the `process/` folder. For example:
```bash
python process/jira_project_process/get_active_projects.py
```
Or run any other script you fancy! Some scripts are interactive and will ask you for input.

### 5. Run the tests 🧪
All tests use Python's built-in `unittest` framework. To run all tests:
```bash
python -m unittest discover tests
```
Or run a specific test file:
```bash
python tests/jira_logic_tests/ticket_logic_test.py
```

---

## 🦸‍♂️ Tips & Tricks
- Many scripts expect CSV or JSON files on your Desktop. Check the code comments for file naming!
- Some scripts use Selenium for browser automation. Make sure you have Chrome and the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) installed if you use those scripts.
- If you get stuck, read the code! It's (mostly) friendly and commented.

---

## 🧩 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss what you want to change.

---

## 📜 License
[MIT](LICENSE)

---

Happy automating! 🚀 