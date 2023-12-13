def followline2():
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 50)
    else:
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
            maqueen.motor_stop(maqueen.Motors.M1)
            if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
                maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
                maqueen.motor_stop(maqueen.Motors.M1)
        else:
            if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
                maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
                maqueen.motor_stop(maqueen.Motors.M2)
                if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
                    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
                    maqueen.motor_stop(maqueen.Motors.M2)
                if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
                    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
                else:
                    maqueen.motor_stop(maqueen.Motors.M2)


# --- main program ---
basic.show_number(maqueen.ultrasonic(PingUnit.CENTIMETERS))
strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
doorgaan = True

while doorgaan:
    followline2()