class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        filesPath = dict()
        for path in paths:
            files = path.split()
            root = files[0]
            for fileName in files[1:]:
                name, content = fileName.split("(")
                pathName = root + "/" + name
                if content in filesPath:
                    filesPath[content].append(pathName)
                else:
                    filesPath[content] = [pathName]

        duplicateFiles = []
        for v in filesPath.values():
            if len(v) > 1:
                duplicateFiles.append(v)

        return duplicateFiles
