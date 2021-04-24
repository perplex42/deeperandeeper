
def receive_msg():
    number = '1234'
    message = input()
    return number, message

def send_msg(number, message):
    print('sending to number [{}]:{}'.format(number,message))