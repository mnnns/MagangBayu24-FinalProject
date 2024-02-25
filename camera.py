import cv2

# Inisialisasi objek untuk mengakses webcam
cap = cv2.VideoCapture(0)

# Periksa apakah kamera terbuka dengan benar
if not cap.isOpened():
    print("Tidak dapat membuka kamera.")
    exit()

while True:
    # Baca frame demi frame
    ret, frame = cap.read()

    # Periksa apakah frame berhasil dibaca
    if not ret:
        print("Tidak dapat menerima frame.")
        break

    # Tampilkan frame yang ditangkap
    cv2.imshow('Webcam', frame)

    # Cek apakah pengguna menekan tombol 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # Cek apakah pengguna menekan tombol 'p' untuk mengambil frame
    elif cv2.waitKey(1) & 0xFF == ord('p'):
        # Simpan frame yang diambil
        cv2.imwrite('frame.png', frame)
        print("Frame telah disimpan sebagai 'frame.png'")

# Tutup webcam dan jendela tampilan
cap.release()
cv2.destroyAllWindows()

