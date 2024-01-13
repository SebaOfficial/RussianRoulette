# Russian Roulette

## ❔ Installation & Usage
* Using `git`:
    ```bash
    git clone https://github.com/SebaOfficial/RussianRoulette.git
    ```

    - Run:
        ```bash
        cd RussianRoulette/ && python3 -m russian_roulette --safe
        ```

* Using `docker`:
    ```bash
    docker pull sebaofficial/russian-roulette:latest
    ```

    - Run:
        ```bash
        docker run -it sebaofficial/russian-roulette:latest
        ```

## 🛠 Compile
You can compile you own version with:
```bash
python -m nuitka --onefile russian_roulette/__main__.py --output-dir=build --output-filename=russian_roulette
```

## ⚖️ License
This project is under the [MIT License](https://github.com/SebaOfficial/RussianRoulette/blob/main/LICENSE).
