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
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/Gear%20Motors%20%E2%80%93%20VLT%C2%AE%20OneGearDrive.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/IC2-Micro.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VACON%C2%AE%20100%20FLOW.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VACON%C2%AE%20100%20INDUSTRIAL.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VACON%C2%AE%2020.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VACON%C2%AE%20NXP%20Air%20Cooled.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VLT%C2%AE%20AQUA%20Drive%20FC-202.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VLT%C2%AE%20Automation%20Drive%20FC-302.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VLT%C2%AE%20Brake%20Resistor%20MCE%20101.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VLT%C2%AE%20Common%20Mode%20Filter%20MCC%20105.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VLT%C2%AE%20HVAC%20Drive%20FC-102.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VLT%C2%AE%20Line%20Reactor%20MCC%20103.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VLT%C2%AE%20Midi%20Drive%20FC-280.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VLT%C2%AE%20Sine-Wave%20Filter%20MCC%20101.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VLT%C2%AE%20Soft%20Starter%20MCD%20202.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VLT%C2%AE%20Soft%20Starter%20MCD%20600.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VLT%C2%AE%20dUdt%20Filter%20MCC%20102.jpg",
  "https://github.com/mbsaloka/custom-wp-post-importer/blob/master/image/VLT%C2%AE%E2%80%AFSoft%E2%80%AFStart%E2%80%AFController%E2%80%AFMCD%E2%80%AF100.jpg",
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
