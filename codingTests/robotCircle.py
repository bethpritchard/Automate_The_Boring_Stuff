class RobotCircle:
    @staticmethod
    def hasMovedToStart(moves):
        n = 0
        s = 0
        e = 0
        w = 0

        for i in range(len(moves)):
            if moves[i] == 'U':
                n += 1
            elif moves[i] == 'R':
                e += 1
            elif moves[i] == 'D':
                s += 1
            else:
                w += 1

        vertical = abs(n-s)
        horizontal = abs(e-w)

        if vertical == 0 and horizontal == 0:
            return True
        else:
            return False



print(RobotCircle.hasMovedToStart("LRUD"))