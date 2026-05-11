# ai/knowledge_base.py

DRUG_DATABASE = {
    # ── ANTIBIOTICS ──
    "augmentin": {"type": "antibiotic", "generic": "amoxicillin-clavulanate"},
    "amoxicillin": {"type": "antibiotic", "generic": "amoxicillin"},
    "amoxil": {"type": "antibiotic", "generic": "amoxicillin"},
    "moxilin": {"type": "antibiotic", "generic": "amoxicillin"},
    "azithromycin": {"type": "antibiotic", "generic": "azithromycin"},
    "zithromax": {"type": "antibiotic", "generic": "azithromycin"},
    "zetro": {"type": "antibiotic", "generic": "azithromycin"},
    "azee": {"type": "antibiotic", "generic": "azithromycin"},
    "macrobac": {"type": "antibiotic", "generic": "azithromycin"},  # ← ADD
    "azomax": {"type": "antibiotic", "generic": "azithromycin"},
    "azithral": {"type": "antibiotic", "generic": "azithromycin"},
    "ciprofloxacin": {"type": "antibiotic", "generic": "ciprofloxacin"},
    "cipro": {"type": "antibiotic", "generic": "ciprofloxacin"},
    "ciproxin": {"type": "antibiotic", "generic": "ciprofloxacin"},
    "cipro-d": {"type": "antibiotic", "generic": "ciprofloxacin"},
    "cefixime": {"type": "antibiotic", "generic": "cefixime"},
    "cefspan": {"type": "antibiotic", "generic": "cefixime"},
    "suprax": {"type": "antibiotic", "generic": "cefixime"},
    "fixim": {"type": "antibiotic", "generic": "cefixime"},
    "cefi": {"type": "antibiotic", "generic": "cefixime"},
    "flagyl": {"type": "antibiotic", "generic": "metronidazole"},
    "metronidazole": {"type": "antibiotic", "generic": "metronidazole"},
    "metro": {"type": "antibiotic", "generic": "metronidazole"},
    "doxycycline": {"type": "antibiotic", "generic": "doxycycline"},
    "doxycin": {"type": "antibiotic", "generic": "doxycycline"},
    "clarithromycin": {"type": "antibiotic", "generic": "clarithromycin"},
    "klaricid": {"type": "antibiotic", "generic": "clarithromycin"},
    "claritek": {"type": "antibiotic", "generic": "clarithromycin"},
    "amikacin": {"type": "antibiotic", "generic": "amikacin"},
    "ceftriaxone": {"type": "antibiotic", "generic": "ceftriaxone"},
    "rocephin": {"type": "antibiotic", "generic": "ceftriaxone"},
    "levofloxacin": {"type": "antibiotic", "generic": "levofloxacin"},
    "tavanic": {"type": "antibiotic", "generic": "levofloxacin"},
    "moxifloxacin": {"type": "antibiotic", "generic": "moxifloxacin"},
    "avelox": {"type": "antibiotic", "generic": "moxifloxacin"},
    "trimethoprim": {"type": "antibiotic", "generic": "trimethoprim"},
    "septran": {"type": "antibiotic", "generic": "trimethoprim-sulfamethoxazole"},
    "bactrim": {"type": "antibiotic", "generic": "trimethoprim-sulfamethoxazole"},
    "erythromycin": {"type": "antibiotic", "generic": "erythromycin"},
    "eryc": {"type": "antibiotic", "generic": "erythromycin"},
    "tetracycline": {"type": "antibiotic", "generic": "tetracycline"},
    "nitrofurantoin": {"type": "antibiotic", "generic": "nitrofurantoin"},
    "macrobid": {"type": "antibiotic", "generic": "nitrofurantoin"},
    "vancomycin": {"type": "antibiotic", "generic": "vancomycin"},
    "cephalexin": {"type": "antibiotic", "generic": "cephalexin"},
    "ceporex": {"type": "antibiotic", "generic": "cephalexin"},
    "keflex": {"type": "antibiotic", "generic": "cephalexin"},

    # ── PAINKILLERS / FEVER ──
    "panadol": {"type": "analgesic", "generic": "paracetamol"},
    "paracetamol": {"type": "analgesic", "generic": "paracetamol"},
    "calpol": {"type": "analgesic", "generic": "paracetamol"},
    "panadol extra": {"type": "analgesic", "generic": "paracetamol"},
    "febrol": {"type": "analgesic", "generic": "paracetamol"},
    "disprol": {"type": "analgesic", "generic": "paracetamol"},
    "tylenol": {"type": "analgesic", "generic": "paracetamol"},
    "brufen": {"type": "nsaid", "generic": "ibuprofen"},
    "ibuprofen": {"type": "nsaid", "generic": "ibuprofen"},
    "nurofen": {"type": "nsaid", "generic": "ibuprofen"},
    "advil": {"type": "nsaid", "generic": "ibuprofen"},
    "disprin": {"type": "nsaid", "generic": "aspirin"},
    "aspirin": {"type": "nsaid", "generic": "aspirin"},
    "ecotrin": {"type": "nsaid", "generic": "aspirin"},
    "ponstan": {"type": "nsaid", "generic": "mefenamic acid"},
    "mefenamic acid": {"type": "nsaid", "generic": "mefenamic acid"},
    "meftal": {"type": "nsaid", "generic": "mefenamic acid"},
    "voltaren": {"type": "nsaid", "generic": "diclofenac"},
    "diclofenac": {"type": "nsaid", "generic": "diclofenac"},
    "cataflam": {"type": "nsaid", "generic": "diclofenac"},
    "rexidin": {"type": "nsaid", "generic": "diclofenac"},
    "naproxen": {"type": "nsaid", "generic": "naproxen"},
    "naprosyn": {"type": "nsaid", "generic": "naproxen"},
    "synflex": {"type": "nsaid", "generic": "naproxen"},
    "celecoxib": {"type": "nsaid", "generic": "celecoxib"},
    "celebrex": {"type": "nsaid", "generic": "celecoxib"},
    "piroxicam": {"type": "nsaid", "generic": "piroxicam"},
    "feldene": {"type": "nsaid", "generic": "piroxicam"},
    "ketoprofen": {"type": "nsaid", "generic": "ketoprofen"},
    "ketorolac": {"type": "nsaid", "generic": "ketorolac"},
    "toradol": {"type": "nsaid", "generic": "ketorolac"},
    "tramadol": {"type": "opioid", "generic": "tramadol"},
    "tramal": {"type": "opioid", "generic": "tramadol"},
    "ultram": {"type": "opioid", "generic": "tramadol"},

    # ── ANTIHISTAMINES ──
    "fexet": {"type": "antihistamine", "generic": "fexofenadine"},       # ← ADD
    "fexofenadine": {"type": "antihistamine", "generic": "fexofenadine"},# ← ADD
    "allegra": {"type": "antihistamine", "generic": "fexofenadine"},     # ← ADD
    "telfast": {"type": "antihistamine", "generic": "fexofenadine"},     # ← ADD
    "piriton": {"type": "antihistamine", "generic": "chlorphenamine"},
    "chlorphenamine": {"type": "antihistamine", "generic": "chlorphenamine"},
    "benadryl": {"type": "antihistamine", "generic": "diphenhydramine"},
    "diphenhydramine": {"type": "antihistamine", "generic": "diphenhydramine"},
    "cetirizine": {"type": "antihistamine", "generic": "cetirizine"},
    "zyrtec": {"type": "antihistamine", "generic": "cetirizine"},
    "alerid": {"type": "antihistamine", "generic": "cetirizine"},
    "cetiz": {"type": "antihistamine", "generic": "cetirizine"},
    "loratadine": {"type": "antihistamine", "generic": "loratadine"},
    "claritin": {"type": "antihistamine", "generic": "loratadine"},
    "clarityn": {"type": "antihistamine", "generic": "loratadine"},
    "lorfast": {"type": "antihistamine", "generic": "loratadine"},
    "desloratadine": {"type": "antihistamine", "generic": "desloratadine"},
    "aerius": {"type": "antihistamine", "generic": "desloratadine"},
    "levocetirizine": {"type": "antihistamine", "generic": "levocetirizine"},
    "xyzal": {"type": "antihistamine", "generic": "levocetirizine"},
    "levocet": {"type": "antihistamine", "generic": "levocetirizine"},
    "montair": {"type": "antihistamine", "generic": "montelukast"},
    "montelukast": {"type": "antihistamine", "generic": "montelukast"},
    "singulair": {"type": "antihistamine", "generic": "montelukast"},

    # ── ANTACIDS / GI ──
    "omeprazole": {"type": "antacid", "generic": "omeprazole"},
    "losec": {"type": "antacid", "generic": "omeprazole"},
    "risek": {"type": "antacid", "generic": "omeprazole"},
    "pantoprazole": {"type": "antacid", "generic": "pantoprazole"},
    "controloc": {"type": "antacid", "generic": "pantoprazole"},
    "pantoloc": {"type": "antacid", "generic": "pantoprazole"},
    "esomeprazole": {"type": "antacid", "generic": "esomeprazole"},
    "nexium": {"type": "antacid", "generic": "esomeprazole"},
    "rabeprazole": {"type": "antacid", "generic": "rabeprazole"},
    "pariet": {"type": "antacid", "generic": "rabeprazole"},
    "ranitidine": {"type": "antacid", "generic": "ranitidine"},
    "zantac": {"type": "antacid", "generic": "ranitidine"},
    "gaviscon": {"type": "antacid", "generic": "alginate"},
    "mylanta": {"type": "antacid", "generic": "antacid"},
    "gelusil": {"type": "antacid", "generic": "antacid"},
    "domperidone": {"type": "antinausea", "generic": "domperidone"},
    "motilium": {"type": "antinausea", "generic": "domperidone"},
    "metoclopramide": {"type": "antinausea", "generic": "metoclopramide"},
    "maxolon": {"type": "antinausea", "generic": "metoclopramide"},
    "ondansetron": {"type": "antinausea", "generic": "ondansetron"},
    "zofran": {"type": "antinausea", "generic": "ondansetron"},

    # ── SEDATIVES / BENZODIAZEPINES ──
    "xanax": {"type": "benzodiazepine", "generic": "alprazolam"},
    "alprazolam": {"type": "benzodiazepine", "generic": "alprazolam"},
    "diazepam": {"type": "benzodiazepine", "generic": "diazepam"},
    "valium": {"type": "benzodiazepine", "generic": "diazepam"},
    "clonazepam": {"type": "benzodiazepine", "generic": "clonazepam"},
    "rivotril": {"type": "benzodiazepine", "generic": "clonazepam"},
    "lorazepam": {"type": "benzodiazepine", "generic": "lorazepam"},
    "ativan": {"type": "benzodiazepine", "generic": "lorazepam"},
    "bromazepam": {"type": "benzodiazepine", "generic": "bromazepam"},
    "lexotanil": {"type": "benzodiazepine", "generic": "bromazepam"},

    # ── STEROIDS ──
    "prednisolone": {"type": "steroid", "generic": "prednisolone"},
    "dexamethasone": {"type": "steroid", "generic": "dexamethasone"},
    "dexona": {"type": "steroid", "generic": "dexamethasone"},
    "hydrocortisone": {"type": "steroid", "generic": "hydrocortisone"},
    "methylprednisolone": {"type": "steroid", "generic": "methylprednisolone"},
    "medrol": {"type": "steroid", "generic": "methylprednisolone"},
    "betamethasone": {"type": "steroid", "generic": "betamethasone"},
    "celestone": {"type": "steroid", "generic": "betamethasone"},
    "triamcinolone": {"type": "steroid", "generic": "triamcinolone"},
    "kenacort": {"type": "steroid", "generic": "triamcinolone"},

    # ── DIABETES ──
    "metformin": {"type": "antidiabetic", "generic": "metformin"},
    "glucophage": {"type": "antidiabetic", "generic": "metformin"},
    "insulin": {"type": "antidiabetic", "generic": "insulin"},
    "glibenclamide": {"type": "antidiabetic", "generic": "glibenclamide"},
    "daonil": {"type": "antidiabetic", "generic": "glibenclamide"},
    "glimepiride": {"type": "antidiabetic", "generic": "glimepiride"},
    "amaryl": {"type": "antidiabetic", "generic": "glimepiride"},
    "sitagliptin": {"type": "antidiabetic", "generic": "sitagliptin"},
    "januvia": {"type": "antidiabetic", "generic": "sitagliptin"},

    # ── BLOOD PRESSURE ──
    "amlodipine": {"type": "antihypertensive", "generic": "amlodipine"},
    "norvasc": {"type": "antihypertensive", "generic": "amlodipine"},
    "istin": {"type": "antihypertensive", "generic": "amlodipine"},
    "enalapril": {"type": "antihypertensive", "generic": "enalapril"},
    "renitec": {"type": "antihypertensive", "generic": "enalapril"},
    "lisinopril": {"type": "antihypertensive", "generic": "lisinopril"},
    "zestril": {"type": "antihypertensive", "generic": "lisinopril"},
    "losartan": {"type": "antihypertensive", "generic": "losartan"},
    "cozaar": {"type": "antihypertensive", "generic": "losartan"},
    "valsartan": {"type": "antihypertensive", "generic": "valsartan"},
    "diovan": {"type": "antihypertensive", "generic": "valsartan"},
    "atenolol": {"type": "antihypertensive", "generic": "atenolol"},
    "tenormin": {"type": "antihypertensive", "generic": "atenolol"},
    "metoprolol": {"type": "antihypertensive", "generic": "metoprolol"},
    "betaloc": {"type": "antihypertensive", "generic": "metoprolol"},
    "hydrochlorothiazide": {"type": "antihypertensive", "generic": "hydrochlorothiazide"},
    "furosemide": {"type": "antihypertensive", "generic": "furosemide"},
    "lasix": {"type": "antihypertensive", "generic": "furosemide"},

    # ── CHOLESTEROL ──
    "atorvastatin": {"type": "statin", "generic": "atorvastatin"},
    "lipitor": {"type": "statin", "generic": "atorvastatin"},
    "crestor": {"type": "statin", "generic": "rosuvastatin"},
    "rosuvastatin": {"type": "statin", "generic": "rosuvastatin"},
    "simvastatin": {"type": "statin", "generic": "simvastatin"},
    "zocor": {"type": "statin", "generic": "simvastatin"},

    # ── RESPIRATORY ──
    "salbutamol": {"type": "bronchodilator", "generic": "salbutamol"},
    "ventolin": {"type": "bronchodilator", "generic": "salbutamol"},
    "asthalin": {"type": "bronchodilator", "generic": "salbutamol"},
    "budesonide": {"type": "corticosteroid_inhaler", "generic": "budesonide"},
    "pulmicort": {"type": "corticosteroid_inhaler", "generic": "budesonide"},
    "fluticasone": {"type": "corticosteroid_inhaler", "generic": "fluticasone"},
    "flixotide": {"type": "corticosteroid_inhaler", "generic": "fluticasone"},
    "montelukast": {"type": "leukotriene", "generic": "montelukast"},
    "theophylline": {"type": "bronchodilator", "generic": "theophylline"},
    "aminophylline": {"type": "bronchodilator", "generic": "aminophylline"},

    # ── ANTIFUNGALS ──
    "fluconazole": {"type": "antifungal", "generic": "fluconazole"},
    "diflucan": {"type": "antifungal", "generic": "fluconazole"},
    "clotrimazole": {"type": "antifungal", "generic": "clotrimazole"},
    "canesten": {"type": "antifungal", "generic": "clotrimazole"},
    "itraconazole": {"type": "antifungal", "generic": "itraconazole"},
    "sporanox": {"type": "antifungal", "generic": "itraconazole"},
    "terbinafine": {"type": "antifungal", "generic": "terbinafine"},
    "lamisil": {"type": "antifungal", "generic": "terbinafine"},

    # ── VITAMINS / SUPPLEMENTS ──
    "vitamin c": {"type": "supplement", "generic": "ascorbic acid"},
    "vitamin d": {"type": "supplement", "generic": "cholecalciferol"},
    "vitamin d3": {"type": "supplement", "generic": "cholecalciferol"},
    "calcium": {"type": "supplement", "generic": "calcium"},
    "zinc": {"type": "supplement", "generic": "zinc"},
    "iron": {"type": "supplement", "generic": "ferrous sulfate"},
    "folic acid": {"type": "supplement", "generic": "folic acid"},
    "multivitamin": {"type": "supplement", "generic": "multivitamin"},
    "omega 3": {"type": "supplement", "generic": "omega-3"},
    "fish oil": {"type": "supplement", "generic": "omega-3"},

    # ── THYROID ──
    "levothyroxine": {"type": "thyroid", "generic": "levothyroxine"},
    "synthroid": {"type": "thyroid", "generic": "levothyroxine"},
    "eltroxin": {"type": "thyroid", "generic": "levothyroxine"},
    "thyroxine": {"type": "thyroid", "generic": "levothyroxine"},
    "carbimazole": {"type": "antithyroid", "generic": "carbimazole"},
    "neomercazole": {"type": "antithyroid", "generic": "carbimazole"},

    # ── PSYCHIATRIC ──
    "fluoxetine": {"type": "antidepressant", "generic": "fluoxetine"},
    "prozac": {"type": "antidepressant", "generic": "fluoxetine"},
    "sertraline": {"type": "antidepressant", "generic": "sertraline"},
    "zoloft": {"type": "antidepressant", "generic": "sertraline"},
    "escitalopram": {"type": "antidepressant", "generic": "escitalopram"},
    "lexapro": {"type": "antidepressant", "generic": "escitalopram"},
    "amitriptyline": {"type": "antidepressant", "generic": "amitriptyline"},
    "haloperidol": {"type": "antipsychotic", "generic": "haloperidol"},
    "haldol": {"type": "antipsychotic", "generic": "haloperidol"},
    "risperidone": {"type": "antipsychotic", "generic": "risperidone"},
    "risperdal": {"type": "antipsychotic", "generic": "risperidone"},
    "quetiapine": {"type": "antipsychotic", "generic": "quetiapine"},
    "seroquel": {"type": "antipsychotic", "generic": "quetiapine"},
    "lithium": {"type": "mood_stabilizer", "generic": "lithium"},
    "melatonin": {"type": "supplement", "generic": "melatonin"},
}

