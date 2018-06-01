#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tarfile
import time
import datetime

choice_server = '/home/vagrant/roots/'
question_user = ''
date = datetime.datetime.now()

#################################################-      Def programme       -#################################################

def menu_gestion():
    print('#------------------------------------------------------------------------------------------------------------#')
    print('|                                                                                                            |')
    print('|                                    Gestionnaire Serveur Minecraft                                          |')
    print('|                                                                                                            |')
    print('|    1) Créer un serveur             2) Supprimer un serveur                 3) Sauvegarde/Restauration      |')
    print('|                                                                                                            |')
    print('|    4) Démarrer le serveur           5) Administration                       6) Quitter                     |')
    print('|                                                                                                            |')
    print('#------------------------------------------------------------------------------------------------------------#')

    if(question_user=='1'):
        print('Lancement de la création du nouveau serveur, veuillez sur les procédures suivante.\n')
        server_creation()
    elif(question_user=='2'):
        print('Lancement de la suppression du serveur, veuillez suivre les procédures mais pensez à faire une sauvegarde si nécessaire.\n')
        delete_server()
    elif(question_user=='3'):
        print('Lancement de la sauvegarde / Backup du serveur, veuillez suivre les procédures suivante.\n')
        server_saveBackup()
    elif(question_user=='4'):
        server_demarage()
    elif(question_user=='5'):
        administration_server()
    elif(question_user=='6'):
        exit()
        
def server_demarage():
    print('Donner nous l\'emplacement du server | exemple: /home/vagrant/roots/Creatif/')
    emplacement_server = input('> ')
    print('Combien de Ram voulez-vous attribuer au serveur ?')
    print('1024 = 1G , 2048 = 2G , 4096 = 4G , 8192 = 8G , 16384 = 16Go, 32768 = 32Go')
    serv_ram = input('> ')
    print('Lancement du serveur en cours ...')
    if os.path.exists(emplacement_server + "eula.txt"):
        replace_line(emplacement_server + 'eula.txt', 2, "eula=true"'\n')
    try:
        os.system('cd ' + emplacement_server + ' && java -Xmx' + serv_ram + 'M -Xms' + serv_ram + 'M -jar server.jar nogui')
    except:
        print("Erreur java n'est pas installé veuillez suivre ce tuto : https://tecadmin.net/install-java-8-on-centos-rhel-and-fedora/")

def server_creation():
    print('Donnez le chemin où vous souhaitez créer votre serveur. | Exemple: /home/vagrant/roots/')
    path = input('> ')
    print('\nNommez votre serveur.')
    server_name = input('> ')

    if os.path.exists(path + server_name):
        print('Le serveur est déjà existant.\n')
        server_creation()

    if os.path.exists(path):
        os.mkdir(path + server_name)
        os.system('cd ' + path + server_name + ' && wget https://launcher.mojang.com/mc/game/1.12.2/server/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar')
        
    elif not os.path.exists(path):
        os.mkdir(path)
        print('Nommez votre nouveau serveur')
        server_name = input('> ')
        os.mkdir(path + server_name)
        os.system('cd ' + path + server_name + ' && wget https://launcher.mojang.com/mc/game/1.12.2/server/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar')
        
def delete_server():
    print('Donnez le chemin où se trouve vôtre serveur. | Exemple: /home/vagrant/roots/')
    delete_servers = input('> ')
    
    if os.path.exists(delete_servers):
        print('Donnez le nom du serveur à supprimer')
        os.system('ls ' + delete_server)
        delete_nameServer = input('> ')
        
        print('Lancement de la suppression du serveur en cours ...')
        os.system('rm -rf ' + delete_servers + delete_nameServer)

    elif not os.path.exists(delete_server):
        print('Vous avez renseigné le mauvais chemin, le dossier est inéxistant.')
        delete_server()

