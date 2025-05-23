# Integral CheatSheet

This project provides a web-based cheat sheet for common integral formulas. All formulas are maintained in LaTeX, automatically converted to JSON, and rendered beautifully on a web page using MathJax.

## Project Structure

```plaintext
Integral CheatSheet/
├── index.html              # Main web page displaying the formulas
├── src/
│   ├── main.tex            # LaTeX source file with all integral formulas
│   ├── get_json.py         # Python script to extract formulas into JSON
│   └── integrals.json      # Generated JSON file with formulas and notes
└── README.md               # Project documentation
```

## Usage

### 1. Edit Integral Formulas

Edit or add formulas in `src/main.tex` using LaTeX, preferably within `enumerate` environments.

### 2. Generate JSON Data

Run the Python script to extract formulas from the LaTeX file and generate the JSON file:

```bash
cd src
python get_json.py
```

This will read `main.tex` and output `integrals.json`.

### 3. View in Browser

Open `index.html` in your browser to view all integral formulas with LaTeX rendering and notes.

> **Note:**  
> Make sure the path to `integrals.json` in `index.html` matches its actual location (default: `src/integrals.json`).

## Technology Stack

- **LaTeX:** For editing and maintaining formulas
- **Python:** For extracting and converting formulas to JSON
- **HTML + JavaScript:** For web display
- **[MathJax](https://www.mathjax.org/):** For rendering LaTeX formulas

## Contribution

Contributions are welcome! Feel free to add or correct formulas, improve scripts, or submit issues and pull requests.

In one word, **PR Welcome!😍**
