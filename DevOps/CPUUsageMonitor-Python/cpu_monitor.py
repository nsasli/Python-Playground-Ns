import psutil
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Fungsi untuk mengirim email
def kirim_email(subject, body, to_email, attachment=None):
    smtp_server = 'smtp.example.com'  # Ganti dengan server SMTP Anda
    smtp_port = 587  # Port SMTP yang digunakan
    smtp_username = 'your_username'  # Ganti dengan username SMTP Anda
    smtp_password = 'your_password'  # Ganti dengan password SMTP Anda

    msg = MIMEMultipart()
    msg['From'] = 'your_email@example.com'  # Ganti dengan alamat email pengirim
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if attachment:
        with open(attachment, 'rb') as file:
            part = MIMEApplication(file.read(), Name="server_log.txt")
        part['Content-Disposition'] = f'attachment; filename="{attachment}"'
        msg.attach(part)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print("Email terkirim")
    except Exception as e:
        print("Gagal mengirim email:", str(e))

# Fungsi untuk memeriksa pemakaian CPU
def cek_pemakaian_cpu(threshold):
    while True:
        pemakaian_cpu = psutil.cpu_percent(interval=5)
        if pemakaian_cpu > threshold:
            subjek = "Pemberitahuan: Pemakaian CPU Tinggi"
            pesan = f"Pemakaian CPU mencapai {pemakaian_cpu}%"
            kirim_email(subjek, pesan, 'admin@example.com', 'server_log.txt')

# Fungsi utama
def main():
    batas_pemakaian_cpu = 90  # Ganti dengan batas pemakaian CPU Anda
    cek_pemakaian_cpu(batas_pemakaian_cpu)

if __name__ == "__main__":
    main()
