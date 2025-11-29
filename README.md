# Purchase-Flight Automation Project

This project contains end-to-end automation scripts for **purchasing flights** on Trip.com using **Python** and **Selenium WebDriver** following the **Page Object Model (POM)** design pattern.

---

## Table of Contents
1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)
4. [Running Tests](#running-tests)
5. [Test Scenarios](#test-scenarios)
6. [Reporting](#reporting)
7. [Assumptions](#assumptions)

---

## Project Structure

automation/
├── drivers/ # Browser drivers (ChromeDriver, etc.)
├── pages/ # Page Object Model classes
├── tests/ # Test cases
├── utilities/ # Helper modules (driver_factory, utils)

---

## Prerequisites

1. **Python 3.10+** installed on your machine
2. **Google Chrome** browser (or desired browser)
3. **ChromeDriver** compatible with your Chrome version
4. **Git** installed and configured

---

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/gulfamh2000-source/Purchase-Flight.git
cd Purchase-Flight/automation
Create a virtual environment (recommended):

python -m venv .venv


Activate the virtual environment:

Windows:

.venv\Scripts\activate


Linux / Mac:

source .venv/bin/activate


Install dependencies:

pip install -r requirements.txt

Running Tests

Run a specific test file:

pytest tests/test_purchase.py


Run all tests:

pytest


HTML report (optional):

pytest --html=report.html

Test Scenarios

The main automation function is purchaseEndToEnd() which supports optional parameters:

deptCity (Departure city) – default: random

desCity (Destination city) – default: random

flightSeq (Flight sequence) – default: random

Example Test Cases:

Boston → Berlin, 2nd flight

All parameters random

Boston → Boston, 1st flight

Paris → Berlin, 0th flight

Any random combination

Reporting

Test logs are printed in console

Optional HTML report is generated using pytest-html

Assumptions

Dummy user data is generated for flight purchase

Validations include:

Status must be PendingCapture

Price must be > $100

Inputs are sanitized and exceptions are thrown for invalid inputs

Explicit waits are used for Selenium operations

