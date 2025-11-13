# Definition des fonctions à utiliser dans main.py
def is_sorted(report):
    """Vérifie si la liste est strictement croissante ou décroissante."""
    increasing = all(report[i] < report[i+1] for i in range(len(report)-1))
    decreasing = all(report[i] > report[i+1] for i in range(len(report)-1))
    return increasing or decreasing

def valid_differences(report):
    """Vérifie que les différences entre niveaux consécutifs sont entre 1 et 3 inclus."""
    return all(1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report)-1))

def is_safe(report):
    """Vérifie si un rapport est sûr."""
    return is_sorted(report) and valid_differences(report)

def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    
    for i in range(len(report)):
        temp = report[:i] + report[i+1:]  
        if is_safe(temp):
            return True
    return False
            