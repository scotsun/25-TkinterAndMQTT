"""
Using a fake robot as the receiver of messages.
"""

# TODO: 1. In mqtt_remote_method_calls, set LEGO_NUMBER at line 131
# to YOUR robot's number.

# TODO: 2. Copy your Tkinter/ttk ROBOT gui code from the previous session (m6).
# Then modify it so that pressing a button sends a message to a teammate
# of the form:
#   (for Forward)
#        ["forward", X, y]
#   where X and Y are from the entry box.
#
# Implement and test.
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time

def main():

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()  # only grid call that does NOT need a row and column

    left_speed_label = ttk.Label(main_frame, text="Left")

    left_speed_entry = ttk.Entry(main_frame, width=8)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)

    forward_button = ttk.Button(main_frame, text="Forward")

    left_speed_label.grid(row=0, column=0)
    left_speed_entry.grid(row=1, column=0)
    right_speed_label.grid(row=0, column=2)
    right_speed_entry.grid(row=1, column=2)
    forward_button.grid(row=2, column=1)

    root.bind('<Up>', lambda event: print("Forward key"))

    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    mqtt_client = com.MqttClient()
    mqtt_client.connect(name1, name2)

    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    forward_button['command'] = (lambda: foo(left_speed_entry, right_speed_entry, mqtt_client))


    root.mainloop()


def foo(left_speed_entry, right_speed_entry, mqtt_client):
        l_speed = left_speed_entry.get()
        r_speed = right_speed_entry.get()
        mqtt_client.send_message("forwardprint", [l_speed, r_speed])


main()