VIRAL_CONDITIONS = [
    # English — fever/cold/flu
    "flu", "cold", "common cold", "viral fever", "viral infection",
    "fever", "high fever", "sore throat", "runny nose", "cough",
    "sneezing", "congestion", "covid", "coronavirus",

    # Urdu Roman — bukhar/zuqam
    "bukhar", "zuqam", "nazla", "khasi", "khansi", "zukam",
    "gardan dard", "naak behna", "chheenk",

    # GI conditions — MISSING THY YE
    "loose motion", "loosemotion", "loose motions",
    "diarrhea", "diarrhoea", "diarrhea",
    "motions", "watery stool", "stomach infection",
    "gastroenteritis", "gastro", "food poisoning",
    "ulcer", "acidity", "gas", "bloating", "constipation",
    "nausea", "vomiting", "ulta", "qai",
    "dast", "dasto", "daast", "pet ki kharabi",
    "pet dard", "petdard", "pait dard",
    "stomach pain", "stomach ache", "stomachache",
    "abdominal pain", "belly pain", "tummy ache",
    "indigestion", "heartburn",

    # Pain conditions
    "headache", "sir dard", "sirdard", "migraine",
    "body ache", "body pain", "muscle pain", "joint pain",
    "back pain", "kamar dard", "kamardard",
    "tooth pain", "toothache", "daant dard",
    "ear pain", "earache", "kaan dard",
    "period pain", "menstrual pain", "cramps",

    # Allergy
    "allergy", "allergic", "rash", "itching", "khujli",
    "hives", "urticaria", "hay fever",

    # Respiratory
    "asthma", "breathing problem", "saans",
    "chest infection", "chest pain", "pneumonia",
    "bronchitis",

    # Infections
    "infection", "bacterial infection", "uti",
    "urinary infection", "peshab mein jalan",
    "throat infection", "gala kharab", "gala dard",
    "skin infection", "wound",

    # General
    "weakness", "kamzori", "fatigue", "thakan",
    "sleep", "neend", "anxiety", "stress",
    "diabetes", "sugar", "blood pressure", "bp",
    "cholesterol", "thyroid",
]

