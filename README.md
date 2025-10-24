# Python Hexagonal Backend Template

## How to use it?
1. Clone the repository
```bash
    git clone git@github.com:facundocarballo/python-hexagonal-backend-template.git project-name
```
2. Go to the project folder
```bash
    cd project-name
```
3. Install all dependencies
```bash
    pip install -r requirements.txt
```
4. Create the `.env` file with these variables
```bash
    INTERNAL_PORT=8000
    EXTERNAL_PORT=8000
```
5. Build the project with docker
```bash
    docker compose up -d --build
```
