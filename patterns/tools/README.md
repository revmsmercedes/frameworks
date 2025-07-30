
# Tools

Reusable scripts and calculators to support Spirit-Wired™ frameworks.

## Current tools

- `roi-calculator.py` — Annual ROI value calculator

---

## ROI Calculator Usage Instructions

This Python script calculates the estimated annual ROI value based on time saved per week and error rate reduction.

### How to run the script

1. **Make sure you have Python installed** on your computer.  
   You can download it from [python.org](https://www.python.org/downloads/)

2. **Download or clone this repo** to your local machine.

3. Open your terminal or command prompt, navigate to the `patterns/tools` directory.

4. Run the script by typing:

```bash
python roi-calculator.py
```

5. When prompted, enter the following values:

- Weekly hours saved (e.g., `10`)  
- Error rate reduction as a decimal (e.g., `0.05` for 5%)  
- Annual transaction volume (e.g., `10000`)

6. The script will calculate and display the estimated annual ROI value.

---

### Formula used

```text
Annual Value = (Weekly Hours Saved × 50 × $75) + (Error Rate Reduction × Transaction Volume)
```

- `50` represents work weeks per year  
- `$75` is the assumed hourly value

---

Feel free to adjust hourly rate or work weeks in the script to fit your needs.
