import re
import math

def calculate_entropy(text):
    if not text:
        return 0.0
    
    entropy = 0.0
    text_length = len(text)
    frequencies = {char: text.count(char) for char in set(text)}
    
    for char, count in frequencies.items():
        probability = count / text_length
        entropy -= probability * math.log2(probability)
        
    return round(entropy, 2)

def classify_strings(strings, entropy_threshold=4.5):
    patterns = {
        "URL": r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[^\s]*',
        "IP_Address": r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b',
        "Email": r'[\w.+-]+@[\w-]+\.[\w.-]+',
        "Cryptographic_Key_Or_Hash": r'(?i)\b[a-f0-9]{32,64}\b|(?:key|secret|token|password)[=:][\w\-]{8,32}'
    }
    
    capability_keywords = [
        "socket", "connect", "bind", "ptrace", "execve", "system", "fork", "chmod", 
        "mprotect", "UPX!", "libc.so", "malloc", "free", "memcpy", "strcpy", "sprintf",
        "OpenProcess", "VirtualAlloc", "WriteProcessMemory", "CreateRemoteThread",
        "RegOpenKeyEx", "GetProcAddress", "LoadLibrary", "InternetOpen", "ShellExecute"
    ]
    
    classified_data = {
        "URL": [],
        "IP_Address": [],
        "Email": [],
        "Cryptographic_Key_Or_Hash": [],
        "Suspicious_Capabilities_Or_APIs": [],
        "High_Risk_Alerts": [],
        "General_Strings": []
    }
    
    for string in strings:
        matched = False
        cleaned_string = string.strip()
        entropy_score = calculate_entropy(cleaned_string)
        
        for category, regex in patterns.items():
            if re.search(regex, cleaned_string):
                item = {"string": cleaned_string, "entropy": entropy_score}
                classified_data[category].append(item)
                matched = True
                
        for keyword in capability_keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', cleaned_string):
                item = {"string": keyword, "context": cleaned_string, "entropy": entropy_score}
                if not any(c["string"] == keyword for c in classified_data["Suspicious_Capabilities_Or_APIs"]):
                    classified_data["Suspicious_Capabilities_Or_APIs"].append(item)
                matched = True
                
        if entropy_score >= entropy_threshold:
            if not any(alert["string"] == cleaned_string for alert in classified_data["High_Risk_Alerts"]):
                classified_data["High_Risk_Alerts"].append({"string": cleaned_string, "entropy": entropy_score})
        
        if not matched and entropy_score < entropy_threshold:
            classified_data["General_Strings"].append({"string": cleaned_string, "entropy": entropy_score})
            
    return classified_data
