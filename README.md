# Orpha rare disease lookup

## Overview

This product allows users to find rare disorders that match specific symptoms. 
It uses orpha database under the hood, to find my information please follow the 
link: http://www.orphadata.org/cgi-bin/index.php 

## Project structure

This project uses monorepo approach. 

```
+ backend/   (includes code related to django api project)
+ frontend/  (includes code related to react single-page application)
```

## Quick start

### Pre-requisites

- Python >= `3.7`;
- Node >= `v14.16`;
- Yarn.

### Run backend project

1. Cd to backend folder: `cd backend`;
2. Create virtual env: `python3 -m venv venv`;
3. Activate it: `. venv/bin/activate`;
4. Install dependencies: `pip install -r requirements_dev.txt`;
5. Run server: `python manage.py runserver`.

[More information on backend](backend/README.md)

### Run frontend project

1. Cd to frontend folder: `cd frontend`;
2. Configure your local env by copying sample file: `cp .env.sample .env.local`;
3. Install dependencies: `yarn`;
4. Run dev server: `yarn start`.

[More information on frontend](frontend/README.md)
