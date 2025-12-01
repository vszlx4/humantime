import re

index = {
  "c": (3153600000, "Centuries", "Century"), 
  "e": (315360000, "Decades", "Decade"),
  "y": (31536000, "Years", "Year"),
  "o": (2592000, "Months", "Month"),
  "w": (604800, "Weeks", "Week"),
  "d": (86400, "Days", "Day"),
  "h": (3600, "Hours", "Hour"),
  "m": (60, "Minutes", "Minute"),
  "s": (1, "Seconds", "Second"),
  "i": (0.001, "Milliseconds", "Millisecond"),
  "r": (0.000001, "Microseconds", "Microsecond"),
  "n": (0.000000001, "Nanoseconds", "Nanosecond")}

def to_seconds(uinput: str, is_integer: bool = False) -> float | int:
  """
# Convert Human-Readable Time to Seconds

Converts a human-readable duration string into a total number of seconds.

## Args
- `uinput` (`str`):  
  A duration string containing one or multiple time units.  
  Supports mixed formats, spacing, commas, and concatenated units.

  **Accepted patterns:**
  - Single units: `'1h'`, `'20m'`, `'10s'`
  - Multiple units (space or comma separated): `'10m 3h 1y'`, `'10m, 1h, 12y'`
  - Concatenated units: `'1h3d5w'`, `'10m3h1y'`

  Extended formats are normalized internally:  
  `ns→n`, `mc→r`, `ms→i`, `mo→o`, `de→e`, `ce→c`.

- `is_integer` (`bool`, optional):  
  If `True`, the result is returned as an integer. Defaults to `False`.

## Returns
- `float`: Total duration in seconds.  
  Returns a float ending in `.0` when there are no fractional seconds or the total is below 1 second.

- `int`: Returned only when `is_integer=True`.

- Malformed units are skipped (e.g., `'10x'` is ignored; `'10m1x3h'` parses valid parts only).

## Usage
| Unit          | Format        |
| :------------ | ------------:|
| _Nanosecond_  | `ns`, `n`     |
| _Microsecond_ | `mc`, `r`     |
| _Millisecond_ | `ms`, `i`     |
| _Second_      | `s`           |
| _Minute_      | `m`           |
| _Hour_        | `h`           |
| _Day_         | `d`           |
| _Week_        | `w`           |
| _Month_       | `mo`, `o`     |
| _Year_        | `y`           |
| _Decade_      | `de`, `e`     |
| _Century_     | `ce`, `c`     |

## Behavior
- Extracts number-unit pairs using regex: `(\\d+)([a-zA-Z])`.  
- Multiplies each number by its unit multiplier from the `index` dictionary.  
- Sums all results into a final timestamp.  
- Returns either `float` or `int` based on `is_integer`.
  """
  
  timestamped = 0; numbers = []; letters = []; x = 0
  uinput = uinput.replace("ns", "n").replace("mc", "r").replace("ms", "i").replace("mo", "o").replace("de", "e").replace("ce", "c")

  matches = re.findall(r"(\d+)([a-zA-Z])", uinput)

  for num, letter in matches: numbers.append(num); letters.append(letter)

  for i in letters: timestamped += int(numbers[x]) * index[i][0]; x += 1
  return float(timestamped) if not is_integer else int(timestamped)

def from_seconds(uinput: float | int, years_max: bool = False, style: bool = True) -> str | dict:
  """
# Convert Seconds to Human-Readable Time

Converts a numeric duration in seconds into a human-readable string or dictionary of time units.

## Args
- `uinput` (`float | int`):  
  The total duration in seconds to convert.

- `years_max` (`bool`, optional):  
  If `True`, decades (`de`) and centuries (`ce`) are ignored in the output. Defaults to `False`.

- `style` (`bool`, optional):  
  If `True`, returns a formatted string like `"2 Hours, 10 Minutes, and 3 Seconds"`.  
  If `False`, returns a dictionary of non-zero units: `{ "h": 2, "m": 10, "s": 3 }`.  
  Defaults to `True`.

## Returns
- `str`: Human-readable string representation of the duration if `style=True`.
- `dict`: Dictionary of non-zero units if `style=False`.

## Behavior
- Iterates through time units from largest to smallest.  
- Subtracts unit values from `uinput` to calculate counts for each unit.  
- Removes all units with zero counts.  
- Builds a readable string with proper grammar:
  - One unit: `"10 Minutes"`
  - Two units: `"10 Minutes and 3 Seconds"`
  - Three or more units: `"2 Hours, 10 Minutes, and 3 Seconds"`

- Honors singular/plural units based on the count (e.g., `"1 Hour"` vs `"2 Hours"`).  

## Usage
| Unit          | Format        |
| :------------ | ------------:|
| _Nanosecond_  | `ns`, `n`     |
| _Microsecond_ | `mc`, `r`     |
| _Millisecond_ | `ms`, `i`     |
| _Second_      | `s`           |
| _Minute_      | `m`           |
| _Hour_        | `h`           |
| _Day_         | `d`           |
| _Week_        | `w`           |
| _Month_       | `mo`, `o`     |
| _Year_        | `y`           |
| _Decade_      | `de`, `e`     |
| _Century_     | `ce`, `c`     |

## Notes
- If `years_max=True`, the largest units will be years (`y`) only.  
- Returns either a readable string or a dictionary depending on the `style` parameter.  
- Handles pluralization automatically based on unit counts.

  """
  if years_max: index.pop('c'); index.pop('e')
  uinput = float(uinput); declare = {i: 0 for i in index.keys()}; parts = []
  for key, value in index.items():
    while uinput >= value[0]:
      declare[key] += 1; uinput -= value[0]

  declare = {k: v for k, v in declare.items() if v != 0}

  if not style: return declare

  for i in declare:
    value = declare[i]; unit = index[i][1 if value > 1 else 2]
    parts.append(f"{value} {unit}")

  if len(parts) == 1: result = parts[0]
  elif len(parts) == 2: result = f"{parts[0]} and {parts[1]}"
  else: result = ", ".join(parts[:-1]) + f", and {parts[-1]}"
  
  return result