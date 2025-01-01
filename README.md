# Телеграм-бот курс валют

---

### Установка:

* Windows
    ```bash
    python -m venv venv
    ```
    ```bash
    venv\Scripts\activate
    ```

* Linux
    ```bash
    python3 -m venv venv
    ```
    ```bash
    source venv/bin/activate
    ```

```bash
pip install -r requirements.txt
```

### Запуск:

* Windows
    ```bash
    python main.py
    ```
* Linux
    ```bash
    python3 main.py
    ```

### Docker

* Разработка:
    ```bash
    docker compose watch
    ```

* Продакшн:
    ```bash
    docker compose up --build -d
    ```
