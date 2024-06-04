12. Write a function `merge_sort(arr: List[int]) -> List[int]` that implements the merge sort  algorithm. 

from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half_sorted = merge_sort(left_half)
    right_half_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half_sorted, right_half_sorted)

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = merge_sort(arr)
print(sorted_arr)


13. Implement a function `find_duplicates(arr: List[int]) -> List[int]` that returns a list of  duplicate elements in the input list. 

from typing import List

def find_duplicates(arr: List[int]) -> List[int]:
    seen = set()
    duplicates = []

    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates

# Example usage:
arr = [1, 2, 3, 4, 1, 2, 5, 6, 7, 8, 4, 9, 10, 1]
duplicate_elements = find_duplicates(arr)
print("Duplicate elements:", duplicate_elements)


14. Write a function `is_palindrome(s: str) -> bool` to check if a given string is a  palindrome (reads the same forward and backward). 

def is_palindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]

# Example usage:
test_strings = ["A man, a plan, a canal, Panama!", "racecar", "hello"]
for s in test_strings:
    print(f"{s}: {is_palindrome(s)}")

15. Sorting 
Implement the quicksort algorithm in Python. 


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)


16. Binary Search Tree (BST) 
Write a class `BST` with methods to insert, find, and delete nodes in a binary search tree.  Also, include a method to find the height of the tree. 

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        return root

    def find(self, key):
        return self._find_recursive(self.root, key)

    def _find_recursive(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self._find_recursive(root.left, key)
        else:
            return self._find_recursive(root.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self._find_min(root.right)
                root.key = successor.key
                root.right = self._delete_recursive(root.right, successor.key)
        return root

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, root):
        if root is None:
            return 0
        else:
            left_height = self._height_recursive(root.left)
            right_height = self._height_recursive(root.right)
            return max(left_height, right_height) + 1

# Example usage:
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Height of the tree:", bst.height())


17. Graph Algorithms 
Write a function `dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Dict[str, int]` that  implements Dijkstra's algorithm to find the shortest path from the start node to all other  

from typing import Dict, List

def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Dict[str, int]:
    # Initialize distances from start node to all other nodes as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Set of visited nodes
    visited = set()

    while len(visited) < len(graph):
        # Find the node with the smallest distance from the start node
        current_node = min((node for node in graph if node not in visited), key=lambda x: distances[x])

        # Mark the current node as visited
        visited.add(current_node)

        # Update distances to neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node, ":", shortest_distances)
