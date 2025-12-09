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
Template files `auth.py` and `config.py` are included in the repository with empty values. You need to fill in your actual credentials and URLs.

**Important:** 
- Open `auth.py` and fill in all the required variables (especially `email` and your API tokens)
- Open `config.py` and fill in all your instance URLs
- The `email` variable is **required** - all API classes use HTTPBasicAuth with email and token for cloud API authentication

**Security Note:** 
- The template files are in the repo with empty strings
- **Never commit your actual secrets!** If you accidentally fill in real values, they won't be committed if you're careful, but it's better to use environment variables or a `.env` file for production use
- Consider using a `.env` file or environment variables for sensitive values in production environments

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

4. **Update your `auth.py` and `config.py` files:**
   The template files are now included in the repo. After pulling:
   - If you already had these files, you may need to merge your values with the new template structure
   - Make sure your `auth.py` file includes the `email` variable (it's in the template)
   - Fill in any new variables that were added to the templates
   - If you get merge conflicts, keep your actual values (not the empty template values)

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