import cv2

# Inicializar la cámara web
cap = cv2.VideoCapture(0)

# Cargar el clasificador de cascada de Haar para detectar rostros
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    # Leer un fotograma de la cámara web
    ret, frame = cap.read()

    # Convertir el fotograma a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en el fotograma
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Dibujar un rectángulo alrededor de cada rostro detectado
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)

    # Mostrar el fotograma con los rostros resaltados
    cv2.imshow("Faces", frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
