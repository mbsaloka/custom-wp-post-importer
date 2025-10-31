def convert_github_url(url: str) -> str:
    """
    Mengubah URL GitHub file biasa menjadi URL raw GitHub.

    Contoh:
    https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Honeywell%20HPM%20Series.png
    → https://raw.githubusercontent.com/mbsaloka/custom-wp-post-importer/master/image/Honeywell%20HPM%20Series.png?raw=true
    """
    if not url.startswith("https://github.com/"):
        raise ValueError("URL tidak valid, harus diawali dengan 'https://github.com/'")

    # Hapus prefix "https://github.com/"
    url = url.replace("https://github.com/", "")
    # Pisahkan berdasarkan '/blob/'
    if "/blob/" not in url:
        raise ValueError("URL tidak mengandung '/blob/'")

    user_repo, path = url.split("/blob/", 1)
    raw_url = f"https://raw.githubusercontent.com/{user_repo}/{path}?raw=true"
    return raw_url


# Contoh penggunaan
url_awal = "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VLT%C2%AE%20Micro%20Drive%20FC-51.jpg"
url_raw = convert_github_url(url_awal)
print(url_raw)
