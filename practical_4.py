import sys 
from difflib import SequenceMatcher
import pathlib
import datetime
import pytz


def convert(seqm):
    output= []
    for opcode, a0, a1, b0, b1 in seqm.get_opcodes():

        if opcode == 'equal':
            for s in seqm.a[a0:a1].split('\n'):
                if s:
                    output.append(f' {s}')
        elif opcode == 'insert':
            for s in seqm.b[b0:b1].split('\n'):
                if s:
                    output.append(f'+{s}')
        elif opcode == 'delete':
            for s in seqm.b[b0:b1].split('\n'):
                if s:
                    output.append(f'-{s}')

        elif opcode == 'replace':
            for s in seqm.a[a0:a1].split('\n'):
                if s:
                    output.append(f'-{s}')
            for s in seqm.b[b0:b1].split('\n'):
                if s:
                    output.append(f'+{s}')

    return '\n'.join(output)

if __name__ == '__main__':

    a_file = pathlib.Path(sys.argv[1])
    b_file = pathlib.Path(sys.argv[2])

    s = SequenceMatcher(None, a_file.read_text(), b_file.read_text())

    a_mtime = datetime.datetime.fromtimestamp(a_file.stat().st_mtime).astimezone()
    b_mtime = datetime.datetime.fromtimestamp(b_file.stat().st_mtime).astimezone()

    print(f'--- {a_file.as_posix()} {a_mtime:%Y-%m-%d %H:%M:%S.%f %z}')
    print(f'+++ {b_file.as_posix()} {b_mtime:%Y-%m-%d %H:%M:%S.%f %z}')

    print(convert(s))
