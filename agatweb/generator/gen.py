# -*- coding: utf-8 -*-
import os
import shutil


class GenTask:
    def __init__(self, surname: str, name: str, task: int):
        self.Name = name
        self.Surname = surname
        self.Task = task

    def gen(self):
        self.__doset()
        self.__parallel()
        self.__clean()
        self.__move()

    @staticmethod
    def __clean():
        shutil.rmtree(os.path.join(os.path.abspath(os.getcwd()), 'bin'))
        shutil.rmtree(os.path.join(os.path.abspath(os.getcwd()), 'include'))
        file_list = os.listdir()
        for f in file_list:
            if (f[-4:] in ['.tex', '.dvi', '.aux', '.log', '.toc', '.txt', '.out']) or (f[-3:] == '.ps'):
                path = os.path.join(os.path.abspath(os.getcwd()), f)
                os.remove(path)

    def __move(self):
        file_list = os.listdir()
        for f in file_list:
            if f[-4:] == '.pdf':
                if f[0:3] == 'ans':
                    path = os.path.join(os.path.abspath(os.getcwd()), str(self.Task), 'Ans')
                else:
                    path = os.path.join(os.path.abspath(os.getcwd()), str(self.Task), 'Task')
                try:
                    os.makedirs(path)
                except:
                    pass
                path = os.path.join(path, f)
                path2 = os.path.join(os.path.abspath(os.getcwd()), f)
                shutil.move(path2, path)

    def __doset(self):
        path = os.path.join(os.path.abspath(os.getcwd()), 'static', 'Stud', self.Surname+self.Name)
        try:
            os.makedirs(path)
        except:
            pass
        shutil.copytree(os.path.join(os.path.abspath(os.getcwd()), 'bin'), os.path.join(path, 'bin'))
        shutil.copytree(os.path.join(os.path.abspath(os.getcwd()), 'include'), os.path.join(path, 'include'))
        os.chdir(path)
        f = open('task.tex', 'w')
        f.write(''.join(['\ChooseTask{', str(self.Task), '}']))
        f.close()
        f = open('tasknumber.tex', 'w')
        s = ''.join(['\setcounter{fifteencount}{', str(self.Task), '}'])
        f.write(s)
        f.close()

    def __parallel(self):
        os.system(r'cmd  /C ".\\bin\\doone.bat {0}  {1} {2}"'.format(self.Surname+self.Name, 100, self.Task))
