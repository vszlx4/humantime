# Humantime

Convert human-readable durations to seconds and vice versa in Python.

---

## Features

- Convert strings like `"1h"`, `"20m"`, `"10s"`, `"1h3d5w"` into **total seconds**.  
- Convert seconds back into **human-readable time strings** or dictionaries.  
- Handles **single units**, **concatenated units**, and **space/comma-separated units**.  
- Preserves singular/plural formatting (`"1 Hour"` vs `"2 Hours"`).  
- Fully **pip-installable via GitHub**.  

---

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/your-username/humantime.git
```
---

# Usage

```py
from humantime import to_seconds, from_seconds

# Convert human-readable time to seconds
seconds = to_seconds("1h 30m 10s")
print(seconds)  # Output: 5410.0

# Convert seconds back to human-readable string
readable = from_seconds(5410)
print(readable)  # Output: "1 Hour, 30 Minutes, and 10 Seconds"

# Get dictionary of non-zero units
dict_form = from_seconds(5410, style=False)
print(dict_form)  # Output: {'h': 1, 'm': 30, 's': 10}
```

---

# Supported Units

| Unit          |    Format |
| :------------ | --------: |
| *Nanosecond*  | `ns`, `n` |
| *Microsecond* | `mc`, `r` |
| *Millisecond* | `ms`, `i` |
| *Second*      |       `s` |
| *Minute*      |       `m` |
| *Hour*        |       `h` |
| *Day*         |       `d` |
| *Week*        |       `w` |
| *Month*       | `mo`, `o` |
| *Year*        |       `y` |
| *Decade*      | `de`, `e` |
| *Century*     | `ce`, `c` |

---

# Notes

- Concatenated units are supported `("1h30m")`.
- Multiple units can be separated by spaces or commas `("10m, 3h, 1y")`.
- If `years_max=True` in from_seconds, decades and centuries are ignored.
- `style=False` in from_seconds returns a dictionary instead of a formatted string.

---

# License

This software is distributed under the Ahmed Mughram Proprietary Software License (AMPSL).
You may use it for personal purposes or for educational content with proper credit.
Selling, modifying, or redistributing the software is strictly prohibited.

See the [LICENSE](LICENSE) file for full details.
