dirs = [('folder1',['file1',( 'folder2', ['file2','file3'] ),( 'folder3', ['file3', 'file4',('folder4', ['file3'])] ),'file5'])]

def func(dirs,l=[],t=[]):
    for i in dirs:
        if isinstance(i,tuple):
            t.append(i)
        else:
            l.append(i)
    res1= l[:]
    res2= t[:]
    l.clear()
    t.clear()
    return res1,res2

def Read(Tuple):
    t = list(Tuple)
    return t[0],t[1:]

def ways(dirs,filename,list=[],str='/'):
    file,folder = func(dirs)
    print(file,folder)
    for i in file:
        if i ==filename:
            if str =='/':
                list.append(filename)
            else:
                list.append(str+'/'+filename)

    for i in folder:
        list1,list2 = Read(i)
        if str == '/':
            new_str =str+list1
        else:
            new_str =str+'//'+list1
        ways(list2[0],filename,list,new_str)
    return list

def decor(func):
    def search(dirs,filename):
        result = func(dirs,filename,list=[],str='/')
        return result
    return search
search = decor(ways)


print(search(dirs, 'file1'))
print(search(dirs, 'file2'))
print(search(dirs, 'file3'))
print(search(dirs, 'file4'))
print(search(dirs, 'file5'))
print(search(dirs, 'file6'))
print(search(dirs, 'folder1'))
assert search(dirs, 'file1') == ['/folder1/file1'], 'Failed test for file1'
assert search(dirs, 'file2') == ['/folder1//folder2/file2'], 'Failed test for file2'
assert search(dirs, 'file3') == ['/folder1//folder2/file3', '/folder1//folder3/file3', '/folder1//folder3//folder4/file3'], 'Failed test for file3'
assert search(dirs, 'file4') == ['/folder1//folder3/file4'], 'Failed test for file4'
assert search(dirs, 'file5') == ['/folder1/file5'], 'Failed test for file5'
assert search(dirs, 'file6') == [], 'Failed test for file6'
assert search(dirs, 'folder1') == [], 'Failed test for folder1'
print('All tests good!')
