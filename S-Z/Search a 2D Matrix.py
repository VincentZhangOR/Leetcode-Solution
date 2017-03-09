# coding=utf-8
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        leftRow=0
        rightRow=len(matrix)-1
        leftCol=0
        rightCol=len(matrix[0])-1
        #print leftRow,rightRow ,leftCol,rightCol
        while leftRow<=rightRow:
            midRow=(leftRow+rightRow )/2
            if leftRow<rightRow:
                if matrix[midRow][rig htCol]<target:
                    leftRow=midRow+1
                elif matrix[midRow][rig htCol]>target:
                    rightRow=midRow
                else:
                    return True
            else:
                if leftCol>rightCol:
                    break
                midCol=(leftCol +rightCol)/2
                #print leftRow ,rightRow,leftCol ,rightCol ,matrix[midRow][mi dCol]
                if matrix[midRow][mid Col]<target:
                    leftCol=midCol+1
                elif matrix[midRow][mid Col]>target:
                    rightCol=midCol
