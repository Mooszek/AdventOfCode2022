import os

os.chdir(os.path.dirname(__file__))

class Directory():
    def __init__(self, name) -> None:
        self.name = name
        self.parent = None
        self.allDirectories = [] #List<Directory>
        self.files = [] #List<File>
        self.totalSize = 0
        self.allFilesSize = 0

    def calculateFilesSize(self):
        totalSize = 0
        for file in self.files:
            totalSize += int(file.size)
        self.totalSize = totalSize
        return self.totalSize

    def calculateAllFilesSize(self):
        allFilesSize = 0
        for directory in self.allDirectories:
            allFilesSize += directory.calculateAllFilesSize()
        self.allFilesSize = allFilesSize + self.calculateFilesSize()
        return self.allFilesSize

class File():
    def __init__(self, name, size) -> None:
        self.parent = []
        self.size = size
        self.name = name

class DirectoryManager():
    def __init__(self) -> None:
        self.allDirectories = [] #List<Directory>
        self.currentPath = [] #stack

    def decipherScript(self):

        with open("input.txt", "r") as input_file:
            for line in input_file:
                if '$ cd /' in line:
                    self.createRoot()
                elif 'dir' in line:
                    self.createDirectory(line.split(' ')[1])
                elif '$ cd ..' in line:
                    self.goBack()
                elif '$ cd ' in line:
                    self.switchDirectory(line.split(' ')[2])
                elif '$ ls' not in line:
                    self.createFile(line.split(' ')[1],line.split(' ')[0])


    def createDirectory(self,name): # $ dir <directory name>

        cur_dir = self.currentPath[-1] #equivalent of peek
        if not self.isDirectoryAlreadyInList(name, cur_dir.allDirectories) and not self.isParentTheSame(name, cur_dir):
            new_dir = Directory(name)
            new_dir.parent = cur_dir
            cur_dir.allDirectories.append(new_dir)
            self.allDirectories.append(new_dir)
        

    def createFile(self, fileName, size): # $ <number> <filename>

        cur_dir = self.currentPath[-1] #equivalent of peek
        if not self.isFileAlreadyInList(fileName, cur_dir.files):
            new_file = File(fileName, size)
            new_file.parent = cur_dir
            cur_dir.files.append(new_file)


    def switchDirectory(self, directoryName): # $ cd <directory name>

        if not self.isDirectoryAlreadyInList(directoryName, self.allDirectories):
            self.createDirectory(directoryName)
            self.currentPath.append(directory)
        else: 
            for directory in self.allDirectories:
                if directoryName == directory.name:
                    self.currentPath.append(directory)


    def goBack(self): # $ cd ..
        self.currentPath.pop()


    def createRoot(self): # $ cd /

        root_dir = Directory('root')
        self.allDirectories.append(root_dir)
        self.currentPath.append(root_dir)

    def isDirectoryAlreadyInList(self, new_directory_name, destination_directory_list):
        for directory in destination_directory_list:
            if new_directory_name == directory.name:
                return True
        return False

    def isParentTheSame(self, new_directory_name, curdir):
        for directory in self.allDirectories:
            if new_directory_name == directory.name:
                if directory.parent == curdir:
                    return True
        return False
    
    def isFileAlreadyInList(self, new_file_name, destination_directory_list):
        for file in destination_directory_list:
            if new_file_name == file.name:
                return True
        return False


directories= DirectoryManager()
directories.decipherScript()
candidates_to_delete = []

for directory in directories.allDirectories:
    directory.calculateAllFilesSize()
    if directory.allFilesSize>358913:
        candidates_to_delete.append(directory.allFilesSize)

candidates_to_delete.sort()

directory_to_delete = candidates_to_delete[0]

print(directory_to_delete)