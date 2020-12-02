import os
import struct


video_path = "C:/Users/DiFFtY/Documents/_Projets/Modding/TheSims4/VP6Video_2.avi"
audio_path = "C:/Users/DiFFtY/Documents/_Projets/Modding/TheSims4/AudioStream_2.dat"
output_path = "C:/Users/DiFFtY/Documents/_Projets/Modding/TheSims4/TestOutput_2.avi"


def encode_video(output_path, video_path, audio_path=None):
    # Création des pointeurs/stream de fichiers

    # Pour le fichier video d'input
    video_fp = open(video_path, "rb")
    video_file_size = os.path.getsize(video_path)

    # Pour le fichier video d'output
    output_fp = open(output_path, "wb")

    audio_fp = None

    # Check de si on a filé un fichier audio
    if audio_path and os.path.exists(audio_path):
        # Pour le fichier audio d'output
        audio_fp = open(audio_path, "rb")
        audio_file_size = os.path.getsize(audio_path)

    audio_buffer = []
    video_buffer = []

    if audio_fp:
        # Lecture du contenu du fichier audio (ebp-c) : 4 bytes ??
        audio_buffer.append(audio_fp.read(4))
        audio_meta_6c = audio_buffer[-1]

    # Seek jusque la position 0x70 dans le fichier video [ebx]
    video_fp.seek(0x70)

    # Lecture du contenu du fichier video (ebx) : 4 bytes ??
    video_buffer.append(video_fp.read(4))
    video_meta_54 = video_buffer[-1]

    # Récupération de la position du curseur du fichier video (ebx)
    video_pos = video_fp.tell()

    # Seek de la position dans le fichier video (ebx)
    video_fp.seek(video_pos + 0x0C)

    # Lecture du contenu du fichier video input (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$40]
    video_buffer.append(video_fp.read(4))
    video_meta_40 = video_buffer[-1]

    # Lecture du contenu du fichier video input (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$44]
    video_buffer.append(video_fp.read(4))
    video_meta_44 = video_buffer[-1]

    # Récupération de la position du curseur du fichier video (ebx)
    video_pos = video_fp.tell()

    # Seek de la position dans le fichier video (ebx)
    video_fp.seek(video_pos + 0x04)

    # Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$4C]
    video_buffer.append(video_fp.read(4))
    video_meta_4c = video_buffer[-1]

    # Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$48]
    video_buffer.append(video_fp.read(4))
    video_meta_48 = video_buffer[-1]

    # Récupération de la position du curseur du fichier video (ebx)
    video_pos = video_fp.tell()

    # Seek de la position dans le fichier video (ebx)
    video_fp.seek(video_pos + 0x0C)

    # Lecture du contenu du fichier video (ebx) : 2 bytes qu'on stocke sur la stack à l'adresse [ebp-$50]
    video_buffer.append(video_fp.read(2))
    video_meta_50 = video_buffer[-1]

    # Lecture du contenu du fichier video (ebx) : 2 bytes qu'on stocke sur la stack à l'adresse [ebp-$4E]
    video_buffer.append(video_fp.read(2))
    video_meta_4e = video_buffer[-1]

    # Ecriture dans fichier output (ebp-$10) : 0x20 bytes
    output_fp.write(bytearray("MVhd", "utf-8"))
    output_fp.write(b'\x20' + b'\x00' * 3)
    output_fp.write(video_meta_54 + video_meta_50 + video_meta_4e + video_meta_4c + video_meta_48  + video_meta_44 + video_meta_40)

    # Récupération de la position du curseur du fichier video (ebx)
    video_pos = video_fp.tell()

    if audio_fp:
        # Lecture du contenu du fichier audio (ebp-$0C) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$68]
        audio_buffer.append(audio_fp.read(4))
        audio_meta_68 = audio_buffer[-1]
        
        taille_audio = struct.unpack("l", audio_meta_68)[0]

        # Lecture du contenu du fichier audio (ebp-$0C) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$64]
        audio_buffer.append(audio_fp.read(4))
        audio_meta_64 = audio_buffer[-1]

        # Lecture du contenu du fichier audio (ebp-$0C) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$60]
        audio_buffer.append(audio_fp.read(4))
        audio_meta_60 = audio_buffer[-1]

        # Récupération de la position du curseur du fichier audio (ebp-$0C)
        audio_pos = audio_fp.tell()
        
        # Ecriture des métas audio
        output_fp.write(audio_meta_6c + audio_meta_68 + audio_meta_64 + audio_meta_60)

        premiere_iteration = True

        while audio_pos < taille_audio:
            if not premiere_iteration:
                # Lecture du contenu du fichier audio (ebp-$0C) : 1 byte qu'on stocke sur la stack à l'adresse [ebp-$34]
                audio_buffer.append(audio_fp.read(1))
                audio_meta_34 = audio_buffer[-1]

                # Ecriture
                output_fp.write(audio_meta_34)

            audio_pos = audio_fp.tell()
            premiere_iteration = False

        audio_pos = audio_fp.tell()
        audio_meta_24_val = audio_pos   # On garde la position de la fin des entête audio ??

    # Seek jusque la position 0xD4 dans le fichier video [ebx]
    video_fp.seek(0xD4)

    video_meta_14 = bytes()
    video_meta_20 = bytes()

    while video_meta_14.decode("ascii") != "movi":
        # Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$18]
        video_buffer.append(video_fp.read(4))
        video_meta_18 = video_buffer[-1]

        # Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$20]
        video_buffer.append(video_fp.read(4))
        video_meta_20 = video_buffer[-1]

        # Lecture du contenu du fichier video (ebx) : 4 byte qu'on stocke sur la stack à l'adresse [ebp-$14]
        video_buffer.append(video_fp.read(4))
        video_meta_14 = video_buffer[-1]

        # Seek de la video jusque la position définie dans video_meta_20 
        video_pos = video_fp.tell()
        new_video_pos = struct.unpack("l", video_meta_20)[0] + video_pos - 4
        video_fp.seek(new_video_pos)


    video_pos = video_fp.tell()
    new_video_pos = video_pos - struct.unpack("l", video_meta_20)[0] + 4

    video_fp.seek(new_video_pos)


    # Allocation du tableau qui recevra la liste des adresses où se trouvent les chunks video
    array_3c = []


    while video_meta_14.decode("ascii") != "idx1":
        # Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$14]
        video_buffer.append(video_fp.read(4))
        video_meta_14 = video_buffer[-1]

        # Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$2C]
        video_buffer.append(video_fp.read(4))
        video_meta_2c = video_buffer[-1]

        la_path_interdite = False
        skip_not_path_interdite = False
        
        if video_meta_14.decode("ascii") != "idx1":

            if video_meta_14.decode("ascii") != "00dc":

                if video_meta_14.decode("ascii") == "01wb":
                    video_pos = video_fp.tell()
                    video_fp.seek(video_pos - 8)

                else:
                    video_pos = video_fp.tell()
                    video_fp.seek(video_pos - 7)

                # Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$14]
                video_buffer.append(video_fp.read(4))
                video_meta_14 = video_buffer[-1]

                video_buffer.append(video_fp.read(4))
                video_meta_2c = video_buffer[-1]

            do_skip = False
            
            if video_meta_14.decode("ascii") != "00dc":

                if video_meta_14.decode("ascii") != "idx1":
                    la_path_interdite = True
                    do_skip = True
            
            if not do_skip:
                output_pos = output_fp.tell()
                array_3c.append(output_pos)

                output_fp.write(b'MV0F')

                video_meta_1c_to_write = (struct.unpack("l", video_meta_2c)[0] + 0x08).to_bytes(4, 'little')
                output_fp.write(video_meta_1c_to_write)

                video_meta_2c_val = struct.unpack("l", video_meta_2c)[0]
                stuff_to_write = video_fp.read(video_meta_2c_val)
                output_fp.write(stuff_to_write)                         

                if audio_fp:
                    audio_pos = audio_fp.tell()
                    
                    if audio_file_size != audio_pos:
                        # Lecture du contenu du fichier audio (ebp-$0C) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$6C]
                        audio_buffer.append(audio_fp.read(4))
                        audio_meta_6c = audio_buffer[-1]
                        output_fp.write(audio_meta_6c)

                        # Lecture du contenu du fichier audio (ebp-$0C) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$68]
                        audio_buffer.append(audio_fp.read(4))
                        audio_meta_68 = audio_buffer[-1]
                        output_fp.write(audio_meta_68)

                        premiere_iteration = True

                        stop = False

                        while not stop:
                            if not premiere_iteration:
                                # Lecture du contenu du fichier audio (ebp-$0C) : 1 byte qu'on stocke sur la stack à l'adresse [ebp-$34]
                                audio_buffer.append(audio_fp.read(1))
                                audio_meta_34 = audio_buffer[-1]
                                output_fp.write(audio_meta_34)

                            premiere_iteration = False

                            audio_pos = audio_fp.tell()

                            # Calcul de l'adresse de fin de boucle
                            audio_meta_68_val = struct.unpack("l", audio_meta_68)[0]
                            audio_pos_goal = audio_meta_24_val + audio_meta_68_val

                            if audio_pos_goal == audio_pos:
                                stop = True

                        audio_pos = audio_fp.tell()
                        audio_meta_24_val = audio_pos   # On garde la position de la fin des entête audio ??

                skip_not_path_interdite = True

            if la_path_interdite:
                video_pos = video_fp.tell()

                # Seek
                video_meta_2c_val =  struct.unpack("l", video_meta_2c)[0]
                video_fp.seek(video_meta_2c_val + video_pos)

                output_pos = output_fp.tell()

                array_3c.append(output_pos)
                
                video_pos = video_fp.tell()

        if not la_path_interdite and not skip_not_path_interdite:
            for pos in array_3c:
                # Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$28]
                video_buffer.append(video_fp.read(4))
                video_meta_28 = video_buffer[-1]

                if video_meta_28.decode("ascii") == "00dc":
                    # Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$28]
                    video_buffer.append(video_fp.read(4))
                    video_meta_28 = video_buffer[-1]

                    video_meta_28_val = struct.unpack("l", video_meta_28)[0]

                    if video_meta_28_val == 0x10:
                        # Seek
                        output_fp.seek(pos)
                        output_fp.write(b"MV0K")

                else:
                    # Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$28]
                    video_buffer.append(video_fp.read(4))
                    video_meta_28 = video_buffer[-1]

                # Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$28]
                video_buffer.append(video_fp.read(4))
                video_meta_28 = video_buffer[-1]

                # Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$28]
                video_buffer.append(video_fp.read(4))
                video_meta_28 = video_buffer[-1]


encode_video(output_path, video_path, audio_path)
