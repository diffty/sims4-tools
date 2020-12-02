import os
import struct


def encode_video(output_path, video_path, audio_path=None):
    # Création des pointeurs/stream de fichiers pour le fichier video
    video_fp = open(video_path, "rb")

    # Création des pointeurs/stream de fichiers pour le fichier d'output
    output_fp = open(output_path, "wb")

    # Création des pointeurs/stream de fichiers pour le fichier audio (s'il existe)
    audio_fp = None

    if audio_path and os.path.exists(audio_path):
        audio_fp = open(audio_path, "rb")
        audio_file_size = os.path.getsize(audio_path)

        # Lecture du contenu du fichier audio
        audio_meta_6c = audio_fp.read(4)

    # Seek jusque la position 0x70 dans le fichier video
    video_fp.seek(0x70)

    # Lecture du contenu du fichier video
    video_meta_54 = video_fp.read(4)

    # Seek de la position dans le fichier video
    video_fp.seek(video_fp.tell() + 0x0C)

    # Lecture du contenu du fichier video input
    video_meta_40 = video_fp.read(4)
    video_meta_44 = video_fp.read(4)

    # Seek de la position dans le fichier video
    video_fp.seek(video_fp.tell() + 0x04)

    # Lecture du contenu du fichier video
    video_meta_4c = video_fp.read(4)
    video_meta_48 = video_fp.read(4)

    # Seek de la position dans le fichier video
    video_fp.seek(video_fp.tell() + 0x0C)

    # Lecture du contenu du fichier video
    video_meta_50 = video_fp.read(2)
    video_meta_4e = video_fp.read(2)

    # Ecriture dans fichier output
    output_fp.write(bytearray("MVhd", "utf-8"))
    output_fp.write(b'\x20' + b'\x00' * 3)
    output_fp.write(video_meta_54 + video_meta_50 + video_meta_4e + video_meta_4c + video_meta_48  + video_meta_44 + video_meta_40)

    if audio_fp:
        # Lecture du contenu du fichier audio
        audio_meta_68 = audio_fp.read(4)
        audio_meta_64 = audio_fp.read(4)
        audio_meta_60 = audio_fp.read(4)

        # Récupération de la position du curseur du fichier audio
        audio_pos = audio_fp.tell()
        
        # Ecriture des métas audio
        output_fp.write(audio_meta_6c + audio_meta_68 + audio_meta_64 + audio_meta_60)

        taille_audio = struct.unpack("l", audio_meta_68)[0]

        premiere_iteration = True

        while audio_pos < taille_audio:
            if not premiere_iteration:
                # Lecture du contenu du fichier audio
                audio_meta_34 = audio_fp.read(1)

                # Ecriture
                output_fp.write(audio_meta_34)

            audio_pos = audio_fp.tell()
            premiere_iteration = False

        audio_pos = audio_fp.tell()
        audio_meta_24_val = audio_pos   # On garde la position de la fin des entête audio ??

    # Seek jusque la position 0xD4 dans le fichier video
    video_fp.seek(0xD4)

    video_meta_14 = bytes()
    video_meta_20 = bytes()

    while video_meta_14.decode("ascii") != "movi":
        # Lecture du contenu du fichier video
        video_meta_18 = video_fp.read(4)
        video_meta_20 = video_fp.read(4)
        video_meta_14 = video_fp.read(4)

        # Seek de la video jusque la position définie dans video_meta_20 
        new_video_pos = struct.unpack("l", video_meta_20)[0] + video_fp.tell() - 4
        video_fp.seek(new_video_pos)

    new_video_pos = video_fp.tell() - struct.unpack("l", video_meta_20)[0] + 4
    video_fp.seek(new_video_pos)

    # Allocation du tableau qui recevra la liste des adresses où se trouvent les chunks video
    array_3c = []

    while video_meta_14.decode("ascii") != "idx1":
        # Lecture du contenu du fichier video
        video_meta_14 = video_fp.read(4)
        video_meta_2c = video_fp.read(4)

        la_path_interdite = False
        skip_not_path_interdite = False
        
        if video_meta_14.decode("ascii") != "idx1":
            if video_meta_14.decode("ascii") != "00dc":
                if video_meta_14.decode("ascii") == "01wb":
                    video_fp.seek(video_fp.tell() - 8)
                else:
                    video_fp.seek(video_fp.tell() - 7)

                # Lecture du contenu du fichier video
                video_meta_14 = video_fp.read(4)
                video_meta_2c = video_fp.read(4)

            do_skip = False
            
            if video_meta_14.decode("ascii") != "00dc":
                if video_meta_14.decode("ascii") != "idx1":
                    la_path_interdite = True
                    do_skip = True
            
            if not do_skip:
                array_3c.append(output_fp.tell())

                output_fp.write(b'MV0F')

                video_meta_1c_to_write = (struct.unpack("l", video_meta_2c)[0] + 0x08).to_bytes(4, 'little')
                output_fp.write(video_meta_1c_to_write)

                video_meta_2c_val = struct.unpack("l", video_meta_2c)[0]
                stuff_to_write = video_fp.read(video_meta_2c_val)
                output_fp.write(stuff_to_write)                         

                if audio_fp:
                    audio_pos = audio_fp.tell()
                    
                    if audio_file_size != audio_pos:
                        # Lecture du contenu du fichier audio
                        audio_meta_6c = audio_fp.read(4)
                        output_fp.write(audio_meta_6c)

                        # Lecture du contenu du fichier audio
                        audio_meta_68 = audio_fp.read(4)
                        output_fp.write(audio_meta_68)

                        premiere_iteration = True

                        stop = False

                        while not stop:
                            if not premiere_iteration:
                                # Lecture du contenu du fichier audio
                                audio_meta_34 = audio_fp.read(1)
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
                # Seek
                video_meta_2c_val =  struct.unpack("l", video_meta_2c)[0]
                video_fp.seek(video_meta_2c_val + video_fp.tell())

                array_3c.append(output_fp.tell())

        if not la_path_interdite and not skip_not_path_interdite:
            for pos in array_3c:
                # Lecture du contenu du fichier video
                video_meta_28 = video_fp.read(4)

                if video_meta_28.decode("ascii") == "00dc":
                    # Lecture du contenu du fichier video
                    video_meta_28 = video_fp.read(4)

                    video_meta_28_val = struct.unpack("l", video_meta_28)[0]

                    if video_meta_28_val == 0x10:
                        # Seek
                        output_fp.seek(pos)
                        output_fp.write(b"MV0K")

                else:
                    # Lecture du contenu du fichier video
                    video_meta_28 = video_fp.read(4)

                # Lecture du contenu du fichier video
                video_meta_28 = video_fp.read(4)
                video_meta_28 = video_fp.read(4)


if __name__ == "__main__":
    video_path = "C:/Users/DiFFtY/Documents/_Projets/Modding/TheSims4/VP6Video_2.avi"
    audio_path = "C:/Users/DiFFtY/Documents/_Projets/Modding/TheSims4/AudioStream_2.dat"
    output_path = "C:/Users/DiFFtY/Documents/_Projets/Modding/TheSims4/TestOutput_2.avi"

    encode_video(output_path, video_path, audio_path)
