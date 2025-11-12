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
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Fluke%20Calibration%20Tools.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Fluke%20Clamp%20Meter.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Fluke%20Digital%20Multimeter.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Fluke%20Environmental%20Testers.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Fluke%20Insulation%20Tester.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Fluke%20Power%20Quality%20Analyzer.jpg",
    "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Fluke%20Thermal%20Imager.jpg",
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
