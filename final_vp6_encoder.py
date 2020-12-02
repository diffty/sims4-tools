import os
import struct


audio = True

video_path = "C:/Users/DiFFtY/Documents/_Projets/Modding/TheSims4/VP6Video_2.avi"
audio_path = "C:/Users/DiFFtY/Documents/_Projets/Modding/TheSims4/AudioStream_2.dat"
output_path = "C:/Users/DiFFtY/Documents/_Projets/Modding/TheSims4/TestOutput_2.avi"

#video_path = "/Users/diffty/ownCloud/Projets/Modding/TheSims4/VP6Video_2.avi"
#audio_path = "/Users/diffty/ownCloud/Projets/Modding/TheSims4/AudioStream_2.dat"



# 0045AC18   55                     push    ebp
# 0045AC19   8BEC                   mov     ebp, esp                    # Base de la pile
# 0045AC1B   81C478FFFFFF           add     esp, $FFFFFF78              # Haut de la pile
# 0045AC21   53                     push    ebx
# 0045AC22   56                     push    esi
# 0045AC23   57                     push    edi
# 0045AC24   33DB                   xor     ebx, ebx                    # Technique d'initialisation à 0 du registre



#### Flush de tous les registres ####

# 0045AC26   899D78FFFFFF           mov     [ebp+$FFFFFF78], ebx
# 0045AC2C   899D7CFFFFFF           mov     [ebp+$FFFFFF7C], ebx
# 0045AC32   895D80                 mov     [ebp-$80], ebx
# 0045AC35   895D84                 mov     [ebp-$7C], ebx
# 0045AC38   895D88                 mov     [ebp-$78], ebx
# 0045AC3B   895D8C                 mov     [ebp-$74], ebx
# 0045AC3E   895D90                 mov     [ebp-$70], ebx
# 0045AC41   895DC4                 mov     [ebp-$3C], ebx
# 0045AC44   894DF8                 mov     [ebp-$08], ecx
# 0045AC47   8955FC                 mov     [ebp-$04], edx
# 0045AC4A   8BF0                   mov     esi, eax
# 0045AC4C   8B45F8                 mov     eax, [ebp-$08]



#### (blc) Incrément du compteru de références pour les variables contenant les paths ####

# * Reference to: System.@LStrAddRef(void;void):Pointer;
# |
# 0045AC4F   E8A896FAFF             call    004042FC
# 0045AC54   8B450C                 mov     eax, [ebp+$0C]
# 
# * Reference to: System.@LStrAddRef(void;void):Pointer;
# |
# 0045AC57   E8A096FAFF             call    004042FC
# 0045AC5C   8B4508                 mov     eax, [ebp+$08]
# 
# * Reference to: System.@LStrAddRef(void;void):Pointer;
# |
# 0045AC5F   E89896FAFF             call    004042FC
# 0045AC64   33C0                   xor     eax, eax
# 0045AC66   55                     push    ebp
# 0045AC67   6803B44500             push    $0045B403



# ***** TRY
# |
# 0045AC6C   64FF30                 push    dword ptr fs:[eax]
# 0045AC6F   648920                 mov     fs:[eax], esp



#### Création des pointeurs/stream de fichiers ####

## Pour le fichier video d'input

# 0045AC72   6A00                   push    $00
# 0045AC74   6A20                   push    $20
# 0045AC76   8B4DF8                 mov     ecx, [ebp-$08]       # [ebp-$08] = Référence au stream du fichier video
# 0045AC79   B201                   mov     dl, $01

# * Reference to class TFileStream
# |
# 0045AC7B   A1E01C4100             mov     eax, dword ptr [$00411CE0]
# 
# * Reference to: Classes.TFileStream.Create(TFileStream;boolean;AnsiString;Word;Cardinal);overload;
# |
# 0045AC80   E8F7AEFBFF             call    00415B7C
# 0045AC85   8BD8                   mov     ebx, eax                # [ebx] = Stream video

video_fp = open(video_path, "rb")
video_file_size = os.path.getsize(video_path)



## Pour le fichier video d'output

# 0045AC87   68FFFF0000             push    $0000FFFF
# 0045AC8C   6A10                   push    $10
# 0045AC8E   8B4D0C                 mov     ecx, [ebp+$0C]          # [ebp+$0C] = Référence au path du fichier output
# 0045AC91   B201                   mov     dl, $01

# * Reference to class TFileStream
# |
# 0045AC93   A1E01C4100             mov     eax, dword ptr [$00411CE0]
# 
# * Reference to: Classes.TFileStream.Create(TFileStream;boolean;AnsiString;Word;Cardinal);overload;
# |
# 0045AC98   E8DFAEFBFF             call    00415B7C
# 0045AC9D   8945F0                 mov     [ebp-$10], eax          # [ebp-$10] = Stream output
# 0045ACA0   8B4508                 mov     eax, [ebp+$08]

output_fp = open(output_path, "wb")

#try:

#### Alors là jcrois qu'on teste voir si l'ouverture du stream a échoué ou pas

# * Possible String Reference to: 'none~'
# |
# 0045ACA3   BA1CB44500             mov     edx, $0045B41C
# 
# * Reference to: System.@LStrCmp;
# |
# 0045ACA8   E8AB95FAFF             call    00404258
# 0045ACAD   7439                   jz      0045ACE8



## Pour le fichier audio d'output

# 0045ACAF   6A00                   push    $00
# 0045ACB1   6A20                   push    $20
# 0045ACB3   8B4D08                 mov     ecx, [ebp+$08]          # [ebp+$08] = Référence au path du fichier audio
# 0045ACB6   B201                   mov     dl, $01
# 
# * Reference to class TFileStream
# |
# 0045ACB8   A1E01C4100             mov     eax, dword ptr [$00411CE0]
# 
# * Reference to: Classes.TFileStream.Create(TFileStream;boolean;AnsiString;Word;Cardinal);overload;
# |
# 0045ACBD   E8BAAEFBFF             call    00415B7C
# 0045ACC2   8945F4                 mov     [ebp-$0C], eax          # [ebp-$0C] = Stream audio
# 0045ACC5   8B45F4                 mov     eax, [ebp-$0C]

audio_fp = open(audio_path, "rb")
audio_file_size = os.path.getsize(audio_path)


# XXX ## [OSEF] GUI update (ProgressBar)

# XXX ## 0045ACC8   8B10                   mov     edx, [eax]
# XXX ## 0045ACCA   FF12                   call    dword ptr [edx]
# XXX ## 0045ACCC   8BD0                   mov     edx, eax
# XXX ## 0045ACCE   8B45FC                 mov     eax, [ebp-$04]
# XXX ## 0045ACD1   8B00                   mov     eax, [eax]
# XXX ## 
# XXX ## * Reference to: ComCtrls.TProgressBar.SetMax(TProgressBar;Integer);
# XXX ## |
# XXX ## 0045ACD3   E8C423FDFF             call    0042D09C                # ComCtrls.TProgressBar.SetMax


audio_buffer = []
video_buffer = []

#### Lecture du contenu du fichier audio (ebp-c) : 4 bytes ??

# 0045ACD8   8D5594                 lea     edx, [ebp-$6C]
# 0045ACDB   B904000000             mov     ecx, $00000004
# 0045ACE0   8B45F4                 mov     eax, [ebp-$0C]
# 
# * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
# |
# 0045ACE3   E8C8ABFBFF             call    004158B0

audio_buffer.append(audio_fp.read(4))
#print("audio [ebp-$6C]:", audio_buffer[-1])

audio_meta_6c = audio_buffer[-1]



# XXX #### [OSEF] GUI update (ProgressBar)
# XXX 
# XXX # 0045ACE8   8BC3                   mov     eax, ebx
# XXX # 0045ACEA   8B10                   mov     edx, [eax]
# XXX # 0045ACEC   FF12                   call    dword ptr [edx]
# XXX # 0045ACEE   8BD0                   mov     edx, eax
# XXX # 0045ACF0   8B06                   mov     eax, [esi]
# XXX # 
# XXX # * Reference to: ComCtrls.TProgressBar.SetMax(TProgressBar;Integer);
# XXX # |
# XXX # 0045ACF2   E8A523FDFF             call    0042D09C



#### Seek jusque la position 0x70 dans le fichier video [ebx]

# 0045ACF7   6A00                   push    $00
# 0045ACF9   6A70                   push    $70

# 0045ACFB   8BC3                   mov     eax, ebx
# 
# |
# 0045ACFD   E8A2A9FBFF             call    004156A4

video_fp.seek(0x70)



#### Lecture du contenu du fichier video (ebx) : 4 bytes ??

# 0045AD02   8D55AC                 lea     edx, [ebp-$54]
# 0045AD05   B904000000             mov     ecx, $00000004
# 0045AD0A   8BC3                   mov     eax, ebx
# 
# * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
# |
# 0045AD0C   E89FABFBFF             call    004158B0

