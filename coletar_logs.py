import csv
import datetime

LOG_FILE = "auth.log"
CSV_OUTPUT = "eventos_seguranca.csv"

def coletar_login_invalidos():
    eventos = []
    try:
        with open(LOG_FILE, "r") as log:
            for linha in log:
                if "Failed password" in linha or "authentication failure" in linha:
                    eventos.append(linha.strip())

        with open(CSV_OUTPUT, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Data e Hora", "Evento"])
            for evento in eventos:
                data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([data, evento])

        print(f"[✓] {len(eventos)} eventos coletados e salvos em '{CSV_OUTPUT}'")
    except FileNotFoundError:
        print("[✗] Arquivo de log não encontrado.")
    except Exception as e:
        print(f"[✗] Erro: {e}")

if __name__ == "__main__":
    coletar_login_invalidos()
