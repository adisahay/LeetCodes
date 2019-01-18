/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        int sum = 0;
        ListNode head = null, tail = null;
        ListNode a = l1, b = l2;

        while (a != null && b != null) {
            sum = a.val + b.val + carry;
            carry = sum / 10;
            sum = sum % 10;

            ListNode newnode = new ListNode(sum);
            // newnode.next = null;

            if (head == null)
                head = newnode;
            else
                tail.next = newnode;

            tail = newnode;

            a = a.next;
            b = b.next;
        }

        if (a == null)
            while (b != null) {
                sum = b.val + carry;
                carry = sum / 10;
                sum = sum % 10;

                ListNode newnode = new ListNode(sum);
                tail.next = newnode;
                tail = newnode;

                b = b.next;
            }
        else
            while (a != null) {
                sum = a.val + carry;
                carry = sum / 10;
                sum = sum % 10;

                ListNode newnode = new ListNode(sum);
                tail.next = newnode;
                tail = newnode;

                a = a.next;
            }

        if (carry == 1)
            tail.next = new ListNode(1);

        return head;
    }
}
