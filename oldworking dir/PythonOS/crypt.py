import socket

pc_name = socket.gethostname()

pc_name_binary = bin(int.from_bytes(pc_name.encode(), 'big'))[2:]

print (pc_name,pc_name_binary)
