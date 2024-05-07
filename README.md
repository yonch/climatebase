# Getting credentials

- Get an API key on [https://console.groq.com/playground]. Write it to a file `.env` as:
```
export GROQ_API_KEY=your-api-key
```


# To install

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install pip-tools
pip-sync
```

# Process

1. Run `./fetch.sh`, it creates jobs_data.json

2. Run `source .env` to get the API key into the environment variables


# To update packages in `requirements.in`

```bash
pip-compile --upgrade -v
```
