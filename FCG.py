import r2pipe
import os
malware = "/home/cmtb/data"
outFolder = "/home/cmtb/r2_FCG_out"

count = 1
for file in os.listdir(malware):
    if file + '.txt' not in os.listdir(outFolder):
        malwarePath = os.path.join(malware, file)
        r2 = r2pipe.open(malwarePath)
        r2.cmd('aaa')
        r2.cmd(f's {"main"}')             #移動到main函數的開頭
        machine_language = r2.cmd(f'agCd f > {outFolder}/{file}.dot')   #0x00008190      00b0a0e3       mov fp, 0
        r2.quit()

    print(f'{count} - {file} done')
    count+=1