def server_saveBackup():
    print('Que voulez-vous faire ? | 1) Sauvegarde, 2)Restauration')
    choice_server = input('> ')

    if(choice_server=='1'):
        print('Où voulez-vous sauvegarder votre serveur ? | Exemple: /home/vagrant/backup/')
        save_server = input('> ')
        print('Donnez le chemin du serveur que vous voulez sauvegarder | Exemple: /home/vagrant/roots/Creatif/')
        link_server = input('> ')
        print('Nommez votre backup | une date sera notifiée sur le fichier du backup automatiquement')
        name_backup = input('> ')

        print("Dossier backup: " + save_server + " | Dossier du serveur: " + link_server + " | Nom du backup: " + name_backup)

        if os.path.exists(save_server):
            with tarfile.open( save_server + name_backup + "-" + str(date.day) + "-" + str(date.month) + "-" + str(date.year) + "-" + str(date.hour) + ":" + str(date.minute) + ".tar.gz", "w:gz" ) as tar:
                print('Tar: ' + str(tar))
                for name in os.listdir(link_server):
                    print(str(name))
                    tar.add(link_server + name)
            print('\nSauvegarde du serveur terminé.')
        
        elif not os.path.exists(save_server):
            os.mkdir(save_server)
            server_saveBackup()

    elif(choice_server=='2'):
        print('Où se situe le fichier de restauration de votre serveur ? | Exemple: /home/vagrant/backup/')
        backup_server = input('> ')
        print('Où voulez vous restaurer votre serveur ? | Exemple: /home/vagrant/roots/Creatif/')
        extract_server = input('> ')
        print('Nom du serveur:')
        server_name = input('> ')
        print('Sélectionnez votre backup:')
        os.system('ls ' + backup_server)
        restauration_server = input('> ')

        if os.path.exists(backup_server):
            print('Lancement de la restauration en cours ...\n')
            os.system('rm -rf ' + extract_server)
            os.mkdir(extract_server)
            tar_extract = tarfile.open(backup_server + restauration_server)
            tar_extract.extractall(extract_server)
            tar_extract.close()
            os.system('cp -r ' + extract_server + extract_server.replace('/home', 'home') + ' ' + extract_server.replace(server_name, ''))
            os.system('rm -rf ' + extract_server + 'home/')
            time.sleep(2)
            print('Restauration terminée, vous pouvez redémarrer le serveur')

        elif not os.path.exists(backup_server):
            os.mkdir(backup_server)
            server_saveBackup()

    else:
        print('Commande impossible, répondez sois par 1 ou 2')

