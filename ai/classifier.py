import os
import json
from groq import Groq
from dotenv import load_dotenv
from ai.extractor import extract_entities
from ai.knowledge_base import DRUG_DATABASE, RECOMMENDATIONS

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_input(user_input):
    # Step 1: Local DB se sirf medicine detect karo
    entities = extract_entities(user_input)
    drugs    = entities["drugs"]
    is_child = entities["is_child"]

    # Step 2: Medicine info prepare karo for Groq
    if drugs:
        medicine_context = ", ".join([
            f"{d['name']} (generic: {d['generic']}, class: {d['type']})"
            for d in drugs
        ])
    else:
        medicine_context = "not found in local database"

    # Step 3: Groq se full analysis lo
    result = groq_analyze(user_input, medicine_context, is_child)
    result["source"] = "ai" if medicine_context == "not found in local database" else "hybrid"
    return result


def groq_analyze(user_input, medicine_context, is_child):
    prompt = f"""You are a senior clinical pharmacist in Pakistan with 20 years experience.
A patient described their self-medication plan. Your job is to analyze it carefully.

DETECTED MEDICINES (from database): {medicine_context}
IS CHILD CASE: {is_child}
USER INPUT: "{user_input}"
p
ANALYZE these specific things:
1. What medicine is the user taking?
2. What condition are they trying to treat?
3. IS THIS MEDICINE CORRECT FOR THIS CONDITION? (Most important check)
4. Are there any dangerous risks?
5. What should they do instead?

CRITICAL RULES YOU MUST FOLLOW:
- Glucophage/Metformin is for DIABETES only — not for stomach pain, petdard, or any pain
- Panadol/Paracetamol is for fever and pain — NOT for weakness, kamzori, diabetes, BP
- Antibiotics (Augmentin, Flagyl, Macrobac etc) for viral infections (flu, cold, zuqam) = HIGH risk
- Flagyl/Metronidazole for loose motion/diarrhea = valid but needs prescription = MEDIUM
- Antihistamines (Fexet, Zyrtec) for allergy = LOW risk, for fever = MEDIUM (wrong use)
- Benzodiazepines (Xanax, Valium) without prescription = HIGH risk
- Steroids (Dexona, Prednisolone) without prescription = HIGH risk
- Aspirin/Disprin for children under 16 = HIGH risk (Reye syndrome)
- Two NSAIDs together = HIGH risk (gastric bleeding)
- Paracetamol + Ibuprofen overdose = MEDIUM risk
- ANY medicine being used for WRONG condition = at least MEDIUM risk
- Supplement/vitamins = LOW risk generally
- If medicine does NOT treat the stated condition = flag it clearly

WRONG USE EXAMPLES:
- "Glucophage for petdard" = MEDIUM risk, wrong medicine for pain
- "Panadol for kamzori" = MEDIUM risk, wrong medicine for weakness  
- "Antibiotic for allergy" = HIGH risk, completely wrong
- "Fexet for fever" = MEDIUM risk, antihistamine doesn't reduce fever
- "Brufen for diabetes" = MEDIUM risk, NSAID doesn't treat diabetes

Respond ONLY with this exact JSON format, no extra text, no markdown:
{{
  "medicine": "medicine name detected",
  "condition": "condition user is trying to treat",
  "risk_level": "HIGH or MEDIUM or LOW",
  "risks": [
    "risk 1 — specific and clear in simple Urdu-English",
    "risk 2",
    "risk 3"
  ],
  "recommendation": "What should the user actually do — practical advice for Pakistan context in 2-3 sentences",
  "is_child_case": {str(is_child).lower()}
}}"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=700
        )

        raw = response.choices[0].message.content.strip()
        print(f"Groq response: {raw[:300]}")

        # Clean markdown
        if "```json" in raw:
            raw = raw.split("```json")[1].split("```")[0].strip()
        elif "```" in raw:
            raw = raw.split("```")[1].split("```")[0].strip()

        # Extract JSON
        start = raw.find('{')
        end   = raw.rfind('}') + 1
        if start != -1 and end > start:
            raw = raw[start:end]

        result = json.loads(raw)

        # Validate
        for field in ['medicine','condition','risk_level','risks','recommendation']:
            if field not in result:
                result[field] = "Could not determine"

        # Force risk level to valid value
        if result['risk_level'] not in ['HIGH','MEDIUM','LOW']:
            result['risk_level'] = 'MEDIUM'

        return result

    except Exception as e:
        print(f"Groq error: {e}")
        return {
            "medicine": "Could not detect",
            "condition": "Could not detect",
            "risk_level": "UNKNOWN",
            "risks": [
                "Analysis fail ho gayi — please dobara try karein",
                "Medicine ka poora naam likhein jaise: 'Panadol le raha hoon bukhar ke liye'"
            ],
            "recommendation": "Dobara try karein ya medicine ka poora naam clearly likhein.",
            "is_child_case": is_child
        }