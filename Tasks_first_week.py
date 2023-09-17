# Данный пример предназначен для тестирования моторов на аппарате!  

# В данном примере мы подаем тягу на 4 мотора продолжительностью в 5 секунд. 


import pymurapi as mur
import time


auv = mur.mur_init()

if __name__ == '__main__':
    left_motor = 0
    right_motor = 1
    left_up_motor = 2
    right_up_motor = 3
    
    depth_max = 2.5
    depth_min = 1.3
    
    def stop():
        auv.set_motor_power(left_motor, 0)
        auv.set_motor_power(right_motor, 0)
        auv.set_motor_power(left_up_motor, 0)
        auv.set_motor_power(right_up_motor, 0)
    
    def forward(speed):
        auv.set_motor_power(left_motor, speed)
        auv.set_motor_power(right_motor, speed)
        time.sleep(5)
        stop()
        
    def change_depth(speed):
        auv.set_motor_power(left_up_motor, speed)
        auv.set_motor_power(right_up_motor, speed)
        
        
        
        
        
        
    '''
    #Task 1
    # Движение вперёд 
    
    forward(30)
    
    yaw = auv.get_yaw()
    yaw_90_c = yaw + 78.5  #c - clockwise, cc - counterclockwise
    yaw_90_cc = yaw - 78.5
    
    #Поворот
    while(yaw < yaw_90_c):
        auv.set_motor_power(left_motor, 10)
        yaw = auv.get_yaw()
        time.sleep(0.5)
    else:
       stop() 
       
    # Движение вперёд    
    forward(30)
    
    #diving
    depth = auv.get_depth()
    
    while(depth < depth_max):
        change_depth(-20)
        depth = auv.get_depth()
        time.sleep(0.2)
    else:
        stop()
    
    time.sleep(3)
    
    #ascent
    while(depth > depth_min):
        change_depth(20)
        depth = auv.get_depth()
        time.sleep(0.2)
    else:
        stop()
    
        
    stop()    
    '''
    #--------------------------------------------------------------------------------------------------
    '''
    
    #Task 2
    depth = auv.get_depth()
    
    
    # погружение на половину
    while(depth < 2):
        change_depth(-10)
        depth = auv.get_depth()
        time.sleep(0.2)
    else:
        stop()
        
    # Движение вперёд    
    forward(30)
    
    # Всплытие
    depth = auv.get_depth()
    while(depth > depth_min):
        change_depth(20)
        depth = auv.get_depth()
        time.sleep(0.2)
    else:
        stop()
    
    time.sleep(3)
    
    # Погружение с двжением
    while(depth < depth_max):
        change_depth(-20)
        forward(30)
        depth = auv.get_depth()
        time.sleep(0.2)
    else:
        stop()
        
        
    stop()
    '''
    #--------------------------------------------------------------------------------------------------
    '''
    
    #Task 3
    #Открываем файл для записи данных
    
    fd = open("C:\Python_Lodka\First Tasks\depth_data.txt", "w")
    
     # Погружение с двжением
    
    depth = auv.get_depth()
    while(depth < depth_max):
        change_depth(-20)
        forward(30)
        print (depth)
        fd.write(str(depth))
        fd.write('\n')
        depth = auv.get_depth()
        time.sleep(0.3)
    
    stop()    
    time.sleep(2)
    fd.close()
    
    '''
    
    #--------------------------------------------------------------------------------------------------

    '''
    #Task 4
    
    #Открываем файл для записи данных
    fy = open("C:\Python_Lodka\First Tasks\yaw_data.txt", "w")
    
    
    #Движение по кругу
    yaw = auv.get_yaw()
    c = true
    
    while(c == true):
        auv.set_motor_power(left_motor, 21.99)
        auv.set_motor_power(right_motor, 12.567)
        print (yaw)
        fy.write(str(yaw))
        fy.write('\n')
        time.sleep(0.3)
        yaw = auv.get_yaw()
        if ((yaw < -3) & (yaw > -10)):
            break
    stop()
    time.sleep(2)
    fy.close()
    
    '''
    
    #--------------------------------------------------------------------------------------------------
    
    '''
    #Task 5/6 Движение по воронке
    
    #Открываем файлы для записи данных
    fd = open("C:\Python_Lodka\First Tasks\depth_data.txt", "w")
    fy = open("C:\Python_Lodka\First Tasks\yaw_data.txt", "w")
    
    lm = 60
    rm = 25
    
    yaw = auv.get_yaw()
    depth = auv.get_depth()
    
    
    while((depth < depth_max) and (lm > 0 or rm > 0)):
        auv.set_motor_power(left_motor, lm)
        auv.set_motor_power(right_motor, rm)
        auv.set_motor_power(left_up_motor, -5)
        auv.set_motor_power(right_up_motor, -5)
        fy.write(str(yaw))
        fy.write('\n')
        fd.write(str(depth))
        fd.write('\n')
        lm = lm - 0.5
        rm = rm - 0.43
        yaw = auv.get_yaw()
        depth = auv.get_depth()
        time.sleep(0.3)
    stop()   
    time.sleep(2)
    
    fd.close()
    fy.close()
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    
