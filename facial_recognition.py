#https://www.pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/

from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import argparse
import imutils
import pickle
import cv2



def main():

    # Processa os argumentos
    ap=argparse.ArgumentParser()
    ap.add_argument("-c","--cascade",required=True,help="Caminho para o arquivo face cascades")
    ap.add_argument("-e","--encodings",required=True,help="Caminho para banco de faces serializadas")
    args=vars(ap.parse_args())

    # Carrega a lista de rostos conhecidos e o arquivo de 
    # haar cascades
    print("[INFO] Carregando encodings e detetor de faces...")
    data=pickle.loads(open(args["encodings"],"rb").read())
    detector=cv2.CascadeClassifier(cv2.data.haarcascades +args["cascade"])
    
    # Inicia a captura de vídeo da câmera
    print("[INFO] Iniciando transmissão...")
    vs=VideoStream(src=0).start()
    
    # Inicia o contador de quadros
    fps=FPS().start()

    # Itera os quadros da captura
    while True:

        # Redimensiona o quadro para melhorar a 
        # velocidade de processamento
        frame=vs.read()
        frame=imutils.resize(frame,width=500)

        # Converte o quadro de BGR para escala de cinza
        # para a detecção de faces e de BGR para RGB para
        # o reconhecimento facial
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        # Detecta a face no quadro em escala de cinza
        rects=detector.detectMultiScale(
            gray,               # Quadro original
            scaleFactor=1.1,    # Especifica o quanto a imagem é reduzida
            minNeighbors=5,     # Quantos "vizinhos" cada candidato deve ter
            minSize=(30,30)     # Tamanho mínimo do objeto detectado
        )

        # OpenCV retorna as coordenadas das caixas de 
        # contorno em (x,y,w,h), mas a ordem necessária é
        # (topo, direita, fundo, esquerda)
        boxes=[(y,x+w,y+h,x) for (x,y,w,h) in rects]

        # Calcula o encoding para cada rosto na caixa
        # de contorno
        encodings=face_recognition.face_encodings(rgb,boxes)
        names=[]

        # Itera os encodings encontrados no frame
        for encoding in encodings:

            # Tenta relacionar com algum dos encodings existentes
            matches=face_recognition.compare_faces(data["encodings"],encoding)
            name="Desconhecido"

            # Verifica se um semelhante foi encontrado
            if True in matches:
                # Encontra os indices de todas as faces detectadas e 
                # inicializa o dicionário para contar o total de vezes 
                # que cada face foi detectada
                matched_indexes=[i for (i,b) in enumerate(matches) if b]
                counts={}

                # Itera sobre os índices detectados e mantém a contagem 
                # para cada face detectada
                for i in matched_indexes:
                    name=data["names"][i]
                    counts[name]=counts.get(name,0)+1

                # Determina qual é o rosto detectado com base no número
                # de votos (se houver empate o primeiro da lista será vencedor)
                name=max(counts,key=counts.get)

            # Atualiza lista de nomes
            names.append(name)

            # Itera os rostos reconhecidos
            for ((top,right,bottom,left),name) in zip(boxes,names):

                # Desenha o retângulo e escreve o nome na imagem
                cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),2)
                y=top-15 if top-15>15 else top+15
                cv2.putText(frame,name,(left,y),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,255,0),2)

        # Mostra a imagem na tela
        cv2.imshow("Frame",frame)

        # Se a tecla 'q' for pressionada, abandona a captura
        key=cv2.waitKey(1)&0xFF
        if key==ord('q'):
            break

        # Atualiza o contador de quadros
        fps.update()

    # Para o contador de quadros e 
    # mostra o resultado
    fps.stop()
    print("[INFO] Tempo decorrido: {:.2f}".format(fps.elapsed()))
    print("[INFO] Taxa de quadros aproximada: {:.2f}".format(fps.fps()))

    # Encerra as janelas e a captura
    cv2.destroyAllWindows()
    vs.stop()
    
if __name__=="__main__":
    main()