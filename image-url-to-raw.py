def convert_github_url(url: str) -> str:
    """
    Mengubah URL GitHub file biasa menjadi URL raw GitHub.

    Contoh:
    https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Honeywell%20HPM%20Series.png
    → https://raw.githubusercontent.com/mbsaloka/custom-wp-post-importer/master/image/Honeywell%20HPM%20Series.png?raw=true
    """
    if not url.startswith("https://github.com/"):
        raise ValueError(f"URL tidak valid: {url}")

    # Hapus prefix
    url = url.replace("https://github.com/", "")

    # Pisahkan berdasarkan '/blob/'
    if "/blob/" not in url:
        raise ValueError(f"URL tidak mengandung '/blob/': {url}")

    user_repo, path = url.split("/blob/", 1)
    raw_url = f"https://raw.githubusercontent.com/{user_repo}/{path}?raw=true"
    return raw_url


# ==== Contoh penggunaan dengan list URL ====

urls_awal = [
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Diaphragm%20Level%20Transmitter.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Differential%20Pressure%20Transmitter.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Direct%20Mount%20Pressure%20Transmitter.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Electromagnetic%20Flow%20Meter.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Metal%20Capacitive%20Pressure%20Sensor.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Oval%20Gear%20Flow%20Meter.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Radar%20Level%20Meter.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Remote%20Diaphragm%20Seal%20Transmitter.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/SP%202088%20Pressure%20Transmitter.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Ultrasonic%20Flow%20Meter.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Vortex%20Flow%20Meter.jpg",
]

urls_raw = []

for u in urls_awal:
    try:
        raw = convert_github_url(u)
        urls_raw.append(raw)
        print(raw)
    except ValueError as e:
        print(f"Error: {e}")

# Jika ingin menyimpannya ke file teks:
with open("converted_urls.txt", "w") as f:
    for raw_url in urls_raw:
        f.write(raw_url + "\n")

print("\nSemua URL berhasil dikonversi dan disimpan ke 'converted_urls.txt'")
