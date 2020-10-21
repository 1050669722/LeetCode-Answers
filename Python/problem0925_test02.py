class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False
        if len(typed) <= 1:
            return name == typed
        
        pn, qn = 0, 0
        pt, qt = 0, 0

        resn = []
        while qn < len(name):
            if name[qn] != name[pn]:
                tmpn = name[pn:qn]
                resn.append(tmpn)
                pn = qn
            qn += 1
        resn.append(name[pn:qn])
        print(resn)

        rest = []
        while qt < len(typed):
            # print(pt, qt, typed[pt], typed[qt])
            if typed[qt] != typed[pt]:
                tmpt = typed[pt:qt]
                rest.append(tmpt)
                pt = qt
            qt += 1
        rest.append(typed[pt:qt])
        print(rest)

        if len(resn) != len(rest):
            return False
        for i, letterGroup in enumerate(resn):
            if letterGroup[0] != rest[i][0]:
                return False
            if len(letterGroup) > len(rest[i]):
                return False
        return True

