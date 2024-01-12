class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l,counter,nices = 0,0,{}
        indexes = deque(maxlen=len(nums))
        changed = False
        for r in range(len(nums)):
            if nums[r] % 2:
                counter += 1
                indexes.append(r)
                # nices += ((r - indexes[-1] + 1) * (indexes[0] - l + 1))
            while counter > k:
                if nums[l] % 2:
                    counter -= 1
                    indexes.popleft()
                    changed = True
                l += 1
            if counter == k:

                # print(l,r)
                # print(indexes)
                # print(indexes[0],indexes[-1])
                # print((r - indexes[-1] + 1) * (indexes[0] - l + 1))
                nices[(indexes[-1], indexes[0])] = ((r - indexes[-1] + 1) * (indexes[0] - l + 1))
                

                
        # print(nices)
        return sum(nices.values())