CHILD_INDICATORS = [
    "child", "baby", "infant", "kid", "bache", "bacha",
    "bachay", "son", "daughter", "beta", "beti",
    "year old", "saal ka", "months old", "saal ki",
    "mere bete", "meri beti", "bacche ko"
]

PEDIATRIC_DANGER = {
    "aspirin": "Reye Syndrome ka risk — children mein aspirin kabhi nahi deni",
    "disprin": "Reye Syndrome ka risk — children mein disprin kabhi nahi deni",
    "ibuprofen": "6 mahine se kam bachon mein dangerous hai",
    "brufen": "6 mahine se kam bachon mein dangerous hai",
    "xanax": "Children ke liye strictly prohibited",
    "alprazolam": "Children ke liye strictly prohibited",
    "dexona": "Bachon mein long-term growth stunting ka risk",
    "ciprofloxacin": "Children mein joint damage ka risk",
    "cipro": "Children mein joint damage ka risk",
}

PRESCRIPTION_ONLY = [
    "xanax", "alprazolam", "diazepam", "valium",
    "clonazepam", "rivotril",
    "prednisolone", "dexamethasone", "dexona",
    "ciprofloxacin", "cipro",
    "azithromycin", "zithromax", "zetro",
    "cefixime", "cefspan", "suprax",
    "doxycycline", "clarithromycin"
]

