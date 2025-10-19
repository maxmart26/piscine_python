# 0_starting/Makefile
DC  := docker compose

EXO ?= ex00
PY  ?=
ARGS ?=

.PHONY: build run sh test fmt lint down clean reinstall help

help:
	@echo "Targets:"
	@echo "  make build                          - Build l'image Docker"
	@echo "  make run EXO=ex00 PY=Hello.py       - Exécute un exo"
	@echo "  make sh EXO=ex00                    - Shell dans le dossier de l'exo"
	@echo "  make test                           - Lance pytest (si présent)"
	@echo "  make fmt | make lint                - Format/Lint"
	@echo "  make down | make clean              - Stop/Nettoyage"

build:
	$(DC) build

_detect_py:
	@if [ -z "$(PY)" ]; then \
		set -e; \
		PY_AUTO=$$(ls -1 $(EXO)/*.py 2>/dev/null | head -n1); \
		if [ -z "$$PY_AUTO" ]; then \
			echo "Aucun fichier .py trouvé dans $(EXO)"; exit 2; \
		fi; \
		echo "PY détecté: $$(basename $$PY_AUTO)"; \
		$(MAKE) _run PY=$$(basename $$PY_AUTO) EXO=$(EXO) ARGS='$(ARGS)'; \
	else \
		$(MAKE) _run; \
	fi

_run:
	$(DC) run --rm app bash -lc "cd $(EXO) && python $(PY) $(ARGS)"

run: _detect_py

sh:
	$(DC) run --rm app bash -lc "cd $(EXO) && exec bash"

test:
	$(DC) run --rm app bash -lc "pytest -q || true"

fmt:
	$(DC) run --rm app bash -lc "black . && isort ."

lint:
	$(DC) run --rm app bash -lc "flake8 ."

down:
	$(DC) down

clean:
	$(DC) down -v

# --- Raccourcis par exo ---
ex00:
	$(MAKE) run EXO=ex00 PY=Hello.py

ex01:
	$(MAKE) run EXO=ex01 PY=format_ft_time.py ARGS="$(ARGS)"

ex02:
	$(MAKE) run EXO=ex02 PY=find_ft_type.py ARGS="$(ARGS)"

ex03:
	$(MAKE) run EXO=ex03 PY=NULL_not_found.py ARGS="$(ARGS)"

ex04:
	$(MAKE) run EXO=ex04 PY=whatis.py ARGS="$(ARGS)"

ex05:
	$(MAKE) run EXO=ex05 PY=building.py ARGS="$(ARGS)"

ex06:
	$(MAKE) run EXO=ex06 PY=filterstring.py ARGS="$(ARGS)"

# Shell rapide dans un exo
sh-%:
	$(MAKE) sh EXO=$*


# --- Vérification PEP8 globale ---
check:
	@echo "🔎 Vérification PEP8 avec flake8 sur tous les fichiers Python..."
	$(DC) run --rm app bash -lc "flake8 || true"


reinstall:
	$(DC) run --rm app pip install --no-cache-dir -r /app/requirements.txt
