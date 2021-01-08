def group_by_owners(files):
    grouped = {}
    for name in files.values():
        if name not in grouped:
            grouped[name] = []

    for fileName, nameInFile in files.items():
        for nameInGrouped in grouped.keys():
            if files[fileName] == nameInGrouped:
                grouped[nameInGrouped].append(fileName)

    return grouped

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))