video_buffer.append(video_fp.read(4))
#print("video [ebp-$54]:", video_buffer[-1])

video_meta_54 = video_buffer[-1]



#### Récupération de la position du curseur du fichier video (ebx)

# 0045AD11   8BC3                   mov     eax, ebx
# 
# * Reference to: Classes.TStream.GetPosition(TStream):Int64;
# |
# 0045AD13   E86CA9FBFF             call    00415684

video_pos = video_fp.tell()
#print("video position: ", video_pos)



#### Seek de la position dans le fichier video (ebx)

# 0045AD18   83C00C                 add     eax, +$0C
# 0045AD1B   83D200                 adc     edx, +$00
# 0045AD1E   52                     push    edx
# 0045AD1F   50                     push    eax
# 0045AD20   8BC3                   mov     eax, ebx
# 
# |
# 0045AD22   E87DA9FBFF             call    004156A4

video_fp.seek(video_pos + 0x0C)



#### Lecture du contenu du fichier video input (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$40]

# 0045AD27   8D55C0                 lea     edx, [ebp-$40]
# 0045AD2A   B904000000             mov     ecx, $00000004
# 0045AD2F   8BC3                   mov     eax, ebx

# * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
# |
# 0045AD31   E87AABFBFF             call    004158B0

video_buffer.append(video_fp.read(4))
#print("video [ebp-$40]: ", video_buffer[-1])

video_meta_40 = video_buffer[-1]



#### Lecture du contenu du fichier video input (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$44]

# 0045AD36   8D55BC                 lea     edx, [ebp-$44]
# 0045AD39   B904000000             mov     ecx, $00000004
# 0045AD3E   8BC3                   mov     eax, ebx
# 
# * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
# |
# 0045AD40   E86BABFBFF             call    004158B0

video_buffer.append(video_fp.read(4))
#print("video [ebp-$44]: ", video_buffer[-1])

video_meta_44 = video_buffer[-1]



#### Récupération de la position du curseur du fichier video (ebx)

# 0045AD45   8BC3                   mov     eax, ebx
# 
# * Reference to: Classes.TStream.GetPosition(TStream):Int64;
# |
# 0045AD47   E838A9FBFF             call    00415684

video_pos = video_fp.tell()
#print("video position: ", video_pos)



#### Seek de la position dans le fichier video (ebx)

# 0045AD4C   83C004                 add     eax, +$04       # On ajoute 4 à la position ?
# 0045AD4F   83D200                 adc     edx, +$00       # le seek se fera depuis une pos depuis le début
# 0045AD52   52                     push    edx
# 0045AD53   50                     push    eax
# 0045AD54   8BC3                   mov     eax, ebx

# |
# 0045AD56   E849A9FBFF             call    004156A4

video_fp.seek(video_pos + 0x04)



#### Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$4C]

# 0045AD5B   8D55B4                 lea     edx, [ebp-$4C]
# 0045AD5E   B904000000             mov     ecx, $00000004
# 0045AD63   8BC3                   mov     eax, ebx
# 
# * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
# |
# 0045AD65   E846ABFBFF             call    004158B0

video_buffer.append(video_fp.read(4))
#print("video [ebp-$4C]:", video_buffer[-1])

video_meta_4c = video_buffer[-1]



#### Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$48]

# 0045AD6A   8D55B8                 lea     edx, [ebp-$48]
# 0045AD6D   B904000000             mov     ecx, $00000004
# 0045AD72   8BC3                   mov     eax, ebx
# 
# * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
# |
# 0045AD74   E837ABFBFF             call    004158B0

video_buffer.append(video_fp.read(4))
#print("video [ebp-$48]:", video_buffer[-1])

video_meta_48 = video_buffer[-1]



#### Récupération de la position du curseur du fichier video (ebx)

# 0045AD79   8BC3                   mov     eax, ebx
# 
# * Reference to: Classes.TStream.GetPosition(TStream):Int64;
# |
# 0045AD7B   E804A9FBFF             call    00415684

video_pos = video_fp.tell()
#print("video position: ", video_pos)



#### Seek de la position dans le fichier video (ebx)

# 0045AD80   83C00C                 add     eax, +$0C
# 0045AD83   83D200                 adc     edx, +$00
# 0045AD86   52                     push    edx
# 0045AD87   50                     push    eax
# 0045AD88   8BC3                   mov     eax, ebx
# 
# |
# 0045AD8A   E815A9FBFF             call    004156A4

video_fp.seek(video_pos + 0x0C)


#### Lecture du contenu du fichier video (ebx) : 2 bytes qu'on stocke sur la stack à l'adresse [ebp-$50]

# 0045AD8F   8D55B0                 lea     edx, [ebp-$50]
# 0045AD92   B902000000             mov     ecx, $00000002
# 0045AD97   8BC3                   mov     eax, ebx
# 
# * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
# |
# 0045AD99   E812ABFBFF             call    004158B0

video_buffer.append(video_fp.read(2))
#print("video [ebp-$50]:", video_buffer[-1])

video_meta_50 = video_buffer[-1]



#### Lecture du contenu du fichier video (ebx) : 2 bytes qu'on stocke sur la stack à l'adresse [ebp-$4E]

# 0045AD9E   8D55B2                 lea     edx, [ebp-$4E]
# 0045ADA1   B902000000             mov     ecx, $00000002
# 0045ADA6   8BC3                   mov     eax, ebx

# * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
# |
# 0045ADA8   E803ABFBFF             call    004158B0

video_buffer.append(video_fp.read(2))
#print("video [ebp-$4E]:", video_buffer[-1])

video_meta_4e = video_buffer[-1]



#### Ecriture dans fichier output (ebp-$10) : 0x20 bytes

# 0045ADAD   C745A820000000         mov     dword ptr [ebp-$58], $00000020
# 0045ADB4   A124B44500             mov     eax, dword ptr [$0045B424]   # [$0045B424] = MVhd
# 0045ADB9   8945A4                 mov     [ebp-$5C], eax
# 0045ADBC   8D55A4                 lea     edx, [ebp-$5C]
# 0045ADBF   B920000000             mov     ecx, $00000020
# 0045ADC4   8B45F0                 mov     eax, [ebp-$10]
# 
# * Reference to: Classes.TStream.WriteBuffer(TStream;void;void;Longint);
# |
# 0045ADC7   E81CABFBFF             call    004158E8

#print("Writing video:", bytearray("MVhd", "utf-8"))
output_fp.write(bytearray("MVhd", "utf-8"))
#print("Writing video:", b'\x20' + b'\x00' * 3)
output_fp.write(b'\x20' + b'\x00' * 3)
#print("Writing video:", video_meta_54 + video_meta_50 + video_meta_4e + video_meta_4c + video_meta_48  + video_meta_44 + video_meta_40)
output_fp.write(video_meta_54 + video_meta_50 + video_meta_4e + video_meta_4c + video_meta_48  + video_meta_44 + video_meta_40)


#### Récupération de la position du curseur du fichier video (ebx)

# 0045ADCC   8BC3                   mov     eax, ebx
# 
# * Reference to: Classes.TStream.GetPosition(TStream):Int64;
# |
# 0045ADCE   E8B1A8FBFF             call    00415684

video_pos = video_fp.tell()
#print("video position:", video_pos)



# XXX #### [OSEF] GUI update (ProgressBar)
# XXX 
# XXX # 0045ADD3   8BD0                   mov     edx, eax
# XXX # 0045ADD5   8B06                   mov     eax, [esi]
# XXX # 
# XXX # * Reference to: ComCtrls.TProgressBar.SetPosition(TProgressBar;Integer);
# XXX # |
# XXX # 0045ADD7   E8D022FDFF             call    0042D0AC



# TEST si pas de fichier audio on jump à 0045AE8C

# 0045ADDC   8B4508                 mov     eax, [ebp+$08]
# 
# * Possible String Reference to: 'none~'
# |
# 0045ADDF   BA1CB44500             mov     edx, $0045B41C
# 
# * Reference to: System.@LStrCmp;
# |
# 0045ADE4   E86F94FAFF             call    00404258
# 0045ADE9   0F849D000000           jz      0045AE8C

