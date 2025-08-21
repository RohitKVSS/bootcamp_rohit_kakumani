api_key_present = get_key("API_KEY") is not None
data_dir_env = get_key("DATA_DIR", str(DATA_DIR))
print("API_KEY present:", api_key_present)
print("DATA_DIR from env:", data_dir_env)

# Ensure data directory exists (non-destructive)
Path(data_dir_env).mkdir(parents=True, exist_ok=True)
print("Ensured data directory exists.")