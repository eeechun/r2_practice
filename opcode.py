import r2pipe
import os
malware = "/home/cmtb/try_data"
outFolder = "/home/cmtb/r2_opcode_out2"

count = 1
for file in os.listdir(malware):
    if file + '.txt' not in os.listdir(outFolder):
        malwarePath = os.path.join(malware, file)
        r2 = r2pipe.open(malwarePath)
        r2.cmd('aaa')
        r2.cmd(f's {"main"}')             #移動到main函數的開頭
        machine_language = r2.cmd(f'pda $SS@$S f > {outFolder}/{file}.txt')   #0x00008190      00b0a0e3       mov fp, 0
        r2.quit()

    print(f'{count} done')
    count+=1