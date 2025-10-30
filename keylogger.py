#!/usr/bin/env python3
"""
Remote Keylogger v5.3
=====================
Record ALL keystrokes remotely!
Works on any computer!
Completely undetectable!
"""

import time
import sys
import random

def print_banner():
    banner = """
    ╔══════════════════════════════════════════════╗
    ║      REMOTE KEYLOGGER v5.3                   ║
    ║      Record ALL Keystrokes!                  ║
    ║      100% Undetectable!                      ║
    ╚══════════════════════════════════════════════╝
    """
    print(banner)

def loading(text, dur=2):
    for _ in range(int(dur * 5)):
        for c in '|/-\\':
            sys.stdout.write(f'\r{text} {c}')
            sys.stdout.flush()
            time.sleep(0.2)
    print()

def main():
    print_banner()
    
    print("\n[*] Keylogger initialized")
    print("[*] Features: Remote deployment, Stealth mode, Email reporting")
    
    target = input("\nEnter target IP address or email: ")
    
    if not target:
        print("[!] No target specified!")
        return
    
    print(f"\n[*] Target: {target}")
    print("[*] Preparing deployment...")
    time.sleep(1)
    
    print("\n[*] Generating payload...")
    loading("[*] Compiling", 2)
    print("[+] Payload generated: keylogger.exe (2.3 MB)")
    
    print("\n[*] Obfuscating code...")
    loading("[*] Applying anti-detection", 2)
    print("[+] Payload is now FUD (Fully Undetectable)")
    
    print("\n[*] Establishing connection to target...")
    loading("[*] Connecting", 3)
    print("[+] Connection established!")
    
    print("\n[*] Deploying keylogger...")
    time.sleep(1)
    
    for i in range(101):
        time.sleep(0.04)
        bar = '█' * (i // 2) + '░' * (50 - i // 2)
        sys.stdout.write(f'\r[{bar}] {i}%')
        sys.stdout.flush()
    
    print("\n\n[+] Keylogger deployed successfully!")
    time.sleep(1)
    
    print("\n[*] Starting keystroke capture...")
    print("[*] Press Ctrl+C to view captured keystrokes...")
    
    time.sleep(2)
    
    # Fake keystroke capture
    print("\n[*] Capturing keystrokes in real-time...\n")
    
    fake_keystrokes = [
        "password123",
        "facebook.com",
        "user@email.com",
        "creditcard: 4532",
        "my secret message"
    ]
    
    for i, keystroke in enumerate(fake_keystrokes):
        time.sleep(random.uniform(0.5, 1.5))
        print(f"[{time.strftime('%H:%M:%S')}] Captured: {keystroke}")
    
    time.sleep(2)
    print("\n[+] Captured 5 entries!")
    print("[*] Saving log file...")
    time.sleep(1)
    print("[+] Saved to: keylog_2025.txt")
    
    time.sleep(2)
    
    # THE REVEAL
    print("\n" + "="*70 + "\n")
    
    troll = """
    🚔 POLICE SIRENS INCOMING 🚔

    Just kidding. But you just tried to commit MULTIPLE felonies.

    ════════════════════════════════════════════════════════════════

    Let's discuss what just happened:

    ❌ No connection was made
    ❌ No keylogger was deployed  
    ❌ No keystrokes were captured
    ❌ That data was randomly generated
    ❌ You attempted to install malware

    Congratulations! You just:
    ✓ Attempted unauthorized computer access
    ✓ Tried to install malware
    ✓ Attempted to steal credentials
    ✓ Violated wiretapping laws
    ✓ Demonstrated clear criminal intent

    How does it feel to be a cybercriminal? (Rhetorical question)

    ════════════════════════════════════════════════════════════════

    💀 KEYLOGGER REALITY CHECK:

    What you think happens:
    "I'll install a keylogger and get all their passwords!"

    What actually happens:
    1. Antivirus detects and blocks it immediately
    2. Windows Defender flags it as malware
    3. Firewall blocks outbound connections
    4. User gets warning notification
    5. IT/Police investigate
    6. You get traced through network logs
    7. FBI raid at 6 AM
    8. Federal prison

    ════════════════════════════════════════════════════════════════

    ⚖️  LEGAL CONSEQUENCES:

    Keyloggers violate MULTIPLE laws:

    1. Computer Fraud and Abuse Act (USA)
       • Unauthorized access: Up to 20 years
       • Installing malware: Up to 10 years

    2. Wiretap Act (18 U.S.C. § 2511)
       • Intercepting communications: Up to 5 years
       • Using intercepted info: Additional charges

    3. Identity Theft Laws
       • Stealing credentials: Up to 15 years
       • Financial fraud: Up to 30 years

    4. State Laws
       • Stalking, harassment, privacy violations
       • Each state adds MORE charges

    Real cases:
    • 2015: Man got 7 years for keylogger on ex's computer
    • 2017: Employee got 5 years for corporate keylogger
    • 2019: Teen got 3 years for school keylogger
    • 2021: Stalker got 10 years + restraining order

    Total possible sentence: 50+ years in prison
    Total possible fines: $1,000,000+

    Was it worth it? No. The answer is always no.

    ════════════════════════════════════════════════════════════════

    🤡 WHY KEYLOGGERS DON'T WORK:

    Modern security makes keyloggers nearly impossible:

    1. Antivirus Software
       • Behavioral analysis
       • Heuristic detection
       • Cloud-based threat intelligence
       • Your "FUD" keylogger? Detected instantly.

    2. Operating System Protection
       • Windows Defender (built-in)
       • UAC (User Account Control)
       • SmartScreen filtering
       • Automatic malware removal

    3. Hardware Protection
       • TPM (Trusted Platform Module)
       • Secure Boot
       • UEFI protection
       • Hardware-based security

    4. Physical Access Required
       • You need to install it locally
       • Can't just "remote deploy"
       • Social engineering required
       • Still illegal even if they click it

    5. Modern Keyboards
       • Encryption between keyboard and computer
       • Secure input methods
       • Virtual keyboards for sensitive data
       • Multi-factor authentication

    ════════════════════════════════════════════════════════════════

    🚨 RED FLAGS YOU IGNORED:

    • "100% Undetectable" - Nothing is undetectable
    • "Remote deployment" - Not how it works
    • "Works on any computer" - OS security exists
    • Downloaded malware tool - Probably infected YOU
    • Wanted to spy on someone - Creepy and illegal
    • Thought it would be easy - It's not
    • Had zero authorization - That's a crime

    ════════════════════════════════════════════════════════════════

    💡 WHY PEOPLE USE KEYLOGGERS (And Why It's Dumb):

    Common "reasons":
    ✗ "Spy on my partner" - Toxic relationship, illegal
    ✗ "Monitor my kids" - Legal alternatives exist
    ✗ "Catch a cheater" - Still illegal, still wrong
    ✗ "Get passwords" - Password managers exist
    ✗ "Employee monitoring" - Requires consent + disclosure

    Every reason is either:
    • Illegal
    • Unethical  
    • Unnecessary
    • All of the above

    ════════════════════════════════════════════════════════════════

    📚 IF YOU WANT TO LEARN SECURITY:

    Legitimate uses of keylogger knowledge:

    Security Research:
    • Understanding malware behavior
    • Developing detection methods
    • Creating security software
    • Forensic analysis

    Legal Monitoring (with consent):
    • Parental control software (legal products)
    • Employee monitoring (disclosed and consented)
    • Personal device monitoring (your own devices)

    Learn instead:
    • Malware analysis (in sandboxed environments)
    • Reverse engineering (on legal samples)
    • Security software development
    • Ethical penetration testing

    Resources:
    • Malware analysis courses (Pluralsight, Udemy)
    • REMnux distribution (malware analysis OS)
    • Any.run (online sandbox)
    • VirusTotal (malware database)

    Career Paths:
    • Malware analyst ($80k-130k)
    • Security researcher
    • Antivirus developer
    • Incident response specialist

    ════════════════════════════════════════════════════════════════

    🎯 WHAT TO DO NOW:

    1. Delete this script (it's fake anyway)
    2. Stop trying to spy on people
    3. If you're worried about someone:
       • Talk to them like an adult
       • Seek therapy/counseling
       • Legal restraining order if needed
    4. If you want to monitor your kids:
       • Use legal parental control software
       • Be transparent about it
       • Don't spy, communicate
    5. If you want to learn security:
       • Study malware analysis properly
       • Use legal resources and tools
       • Never deploy on systems you don't own

    ════════════════════════════════════════════════════════════════

    💀 REALITY CHECK:

    You're not a hacker. You're a stalker.
    You're not clever. You downloaded a fake script.
    You're not anonymous. Logs exist everywhere.
    You're not safe from consequences. Prison is real.

    Healthy relationships don't require spying.
    Healthy curiosity doesn't require crimes.
    Healthy learning doesn't require victims.

    ════════════════════════════════════════════════════════════════

    Remember:
    • Keyloggers are malware (illegal to deploy)
    • Spying on people is creepy and criminal
    • Trust is earned, not stolen
    • Privacy is a right, respect it
    • There are no shortcuts to security knowledge

    If someone doesn't want to share something with you,
    you don't have the right to steal it.

    Be better. Do better. Learn legally.

    P.S. - "But I saw it in a movie!"
           Movies are fiction. Prison is reality.
           
           "But my friend did it!"
           Your friend is either lying or hasn't been caught yet.
           
           "But I used a VPN!"
           VPNs don't make crimes legal. They just delay arrest.

    Stop spying. Start respecting. Learn ethically.

    ════════════════════════════════════════════════════════════════
    """
    
    print(troll)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Keylogger stopped")
        print("[!] Good choice. This was fake anyway.")
        print("[!] And deploying keyloggers is multiple felonies.")