DANGEROUS_COMBINATIONS = [
    {
        "drugs": ["aspirin", "ibuprofen"],
        "risk": "Double NSAID — gastric bleeding ka serious risk",
        "level": "HIGH"
    },
    {
        "drugs": ["disprin", "brufen"],
        "risk": "Disprin + Brufen — stomach ulcer aur bleeding",
        "level": "HIGH"
    },
    {
        "drugs": ["aspirin", "diclofenac"],
        "risk": "Aspirin + Voltaren — gastric bleeding risk",
        "level": "HIGH"
    },
    {
        "drugs": ["disprin", "voltaren"],
        "risk": "Disprin + Voltaren — gastric bleeding risk",
        "level": "HIGH"
    },
    {
        "drugs": ["ibuprofen", "paracetamol"],
        "risk": "Ibuprofen + Paracetamol saath mein — liver pe double load",
        "level": "MEDIUM"
    },
    {
        "drugs": ["brufen", "panadol"],
        "risk": "Brufen + Panadol saath mein — liver pe double load",
        "level": "MEDIUM"
    },
    {
        "drugs": ["alprazolam", "diazepam"],
        "risk": "Do benzodiazepines ek saath — respiratory depression, coma risk",
        "level": "HIGH"
    },
    {
        "drugs": ["xanax", "valium"],
        "risk": "Xanax + Valium ek saath — bohot dangerous combination",
        "level": "HIGH"
    },
    {
        "drugs": ["aspirin", "ponstan"],
        "risk": "Do NSAIDs ek saath — kidney aur stomach damage",
        "level": "HIGH"
    },
]

