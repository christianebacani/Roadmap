# 1598.) Crawler Log Folder
# Categories: Array, String, Stack

class Solution:
    def minOperations(self, logs: list[str]) -> int:
        directories = [] 

        for i in range(len(logs)):
            if logs[i] == '../' and directories != []:
                directories.pop(-1)
            
            elif logs[i] == '../' and directories == []:
                pass

            elif logs[i] != './':
                directories.append(logs[i])

        return len(directories)