if audio:

    #### Lecture du contenu du fichier audio (ebp-$0C) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$68]

    # 0045ADEF   8D5598                 lea     edx, [ebp-$68]
    # 0045ADF2   B904000000             mov     ecx, $00000004
    # 0045ADF7   8B45F4                 mov     eax, [ebp-$0C]
    # 
    # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
    # |
    # 0045ADFA   E8B1AAFBFF             call    004158B0

    
    audio_buffer.append(audio_fp.read(4))
    #print("audio [ebp-$68]:", audio_buffer[-1])

    audio_meta_68 = audio_buffer[-1]
    
    taille_audio = struct.unpack("l", audio_meta_68)[0]



    #### Lecture du contenu du fichier audio (ebp-$0C) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$64]

    # 0045ADFF   8D559C                 lea     edx, [ebp-$64]
    # 0045AE02   B904000000             mov     ecx, $00000004
    # 0045AE07   8B45F4                 mov     eax, [ebp-$0C]
    # 
    # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
    # |
    # 0045AE0A   E8A1AAFBFF             call    004158B0

    audio_buffer.append(audio_fp.read(4))
    #print("audio [ebp-$64]:", audio_buffer[-1])

    audio_meta_64 = audio_buffer[-1]


    #### Lecture du contenu du fichier audio (ebp-$0C) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$60]

    # 0045AE0F   8D55A0                 lea     edx, [ebp-$60]
    # 0045AE12   B904000000             mov     ecx, $00000004
    # 0045AE17   8B45F4                 mov     eax, [ebp-$0C]
    # 
    # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
    # |
    # 0045AE1A   E891AAFBFF             call    004158B0

    audio_buffer.append(audio_fp.read(4))
    #print("audio [ebp-$60]:", audio_buffer[-1])

    audio_meta_60 = audio_buffer[-1]

    #### Récupération de la position du curseur du fichier audio (ebp-$0C)

    # 0045AE1F   8B45F4                 mov     eax, [ebp-$0C]
    # 
    # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
    # |
    # 0045AE22   E85DA8FBFF             call    00415684

    audio_pos = audio_fp.tell()
    #print("audio position: ", audio_pos)



    # XXX #### [OSEF] GUI update (ProgressBar)

    # XXX # 0045AE27   8BD0                   mov     edx, eax
    # XXX # 0045AE29   8B45FC                 mov     eax, [ebp-$04]
    # XXX # 0045AE2C   8B00                   mov     eax, [eax]
    # XXX # 
    # XXX # * Reference to: ComCtrls.TProgressBar.SetPosition(TProgressBar;Integer);
    # XXX # |
    # XXX # 0045AE2E   E87922FDFF             call    0042D0AC



    # 0045AE33   8D5594                 lea     edx, [ebp-$6C]
    # 0045AE36   B910000000             mov     ecx, $00000010
    # 0045AE3B   8B45F0                 mov     eax, [ebp-$10]
    # 
    # * Reference to: Classes.TStream.WriteBuffer(TStream;void;void;Longint);
    # |
    # 0045AE3E   E8A5AAFBFF             call    004158E8

    #print("Writing audio:", audio_meta_6c)
    #print("Writing ", b'\0' * (0x10 - len(audio_meta_6c)))
    
    output_fp.write(audio_meta_6c + audio_meta_68 + audio_meta_64 + audio_meta_60)


    #### On jump à 0045AE65

    # 0045AE43   EB20                   jmp     0045AE65

    premiere_iteration = True

    while audio_pos < taille_audio:
        if not premiere_iteration:
            #### Lecture du contenu du fichier audio (ebp-$0C) : 1 byte qu'on stocke sur la stack à l'adresse [ebp-$34]

            # 0045AE45   8D55CC                 lea     edx, [ebp-$34]
            # 0045AE48   B901000000             mov     ecx, $00000001
            # 0045AE4D   8B45F4                 mov     eax, [ebp-$0C]
            # 
            # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
            # |
            # 0045AE50   E85BAAFBFF             call    004158B0

            audio_buffer.append(audio_fp.read(1))
            #print("audio [ebp-$34]:", audio_buffer[-1])

            audio_meta_34 = audio_buffer[-1]

            # 0045AE55   8D55CC                 lea     edx, [ebp-$34]
            # 0045AE58   B901000000             mov     ecx, $00000001
            # 0045AE5D   8B45F0                 mov     eax, [ebp-$10]
            # 
            # * Reference to: Classes.TStream.WriteBuffer(TStream;void;void;Longint);
            # |
            # 0045AE60   E883AAFBFF             call    004158E8

            #output_fp.write(struct.unpack("l", audio_meta_34)[0])

            #print("Writing audio:", audio_meta_34)
            output_fp.write(audio_meta_34)


        # 0045AE65   8B45F4                 mov     eax, [ebp-$0C]
        # 
        # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
        # |
        # 0045AE68   E817A8FBFF             call    00415684

        audio_pos = audio_fp.tell()
        #print("audio position: ", audio_pos)

        premiere_iteration = False


        # 0045AE6D   52                     push    edx
        # 0045AE6E   50                     push    eax
        # 0045AE6F   8B4598                 mov     eax, [ebp-$68]
        
        # As a sweetener, this is now the preferred way to zero a register on modern x86-64 micro-architectures.
        # It doesn't require any execution units (essentially handled in the decoder), effectively eliminates stalls (waiting)
        # on the dst=src register, and breaks partial flags register stalls.
        # (https://stackoverflow.com/questions/4749585/what-is-the-meaning-of-xor-in-x86-assembly)

        # 0045AE72   33D2                   xor     edx, edx
        
        # 0045AE74   3B542404               cmp     edx, [esp+$04]
        # 0045AE78   7503                   jnz     0045AE7D                # if != 0
        # 0045AE7A   3B0424                 cmp     eax, [esp]
        # 0045AE7D   5A                     pop     edx
        # 0045AE7E   58                     pop     eax
        # 0045AE7F   75C4                   jnz     0045AE45                # if != 0
        
    # 0045AE81   8B45F4                 mov     eax, [ebp-$0C]
    # 
    # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
    # |
    # 0045AE84   E8FBA7FBFF             call    00415684

    audio_pos = audio_fp.tell()
    #print("audio position: ", audio_pos)

    # 0045AE89   8945DC                 mov     [ebp-$24], eax

    audio_meta_24_val = audio_pos   # On garde la position de la fin des entête audio ??


#### Seek jusque la position 0xD4 dans le fichier video [ebx]

# 0045AE8C   6A00                   push    $00
# 0045AE8E   68D4000000             push    $000000D4
# 0045AE93   8BC3                   mov     eax, ebx
# 
# |
# 0045AE95   E80AA8FBFF             call    004156A4
# 0045AE9A   EB70                   jmp     0045AF0C

video_fp.seek(0xD4)


video_meta_14 = bytes()
video_meta_20 = bytes()

def parse_video_infos_movi():
    global video_meta_14
    global video_meta_20

    #### Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$18]

    # 0045AE9C   8D55E8                 lea     edx, [ebp-$18]
    # 0045AE9F   B904000000             mov     ecx, $00000004
    # 0045AEA4   8BC3                   mov     eax, ebx
    # 
    # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
    # |
    # 0045AEA6   E805AAFBFF             call    004158B0

    video_buffer.append(video_fp.read(4))
    #print("video [ebp-$18]: ", video_buffer[-1])

    video_meta_18 = video_buffer[-1]


    #### Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$20]

    # 0045AEAB   8D55E0                 lea     edx, [ebp-$20]
    # 0045AEAE   B904000000             mov     ecx, $00000004
    # 0045AEB3   8BC3                   mov     eax, ebx
    # 
    # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
    # |
    # 0045AEB5   E8F6A9FBFF             call    004158B0

    video_buffer.append(video_fp.read(4))
    #print("video [ebp-$20]: ", video_buffer[-1])

    video_meta_20 = video_buffer[-1]



    #### Lecture du contenu du fichier video (ebx) : 4 byte qu'on stocke sur la stack à l'adresse [ebp-$14]

    # 0045AEBA   8D55EC                 lea     edx, [ebp-$14]
    # 0045AEBD   B904000000             mov     ecx, $00000004
    # 0045AEC2   8BC3                   mov     eax, ebx
    # 
    # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
    # |
    # 0045AEC4   E8E7A9FBFF             call    004158B0

    video_buffer.append(video_fp.read(4))
    #print("video [ebp-$14]: ", video_buffer[-1])

    video_meta_14 = video_buffer[-1]


    # 0045AEC9   8BC3                   mov     eax, ebx
    # 
    # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
    # |
    # 0045AECB   E8B4A7FBFF             call    00415684

    video_pos = video_fp.tell()
    #print("video position: ", video_pos)

    
    #### Seek jusque la position ??? dans le fichier video [ebx]

    # 0045AED0   52                     push    edx
    # 0045AED1   50                     push    eax
    # 0045AED2   8B45E0                 mov     eax, [ebp-$20]
    # 0045AED5   33D2                   xor     edx, edx            # ebx = 0
    # 0045AED7   030424                 add     eax, [esp]          # la position précédemment recup
    # 0045AEDA   13542404               adc     edx, [esp+$04]
    # 0045AEDE   83C408                 add     esp, +$08
    # 0045AEE1   83E804                 sub     eax, +$04
    # 0045AEE4   83DA00                 sbb     edx, +$00
    # 0045AEE7   52                     push    edx
    # 0045AEE8   50                     push    eax
    # 0045AEE9   8BC3                   mov     eax, ebx
    # 
    # |
    # 0045AEEB   E8B4A7FBFF             call    004156A4

    truc_video_20 = struct.unpack("l", video_meta_20)[0]
    new_video_pos = truc_video_20 + video_pos - 4

    video_fp.seek(new_video_pos)



    # XXX #### [OSEF] GUI update (ProgressBar)

    # XXX # 0045AEF0   8BC3                   mov     eax, ebx
    # XXX # 
    # XXX # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
    # XXX # |
    # XXX # 0045AEF2   E88DA7FBFF             call    00415684



    # XXX # 0045AEF7   8BD0                   mov     edx, eax
    # XXX # 0045AEF9   8B06                   mov     eax, [esi]
    # XXX # 
    # XXX # * Reference to: ComCtrls.TProgressBar.SetPosition(TProgressBar;Integer);
    # XXX # |
    # XXX # 0045AEFB   E8AC21FDFF             call    0042D0AC
    # XXX # 
    # XXX # * Reference to TApplication instance
    # XXX # |
    # XXX # 0045AF00   A158F14500             mov     eax, dword ptr [$0045F158]
    # XXX # 0045AF05   8B00                   mov     eax, [eax]
    # XXX # 
    # XXX # * Reference to: Forms.TApplication.ProcessMessages(TApplication);
    # XXX # |
    # XXX # 0045AF07   E810DBFFFF             call    00458A1C




