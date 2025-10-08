Cette documentation contient toutes les étapes et les explications sur comment créer un serveur MCP personnalisé et le rendre accessible via ChatGPT.
### Disclaimer
Le serveur MCP sera construit avec le SDK Python[^1] prévu à cet effet, ceci n'a pas pour but d'expliquer et/ou de montrer tout ce dont le SDK est capable. Seules les choses absolument nécessaires au déploiement d'un serveur custom avec ChatGPT seront montrées.

---

## Prérequis
- Le [SDK](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#cors-configuration-for-browser-based-clients) python doit être installer sur la machine ou un venv.
- Un VPS ou tout autre set-up permettant à ChatGpt de communiquer avec votre machine doit être mis en place.
