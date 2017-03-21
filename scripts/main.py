#import cv2
#from VideoManager import *
#As rodas estao invertidas
#As rodas estao invertidas
#As rodas estao invertidas
#As rodas estao invertidas
#As rodas estao invertidas
#As rodas estao invertidas
#As rodas estao invertidas
#As rodas estao invertidas
#As rodas estao invertidas
#As rodas estao invertidas
from Communication import *
from time import *
from World import *
from lista_marcacoes import *
import cProfile

world = World()
com = Communication('COM4')
fps = 0
time_start = time()

f = open('log.txt', 'w')

def main():
    fps = 0
    time_start = time()
    # Loads and initialize the camera
    #vm = VideoManager() #tirando controle de video
    rodando = True
    cobrando_penalidade = False

    # Loads and initialize serial communication between players and computer
    
    global com
    global world
    while (1):
        fps += 1
        t = time() - time_start
        if t > 1.0:
            print (fps, t, fps/t)
            fps = 0
            time_start = time()

        # Takes a frame from the camera, process it and creates a World instance with useful information
        #world = vm.process_frame(world) #tirando controle de video

        #Teste
        run((50,50),(55,50),(60,60),(65,60),(70,70),(75,70),(80,80), False)

        # NAO FACO IDEIA DO QUE ESTEJA ACONTECENDO
        if com.ser.inWaiting() >= 4:
            l1 = com.ser.read()
            l2 = com.ser.read()
            l3 = com.ser.read()
            l4 = com.ser.read()
            print 'recebido: ' + l1 + ' ' + str(ord(l2)) + ', ' + l3 + ' ' + str(ord(l4))

        #vai ser feito no c++
        """
        # limits of the soccer field
        vm.draw_circle(World.left_lower, 5, (255, 255, 255))
        vm.draw_circle(World.left_upper, 5, (255, 255, 255))
        vm.draw_circle(World.right_lower, 5, (255, 255, 255))
        vm.draw_circle(World.right_upper, 5, (255, 255, 255))

        vm.draw_circle(World.trave_left_lower, 5, (255, 255, 255))
        vm.draw_circle(World.trave_left_upper, 5, (255, 255, 255))
        """

        #Mudado para a funcao updateInfo()
        """
        # Controls each robot individually
        # msg = Message()
        for i in [0, 1, 2]:
            p = world.get_teammate(i)
            vr, vl = p.controle(world)
            if i == 0:
                vr = int(vr/1.5)
                vl = int(vl/1.5)
            elif i == 1:
                vr = int(vr/1.5)
                vl = int(vl/1.5)

            if cobrando_penalidade:
                cobrando_penalidade = False
                rodando = True
                com.set_speed_right('1', 200)
                com.set_speed_left('1', 200)
                com.stop('3')
                com.stop('4')
                sleep(0.25)


            # msg.add_new_param(vl, vr)
            if rodando:
                com.set_speed_right(p.get_id(), vr)
                com.set_speed_left(p.get_id(), vl)
            else:
                p = world.get_teammate(i)
                com.stop(p.get_id())
            # if i == 0:
            #     print str(i) + ' ' + 'enviado: ' + str(vl) + ' ' + str(vr)

            #if i == 0:
                #(aa, bb) = world.get_ball().predict_ball_method(p)
                #vm.draw_circle((int(aa), int(bb)), 5, (255, 0, 0))  # exibindo bola predita pelo robo 1 na tela
                #vm.draw_circle(p.chuta(world), 5, (255,255,255))
            if i == 2:
                (aa, bb) = p.defende(world)
                #vm.draw_circle((int(aa), int(bb)), 5, (78, 26, 200)) #tirando controle de video

        """
 
        # msg.generate_message()
        # com.send_message(msg)

        #vm.show()  #tirando controle de video

        # Checks for any event (necessary to cv2 to work)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            for i in [0, 1, 2]:
                p = world.get_teammate(i)
                com.stop(p.get_id())
            break
        elif chr(k) == 'b':
            print world.get_ball().getxy()
        elif k == 32:
            if rodando:
                rodando = False
            print rodando
        elif k == 112:
            cobrando_penalidade = True

    #cv2.destroyAllWindows()