# 0045AF0C   8D4590                 lea     eax, [ebp-$70]
# 0045AF0F   8D55EC                 lea     edx, [ebp-$14]
# 0045AF12   B904000000             mov     ecx, $00000004
# 
# * Reference to: System.@LStrFromArray(String;String;PAnsiChar;Integer);
# |
# 0045AF17   E8A091FAFF             call    004040BC
# 0045AF1C   8B4590                 mov     eax, [ebp-$70]
# 
# * Possible String Reference to: 'movi'
# |
# 0045AF1F   BA30B44500             mov     edx, $0045B430
# 
# * Reference to: System.@LStrCmp;
# |
# 0045AF24   E82F93FAFF             call    00404258
# 0045AF29   0F856DFFFFFF           jnz     0045AE9C

while video_meta_14.decode("ascii") != "movi":
    parse_video_infos_movi()



# 0045AF2F   8BC3                   mov     eax, ebx
# 
# * Reference to: Classes.TStream.GetPosition(TStream):Int64;
# |
# 0045AF31   E84EA7FBFF             call    00415684

video_pos = video_fp.tell()
#print("video position: ", video_pos)



# 0045AF36   52                     push    edx
# 0045AF37   50                     push    eax
# 0045AF38   8B45E0                 mov     eax, [ebp-$20]
# 0045AF3B   33D2                   xor     edx, edx
# 0045AF3D   290424                 sub     dword ptr [esp], eax        # On modifie la dernière valeur de la stack (ici, normalement la position du fichier) -> du coup ça modifie direct la valeur d'eax qu'on a push juste avant !! (et qu'on va repop après)
# 0045AF40   19542404               sbb     [esp+$04], edx
# 0045AF44   58                     pop     eax
# 0045AF45   5A                     pop     edx
# 0045AF46   83C004                 add     eax, +$04
# 0045AF49   83D200                 adc     edx, +$00
# 0045AF4C   52                     push    edx
# 0045AF4D   50                     push    eax
# 0045AF4E   8BC3                   mov     eax, ebx
# 
# |
# 0045AF50   E84FA7FBFF             call    004156A4

truc_video_20 = struct.unpack("l", video_meta_20)[0]
new_video_pos = video_pos - truc_video_20 + 4

video_fp.seek(new_video_pos)



####### ON EN EST A ICI #######


# Allocation d'un tableau ?   <-- Tableau probablement un pointeur !
# C'est pour ça qu'il reçoit pas de valeur. On utilise son adresse pour aller taper dedans.


# 0045AF55   6A01                   push    $01
# 0045AF57   8D45C4                 lea     eax, [ebp-$3C]
# 0045AF5A   B901000000             mov     ecx, $00000001
# 
# * Reference to object .4
# |
# 0045AF5F   8B15FCAB4500           mov     edx, [$0045ABFC]
# 
# * Reference to: System.@DynArraySetLength;
# |
# 0045AF65   E8C29EFAFF             call    00404E2C



# 0045AF6A   83C404                 add     esp, +$04
# 0045AF6D   C745C801000000         mov     dword ptr [ebp-$38], $00000001      # <-- on initialise la taille de la table avec le premier element
# 0045AF74   E9C1030000             jmp     0045B33A

array_3c = [None]


if video_meta_14 != "idx1":
    """ go en 0045AF79 """
    stop = False
else:
    stop = True


