# Bargdoktor 🌿

Plant-care app prototype: scan a plant, find out what it is and what it suffers from, get watering and treatment advice, keep a garden with a care routine, and learn about endangered species.
Raqamli Avlod Qizlari · direction: Suniy intellekt (Artificial Intelligence).

## Features
- Camera scan, photo upload and a demo scan
- Library of 49 plants with search and categories
- My garden: care routine (this week / next week), notes
- Endangered plants (IUCN status)
- 5 languages (uz, ru, en, tr, zh), profile photo, location toggle, dark mode

## Run
Open `index.html` in a browser, or enable **GitHub Pages** (Settings → Pages → Branch: main) to get a public link. Pages uses https, so the camera works on a phone.

`build.py` regenerates `index.html` from `template.html` (plant list and SVG drawings are made in Python): `python build.py`

## Note on AI
The real AI recognition runs only inside Claude artifacts. Outside it the app uses the demo scan. In production, connect a plant-recognition API (Plant.id, Pl@ntNet) or an AI vision model.