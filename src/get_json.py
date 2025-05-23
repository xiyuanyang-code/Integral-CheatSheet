import re
import json


def extract_formulas(tex_path):
    with open(tex_path, encoding="utf-8") as f:
        content = f.read()

    # match the expressions in the enumerate
    pattern = re.compile(r"\\begin{enumerate}(.*?)\\end{enumerate}", re.S)
    matches = pattern.findall(content)

    formulas = []
    for section in matches:
        # match every item
        items = re.findall(r"\\item\s*(.*?)\n", section)
        for item in items:
            if "." in item:
                formula, *rest = item.split(".")
                formula = formula.strip()
                note = ".".join(rest).strip()
            else:
                formula = item.strip()
                note = ""
            # remove all $ symbols from formula
            formula = formula.replace("$", "")
            formulas.append({"formula": formula, "note": note})
    return formulas


if __name__ == "__main__":
    formulas = extract_formulas("main.tex")
    with open("integrals.json", "w", encoding="utf-8") as f:
        json.dump(formulas, f, ensure_ascii=False, indent=2)
