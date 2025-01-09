🤺 MASHER

This Automation framework is designed to automate UI testcases of HMI functionality for polaris welding machine.

🖊️ Authors

	• Sneha Chavan



💻 Create a Virtual Environment

  ```bash
  # Install the virtualenv module
  pip install virtualenv

  # Create the virtual Environment named venv
  python -m venv venv
  or
  virtualenv venv

  # Activate the Virtual Environment
  venv\Scripts\activate
  ```


🚀 Install the Application
  ```bash
  # Install the MASHER
  pip install -e.
  ```

😎 Install the Extras

  ```bash
  pip install -e ".[dev,test]"
  ```
✔ Running Tests
To run the tests, refer the following

❄ Flake8

```bash
flake8 src test
```

🧪 Pytest
```bash
pytest -v
```

💘 mypy
```bash
mypy src test
```

🧹 pylint
```bash
pylint src test
```

🦅 vulture
```bash
vulture src test
```


## Features

- Automate manual testcases for HMI based testing.