"""Tests for data_structures module."""

import pytest

from own.data_structures import LinkedList, Queue, Stack


class TestStack:
    def test_new_stack_is_empty(self):
        s = Stack()
        assert s.is_empty() is True
        assert s.size() == 0

    def test_push_and_peek(self):
        s = Stack()
        s.push(1)
        assert s.peek() == 1
        assert s.size() == 1
        assert s.is_empty() is False

    def test_push_multiple(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        assert s.peek() == 3
        assert s.size() == 3

    def test_pop(self):
        s = Stack()
        s.push("a")
        s.push("b")
        assert s.pop() == "b"
        assert s.pop() == "a"
        assert s.is_empty() is True

    def test_pop_empty_raises(self):
        s = Stack()
        with pytest.raises(IndexError, match="empty stack"):
            s.pop()

    def test_peek_empty_raises(self):
        s = Stack()
        with pytest.raises(IndexError, match="empty stack"):
            s.peek()


class TestQueue:
    def test_new_queue_is_empty(self):
        q = Queue()
        assert q.is_empty() is True
        assert q.size() == 0

    def test_enqueue_and_front(self):
        q = Queue()
        q.enqueue(1)
        assert q.front() == 1
        assert q.size() == 1
        assert q.is_empty() is False

    def test_enqueue_multiple(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        assert q.front() == 1
        assert q.size() == 3

    def test_dequeue(self):
        q = Queue()
        q.enqueue("a")
        q.enqueue("b")
        q.enqueue("c")
        assert q.dequeue() == "a"
        assert q.dequeue() == "b"
        assert q.dequeue() == "c"
        assert q.is_empty() is True

    def test_dequeue_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError, match="empty queue"):
            q.dequeue()

    def test_front_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError, match="empty queue"):
            q.front()


class TestLinkedList:
    def test_new_list_is_empty(self):
        ll = LinkedList()
        assert ll.is_empty() is True
        assert ll.size() == 0
        assert ll.to_list() == []

    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.to_list() == [1, 2, 3]
        assert ll.size() == 3

    def test_prepend(self):
        ll = LinkedList()
        ll.prepend(1)
        ll.prepend(2)
        ll.prepend(3)
        assert ll.to_list() == [3, 2, 1]
        assert ll.size() == 3

    def test_find_existing(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        assert ll.find(20) is True

    def test_find_missing(self):
        ll = LinkedList()
        ll.append(10)
        assert ll.find(99) is False

    def test_find_in_empty_list(self):
        ll = LinkedList()
        assert ll.find(1) is False

    def test_delete_head(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.delete(1) is True
        assert ll.to_list() == [2, 3]
        assert ll.size() == 2

    def test_delete_middle(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.delete(2) is True
        assert ll.to_list() == [1, 3]

    def test_delete_tail(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.delete(3) is True
        assert ll.to_list() == [1, 2]

    def test_delete_missing(self):
        ll = LinkedList()
        ll.append(1)
        assert ll.delete(99) is False

    def test_delete_from_empty(self):
        ll = LinkedList()
        assert ll.delete(1) is False

    def test_mixed_operations(self):
        ll = LinkedList()
        ll.append(1)
        ll.prepend(0)
        ll.append(2)
        assert ll.to_list() == [0, 1, 2]
        ll.delete(1)
        assert ll.to_list() == [0, 2]
        assert ll.size() == 2
        assert ll.is_empty() is False
