# Russian Roulette
Are you an adrenaline junkie and you want to risk it all?
Now you can play with everything you've saved on you home directory (e.g. `/home/username/` or `:\Users\username\`).

## ❔ Installation & Usage
* Using `git`:
    ```bash
    git clone https://github.com/SebaOfficial/RussianRoulette.git
    ```

    - Run:
        ```bash
        cd RussianRoulette/ && python3 -m russian_roulette --safe
        ```
        Note: the `--safe` flag doesn't remove your home directory.

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