"""
#Guilherme: Funcao chamada quando o c++ processar um novo frame
def run(p0_front_x, p0_front_y, p0_back_x, p0_back_y, p1_front_x, p1_front_y, p1_back_x, p1_back_y, p2_front_x, p2_front_y, p2_back_x, p2_back_y, pos_ball_x, pos_ball_y, cobrando_penalidade):
    global world
    global com
    global fps
    global time_start

    fps += 1
    t = time() - time_start
    if t > 1.0:
        print (fps, t, fps/t)
        fps = 0
        time_start = time()

    world.update((p0_front_x, p0_front_y), (p0_back_x, p0_back_y), (p1_front_x, p1_front_y), (p1_back_x, p1_back_y), (p2_front_x, p2_front_y), (p2_back_x, p2_back_y), (pos_ball_x, pos_ball_y))

    # Controls each robot individually
    # msg = Message()
    for i in [0, 1, 2]:
        p = world.get_teammate(i)
        vr, vl = p.controle(world)
        if i == 0:
            vr = int(vr/1.5)
            vl = int(vl/1.5)
        elif i == 1:
            vr = int(vr/1.5)
            vl = int(vl/1.5)

        #Bloco criado na competicao, modularizar ele...
        if cobrando_penalidade:
            cobrando_penalidade = False
            rodando = True
            com.set_speed_right('1', 200)
            com.set_speed_left('1', 200)
            com.stop('3')
            com.stop('4')
            sleep(0.25)

        com.set_speed_right(p.get_id(), vr)
        com.set_speed_left(p.get_id(), vl)

        #if i == 2:
        #    (aa, bb) = p.defende(world)

    return 50
"""
#Guilherme: Funcao chamada quando o c++ processar um novo frame
#Guilherme: Versao para atualizacao de jogador usando, x,y,angle
def run(p0_x, p0_y, p0_theta, p1_x, p1_y, p1_theta, p2_x, p2_y, p2_theta, pos_ball_x, pos_ball_y, cobrando_penalidade, pausado, op1_x, op1_y, op2_x, op2_y, op3_x, op3_y):
    global world
    global com
    global fps
    global time_start

    adiciona_ponto(int(pos_ball_x), int(pos_ball_y), 35, 100, 215, 'bola',int(pos_ball_x), int(pos_ball_y)) #laranja
    adiciona_ponto(int(p0_x),int(p0_y), 128, 200, 126, 'atacante',int(pos_ball_x), int(pos_ball_y)) # verde escuro
    adiciona_ponto(int(p1_x),int(p1_y), 170, 0, 255, 'zagueiro',int(pos_ball_x), int(pos_ball_y)) # rosa
    adiciona_ponto(int(p2_x),int(p2_y), 0, 80, 0, 'goleiro',int(pos_ball_x), int(pos_ball_y)) # verde claro
    #adiciona_ponto(int(op1_x),int(op1_y), 0, 0, 255, 'op1',int(op1_x),int(op1_y)) # vermelho
    #adiciona_ponto(int(op2_x),int(op2_y), 0, 0, 255, 'op2',int(op2_x),int(op2_y)) # vermelho
    #adiciona_ponto(int(op3_x),int(op3_y), 0, 0, 255, 'op3',int(op3_x),int(op3_y)) # vermelho

    """
    print (p0_x, p0_y, p0_theta, p1_x, p1_y, p1_theta, p2_x, p2_y, p2_theta, pos_ball_x, pos_ball_y, cobrando_penalidade, pausado)
    """
    #sleep(2);
    #limpa_lista()

    world.update(p0_x, p0_y, p0_theta, p1_x, p1_y, p1_theta, p2_x, p2_y, p2_theta, (pos_ball_x, pos_ball_y))
    
    # Controls each robot individually
    # msg = Message()
    for i in [0,1,2]:  # [0] = atk , [1] defesa e [2] goleiro
        p = world.get_teammate(i)
        vr, vl = p.controle(world) #xt, yt = posicao retornada pela funcao chuta
        """
        if i == 0:
            vr = int(vr/1.5)
            vl = int(vl/1.5)
        elif i == 1:
            vr = int(vr/1.5)
            vl = int(vl/1.5)
        """

        #Bloco criado na competicao, modularizar ele...
        #cobrando_penalidade = True;
        if not(pausado):
            if cobrando_penalidade == 1:
                print "penalty ataque"
                cobrando_penalidade = False
                rodando = True
                start_time = time()
                while(time() - start_time < 1.5):
                    com.set_pwm_right('3', 95)
                    com.set_pwm_left('3', 250)
                    com.stop('1')
                    com.stop('2')
                    sleep(0.3)
                """
                com.set_pwm_right('3', 95)
                com.set_pwm_left('3', 250)
                com.stop('1')
                com.stop('2')
                com.set_pwm_right('3', 95)
                com.set_pwm_left('3', 250)
                com.stop('1')
                com.stop('2')

                sleep(1.5)"""

            if cobrando_penalidade == 2:
                print "penalty defesa"
                cobrando_penalidade = False
                rodando = True
                com.set_pwm_right('2', 80)
                com.set_pwm_left('2', 250)
                com.stop('1')
                com.stop('3')
                com.set_pwm_right('2', 80)
                com.set_pwm_left('2', 250)
                com.stop('1')
                com.stop('3')
                com.set_pwm_right('2', 80)
                com.set_pwm_left('2', 250)
                com.stop('1')
                com.stop('3')
                sleep(1.5)

            com.set_speed_right(p.get_id(), vr)
            com.set_speed_left(p.get_id(), vl)
        

        #if i == 2:
        #    (aa, bb) = p.defende(world)
        #f.close()

    #return (aa,bb)
    
    #return [(int(xt), int(yt) ,0,0,255), (p0_x,p0_y,255,0,0), (pos_ball_x, pos_ball_y,0,255,0)]

    #adiciona_ponto(int(p1_x),int(p1_y), 255, 255, 0, 'jogador1')
    
    #adiciona_ponto(int(p0_x),int(p0_y), 255, 0, 0, 'jogador1')
    #adiciona_ponto(int(world.trave_left_upper[0]), int(world.trave_left_upper[1]), 0, 100, 200, 'trave')

    ls = pega_lista()
    #print ls
    limpa_lista()
    return ls


def pause():

    global world
    global com

    for i in [0, 1, 2]:
        p = world.get_teammate(i)
        com.stop(p.get_id())

def updateBorders(fieldRight, fieldLeft, fieldTop, fieldBottom):
    global world
   
    world.updateField(fieldRight, fieldLeft, fieldTop, fieldBottom)


if __name__ == '__main__':
    # cProfile.run('main()')
    main()