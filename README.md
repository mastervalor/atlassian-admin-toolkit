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

### 2. Install as a package (editable)
You'll need Python 3.7+ and pip. Install in editable mode so local changes are picked up:
```bash
python3 -m pip install -e .
```

### 3. Set up your secrets 🔑
Some scripts require API tokens or config files (like `auth.py` and `config.py`). These are **not** included for security reasons. Check the scripts in `calls/` and `process/` for what you need, and create these files in the root directory.

- `auth.py` – Store your API tokens and email here. **Important:** You must define an `email` variable in this file (e.g., `email = "your-email@example.com"`). All API classes now use HTTPBasicAuth with email and token for cloud API authentication.
- `config.py` – Store your instance URLs and other config.

**Pro tip:** Never commit your secrets! `.gitignore` already helps with that.

#### Cloud API Authentication
All API calls have been updated to support Atlassian Cloud APIs using HTTPBasicAuth. Each API class now:
- Imports `email` from `auth.py`
- Sets up `self.auth = HTTPBasicAuth(email, self.token)` in the `__init__` method
- Uses `auth=self.auth` in all `requests.request()` calls

Make sure your `auth.py` file includes the `email` variable:
```python
email = "your-email@example.com"
# ... your other tokens
```

### 4. Use from your own scripts
After installing, you can import modules directly. Remember your `auth.py` / `config.py` must be on the Python path (placing them next to your script or in the project root both work).
```python
from calls.jira_api_calls import jira_api_projects

projects = jira_api_projects.get_projects(auth, staging_auth)
print(projects)
```

### 5. Run packaged scripts directly
You can still call the bundled automation scripts, e.g.:
```bash
python process/jira_project_process/get_active_projects.py
```
Some scripts are interactive and will prompt for input.

### 6. Run the tests 🧪
All tests use Python's built-in `unittest` framework. To run all tests:
```bash
python -m unittest discover tests
```
Or run a specific test file:
```bash
python tests/jira_logic_tests/ticket_logic_test.py
```

---

## 🔄 Updating on Another Machine

If you already have this repository cloned on another machine and want to pull the latest changes:

### Quick Update Steps

1. **Navigate to the repository directory:**
   ```bash
   cd /path/to/atlassian-admin-toolkit
   ```

2. **Fetch the latest changes from the remote repository:**
   ```bash
   git fetch origin
   ```

3. **Pull the latest changes:**
   ```bash
   git pull origin main
   ```
   (Replace `main` with your branch name if different, e.g., `master`)

4. **Update your `auth.py` file:**
   After pulling, make sure your `auth.py` file includes the `email` variable required for cloud API authentication:
   ```python
   email = "your-email@example.com"
   ```
   If you don't have this variable, add it to your `auth.py` file.

5. **Reinstall the package (if needed):**
   If you made any changes to `setup.py` or dependencies, reinstall:
   ```bash
   python3 -m pip install -e .
   ```

### What Changed?
- All API call files now use HTTPBasicAuth with email and token for cloud API support
- 14 API files were updated across Jira, Confluence, and Atlassian Admin APIs
- The `email` variable is now required in `auth.py`

### Troubleshooting
- If you get import errors about `email`, make sure it's defined in your `auth.py` file
- If API calls fail, verify your `email` and token values are correct in `auth.py`
- If you have merge conflicts, resolve them manually or use `git stash` to save your local changes first

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