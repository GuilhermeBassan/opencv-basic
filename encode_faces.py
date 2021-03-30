from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os



def main():

    # Processa os argumentos
    ap=argparse.ArgumentParser()
    ap.add_argument("-i","--dataset",required=True,help="Caminho do diretório de imagens")
    ap.add_argument("-e","--encodings",required=True,help="Caminho para base de dados de encoding facial")
    ap.add_argument("-d","--detection-method",type=str,default="cnn",help="Método de detecção (hog ou cnn)")
    args=vars(ap.parse_args())

    # Aquisita os diretórios das imagens no dataset
    print("[INFO] Quantificando faces...")
    image_paths=list(paths.list_images(args["dataset"]))

    # Inicializa a lista de nomes e encodings conhecidos
    known_encodings=[]
    known_names=[]

    # Itera as imagens
    for(i, image_path) in enumerate(image_paths):
        # Extrai o nome da pessoa do caminho
        print("[INFO] Processando imagem {}/{}".format(i+1,len(image_paths)))
        name=image_path.split(os.path.sep)[-2]

        # Carrega imagem e converte do padrão opencv (BGR) para 
        # o padrão dlib (RGB)
        image=cv2.imread(image_path)
        rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

        # Detecta as coordenadas (x,y) das caixas de contorno de 
        # cada uma das faces na imagem
        boxes=face_recognition.face_locations(rgb,model=args["detection_method"])

        # Calcula o encoding da face
        encodings=face_recognition.face_encodings(rgb,boxes)

        # Itera os encodings
        for encoding in encodings:
            # Adiciona o encoding e o nome para a coleção de 
            # nomes e encodings conhecidos
            known_encodings.append(encoding)
            known_names.append(name)

        # Exporta os encodings e nomes para o disco
        print("[INFO] Serializando encodings...")
        data={"encodings":known_encodings,"names":known_names}
        f=open(args["encodings"],"wb")
        f.write(pickle.dumps(data))
        f.close()



if __name__=="__main__":
    main()