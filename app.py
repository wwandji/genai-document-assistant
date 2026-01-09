import os
from dotenv import load_dotenv
from openai import OpenAI

# -----------------------------
# CONFIG
# -----------------------------
SAMPLE_DIR = "sample_docs"
MAX_CHARS = 8000  # limite pour éviter des prompts trop longs

# -----------------------------
# Charger la clé API
# -----------------------------
load_dotenv(dotenv_path=".env")
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY introuvable. Vérifie le fichier .env")

client = OpenAI(api_key=api_key)

# -----------------------------
# Lister les documents disponibles
# -----------------------------
files = [f for f in os.listdir(SAMPLE_DIR) if f.lower().endswith(".txt")]
files.sort()

if not files:
    raise RuntimeError(f"Aucun fichier .txt trouvé dans '{SAMPLE_DIR}'.")

print("\n📄 Verfügbare Dokumente:")
for i, fname in enumerate(files, start=1):
    print(f"  {i}. {fname}")

# -----------------------------
# Choisir un document
# -----------------------------
choice = input("\nWähle eine Nummer (z.B. 1): ").strip()

if not choice.isdigit():
    raise ValueError("Bitte eine Zahl eingeben (z.B. 1).")

idx = int(choice) - 1
if idx < 0 or idx >= len(files):
    raise ValueError("Ungültige Auswahl. Bitte eine gültige Nummer wählen.")

selected_file = os.path.join(SAMPLE_DIR, files[idx])

# -----------------------------
# Lire le document
# -----------------------------
with open(selected_file, "r", encoding="utf-8") as f:
    document_text = f.read()

doc_len = len(document_text)
doc_trimmed = document_text[:MAX_CHARS]
was_trimmed = doc_len > MAX_CHARS

print(f"\n✅ Dokument geladen: {selected_file} ({doc_len} Zeichen)\n")

# -----------------------------
# Poser une question
# -----------------------------
frage = input("Stell deine Frage zum Dokument: ").strip()

# -----------------------------
# Prompt structuré
# -----------------------------
prompt = f"""
Du bist ein hilfreicher Assistent. Beantworte die Frage NUR anhand des folgenden Dokuments.
Wenn die Antwort nicht im Dokument steht, sage: "Ich finde das nicht im Dokument."

Gib die Antwort im folgenden Format aus:

1) Kurze Antwort (1–3 Sätze)
2) Details (maximal 5 Bullet Points)
3) Textstelle(n): zitiere 1–3 kurze Ausschnitte aus dem Dokument
   (maximal 2 Sätze pro Ausschnitt)

DOKUMENT:
{doc_trimmed}

FRAGE:
{frage}
""".strip()

# -----------------------------
# Appel au modèle
# -----------------------------
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2
)

# -----------------------------
# Affichage de la réponse
# -----------------------------
print("\n--- 📌 Antwort (aus dem Dokument) ---")
print(response.choices[0].message.content)

if was_trimmed:
    print(
        f"\n[Hinweis] Das Dokument wurde auf {MAX_CHARS} Zeichen gekürzt, "
        "um Token-Kosten und Kontextlänge zu begrenzen."
    )
