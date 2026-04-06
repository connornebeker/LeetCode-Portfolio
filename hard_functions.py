class Solution:  
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next
    # print(reverseKGroup([1,2,3,4,5], 2))

    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0  # global index tracking position in vals

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
    # print(deserialize(serialize([1,2,3,None,None,4,5])))

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereqs[course].append(pre)

        state = [0] * numCourses
        order = []

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False

            state[course] = 2
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order
    # print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))