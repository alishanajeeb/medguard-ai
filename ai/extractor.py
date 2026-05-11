# ai/extractor.py

import re
from ai.knowledge_base import DRUG_DATABASE, VIRAL_CONDITIONS, CHILD_INDICATORS


def extract_entities(text):
    text_lower = text.lower()

    detected_drugs = []
    detected_conditions = []
    is_child = False

    # Step 1: Drugs detect karo
    for drug_name, drug_info in DRUG_DATABASE.items():
        if drug_name in text_lower:
            detected_drugs.append({
                "name": drug_name,
                "type": drug_info["type"],
                "generic": drug_info["generic"]
            })

    # Step 2: Conditions detect karo — longer phrases pehle check karo
    sorted_conditions = sorted(VIRAL_CONDITIONS, key=len, reverse=True)
    for condition in sorted_conditions:
        if condition in text_lower:
            detected_conditions.append(condition)

    # Step 3: Child case detect karo
    for indicator in CHILD_INDICATORS:
        if indicator in text_lower:
            is_child = True
            break

    # Step 4: Age extract
    age = extract_age(text_lower)
    if age is not None and age < 18:
        is_child = True

    # Step 5: Remove duplicate/overlapping conditions
    # e.g. agar "loose motion" mila toh "motion" alag na rakho
    final_conditions = []
    for c in detected_conditions:
        is_subset = any(
            c != other and c in other
            for other in detected_conditions
        )
        if not is_subset:
            final_conditions.append(c)

    return {
        "drugs": detected_drugs,
        "conditions": list(set(final_conditions)),
        "is_child": is_child,
        "age": age
    }


def extract_age(text):
    patterns = [
        r'(\d+)\s*year',
        r'(\d+)\s*saal',
        r'(\d+)\s*month',
        r'age\s*[:\s]\s*(\d+)',
        r'(\d+)\s*sal',
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return int(match.group(1))
    return None