import keyboard


def e(q):
    print(q.name)

keyboard.hook(e)
keyboard.wait()