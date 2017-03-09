# coding=utf-8
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1=(C-A)*(D-B)
        area2=(G-E)*(H-F)
        if (area1 and area2)==0:
            return area1 or area2
        if E>=C or A>=G or B>=H or F >=D:
            return area1+area2
        left=max(A,E)
        right=min(C,G)
        down=max(B,F)
        up=min(D,H)
        heng=right-left
        shu=up-down
        return area1+area2-heng*shu
