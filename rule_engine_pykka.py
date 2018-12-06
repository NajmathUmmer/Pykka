import pykka

class Node(pykka.ThreadingActor):

    def __init__(self,message=None):
        super(Node, self).__init__()
        self.msg = message
       
    def __repr__(self):
        return repr(self.msg)

    def set_succ_node(self, message):
        future_succ = Node.start(message).proxy()
        return(future_succ.msg.get())

    def set_fail_node(self, message):
        future_fail = Node.start(message).proxy()
        return(future_fail.msg.get())

if __name__ == '__main__':
    
    node0 = Node.start("first").proxy()
    node1 = Node.start("second").proxy()
    node2 = Node.start("third").proxy()
    print(node0.set_succ_node(node1.msg.get()).get())
    print(node0.set_fail_node(node2.msg.get()).get())
    