from solution import Solution

solution = Solution()


def test_1():
    nums = [3,2,2,3]
    val = 3
    
    expected_res = 2
    expected_nums = [2, 2]

    result = solution.removeElement(nums, val)
    nums.sort()

    assert result == expected_res, \
        "Expected result not match with actual one. {expected} != {actual}" \
            .format(expected=expected_res, actual=result)
    for i in range(len(expected_nums)):
        assert nums[i] == expected_nums[i], \
            "Expected array not match with actual one on position [{}].".format(i)
        
