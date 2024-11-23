import socket
from _thread import *
import pickle
import pygame
from rpg.game import Game
server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games : dict[int,Game] = {}
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data:str = pickle.loads(conn.recv(4096))

            if gameId in games:
                game : Game = games[gameId]

                if not data:
                    break
                else:

                    if 'trainer' in data.keys() and 'ankimons' in data.keys():
                        games[gameId].add_data(data, p)
                    if 'cards_learned' in data.keys():
                        games[gameId].cards_learned[p] = data['cards_learned']
                    message = pickle.dumps(game)

                    conn.sendall(message)
            else:
                break
        except Exception as e:
            print(e)
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game()
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))