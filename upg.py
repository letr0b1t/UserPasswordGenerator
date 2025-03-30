import itertools
import os
from datetime import datetime
import random

def print_header():
    header = r"""
   |\_/|
   (O,o)
   /)__)
   --"-"--
:  UPG - UserPasswordGenerator  :
:       By Letr0b1t             :
    """
    print(header)

def split_date(date_str):
    if not date_str:
        return None
    day, month, year = date_str.split("/")
    return {"day": day, "month": month, "year": year}

MONTHS = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December"
}

def generate_passwords(data, min_length):
    words = [data[key] for key in data if key not in ["birth_date", "partner_birth_date", "pet_birth_date", "min_length", "keywords"] and data[key]]
    if data["keywords"]:
        words.extend(data["keywords"])
    passwords = set()

    for r in range(1, min(4, len(words) + 1)):
        for perm in itertools.permutations(words, r):
            base = "".join(perm)
            passwords.add(base)
            
            passwords.add(base.lower())
            passwords.add(base.capitalize())
            passwords.add("".join(w.capitalize() for w in perm))
            
            for suffix in ["!", "@", "#", "$", "%"]:
                passwords.add(base + suffix)
                passwords.add(base.lower() + suffix)
                passwords.add("".join(w.capitalize() for w in perm) + suffix)
            
            for _ in range(3):
                num = str(random.randint(0, 999))
                passwords.add(base + num)
                passwords.add(base.lower() + num)
                passwords.add("".join(w.capitalize() for w in perm) + num)
            
            leet_base = base.replace("a", "4").replace("e", "3").replace("i", "1").replace("o", "0").replace("s", "5")\
                           .replace("t", "7").replace("l", "1").replace("b", "8").replace("z", "2")
            passwords.add(leet_base)
            passwords.add(leet_base + "!1")
            passwords.add(leet_base + str(random.randint(0, 99)))
            leet_partial = base.replace("a", "4").replace("s", "5")
            passwords.add(leet_partial)
            
            if len(perm) > 1:
                passwords.add("-".join(perm))
                passwords.add(".".join(perm))
                passwords.add("_".join(perm))

    for date in [split_date(data["birth_date"]), split_date(data["partner_birth_date"]), split_date(data["child_birth_date"])]:
        if date:
            day, month, year = date["day"], date["month"], date["year"]
            passwords.add(day)
            passwords.add(month)
            passwords.add(year)
            passwords.add(year[-2:])
            passwords.add(day + month)
            passwords.add(month + day)
            passwords.add(day + month + year)
            passwords.add(year + month + day)
            passwords.add(base + day)
            passwords.add(base + month)
            passwords.add(base + year)
            passwords.add(base + day + month + year)
            passwords.add(f"{day}-{month}-{year}")
            passwords.add(f"{year}/{month}/{day}")

            if month in MONTHS:
                passwords.add(MONTHS[month])
                passwords.add(base + MONTHS[month])

    common_patterns = ["1234", "0000", "!@#", "qwerty"]
    for pattern in common_patterns:
        passwords.add(base + pattern)
        passwords.add(base.lower() + pattern)
        passwords.add("".join(w.capitalize() for w in perm) + pattern)

    filtered_passwords = [pwd for pwd in passwords if len(pwd) >= min_length]
    return filtered_passwords

def collect_data():
    data = {
        "first_name": "",
        "surname": "",
        "nickname": "",
        "birth_date": "",
        "partner_name": "",
        "partner_nickname": "",
        "partner_birth_date": "",
        "child_name": "",
        "child_nickname": "",
        "child_birth_date": "",
        "pet_name": "",
        "company_name": "",
        "keywords": [],
        "min_length": 6
    }
    
    print("[+] Insert the information about the victim to make a dictionary")
    print("[+] If you don't know all the info, just hit enter when asked! ;)")
    data["first_name"] = input("> First Name: ").strip()
    data["surname"] = input("> Surname: ").strip()
    data["nickname"] = input("> Nickname: ").strip()
    data["birth_date"] = input("> Birthdate (DD/MM/YYYY): ").strip()
    data["partner_name"] = input("> Partner's name: ").strip()
    data["partner_nickname"] = input("> Partner's nickname: ").strip()
    data["partner_birth_date"] = input("> Partner's birthdate (DD/MM/YYYY): ").strip()
    data["child_name"] = input("> Child's name: ").strip()
    data["child_nickname"] = input("> Child's nickname: ").strip()
    data["child_birth_date"] = input("> Child's birthdate (DD/MM/YYYY): ").strip()
    data["pet_name"] = input("> Pet's name: ").strip()
    data["company_name"] = input("> Company name: ").strip()
    keywords = input("> Do you want to add some key words about the victim? (comma-separated): ").strip()
    if keywords:
        data["keywords"] = [k.strip() for k in keywords.split(",")]
    
    min_length_input = input("> Minimum password length (default is 6): ").strip()
    try:
        data["min_length"] = int(min_length_input) if min_length_input else 6
    except ValueError:
        print("[!] Invalid input, using default minimum length of 6.")
        data["min_length"] = 6
    
    return data

def main():
    print_header()
    data = collect_data()
    passwords = generate_passwords(data, data["min_length"])
    
    filename = f"passwords_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for pwd in passwords:
            f.write(pwd + "\n")
    
    print(f"\n[+] Generated passwords: {len(passwords)}")
    print(f"[+] Saved to: {filename}")

if __name__ == "__main__":
    main()
