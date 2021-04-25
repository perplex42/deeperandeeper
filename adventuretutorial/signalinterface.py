
def receive_msg():
    number = input("number:")
    message = input("message:")
    return number, message

def send_msg(number, message):
    print('sending to number [{}]:{}'.format(number,message))