def administration_server():
    os.system('clear')
    print('Vous entrez dans le système d\'administration de votre serveur, pensez à établir une sauvegarde avant toute action auprès du serveur qui pourrais causer d\'éventuelle dommage.\n')
    print('Donnez le chemin du serveur que vous voulez administrer | exemple: /home/vagrant/roots/Creatif/ , ne pas oublier le dernier /')
    admin_server = input('> ')

    while True:
        os.system('clear')

        print('#------------------------------------------------------------------------------------------------------------#')
        print('|                                                                                                            |')
        print('|                                Administration Serveur Minecraft                                            |')
        print('|                                                                                                            |')
        print('|    1) Gestion port                 2) Gestion ip                           3) Nombre de joueurs max        |')
        print('|                                                                                                            |')
        print('|    4) Difficulté                   5) PvP                                  6) Hardcore                     |')
        print('|                                                                                                            |')
        print('|    7) Description                  8) Version Crack/Payante                9) Whitelist                    |')
        print('|                                                                                                            |')
        print('|    10) Supprimer monde             11) Seed                                12) Commande-bloc               |')
        print('|                                                                                                            |')
        print('|                                    13) Quitter                                                             |')
        print('|                                                                                                            |')
        print('#------------------------------------------------------------------------------------------------------------#')
        
        admin_question = input('> ')
        
        if(admin_question == '1'):
            print('Vous êtes sur le point de changer le port du server | Par défaut: 25565')
            serv_port = input('> ')
            replace_line(admin_server + 'server.properties', 21, "server-port=" + serv_port + '\n')
        elif(admin_question == '2'):
            print('Vous êtes sur le point de changer l\'ip du serveur.')
            serv_ip = input('> ')
            replace_line(admin_server + 'server.properties', 22, "server-ip=" + serv_ip + '\n')
        elif(admin_question == '3'):
            print('Vous êtes sur le point de changer le nombre maximum de joueurs.')
            serv_player = input('> ')
            replace_line(admin_server + 'server.properties', 17, "max-player=" + serv_player + '\n')
        elif(admin_question == '4'):
            print('Vous êtes sur le point de changer la difficulté du jeu ce qui peut alterer le gameplay actuel | 0: Peacefull, 1: Easy, 2: Normal, 3:Hard')
            serv_difficulty = input('> ')
            replace_line(admin_server + 'server.properties', 9, "difficulty=" + serv_difficulty + '\n')
        elif(admin_question == '5'):
            print('Vous êtes sur le point de changer le pvp du jeu ce qui peut alterer le gameplay actuel | Activé: True , Désactivé: False')
            serv_pvp = input('> ')
            replace_line(admin_server + 'server.properties', 12, "pvp=" + serv_pvp + '\n')
        elif(admin_question == '6'):
            print('Vous êtes sur le point de passer le serveur en hardcore ce qui signifie qu\'une mort dans le jeu est définitif | Activé: True , Désactiver: False')
            serv_hardcore = input('> ')
            replace_line(admin_server + 'server.properties', 38, "hardcore=" + serv_hardcore + '\n')
        elif(admin_question == '7'):
            print('Vous êtes sur le point de changer la description du serveur.')
            serv_description = input('> ')
            replace_line(admin_server + 'server.properties', 36, "modt=" + serv_description + '\n')
        elif(admin_question == '8'):
            print('Vous êtes sur le point de changer le type d\'accès au serveur ce qui signifie que si vous acceptez les versions crack. | Payant: True , Crack: False')
            serv_version = input('> ')
            replace_line(admin_server + 'server.properties', 31, "online-mode=" + serv_version + '\n')
        elif(admin_question == '9'):
            print('Vous êtes sur le point de passer le serveur en accès privée, pensez à ajouter les joueurs dans la whitelist à la suite | Activé: True , Désactiver: False')
            serv_whitelist = input('> ')
            replace_line(admin_server + 'server.properties', 29, "white-list=" + serv_whitelist + '\n')
        elif(admin_question == '10'):
            print('Vous êtes sur le point de supprimer un monde, pensez à sauvegarder avant de commencer à supprimer vos mondes | 1) OverWorld , 2) Nether , 3) End')
            serv_world = input('> ')

            print('Chemin du dossier où se trouve ' + serv_world)
            del_world = input('> ')

            if(serv_world == '1'):
                print('Vous êtes sur le point de supprimer le monde.')
                os.system('rm -rf ' + del_world + '/world/overworld')

            elif(serv_world == '2'):
                print('Vous êtes sur le point de supprimer le nether')
                os.system('rm -rf ' + del_world + '/world/the_nether')

            elif(serv_world == '3'):
                print('Vous êtes sur le point de supprimer l\'end')
                os.system('rm -rf ' + del_world + '/world/the_end')
              
        elif(admin_question == '11'):
            print('Vous êtes sur le point de changer le seed de la map, qui vous permettra de générer un monde grâce à ce seed.')
            serv_seed = input('> ')
            replace_line(admin_server + 'server.properties', 33, "level-seed=" + serv_seed + '\n')
        elif(admin_question == '12'):
            print('Vous êtes sur le point d\'activer les command-bloc sur le serveur | Activé: True , Désactiver: False')
            serv_command = input('> ')
            replace_line(admin_server + 'server.properties', 16, "command-bloc=" + serv_command + '\n')
        elif(admin_question == '13'):
            print('Bonne continuation à vous')
            break

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
    

 def read_line(file_name, line_num, text):
    lines = open(file_name, 'r').readline()
    lines[line_num] = text
    out = open(file_name, 'r')
    out.readline(lines)
    out.close() 

#################################################-	Programme	-#################################################

while True:
    os.system('clear')
    menu_gestion() 
    question_user = input('> ')
