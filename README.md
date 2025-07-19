# AI Dungeon Master

🚧 ***This project is in early development.
Contributions and suggestions are welcome. Follow along as I build my custom AI-powered D&D DM assistant.***

An open-source AI-powered Dungeon Master assistant for D&D 5e campaigns. Designed for solo or small-group play with persistent memory and optional voice/image features.

![MIT License](https://img.shields.io/badge/license-MIT-green.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/Dokt-R/ai-dm)
![Last Commit](https://img.shields.io/github/last-commit/Dokt-R/ai-dm)

---

## 🧙‍♂️ Overview

This project is an AI Dungeon Master simulator that assists in running Dungeons & Dragons 5e games. It features dice rolling, ability checks, config-driven characters and monsters, and is designed to grow into a full AI-powered tabletop RPG experience.

---

## 🚀 Features

- 🎲 (Planned) Options for physical/digital dice rolling options (`d20`, `4d6`, etc.)
- 🤹 (Planned) Handles advantage/disadvantage
- 🧾 (Planned) Options to run physical/config file support for characters and monsters
- ⚙️ (Planned) Modular and expandable design
- 🧠 (Planned) GPT-powered narration and responses
- 🔊 (Planned) Voice acting via ElevenLabs API
- 🖼️ (Planned) Image generation via OpenAI/Sora

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.10+
- A virtual environment (recommended)
- Optional: OpenAI API key, ElevenLabs API key

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Create a `.env` file

```bash
OPENAI_API_KEY=your_openai_key
```

### Run the CLI

```bash
python cli.py
```

---

## 🗺️ Roadmap

- [ ] Dice roller module
- [ ] Command parser for CLI inputs
- [ ] Ability checks (with advantage/disadvantage)
- [ ] Character/monster data from config files
- [ ] GPT integration for storytelling
- [ ] Voice + image generation
- [ ] Save/load session states
- [ ] Web UI (optional)

---

## 📦 Project Structure

```
.
├── cli.py
├── config/
├── core/
├── tests/
├── venv/
├── .env
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or add. Contributions to CLI tools, game logic, AI narration, and voice/image integration are especially welcome.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

