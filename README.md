# 🧠 Piscine Python – 42 Paris

> Collection d’exercices réalisés durant la **Piscine Python** de l’école 42.  
> Tout le projet est encapsulé dans un environnement **Docker** léger et reproductible, pour garantir un comportement identique sur toutes les machines 🐳.

---

## 🚀 Structure du projet

```
0_starting/
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── requirements.txt
├── ex00/
│   └── Hello.py
├── ex01/
│   └── format_ft_time.py
├── ex02/
│   └── find_ft_type.py
├── ex03/
│   └── NULL_not_found.py
├── ex04/
│   └── whatis.py
├── ex05/
│   └── building.py
└── ex06/
    ├── filterstring.py
    └── ft_filter.py
```

Chaque dossier `ex0X` contient un exercice indépendant.

---

## 🐳 Environnement Docker

### 🔧 Build de l’image
```bash
make build
```

### ▶️ Lancer un exercice
```bash
make run EXO=ex00 PY=Hello.py
```

ou plus simplement avec les raccourcis :
```bash
make ex00
make ex01 ARGS="2025-10-19"
make ex06
```

### 💬 Ouvrir un shell dans le conteneur
```bash
make sh EXO=ex03
```

---

## 🧹 Qualité & tests

### Vérifier la conformité PEP8
```bash
make check
```

Exemple de sortie :
```
./ex04/whatis.py:4:1: E302 expected 2 blank lines, found 1
./ex02/find_ft_type.py:2:8: E721 do not compare types, use isinstance()
```

### Formatter automatiquement
```bash
make fmt
```

### Linter (analyse stricte)
```bash
make lint
```

---

## 📦 Dépendances (requirements.txt)

```text
pytest
flake8
black
isort
```

Tu peux les réinstaller à tout moment avec :
```bash
make reinstall
```

---

## 🧠 Notes pédagogiques

- Tous les scripts respectent les **bonnes pratiques Python (PEP8)**.
- L’environnement est totalement isolé via **Docker**, aucun besoin de `sudo` local.
- Le **Makefile** permet d’exécuter, tester et formatter en une seule commande.
- Le projet est compatible avec **Mac, Linux et les machines 42**.

---

## 🧰 Commandes utiles

| Commande | Description |
|-----------|--------------|
| `make build` | Build l’image Docker |
| `make run EXO=ex00 PY=Hello.py` | Exécute un exercice |
| `make ex00` | Raccourci pratique |
| `make sh EXO=ex03` | Ouvre un shell dans le dossier ex03 |
| `make check` | Vérifie la conformité PEP8 |
| `make fmt` | Formatte tout le code (black + isort) |
| `make lint` | Analyse flake8 stricte |
| `make reinstall` | Réinstalle les dépendances Python |
| `make clean` | Supprime les conteneurs et volumes |
| `make down` | Stoppe les services Docker |

---

## 🧾 Exemple de sortie

```
$ make ex00
['Hello', 'World!']
('Hello', 'France!')
{'Hello', 'Paris!'}
{'Hello': '42Paris!'}
```

---

## 🧑‍💻 Auteur

**Maxime Torgue** *(alias chou)*  
📫 [torgue.maxime@gmail.com](mailto:torgue.maxime@gmail.com)  
🌐 [mtorgue.fr](https://mtorgue.fr)

---

### ❤️ Remerciements
Un grand merci à l’école **42 Paris** pour la pédagogie et l’émulation,  
et à toi, lecteur, pour avoir pris le temps de parcourir ce repo ✨

---

> 🐍 *Code clean, linted & containerized — comme à la maison chez Python.*
