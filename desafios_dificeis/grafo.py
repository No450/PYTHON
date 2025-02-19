import requests

def buscar_produtos(termo, chave_api, id_cx):
    url = "https://www.googleapis.com/customsearch/v1"
    parametros = {
        "q": termo,
        "key": chave_api,
        "cx": id_cx,
    }

    resposta = requests.get(url, params=parametros)

    if resposta.status_code == 200:
        resultados = resposta.json().get("items", [])
        if resultados:
            print(f"Resultados para '{termo}':\n")
            for idx, item in enumerate(resultados, start=1):
                titulo = item.get("title")
                link = item.get("link")
                snippet = item.get("snippet")
                print(f"{idx}. {titulo}\nLink: {link}\nDescrição: {snippet}\n")
        else:
            print("Nenhum resultado encontrado.")
    else:
        print("Erro ao buscar produtos:", resposta.status_code, resposta.text)


CHAVE_API = "AIzaSyAOcYmj79s1gGStfJlrVn-D48CdhGfEFVo"
ID_CX = "811ca4c7d464e4f5f"

termo_de_busca = "Sensor ultrassonico "
buscar_produtos(termo_de_busca, CHAVE_API, ID_CX)