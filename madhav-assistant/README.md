# Madhav Personal Assistant

Madhav is an advanced personal assistant system inspired by Iron Man's JARVIS. It leverages the Mistral 7B instruction-tuned model and integrates self-learning, self-healing, self-upgrading, and multimedia training capabilities.

## Features

- AI model integration with Mistral 7B int4 via OpenRouter API
- Bilingual Hindi-English support with domain-specific tuning
- Self ethical hacking learning and security monitoring
- Self code generation, testing, and deployment
- Multimedia processing with FFmpeg, OpenCV, and Stable Diffusion
- Dockerized environment for easy deployment
- GUI launcher for user interaction and configuration
- Phase-wise development and modular architecture

## Folder Structure

```
madhav-assistant/
├── ai-model/
├── security/
├── self_development/
├── multimedia_training/
├── gui_launcher/
├── docker/
├── config/
├── tests/
├── requirements.txt
├── README.md
└── setup.py
```

## Setup Instructions

1. Provide API keys for OpenRouter and Stability AI in `config/settings.yaml`.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the GUI launcher with `python gui_launcher/main.py`.
4. Use Docker for containerized deployment (`docker-compose up`).

## API Keys

- OpenRouter API key
- Stability AI API key

## Contact

For support or contributions, please contact the maintainer.
