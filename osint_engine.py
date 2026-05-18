import requests
import json

# 1. THE DATA GATHERER
def fetch_github_data(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 403:
            # THIS TELLS US IF WE GOT BLOCKED!
            print(f"[!] BLOCKED BY GITHUB SEC (Rate Limit Exceeded) on handle: {username}")
            return None
        return None
    except Exception:
        return None

# 2. THE IDENTITY DISAMBIGUATION BRAIN
def calculate_confidence_score(scraped_data, seed_data):
    if not scraped_data:
        return 0
    score = 0
    if seed_data.get("location") and scraped_data.get("location"):
        if seed_data["location"].lower() in scraped_data["location"].lower():
            score += 40
    if seed_data.get("company") and scraped_data.get("company"):
        if seed_data["company"].lower() in scraped_data["company"].lower():
            score += 40
    if scraped_data.get("public_repos", 0) > 0:
        score += 20
    return score

# 3. THE DYNAMIC PERMUTATOR
def generate_username_permutations(first_name, last_name):
    f = first_name.lower().strip()
    l = last_name.lower().strip()
    
    base_patterns = [
        f"{f}{l}", f"{f}.{l}", f"{f}_{l}", 
        f"{f[0]}{l}", f"{f}{l[0]}", f"{l}{f}"
    ]
    
    all_permutations = list(base_patterns)
    common_suffixes = ["1", "11", "22", "123", "007", "99", "00", "01", "02", "03", "04", "05"]
    
    for base in base_patterns:
        for num in common_suffixes:
            all_permutations.append(f"{base}{num}")
            all_permutations.append(f"{base}_{num}")
            
    return all_permutations

# 4. THE CORE ENGINE & EVIDENCE EXPORTER
def run_engine(target_username, known_seed_data):
    print(f"[*] Initializing Vanguard OSINT Engine for target: {target_username}...")
    
    github_data = fetch_github_data(target_username)
    
    if github_data:
        confidence = calculate_confidence_score(github_data, known_seed_data)
        
        report = "="*45 + "\n"
        report += "🎯 TARGET INTELLIGENCE REPORT\n"
        report += "="*45 + "\n"
        report += f"Target Username : {target_username}\n"
        report += f"Name Found      : {github_data.get('name', 'Unknown')}\n"
        report += f"Location Found  : {github_data.get('location', 'Unknown')}\n"
        report += f"Company Found   : {github_data.get('company', 'Unknown')}\n"
        report += "-" * 45 + "\n"
        report += f"🔥 CONFIDENCE SCORE: {confidence}/100\n"
        
        if confidence >= 80:
            report += "[!] HIGH PROBABILITY MATCH. Target isolated.\n"
        elif confidence >= 40:
            report += "[~] PARTIAL MATCH. Further manual OSINT required.\n"
        else:
            report += "[-] LOW PROBABILITY. Likely a false positive.\n"
        report += "="*45 + "\n"
        
        print(report)
        
        filename = f"{target_username}_osint_report.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(report)
        print(f"[+] EVIDENCE SAVED: A hard copy has been exported to '{filename}'")

# 5. THE IGNITION SWITCH & SMART HUNTER
if __name__ == "__main__":
    print("[*] Initiating Vanguard Permutation Hunter...")
    
    test_first = "Rahul"
    test_last = "Jangir"
    
    usernames_to_test = generate_username_permutations(test_first, test_last)
    print(f"[*] Generated {len(usernames_to_test)} potential handles. Commencing hunt...\n")
    
    found_profile = None
    seed_intel = {"location": "Bengaluru"} 
    
    for u in usernames_to_test:
        print(f"[*] Testing handle: {u}...")
        
        profile_data = fetch_github_data(u)
        
        if profile_data:
            print(f"[~] Profile exists. Checking confidence...")
            
            confidence = calculate_confidence_score(profile_data, seed_intel)
            
            if confidence >= 40:
                print(f"\n[+] BOOM! High-confidence target acquired under handle: '{u}'")
                found_profile = profile_data
                run_engine(u, seed_intel)
                break  
            else:
                print("[-] False positive. Continuing the hunt...\n")
                
    if not found_profile:
        print("\n[-] Hunt finished. Target not found on this platform.")