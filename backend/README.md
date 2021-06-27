# Orpha lookup backend

## Overview

This folder contains backend part of the product. It uses `django` as a main framework library
and `rest_framework` as a main api library under the hood.

## Project structure

Project structure follows the general Django approach with a few differences:

```
+ orpha_lookup/         (the main project folder)
+   api/                (api-related code: urls, views, etc.)
+   apps/               (business logic splitted into django apps)
+   core/               (app-independent code: middlewares, auth providers, etc.)
+   settings/           (project configuration splitted into small files)
+ var/                  (contains downloaded data)
+ db.sqlite3            (sqlite database with sample data)
+ requirements.txt      (requirements file for using on prod environment)
+ requirements_dev.txt  (requirements file for using on dev environments)
+ tox.ini               (configuration for an automation tool)
```

## Applications

This project contains 2 django applications.

### data_parser

This application enables data synchronization pipeline, including: data downloading, data parsing, and data persisting.
This application exposes 2 CLI commands that allows to initiate downloading and importing process:
- `download_data`
- `import_data`

### orpha

This application is a heart of the project. It contains essential data models, admin views, and data fetching logic.
The data itself exposed by api that is located in the corresponding folder. 
