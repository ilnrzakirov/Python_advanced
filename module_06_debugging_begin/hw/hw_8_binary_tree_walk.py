"""
Помимо того чтобы логи писать, нужно их ещё и уметь читать,
иначе мы будем как в известном анекдоте, писателями, а не читателями.

Для вас мы написали простую функцию обхода binary tree по уровням.
Также в репозитории есть файл с логами, написанными этой программой.

Напишите функцию restore_tree, которая принимает на вход путь до файла с логами
    и восстанавливать исходное BinaryTree.

Функция должна возвращать корень восстановленного дерева

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass

Примечание: гарантируется, что все значения, хранящиеся в бинарном дереве уникальны
"""
import itertools
import logging
import random
from collections import deque
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("tree_walk")


@dataclass
class BinaryTreeNode:
    val: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    tree_list = []
    ind = 0
    with open(path_to_log_file, "r") as file:
        for line in file.readlines():
            if "INFO" in line:
                value = int(line[line.find("[") + 1: line.find("]")])
                lst = BinaryTreeNode(val=value)
                tree_list.append(lst)
                ind += 1
            elif "DEBUG" in line:
                str = line.split(' ')
                tree_s = int(str[0][str[0].find("[") + 1: str[0].find("]")])
                tree_e = int(str[6][str[6].find("[") + 1: str[6].find("]")])
                if "left" in line:
                    left = BinaryTreeNode(tree_e)
                    tree_list[tree_s - 1].left = left
                elif "right" in line:
                    right = BinaryTreeNode(tree_e)
                    tree_list[tree_s - 1].right = right

    return tree_list[0]

def walk(root: BinaryTreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                    f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                    f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


counter = itertools.count(random.randint(1, 10 ** 6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)

    node_right = get_tree(max_depth - 1, level=level + 1)

    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node


if __name__ == "__main__":
    logging.basicConfig(
            level=logging.DEBUG,
            format="%(levelname)s:%(message)s",
            filename="hw_8_walk_log_4.txt",
    )
    restore_tree("hw_8_walk_log_1.txt")
    # root = get_tree(7)
    #
    # walk(root)