while not stop:
    # 
    # * Reference to TApplication instance
    # |
    # 0045AF79   A158F14500             mov     eax, dword ptr [$0045F158]
    # 0045AF7E   8B00                   mov     eax, [eax]
    # 
    # * Reference to: Forms.TApplication.ProcessMessages(TApplication);
    # |
    # 0045AF80   E897DAFFFF             call    00458A1C



    # XXX #### [OSEF] GUI update (ProgressBar)
    # XXX 
    # XXX # 0045AF85   8BC3                   mov     eax, ebx
    # XXX # 
    # XXX # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
    # XXX # |
    # XXX # 0045AF87   E8F8A6FBFF             call    00415684
    # XXX # 0045AF8C   8BD0                   mov     edx, eax
    # XXX # 0045AF8E   8B06                   mov     eax, [esi]
    # XXX # 
    # XXX # * Reference to: ComCtrls.TProgressBar.SetPosition(TProgressBar;Integer);
    # XXX # |
    # XXX # 0045AF90   E81721FDFF             call    0042D0AC



    #### Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$14]

    # 0045AF95   8D55EC                 lea     edx, [ebp-$14]
    # 0045AF98   B904000000             mov     ecx, $00000004
    # 0045AF9D   8BC3                   mov     eax, ebx
    # 
    # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
    # |
    # 0045AF9F   E80CA9FBFF             call    004158B0

    video_buffer.append(video_fp.read(4))
    #print("video [ebp-$14]:", video_buffer[-1])

    video_meta_14 = video_buffer[-1]


    #### Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$2C]

    # 0045AFA4   8D55D4                 lea     edx, [ebp-$2C]
    # 0045AFA7   B904000000             mov     ecx, $00000004
    # 0045AFAC   8BC3                   mov     eax, ebx
    # 
    # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
    # |
    # 0045AFAE   E8FDA8FBFF             call    004158B0

    video_buffer.append(video_fp.read(4))
    #print("video [ebp-$2C]:", video_buffer[-1])

    video_meta_2c = video_buffer[-1]


    # 0045AFB3   8D458C                 lea     eax, [ebp-$74]
    # 0045AFB6   8D55EC                 lea     edx, [ebp-$14]
    # 0045AFB9   B904000000             mov     ecx, $00000004
    # 
    # * Reference to: System.@LStrFromArray(String;String;PAnsiChar;Integer);
    # |
    # 0045AFBE   E8F990FAFF             call    004040BC
    # 0045AFC3   8B458C                 mov     eax, [ebp-$74]
    # 
    # * Possible String Reference to: 'idx1'
    # |
    # 0045AFC6   BA40B44500             mov     edx, $0045B440
    # 
    # * Reference to: System.@LStrCmp;
    # |
    # 0045AFCB   E88892FAFF             call    00404258
    # 0045AFD0   0F84A0020000           jz      0045B276

    """ sinon go en 0045B276 """

    la_path_interdite = False
    skip_not_path_interdite = False
    
    if video_meta_14.decode("ascii") != "idx1":

        # 0045AFD6   8D4588                 lea     eax, [ebp-$78]
        # 0045AFD9   8D55EC                 lea     edx, [ebp-$14]
        # 0045AFDC   B904000000             mov     ecx, $00000004
        # 
        # * Reference to: System.@LStrFromArray(String;String;PAnsiChar;Integer);
        # |
        # 0045AFE1   E8D690FAFF             call    004040BC
        # 0045AFE6   8B4588                 mov     eax, [ebp-$78]
        # 
        # * Possible String Reference to: '00dc'
        # |
        # 0045AFE9   BA50B44500             mov     edx, $0045B450
        # 
        # * Reference to: System.@LStrCmp;
        # |
        # 0045AFEE   E86592FAFF             call    00404258
        # 0045AFF3   746B                   jz      0045B060

        """ sinon go en 0045B060 """
        if video_meta_14.decode("ascii") != "00dc":

            # 0045AFF5   8D4584                 lea     eax, [ebp-$7C]
            # 0045AFF8   8D55EC                 lea     edx, [ebp-$14]
            # 0045AFFB   B904000000             mov     ecx, $00000004
            # 
            # * Reference to: System.@LStrFromArray(String;String;PAnsiChar;Integer);
            # |
            # 0045B000   E8B790FAFF             call    004040BC
            # 0045B005   8B4584                 mov     eax, [ebp-$7C]
            # 
            # * Possible String Reference to: '01wb'
            # |
            # 0045B008   BA60B44500             mov     edx, $0045B460
            # 
            # * Reference to: System.@LStrCmp;
            # |
            # 0045B00D   E84692FAFF             call    00404258
            # 0045B012   7518                   jnz     0045B02C

            """ sinon, go 0045B02C """

            if video_meta_14.decode("ascii") == "01wb":
                    
                # 0045B014   8BC3                   mov     eax, ebx
                # 
                # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
                # |
                # 0045B016   E869A6FBFF             call    00415684

                video_pos = video_fp.tell()
                #print("video position: ", video_pos)


                # 0045B01B   83E808                 sub     eax, +$08
                # 0045B01E   83DA00                 sbb     edx, +$00
                # 0045B021   52                     push    edx
                # 0045B022   50                     push    eax
                # 0045B023   8BC3                   mov     eax, ebx
                # 
                # |
                # 0045B025   E87AA6FBFF             call    004156A4

                video_fp.seek(video_pos - 8)


                # 0045B02A   EB16                   jmp     0045B042

            else:

                # 0045B02C   8BC3                   mov     eax, ebx
                # 
                # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
                # |
                # 0045B02E   E851A6FBFF             call    00415684

                video_pos = video_fp.tell()
                #print("video position: ", video_pos)


                # 0045B033   83E807                 sub     eax, +$07
                # 0045B036   83DA00                 sbb     edx, +$00
                # 0045B039   52                     push    edx
                # 0045B03A   50                     push    eax
                # 0045B03B   8BC3                   mov     eax, ebx
                # 
                # |
                # 0045B03D   E862A6FBFF             call    004156A4

                video_fp.seek(video_pos - 7)


            #### Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$14]

            # 0045B042   8D55EC                 lea     edx, [ebp-$14]
            # 0045B045   B904000000             mov     ecx, $00000004
            # 0045B04A   8BC3                   mov     eax, ebx
            # 
            # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
            # |
            # 0045B04C   E85FA8FBFF             call    004158B0

            video_buffer.append(video_fp.read(4))
            #print("video [ebp-$14]:", video_buffer[-1])

            video_meta_14 = video_buffer[-1]


            #### Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$2C]

            # 0045B051   8D55D4                 lea     edx, [ebp-$2C]
            # 0045B054   B904000000             mov     ecx, $00000004
            # 0045B059   8BC3                   mov     eax, ebx
            # 
            # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
            # |
            # 0045B05B   E850A8FBFF             call    004158B0

            video_buffer.append(video_fp.read(4))
            #print("video [ebp-$2C]:", video_buffer[-1])

            video_meta_2c = video_buffer[-1]


        # 0045B060   8D4580                 lea     eax, [ebp-$80]
        # 0045B063   8D55EC                 lea     edx, [ebp-$14]
        # 0045B066   B904000000             mov     ecx, $00000004
        # 
        # * Reference to: System.@LStrFromArray(String;String;PAnsiChar;Integer);
        # |
        # 0045B06B   E84C90FAFF             call    004040BC
        # 0045B070   8B4580                 mov     eax, [ebp-$80]
        # 
        # * Possible String Reference to: '00dc'
        # |
        # 0045B073   BA50B44500             mov     edx, $0045B450
        # 
        # * Reference to: System.@LStrCmp;
        # |
        # 0045B078   E8DB91FAFF             call    00404258
        # 0045B07D   7429                   jz      0045B0A8

        do_skip = False
        
        """ sinon, go 0045B0A8 """

        if video_meta_14.decode("ascii") != "00dc":

            # 0045B07F   8D857CFFFFFF           lea     eax, [ebp+$FFFFFF7C]
            # 0045B085   8D55EC                 lea     edx, [ebp-$14]
            # 0045B088   B904000000             mov     ecx, $00000004
            # 
            # * Reference to: System.@LStrFromArray(String;String;PAnsiChar;Integer);
            # |
            # 0045B08D   E82A90FAFF             call    004040BC
            # 0045B092   8B857CFFFFFF           mov     eax, [ebp+$FFFFFF7C]
            # 
            # * Possible String Reference to: 'idx1'
            # |
            # 0045B098   BA40B44500             mov     edx, $0045B440
            # 
            # * Reference to: System.@LStrCmp;
            # |
            # 0045B09D   E8B691FAFF             call    00404258
            # 0045B0A2   0F8557010000           jnz     0045B1FF

            if video_meta_14.decode("ascii") != "idx1":
                """ go en 0045B1FF """

                la_path_interdite = True
                do_skip = True
        
        
        if not do_skip:

            # 0045B0A8   8B45F0                 mov     eax, [ebp-$10]
            # 
            # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
            # |
            # 0045B0AB   E8D4A5FBFF             call    00415684

            output_pos = output_fp.tell()
            #print("output position: ", output_pos)


            # 0045B0B0   8B55C4                 mov     edx, [ebp-$3C]              # <-- Ref vers le tableau
            # 0045B0B3   8B4DC8                 mov     ecx, [ebp-$38]              # <-- Taille du tableau ?
            # 0045B0B6   89448AFC               mov     [edx+ecx*4-$04], eax

            array_3c[-1] = output_pos


            # 0045B0BA   B904000000             mov     ecx, $00000004
            # 
            # * Possible String Reference to: 'MV0F'
            # |
            # 0045B0BF   BA70B44500             mov     edx, $0045B470
            # 0045B0C4   8B45F0                 mov     eax, [ebp-$10]
            # 
            # * Reference to: Classes.TStream.WriteBuffer(TStream;void;void;Longint);
            # |
            # 0045B0C7   E81CA8FBFF             call    004158E8

            #print("Writing video:", b'MV0F')
            output_fp.write(b'MV0F')


            # 0045B0CC   8B45D4                 mov     eax, [ebp-$2C]     = b'8\x00\x00\x00'
            # 0045B0CF   83C008                 add     eax, +$08
            # 0045B0D2   8945E4                 mov     [ebp-$1C], eax

            #video_meta_1c = struct.unpack("l", video_meta_2c)[0] + 0x08


            # 0045B0D5   8D55E4                 lea     edx, [ebp-$1C]
            # 0045B0D8   B904000000             mov     ecx, $00000004
            # 0045B0DD   8B45F0                 mov     eax, [ebp-$10]
            # 
            # * Reference to: Classes.TStream.WriteBuffer(TStream;void;void;Longint);
            # |
            # 0045B0E0   E803A8FBFF             call    004158E8

            #utput_fp.write(struct.unpack("l", video_meta_1c)[0])

            #video_meta_1c_to_write = (struct.unpack("l", b'e\x0e\x00\x00')[0] + 0x08).to_bytes(4, 'little')
            video_meta_1c_to_write = (struct.unpack("l", video_meta_2c)[0] + 0x08).to_bytes(4, 'little')
            
            #print("Writing video: ", video_meta_1c_to_write)
            output_fp.write(video_meta_1c_to_write)


            # 0045B0E5   8B45D4                 mov     eax, [ebp-$2C]
            # 0045B0E8   33D2                   xor     edx, edx
            # 0045B0EA   52                     push    edx
            # 0045B0EB   50                     push    eax
            # 0045B0EC   8BD3                   mov     edx, ebx
            # 0045B0EE   8B45F0                 mov     eax, [ebp-$10]
            # 
            # * Reference to: Classes.TStream.CopyFrom(TStream;TStream;Int64):Int64;
            # |
            # 0045B0F1   E82AA8FBFF             call    00415920

            video_meta_2c_val = struct.unpack("l", video_meta_2c)[0]
            stuff_to_write = video_fp.read(video_meta_2c_val)       
            #print("Writing (CopyFrom) video: ", stuff_to_write)     
            output_fp.write(stuff_to_write)                         


            # 0045B0F6   8B4508                 mov     eax, [ebp+$08]
            # 
            # * Possible String Reference to: 'none~'
            # |
            # 0045B0F9   BA1CB44500             mov     edx, $0045B41C
            # 
            # * Reference to: System.@LStrCmp;
            # |
            # 0045B0FE   E85591FAFF             call    00404258
            # 0045B103   0F84CE000000           jz      0045B1D7

            if audio:

                # 0045B109   8B45F4                 mov     eax, [ebp-$0C]     # |
                # 0045B10C   8B10                   mov     edx, [eax]         # |
                # 0045B10E   FF12                   call    dword ptr [edx]    # | <-- Récupération de la taille totale du fichier
                # 0045B110   52                     push    edx
                # 0045B111   50                     push    eax
                # 0045B112   8B45F4                 mov     eax, [ebp-$0C]
                # 
                # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
                # |
                # 0045B115   E86AA5FBFF             call    00415684

                audio_pos = audio_fp.tell()
                #print("audio position: ", audio_pos)


                # 0045B11A   3B542404               cmp     edx, [esp+$04]
                # 0045B11E   7503                   jnz     0045B123
                # 0045B120   3B0424                 cmp     eax, [esp]         # <-- On teste entre la position actuelle du fichier audio et sa taille totale.
                # 0045B123   5A                     pop     edx
                # 0045B124   58                     pop     eax
                # 0045B125   0F84AC000000           jz      0045B1D7
                
                if audio_file_size != audio_pos:
                    
                    # XXX # * Reference to TApplication instance
                    # XXX # |
                    # XXX # 0045B12B   A158F14500             mov     eax, dword ptr [$0045F158]
                    # XXX # 0045B130   8B00                   mov     eax, [eax]
                    # XXX # 
                    # XXX # * Reference to: Forms.TApplication.ProcessMessages(TApplication);
                    # XXX # |
                    # XXX # 0045B132   E8E5D8FFFF             call    00458A1C
                    # XXX # 0045B137   8B45F4                 mov     eax, [ebp-$0C]
                    # XXX # 
                    # XXX # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
                    # XXX # |
                    # XXX # 0045B13A   E845A5FBFF             call    00415684



                    # XXX #### [OSEF] GUI update (ProgressBar)
                    # XXX 
                    # XXX # 0045B13F   8BD0                   mov     edx, eax
                    # XXX # 0045B141   8B45FC                 mov     eax, [ebp-$04]
                    # XXX # 0045B144   8B00                   mov     eax, [eax]
                    # XXX # 
                    # XXX # * Reference to: ComCtrls.TProgressBar.SetPosition(TProgressBar;Integer);
                    # XXX # |
                    # XXX # 0045B146   E8611FFDFF             call    0042D0AC



                    #### Lecture du contenu du fichier audio (ebp-$0C) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$6C]

                    # 0045B14B   8D5594                 lea     edx, [ebp-$6C]
                    # 0045B14E   B904000000             mov     ecx, $00000004
                    # 0045B153   8B45F4                 mov     eax, [ebp-$0C]
                    # 
                    # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
                    # |
                    # 0045B156   E855A7FBFF             call    004158B0

                    audio_buffer.append(audio_fp.read(4))
                    #print("audio: ", audio_buffer[-1])

                    audio_meta_6c = audio_buffer[-1]

                    #### Lecture du contenu du fichier audio (ebp-$0C) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$68]

                    # 0045B15B   8D5598                 lea     edx, [ebp-$68]
                    # 0045B15E   B904000000             mov     ecx, $00000004
                    # 0045B163   8B45F4                 mov     eax, [ebp-$0C]
                    # 
                    # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
                    # |
                    # 0045B166   E845A7FBFF             call    004158B0

                    audio_buffer.append(audio_fp.read(4))
                    #print("audio: ", audio_buffer[-1])

                    audio_meta_68 = audio_buffer[-1]

                    # 0045B16B   8D5594                 lea     edx, [ebp-$6C]
                    # 0045B16E   B904000000             mov     ecx, $00000004
                    # 0045B173   8B45F0                 mov     eax, [ebp-$10]
                    # 
                    # * Reference to: Classes.TStream.WriteBuffer(TStream;void;void;Longint);
                    # |
                    # 0045B176   E86DA7FBFF             call    004158E8

                    #output_fp.write(struct.unpack("l", audio_meta_6c)[0])

                    #print("Writing audio:", audio_meta_6c)
                    output_fp.write(audio_meta_6c)

                    # 0045B17B   8D5598                 lea     edx, [ebp-$68]
                    # 0045B17E   B904000000             mov     ecx, $00000004
                    # 0045B183   8B45F0                 mov     eax, [ebp-$10]
                    # 
                    # * Reference to: Classes.TStream.WriteBuffer(TStream;void;void;Longint);
                    # |
                    # 0045B186   E85DA7FBFF             call    004158E8

                    #output_fp.write(struct.unpack("l", audio_meta_68)[0])

                    #print("Writing audio:", audio_meta_68)
                    output_fp.write(audio_meta_68)

                    # 0045B18B   EB20                   jmp     0045B1AD

                    premiere_iteration = True

                    stop2 = False

                    while not stop2:
                        if not premiere_iteration:
                            #### Lecture du contenu du fichier audio (ebp-$0C) : 1 byte qu'on stocke sur la stack à l'adresse [ebp-$34]

                            # 0045B18D   8D55CC                 lea     edx, [ebp-$34]
                            # 0045B190   B901000000             mov     ecx, $00000001
                            # 0045B195   8B45F4                 mov     eax, [ebp-$0C]
                            # 
                            # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
                            # |
                            # 0045B198   E813A7FBFF             call    004158B0

                            audio_buffer.append(audio_fp.read(1))
                            #print("audio: ", audio_buffer[-1])

                            audio_meta_34 = audio_buffer[-1]

                            # 0045B19D   8D55CC                 lea     edx, [ebp-$34]
                            # 0045B1A0   B901000000             mov     ecx, $00000001
                            # 0045B1A5   8B45F0                 mov     eax, [ebp-$10]
                            # 
                            # * Reference to: Classes.TStream.WriteBuffer(TStream;void;void;Longint);
                            # |
                            # 0045B1A8   E83BA7FBFF             call    004158E8

                            #output_fp.write(struct.unpack("l", audio_meta_34)[0])
                            #print("Writing audio:", audio_meta_34)
                            output_fp.write(audio_meta_34)

                        premiere_iteration = False


                        # 0045B1AD   8B45F4                 mov     eax, [ebp-$0C]
                        # 
                        # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
                        # |
                        # 0045B1B0   E8CFA4FBFF             call    00415684

                        audio_pos = audio_fp.tell()
                        #print("audio position: ", audio_pos)


                        # 0045B1B5   52                     push    edx
                        # 0045B1B6   50                     push    eax
                        # 0045B1B7   8B45DC                 mov     eax, [ebp-$24]
                        # 0045B1BA   034598                 add     eax, [ebp-$68]

                        audio_meta_68_val = struct.unpack("l", audio_meta_68)[0]
                        audio_pos_goal = audio_meta_24_val + audio_meta_68_val

                        # 0045B1BD   33D2                   xor     edx, edx
                        # 0045B1BF   3B542404               cmp     edx, [esp+$04]  #     = edx précédemment pushed
                        # 0045B1C3   7503                   jnz     0045B1C8
                        # 0045B1C5   3B0424                 cmp     eax, [esp]      # <-- On compare la position en cours dans le fichier audio ([esp])
                        # 0045B1C8   5A                     pop     edx             #     avec audio_pos_goal
                        # 0045B1C9   58                     pop     eax
                        # 0045B1CA   75C1                   jnz     0045B18D

                        if audio_pos_goal == audio_pos:
                            stop2 = True


                    # 0045B1CC   8B45F4                 mov     eax, [ebp-$0C]
                    # 
                    # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
                    # |
                    # 0045B1CF   E8B0A4FBFF             call    00415684

                    audio_pos = audio_fp.tell()
                    #print("audio position: ", audio_pos)

                    # 0045B1D4   8945DC                 mov     [ebp-$24], eax

                    audio_meta_24_val = audio_pos   # On garde la position de la fin des entête audio ??


            # 0045B1D7   FF45C8                 inc     dword ptr [ebp-$38]
            # 0045B1DA   8B45C4                 mov     eax, [ebp-$3C]
            # 
            # * Reference to: System.@LStrLen(String):Integer;
            # |
            # 0045B1DD   E88E9AFAFF             call    00404C70

            taille_3c = len(array_3c)

            # 0045B1E2   40                     inc     eax
            # 0045B1E3   50                     push    eax
            # 0045B1E4   8D45C4                 lea     eax, [ebp-$3C]
            # 0045B1E7   B901000000             mov     ecx, $00000001
            # 
            # * Reference to object .4
            # |
            # 0045B1EC   8B15FCAB4500           mov     edx, [$0045ABFC]
            # 
            # * Reference to: System.@DynArraySetLength;
            # |
            # 0045B1F2   E8359CFAFF             call    00404E2C
            # 0045B1F7   83C404                 add     esp, +$04


            # 0045B1FA   E93B010000             jmp     0045B33A

            array_3c.append(None)

            skip_not_path_interdite = True

        if la_path_interdite:
            
            # 0045B1FF   8BC3                   mov     eax, ebx
            # 
            # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
            # |
            # 0045B201   E87EA4FBFF             call    00415684

            video_pos = video_fp.tell()
            #print("video position: ", video_pos)


            #### Seek

            # 0045B206   52                     push    edx
            # 0045B207   50                     push    eax
            # 0045B208   8B45D4                 mov     eax, [ebp-$2C]
            # 0045B20B   33D2                   xor     edx, edx
            # 0045B20D   030424                 add     eax, [esp]
            # 0045B210   13542404               adc     edx, [esp+$04]
            # 0045B214   83C408                 add     esp, +$08         # | <-- On dirait qu'on cancel les 2 derniers éléments de la pile
            # 0045B217   52                     push    edx               # |     pour les réécrire
            # 0045B218   50                     push    eax               # |
            # 0045B219   8BC3                   mov     eax, ebx
            # 
            # |
            # 0045B21B   E884A4FBFF             call    004156A4
            
            video_meta_2c_val =  struct.unpack("l", video_meta_2c)[0]
            video_fp.seek(video_meta_2c_val + video_pos)


            # 0045B220   8B45F0                 mov     eax, [ebp-$10]
            # 
            # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
            # |
            # 0045B223   E85CA4FBFF             call    00415684

            output_pos = output_fp.tell()
            #print("output position: ", output_pos)



            # 0045B228   8B55C4                 mov     edx, [ebp-$3C]
            # 0045B22B   8B4DC8                 mov     ecx, [ebp-$38]
            # 0045B22E   89448AFC               mov     [edx+ecx*4-$04], eax

            array_3c[-1] = output_pos


            # 0045B232   FF45C8                 inc     dword ptr [ebp-$38]
            # 0045B235   8B45C4                 mov     eax, [ebp-$3C]
            # 
            # * Reference to: System.@LStrLen(String):Integer;
            # |
            # 0045B238   E8339AFAFF             call    00404C70
            
            len_array_3c = len(array_3c)        # Probablement inutile car je suppsoe que c'est pour incrémenter la valeur de la taille de l'array stockée en première valeur de celle-ci


            # 0045B23D   40                     inc     eax                 # |-- nouvelle taille array
            # 0045B23E   50                     push    eax                 # | 
            # 0045B23F   8D45C4                 lea     eax, [ebp-$3C]      # <-- array(/str?) à resize
            # 0045B242   B901000000             mov     ecx, $00000001
            # 
            # * Reference to object .4
            # |
            # 0045B247   8B15FCAB4500           mov     edx, [$0045ABFC]    # <-- type/class d'array?
            # 
            # * Reference to: System.@DynArraySetLength;
            # |
            # 0045B24D   E8DA9BFAFF             call    00404E2C

            array_3c.append(None)


            # 0045B252   83C404                 add     esp, +$04
            # 
            # * Reference to TApplication instance
            # |
            # 0045B255   A158F14500             mov     eax, dword ptr [$0045F158]
            # 0045B25A   8B00                   mov     eax, [eax]
            # 
            # * Reference to: Forms.TApplication.ProcessMessages(TApplication);
            # |
            # 0045B25C   E8BBD7FFFF             call    00458A1C
            # 0045B261   8BC3                   mov     eax, ebx
            # 
            # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
            # |
            # 0045B263   E81CA4FBFF             call    00415684

            video_pos = video_fp.tell()
            #print("video position: ", video_pos)


            # XXX #### [OSEF] GUI update (ProgressBar)
            # XXX 
            # XXX # 0045B268   8BD0                   mov     edx, eax
            # XXX # 0045B26A   8B06                   mov     eax, [esi]
            # XXX # 
            # XXX # * Reference to: ComCtrls.TProgressBar.SetPosition(TProgressBar;Integer);
            # XXX # |
            # XXX # 0045B26C   E83B1EFDFF             call    0042D0AC



            # 0045B271   E9C4000000             jmp     0045B33A


    if not la_path_interdite and not skip_not_path_interdite:
        # 0045B276   8B45C4                 mov     eax, [ebp-$3C]
        # 
        # * Reference to: System.@LStrLen(String):Integer;
        # |
        # 0045B279   E8F299FAFF             call    00404C70

        len_array_3c = len(array_3c)

        # 0045B27E   8BF8                   mov     edi, eax

        i = len_array_3c

        # 0045B280   4F                     dec     edi

        i -= 1

        # 0045B281   85FF                   test    edi, edi
        # 0045B283   0F8EB1000000           jle     0045B33A

        if not (i <= 0):
        
            # 0045B289   C745D001000000         mov     dword ptr [ebp-$30], $00000001

            compteur_30 = 1

            stop_in_stop = False

            while not stop_in_stop:
                #### Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$28]

                # 0045B290   8D55D8                 lea     edx, [ebp-$28]
                # 0045B293   B904000000             mov     ecx, $00000004
                # 0045B298   8BC3                   mov     eax, ebx
                # 
                # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
                # |
                # 0045B29A   E811A6FBFF             call    004158B0

                video_buffer.append(video_fp.read(4))
                #print("video [ebp-$28]:", video_buffer[-1])
                
                video_meta_28 = video_buffer[-1]

                # XXX #### [OSEF] GUI update (TApplication.ProcessMessages)
                # XXX 
                # XXX # * Reference to TApplication instance
                # XXX # |
                # XXX # 0045B29F   A158F14500             mov     eax, dword ptr [$0045F158]
                # XXX # 0045B2A4   8B00                   mov     eax, [eax]
                # XXX # 
                # XXX # * Reference to: Forms.TApplication.ProcessMessages(TApplication);
                # XXX # |
                # XXX # 0045B2A6   E871D7FFFF             call    00458A1C
                # XXX 
                # XXX 
                # XXX 
                # XXX # 0045B2AB   8BC3                   mov     eax, ebx
                # XXX # 
                # XXX # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
                # XXX # |
                # XXX # 0045B2AD   E8D2A3FBFF             call    00415684
                # XXX 
                # XXX 
                # XXX 
                # XXX #### [OSEF] GUI update (ProgressBar)
                # XXX 
                # XXX # 0045B2B2   8BD0                   mov     edx, eax
                # XXX # 0045B2B4   8B06                   mov     eax, [esi]
                # XXX # 
                # XXX # * Reference to: ComCtrls.TProgressBar.SetPosition(TProgressBar;Integer);
                # XXX # |
                # XXX # 0045B2B6   E8F11DFDFF             call    0042D0AC


                # 0045B2BB   817DD830306463         cmp     dword ptr [ebp-$28], $63643030
                # 0045B2C2   753F                   jnz     0045B303

                """ sinon on jump à 0045B303 """

                if video_meta_28.decode("ascii") == "00dc":

                    #### Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$28]

                    # 0045B2C4   8D55D8                 lea     edx, [ebp-$28]
                    # 0045B2C7   B904000000             mov     ecx, $00000004
                    # 0045B2CC   8BC3                   mov     eax, ebx
                    # 
                    # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
                    # |
                    # 0045B2CE   E8DDA5FBFF             call    004158B0

                    video_buffer.append(video_fp.read(4))
                    #print("video [ebp-$28]:", video_buffer[-1])

                    video_meta_28 = video_buffer[-1]

                    # TEST si la valeur qu'on vient de lire est différente de 10 alors on jump à 0045B312

                    # 0045B2D3   837DD810               cmp     dword ptr [ebp-$28], +$10
                    # 0045B2D7   7539                   jnz     0045B312

                    video_meta_28_val = struct.unpack("l", video_meta_28)[0]

                    if video_meta_28_val == 0x10:
                        
                        #### Seek

                        # 0045B2D9   8B45C4                 mov     eax, [ebp-$3C]
                        # 0045B2DC   8B55D0                 mov     edx, [ebp-$30]
                        # 0045B2DF   8B4490FC               mov     eax, [eax+edx*4-$04]
                        # 0045B2E3   33D2                   xor     edx, edx
                        # 0045B2E5   52                     push    edx
                        # 0045B2E6   50                     push    eax
                        # 0045B2E7   8B45F0                 mov     eax, [ebp-$10]
                        # 
                        # |
                        # 0045B2EA   E8B5A3FBFF             call    004156A4

                        new_pos = array_3c[compteur_30-1]

                        output_fp.seek(new_pos)


                        # 0045B2EF   B904000000             mov     ecx, $00000004
                        # 
                        # * Possible String Reference to: 'MV0K'
                        # |
                        # 0045B2F4   BA80B44500             mov     edx, $0045B480
                        # 0045B2F9   8B45F0                 mov     eax, [ebp-$10]
                        # 
                        # * Reference to: Classes.TStream.WriteBuffer(TStream;void;void;Longint);
                        # |
                        # 0045B2FC   E8E7A5FBFF             call    004158E8

                        #print("Writing video:", b"MV0K")
                        output_fp.write(b"MV0K")

                        # 0045B301   EB0F                   jmp     0045B312

                else:

                    #### Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$28]

                    # 0045B303   8D55D8                 lea     edx, [ebp-$28]
                    # 0045B306   B904000000             mov     ecx, $00000004
                    # 0045B30B   8BC3                   mov     eax, ebx
                    # 
                    # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
                    # |
                    # 0045B30D   E89EA5FBFF             call    004158B0

                    video_buffer.append(video_fp.read(4))
                    #print("video [ebp-$28]:", video_buffer[-1])

                    video_meta_28 = video_buffer[-1]



                #### Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$28]

                # 0045B312   8D55D8                 lea     edx, [ebp-$28]
                # 0045B315   B904000000             mov     ecx, $00000004
                # 0045B31A   8BC3                   mov     eax, ebx
                # 
                # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
                # |
                # 0045B31C   E88FA5FBFF             call    004158B0

                video_buffer.append(video_fp.read(4))
                #print("video [ebp-$28]:", video_buffer[-1])

                video_meta_28 = video_buffer[-1]


                #### Lecture du contenu du fichier video (ebx) : 4 bytes qu'on stocke sur la stack à l'adresse [ebp-$28]

                # 0045B321   8D55D8                 lea     edx, [ebp-$28]
                # 0045B324   B904000000             mov     ecx, $00000004
                # 0045B329   8BC3                   mov     eax, ebx
                # 
                # * Reference to: Classes.TStream.ReadBuffer(TStream;void;void;Longint);
                # |
                # 0045B32B   E880A5FBFF             call    004158B0

                video_buffer.append(video_fp.read(4))
                #print("video [ebp-$28]:", video_buffer[-1])

                video_meta_28 = video_buffer[-1]


                # 0045B330   FF45D0                 inc     dword ptr [ebp-$30]
                # 0045B333   4F                     dec     edi                     # | le compteur est à 0 ? si oui on casse la boucle
                # 0045B334   0F8556FFFFFF           jnz     0045B290                # |

                compteur_30 += 1

                i -= 1

                if i == 0:
                    stop_in_stop = True



    # 0045B33A   8D8578FFFFFF           lea     eax, [ebp+$FFFFFF78]
    # 0045B340   8D55EC                 lea     edx, [ebp-$14]
    # 0045B343   B904000000             mov     ecx, $00000004
    # 
    # * Reference to: System.@LStrFromArray(String;String;PAnsiChar;Integer);
    # |
    # 0045B348   E86F8DFAFF             call    004040BC
    # 0045B34D   8B8578FFFFFF           mov     eax, [ebp+$FFFFFF78]
    # 
    # * Possible String Reference to: 'idx1'
    # |
    # 0045B353   BA40B44500             mov     edx, $0045B440
    # 
    # * Reference to: System.@LStrCmp;
    # |
    # 0045B358   E8FB8EFAFF             call    00404258
    # 0045B35D   0F8516FCFFFF           jnz     0045AF79

    if video_meta_14.decode("ascii") != "idx1":
        """ go en 0045AF79 """
        stop = False
    else:
        stop = True




