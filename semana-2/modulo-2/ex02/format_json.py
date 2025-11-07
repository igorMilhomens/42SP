import httpx

if __name__ == "__main__":
    result = httpx.get(
        "https://assets.breatheco.de/apis/fake/sample/project1.php"
    ).json()
    print(f"Projeto: '{result['name']}', Imagem: '{result['images'][0]}'")
