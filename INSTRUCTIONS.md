# Instructions pour le backend Django La Colombe

## 1. Installation des dépendances

Activez l'environnement virtuel et installez les dépendances:

```bash
cd H:\Projet\AReussi\backend_la_colombe
venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Créer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 3. Charger les données par défaut

Les images sont déjà copiées dans le dossier `media/`. Chargez les données avec:

```bash
python manage.py loaddata application/fixtures/initial_data_with_files.json
```

## 4. Créer un superutilisateur pour l'admin

```bash
python manage.py createsuperuser
```

## 5. Démarrer le serveur

```bash
python manage.py runserver
```

Le serveur démarrera sur http://127.0.0.1:8000

## 6. Accéder à l'admin

Allez sur http://127.0.0.1:8000/admin pour gérer les données (services, équipe, équipements, espaces)

## 7. Endpoints API disponibles

- GET /api/services/ - Liste des services
- GET /api/equipe/ - Liste de l'équipe
- GET /api/equipements/ - Liste des équipements
- GET /api/spaces/ - Liste des espaces

Les images sont accessibles via `/media/` (ex: http://127.0.0.1:8000/media/services/medicine_interne.jpg)

## 8. Configuration du frontend

Dans le fichier `.env.local` du frontend Next.js, ajoutez:

```
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

## Notes

- Les données par défaut sont les mêmes que celles actuellement dans le frontend statique
- Les images sont stockées localement dans le dossier `media/` et servies par Django
- Vous pouvez modifier les données via l'admin Django et elles seront automatiquement disponibles dans l'API
- CORS est configuré pour autoriser les requêtes depuis localhost:3000
- Pillow est requis pour gérer les images