#### [OSEF] GUI update (ProgressBar)

# XXX # 0045B363   8BC3                   mov     eax, ebx
# XXX # 
# XXX # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
# XXX # |
# XXX # 0045B365   E81AA3FBFF             call    00415684

# XXX # 0045B36A   8BD0                   mov     edx, eax
# XXX # 0045B36C   8B06                   mov     eax, [esi]
# XXX # 
# XXX # * Reference to: ComCtrls.TProgressBar.SetPosition(TProgressBar;Integer);
# XXX # |
# XXX # 0045B36E   E8391DFDFF             call    0042D0AC



# 0045B373   8BC3                   mov     eax, ebx
# 
# * Reference to: System.TObject.Free(TObject);
# |
# 0045B375   E8827DFAFF             call    004030FC


if audio:
    # 0045B37A   8B4508                 mov     eax, [ebp+$08]
    # 
    # * Possible String Reference to: 'none~'
    # |
    # 0045B37D   BA1CB44500             mov     edx, $0045B41C
    # 
    # * Reference to: System.@LStrCmp;
    # |
    # 0045B382   E8D18EFAFF             call    00404258
    # 0045B387   741C                   jz      0045B3A5
    # 0045B389   8B45F4                 mov     eax, [ebp-$0C]
    # 
    # * Reference to: Classes.TStream.GetPosition(TStream):Int64;
    # |
    # 0045B38C   E8F3A2FBFF             call    00415684

    audio_pos = audio_fp.tell()
    #print("audio position: ", audio_pos)


    #### [OSEF] GUI update (ProgressBar)

    # 0045B391   8BD0                   mov     edx, eax
    # 0045B393   8B45FC                 mov     eax, [ebp-$04]
    # 0045B396   8B00                   mov     eax, [eax]
    # 
    # * Reference to: ComCtrls.TProgressBar.SetPosition(TProgressBar;Integer);
    # |
    # 0045B398   E80F1DFDFF             call    0042D0AC



    # 0045B39D   8B45F4                 mov     eax, [ebp-$0C]
    # 
    # * Reference to: System.TObject.Free(TObject);
    # |
    # 0045B3A0   E8577DFAFF             call    004030FC



