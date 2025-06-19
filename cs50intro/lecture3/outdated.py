months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def parse_numeric_date(date_str):
    # Try parsing month/day/year numeric format like 9/8/1636
    try:
        parts = date_str.split('/')
        if len(parts) != 3:
            return None
        month, day, year = parts
        month = int(month)
        day = int(day)
        year = int(year)
        if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
            return (year, month, day)
    except ValueError:
        return None

def parse_written_date(date_str):
    
    try:
        
        parts = date_str.split()
        if len(parts) != 3:
            return None
        month_name, day_str, year_str = parts
        
       
        if not day_str.endswith(','):
            return None
        day = int(day_str[:-1])
        year = int(year_str)
        
        
        if month_name not in months:
            return None
        month = months.index(month_name) + 1
        
        if 1 <= day <= 31 and year > 0:
            return (year, month, day)
    except ValueError:
        return None

def main():
    while True:
        date_input = input("Enter a date (e.g., 9/8/1636 or September 8, 1636): ").strip()
        
        parsed = parse_numeric_date(date_input)
        if parsed is None:
            parsed = parse_written_date(date_input)
        
        if parsed is not None:
            year, month, day = parsed
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
        else:
            print("Invalid date format. Please try again.")

if __name__ == "__main__":
    main()
