#!/usr/bin/env python3
"""Validates the color scheme: strict JSON, every color a palette variable or
hex, no scope listed twice, and love used only for errors and deletions."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEME = ROOT / "Yugure.sublime-color-scheme"
failures = []


def check(ok, message):
    if not ok:
        failures.append(message)


scheme = json.loads(SCHEME.read_text(encoding="utf-8"))
variables = scheme["variables"]
check(len(variables) == 17, f"{len(variables)} variables, expected 17")
for name, value in variables.items():
    check(re.fullmatch(r"#[0-9A-F]{6}", value), f"variable {name} is not an uppercase hex color: {value}")

COLOR = re.compile(r"^(var\((\w+)\)|color\(var\((\w+)\) alpha\([0-9.]+\)\)|#[0-9A-Fa-f]{6}([0-9A-Fa-f]{2})?)$")


def check_color(where, value):
    match = COLOR.match(value)
    check(match, f"{where} is not a color: {value}")
    if match:
        variable = match.group(2) or match.group(3)
        if variable:
            check(variable in variables, f"{where} references unknown variable {variable}")


for key, value in scheme["globals"].items():
    if key.endswith("_css") or key.endswith("_options") or key.endswith("_width") or key.endswith("_radius") or key.endswith("_style"):
        continue
    check_color(f"globals.{key}", value)

seen = set()
for rule in scheme["rules"]:
    check("scope" in rule and rule["scope"].strip(), f"rule {rule.get('name')} has no scope")
    for scope in [part.strip() for part in rule["scope"].split(",")]:
        check(scope not in seen, f"scope listed twice: {scope}")
        seen.add(scope)
    for key in ("foreground", "background"):
        if key in rule:
            check_color(f"rule {rule.get('name')}.{key}", rule[key])
    if rule.get("foreground") == "var(love)":
        check(all(re.search(r"invalid|deleted|error|from-file|redish", part) for part in rule["scope"].split(",")),
              f"rule {rule.get('name')} uses love on a non-error scope")
    if "font_style" in rule:
        check(set(rule["font_style"].split()) <= {"bold", "italic", "underline", "glow", "stippled_underline", "squiggly_underline"},
              f"rule {rule.get('name')} has an unknown font_style")

check(len(scheme["rules"]) >= 40, f"only {len(scheme['rules'])} rules")

if failures:
    print("FAIL\n" + "\n".join(failures), file=sys.stderr)
    sys.exit(1)
print(f"ok: {len(scheme['rules'])} rules, {len(scheme['globals'])} globals")
