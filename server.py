import datetime
import socket


def change_data_of_file(file_path):
    """
    Gets file and changes the date and day of week and returns the contents as a string
    """
    today = datetime.date.today()
    day = today.strftime('%A')
    # reads the contents of the file
    with open(file_path, 'r') as file:
        contents = file.read()
    # replacing the parameters with their values
    contents_edited = contents.replace('[DAY_OF_WEEK]', str(day))
    contents_edited = contents_edited.replace('[CURRENT_DATE]', str(today))
    return contents_edited


def main():

    file_path = 'C:\\Users\\omer7\\Documents\\edit.txt'
    # create a socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a host
    serversocket.bind((socket.gethostname(), 8080))
    # become a server socket
    serversocket.listen(5)
    while True:
        # accept connections from outside
        conn, addr = serversocket.accept()
        # send the data to the client on port 8080
        conn.send(change_data_of_file(file_path))


if __name__ == '__main__':
    main()