# 0045B3A5   8B45F0                 mov     eax, [ebp-$10]
# 
# * Reference to: System.TObject.Free(TObject);
# |
# 0045B3A8   E84F7DFAFF             call    004030FC



# XXX #### [OSEF] GUI update (ProgressBar)
# XXX 
# XXX # 0045B3AD   8B45FC                 mov     eax, [ebp-$04]
# XXX # 0045B3B0   8B00                   mov     eax, [eax]
# XXX # 0045B3B2   33D2                   xor     edx, edx
# XXX # 
# XXX # * Reference to: ComCtrls.TProgressBar.SetPosition(TProgressBar;Integer);
# XXX # |
# XXX # 0045B3B4   E8F31CFDFF             call    0042D0AC



# XXX #### [OSEF] GUI update (ProgressBar)
# XXX 
# XXX # 0045B3B9   8B06                   mov     eax, [esi]
# XXX # 0045B3BB   33D2                   xor     edx, edx
# XXX # 
# XXX # * Reference to: ComCtrls.TProgressBar.SetPosition(TProgressBar;Integer);
# XXX # |
# XXX # 0045B3BD   E8EA1CFDFF             call    0042D0AC



# 0045B3C2   33C0                   xor     eax, eax
# 0045B3C4   5A                     pop     edx
# 0045B3C5   59                     pop     ecx
# 0045B3C6   59                     pop     ecx
# 0045B3C7   648910                 mov     fs:[eax], edx
# 
# ****** FINALLY
# |
# 0045B3CA   680AB44500             push    $0045B40A
# 0045B3CF   8D8578FFFFFF           lea     eax, [ebp+$FFFFFF78]
# 0045B3D5   BA07000000             mov     edx, $00000007
# 
# * Reference to: System.@LStrArrayClr(void;void;Integer);
# |
# 0045B3DA   E8918AFAFF             call    00403E70
# 0045B3DF   8D45C4                 lea     eax, [ebp-$3C]
# 
# * Reference to object .4
# |
# 0045B3E2   8B15FCAB4500           mov     edx, [$0045ABFC]
# 
# * Reference to: System.@DynArrayClear(Pointer;Pointer;Pointer);
# |
# 0045B3E8   E84B9AFAFF             call    00404E38
# 0045B3ED   8D45F8                 lea     eax, [ebp-$08]
# 
# * Reference to: System.@LStrClr(void;void);
# |
# 0045B3F0   E8578AFAFF             call    00403E4C
# 0045B3F5   8D4508                 lea     eax, [ebp+$08]
# 0045B3F8   BA02000000             mov     edx, $00000002
# 
# * Reference to: System.@LStrArrayClr(void;void;Integer);
# |
# 0045B3FD   E86E8AFAFF             call    00403E70
# 0045B402   C3                     ret
# 
# 
# * Reference to: System.@HandleFinally;
# |
# 0045B403   E94884FAFF             jmp     00403850
# 0045B408   EBC5                   jmp     0045B3CF
# 
# ****** END
# |
# 0045B40A   5F                     pop     edi
# 0045B40B   5E                     pop     esi
# 0045B40C   5B                     pop     ebx
# 0045B40D   8BE5                   mov     esp, ebp
# 0045B40F   5D                     pop     ebp
# 0045B410   C20800                 ret     $0008

#except Exception as e:
#    output_fp.close()
#    raise e