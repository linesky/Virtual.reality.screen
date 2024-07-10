import cv2
import numpy as np
from PIL import Image
global xxx
global yyy
global im
xxx=640-1
yyy=480-1
sets=0
im=None
def find_blue_cursor_position(frame):
    global xxx
    global yyy
    global im
    
    for yy in range(480):
        
            
        for xx in range(640):
            
            blue_channel,green_channel,red_channel=frame[yy,xx]
            if blue_channel>80 and green_channel<64 and red_channel<64:
                
                red_channel2,green_channel2,blue_channel2=im.getpixel((xx,yy))
                frame[yy,xx]=[blue_channel2,green_channel2,red_channel2]
                
            else:
                frame[yy,xx]=[blue_channel,green_channel,red_channel]
    return frame        

def main():
    global im
    cap = cv2.VideoCapture(0)
    imm=Image.open("mask.jpg")
    im=imm.convert('RGB')
    

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Espelhar a imagem
        frame = cv2.flip(frame, 1)
       
        # Procurar a posição do cursor azul
        frame = find_blue_cursor_position(frame)

        
        # Mostrar a imagem
        cv2.imshow('Augmented Reality - Blue Cursor Detection', frame)

        # Sair ao pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
