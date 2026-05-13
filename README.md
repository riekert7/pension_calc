# Pension Calculator

A simple retirement projection tool built with Flask, Bootstrap 5 and chart.js integration.

A stateless Flask web app that takes five retirement inputs (plus currency for visuals) and outputs four summary stats, a dual-line Chart.js projection chart, and a year-by-year breakdown table showing projected balance, total contributed, and investment growth.

## Run locally

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit http://127.0.0.1:5000

## Assumptions

- Contributions are added at the start of each year after year zero
- Growth is already applied to year 0
- Growth is compounded annually after contributions are added
- No tax relief, employer matching, or inflation adjustment
- Currency is display-only — all maths is currency-agnostic
- Growth rate capped at 30% with a validation warning
- A growth rate of 0% is valid and produces a flat contribution line
- A starting pension balance of 0 is valid for those who have no pension as of yet
- Unit tests and integration tests are not neccessary for POC
- Showing the growth of investment over time is the key to winning the POC


## AI Usage

Used Claude to plan the approach, architecture and write a spec. Used Claude Code to scaffold the Flask route structure, Bootstrap form layout, and Chart.js integration. Reviewed all generated code line by line, formatted and refactored code along the way.

**Rejected:** 
- Database models/usage ruling out Django, and FastAPI — overkill for a stateless PoC. 
- Inline JavaScript and CSS (Extracted to seperate files for better readibility).
- Unused imports or unnecessary imports.

**Accepted:** 
- Chart.js for the projection chart. I wanted one visually compelling feature that adds real value without inflating complexity or time. The dual-line chart — projected balance vs total contributed — makes the power of compounding immediately visible.
- Jinja base, index and results html structure (reusability).
- Splitting up app.py and calculator.py (Make code modularity).


## Time spent

Roughly just under 3 hours:
- 30 minutes for planning
- 15 minutes for boilerplate code generation and testing
- 2 and 1/2 hours for in depth code reviewing, formatting, refactoring and README.


## What I would do with more time

- Pass back state through recalculate button (avoiding entering form info again if form is not refreshed)
- Maybe make results shareable (add GET route that takes inputs as query params)
- Add employer contribution field and take into account
- Let the customer change contribution rate over time
- Setup SMTP with button (Get my results)
- Add the ability to compare 2 different scenarios