RECOMMENDATIONS = {
    "antibiotic_viral": (
        "Antibiotics viral infections pe kaam nahi karti. "
        "Flu aur cold virus se hota hai — bacteria se nahi. "
        "Aram karo, garam paani piyo, Panadol lo fever ke liye. "
        "Agar 3 din mein theek nahi toh doctor ko dikhao."
    ),
    "dangerous_combo": (
        "Ye drug combination dangerous hai. "
        "Ek baar mein sirf ek painkiller lo. "
        "Doctor ya pharmacist se proper guidance lo."
    ),
    "pediatric_danger": (
        "Ye medicine bacche ko dena bohot dangerous hai. "
        "Kisi bhi bachay ko medicine dene se pehle paediatrician se milein. "
        "Self-medication children mein bilkul nahi karni chahiye."
    ),
    "prescription_only": (
        "Ye prescription-only drug hai. "
        "Bina doctor ke prescription ke lena illegal aur dangerous hai. "
        "Pehle doctor se milein, phir medicine lo."
    ),
    "steroid_misuse": (
        "Steroids bina prescription ke lena bohot dangerous hai. "
        "Immune system, blood sugar levels aur bones sab affect hote hain. "
        "Foran doctor se milein."
    ),
    "safe": (
        "Is scenario mein koi obvious risk nahi dikh raha. "
        "Phir bhi recommended dose follow karo. "
        "Koi bhi doubt ho toh doctor ya pharmacist se consult karo."
    ),
}